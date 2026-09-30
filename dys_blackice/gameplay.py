"""Gameplay layer for dys_blackice: spawns, objectives, logic, doors, screens, jackpoints.

Objective chain (Punks attack, Corps defend):
  1 GATE   meatspace only: 30 s override (Corps can abort) at the  -> Neon Arcade spawn for Punks
           north guard post.
  2 HUB    decker crack (trigger_crackable) in the Security Hub. -> lobby spawn flips, vault spawn opens
  3 CORE   final. Core is invulnerable while its shield is up. The shield drops for 40 s
           from cyberspace (encrypted ICE), or permanently when both emitters are destroyed.
"""
from __future__ import annotations

import kit
from vmflib import VMF, box, ngon, NODRAW, TRIGGER, INVISIBLE, PLAYERCLIP

PUNKS, CORPS = 2, 3
FF_MAT = "termitex/t_forcefield"
SCREEN_MAT = "dys_monitor1a"


# ------------------------------------------------------------------ helpers

def forcefield(m: VMF, name, x0, y0, z0, x1, y1, z1, team, start_disabled=False):
    dx, dy = x1 - x0, y1 - y0
    thin_x = dx < dy
    mats = {k: NODRAW for k in ("top", "bottom", "north", "south", "east", "west")}
    if thin_x:
        mats["east"] = mats["west"] = FF_MAT
    else:
        mats["north"] = mats["south"] = FF_MAT
    kv = dict(targetname=name, team=str(team))
    if start_disabled:
        kv["startdisabled"] = "1"
    return m.brush_ent("dys_forcefield", box(x0, y0, z0, x1, y1, z1, mats), **kv)


def spawn_area(m: VMF, name, sid, team, label, points, yaw, enabled=True):
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)
    cz = min(p[2] for p in points)
    m.ent("dys_spawn", (cx, cy, cz + 16), targetname=name, team=str(team), spawnid=str(sid),
          spawnname=label, spawnflags="1" if enabled else "0")
    for (x, y, z) in points:
        # the entity's own pad model is solid and players bump into it: disable it (spawnflags 1) and show the
        # same pad as a non-solid prop instead
        m.ent("dys_spawn_point", (x, y, z + 1), spawnid=str(sid), angles=f"0 {yaw} 0", spawnflags="1")
        kit.prop(m, "models/props/prop_spawner.mdl", x, y, z, yaw=yaw, solid=0)


def grid(x0, y0, x1, y1, z, nx, ny):
    pts = []
    for i in range(nx):
        for j in range(ny):
            x = x0 + (x1 - x0) * (i + 0.5) / nx
            y = y0 + (y1 - y0) * (j + 0.5) / ny
            pts.append((round(x), round(y), z))
    return pts


def jack_terminal(m: VMF, name, x, y, z, facing, target, model="models/props/prop_jackin_punks.mdl"):
    """Wall terminal: prop + 30x30 jackpoint brush 5.5u in front. facing: '+x','-x','+y','-y'.
    (x, y) is the wall surface point, z the terminal centre height."""
    yaw = {"-x": 0, "+x": 180, "-y": 90, "+y": 270}[facing]
    fx, fy = {"-x": (-1, 0), "+x": (1, 0), "-y": (0, -1), "+y": (0, 1)}[facing]
    ox, oy = x + fx * 12, y + fy * 12   # prop origin sits half its depth off the wall
    kit.prop(m, model, ox, oy, z, yaw=yaw, on_floor=False, solid=6)
    jx, jy = ox + fx * 5.5, oy + fy * 5.5
    if fx:
        b = box(jx - 0.5, jy - 15, z - 15, jx + 0.5, jy + 15, z + 15,
                {"all": NODRAW, "east" if fx > 0 else "west": SCREEN_MAT})
    else:
        b = box(jx - 15, jy - 0.5, z - 15, jx + 15, jy + 0.5, z + 15,
                {"all": NODRAW, "north" if fy > 0 else "south": SCREEN_MAT})
    return m.brush_ent("dys_jackpoint", b, targetname=name, target=target, spawnflags="0",
                       disablereceiveshadows="1", disableshadows="1")


def screen(m: VMF, cls, name, panel, x, y, z, facing, w=32, h=32, **kv):
    """dys_screen / dys_cyberscreen mounted on a wall. (x, y, z) = centre of the screen surface.
    VGUI screens draw in the entity's local +y/+z plane from its origin (lower-left corner)
    and face along local +x."""
    yaw = {"+x": 0, "+y": 90, "-x": 180, "-y": 270}[facing]
    rx, ry = {"+x": (0, 1), "+y": (-1, 0), "-x": (0, -1), "-y": (1, 0)}[facing]   # local +y in world
    fx, fy = {"+x": (1, 0), "+y": (0, 1), "-x": (-1, 0), "-y": (0, -1)}[facing]
    ox = x - rx * w / 2 + fx * 1
    oy = y - ry * w / 2 + fy * 1
    oz = z - h / 2
    return m.ent(cls, (ox, oy, oz), targetname=name, panelname=panel, angles=f"0 {yaw} 0",
                 width=str(w), height=str(h), reswidth="256", resheight="256", **kv)


def turret(m: VMF, name, x, y, z, yaw, health=800):
    """Corps ceiling turret, (x, y, z) 2u below the ceiling. 800 hp = 10 boltgun bolts (82 each)."""
    return m.ent("npc_turret_ceiling", (x, y, z), targetname=name, angles=f"0 {yaw} 0", team=str(CORPS),
                 maxhealth=str(health), minhealthdmg="30", spawnflags="0",
                 model="models/Combine_turrets/Ceiling_turret.mdl")


def relay(m: VMF, name, x, y, z, once=False):
    return m.ent("logic_relay", (x, y, z), targetname=name, spawnflags="1" if once else "0")


def msg(m: VMF, name, text, color="255 180 60", y="0.3", hold=5, channel=3):
    return m.ent("game_text", (0, 0, 0), targetname=name, message=text, x="-1", y=y, effect="0",
                 color=color, color2="240 110 0", fadein="0.3", fadeout="1.0", holdtime=str(hold),
                 fxtime="0.25", channel=str(channel), spawnflags="1")


# ------------------------------------------------------------------ main

def add_gameplay(b):
    m: VMF = b.m
    ents = {}

    # --- filters
    kit.filter_team(m, "f_punks", PUNKS)
    kit.filter_team(m, "f_corps", CORPS)
    m.ent("filter_activator_name", (0, 0, 64), targetname="f_nobody", filtername="__nobody__", Negated="0")

    # --- spawns (ids increase from the Punk side toward the Corps side)
    spawn_area(m, "spawn_punk_hq", 1, PUNKS, "Metro Hideout", grid(-5840, -176, -4656, 448, -384, 5, 4), 0)
    jip = (-2304, 640)                  # keep the arcade jack-in terminal clear: no spawn points in front of it
    spawn_area(m, "spawn_arcade", 2, 0, "NetExcess Arcade",
               [p for p in grid(-2272, 432, -1872, 848, 0, 4, 4) if abs(p[0] - jip[0]) > 160], 270)
    spawn_area(m, "spawn_corp_lobby", 3, CORPS, "Kuroda Security", grid(1936, -464, 2368, 464, 192, 4, 5), 180)
    spawn_area(m, "spawn_corp_vault", 4, CORPS, "Datavault Control", grid(4592, -336, 4960, 336, -128, 4, 5), 180,
               enabled=False)       # enabled when the hub falls
    for (x, y, z, yaw) in [(-5856, 384, -384, 0), (-4608, 384, -384, 180), (-2272, 864, 0, 0),
                           (1920, 480, 192, 270), (2400, -480, 192, 90), (5024, 352, -128, 180)]:
        m.ent("dys_ammodisp", (x, y, z), angles=f"0 {yaw} 0")

    # --- spawn protection
    forcefield(m, "ff_hq_stairs", -4460, -192, -384, -4452, 192, -160, PUNKS)     # behind the arch lintel
    forcefield(m, "ff_hq_maint", -5120, 528, -384, -4992, 536, -224, PUNKS)
    # the metro tunnels are closed to everyone: forcefield + clip a little inside each mouth
    for (i, x) in enumerate((-6048, -4456)):
        forcefield(m, f"ff_tunnel{i}", x, -640, -448, x + 8, -256, -192, PUNKS)
        m.add(box(x, -640, -448, x + 8, -256, -192, PLAYERCLIP))
    forcefield(m, "ff_arcade_front", -2176, 348, 0, -1920, 356, 160, PUNKS, start_disabled=True)
    forcefield(m, "ff_arcade_back", -1920, 956, 0, -1792, 964, 160, PUNKS, start_disabled=True)
    forcefield(m, "ff_lobby_1", 1868, -256, 192, 1876, -128, 320, CORPS)
    forcefield(m, "ff_lobby_2", 1868, 128, 192, 1876, 256, 320, CORPS)
    forcefield(m, "ff_lobby_3", 1920, 540, 192, 2048, 548, 320, CORPS)
    forcefield(m, "ff_vault_1", 4524, -320, -128, 4532, -192, 0, CORPS)
    forcefield(m, "ff_vault_2", 4524, 192, -128, 4532, 320, 0, CORPS)
    la = m.ent("logic_auto", (-5200, 0, -300), spawnflags="0")
    la.out("OnMapSpawn", "ff_arcade_front", "Disable")
    la.out("OnMapSpawn", "ff_arcade_back", "Disable")
    # guard-post corridors and the north service door are Corps-only until the gate falls
    forcefield(m, "ff_guard_n", 552, 560, 0, 560, 656, 128, CORPS)
    forcefield(m, "ff_guard_s", 552, -656, 0, 560, -560, 128, CORPS)
    forcefield(m, "ff_service_n", 460, 1024, 0, 468, 1152, 128, CORPS)
    # the cooling route from the hub to the vault is Corps-only until the hub falls
    forcefield(m, "ff_cooling", 1536, 1164, 192, 1664, 1172, 320, CORPS)

    # --- objectives
    m.ent("dys_objective", (300, 0, 64), targetname="obj_gate", team=str(CORPS), Index="1", IsPrimary="1",
          CyberSpace="0", IconType="8", spawnflags="0", objtarget="gate1",
          PunksText="Breach the security gate", CorpsText="Hold the security gate")
    m.ent("dys_objective", (1408, 1088, 256), targetname="obj_hub", team=str(CORPS), Index="2", IsPrimary="1",
          CyberSpace="0", IconType="4", spawnflags="0", objtarget="hub_console",
          PunksText="Crack the security hub", CorpsText="Protect the security hub")
    m.ent("dys_objective", (4128, 0, -200), targetname="obj_core", team=str(CORPS), Index="3", IsPrimary="1",
          CyberSpace="0", IconType="5", spawnflags="8", objtarget="core",
          PunksText="Crash the BLACK ICE core", CorpsText="Protect the BLACK ICE core")
    m.ent("dys_objective", (4128, 0, 0), targetname="obj_shield", team=str(CORPS), Index="4", IsPrimary="0",
          CyberSpace="1", IconType="1", spawnflags="0", objtarget="core_shield",
          PunksText="Drop the core shield", CorpsText="Keep the core shield up")

    # --- messages
    msg(m, "msg_override", "GATE OVERRIDE IN PROGRESS - 30 SECONDS", "255 200 60")
    msg(m, "msg_override10", "GATE OVERRIDE - 10 SECONDS", "255 140 40", hold=3)
    msg(m, "msg_abort", "GATE OVERRIDE ABORTED", "90 200 255")
    msg(m, "msg_gate", "THE SECURITY GATE HAS BEEN BREACHED", "255 120 40", hold=6)
    msg(m, "msg_hub", "SECURITY HUB COMPROMISED - DATAVAULT ACCESS OPEN", "255 120 40", hold=6)
    msg(m, "msg_shield_down", "CORE SHIELD OFFLINE", "255 60 60", hold=4)
    msg(m, "msg_shield_up", "CORE SHIELD RESTORED", "90 200 255", hold=4)
    msg(m, "msg_emitter", "SHIELD EMITTER DESTROYED", "255 160 60", hold=4)
    msg(m, "msg_shield_dead", "SHIELD EMITTERS DESTROYED - CORE EXPOSED", "255 60 60", hold=6)
    msg(m, "msg_core", "BLACK ICE CORE CRASHED", "255 40 40", hold=8)

    # ============================================================ OBJ 1: gate
    g = kit.gate(m, "gate1", 496, -192, 0, 528, 192, 256, "metal/metalgate001a", speed=48, lip=16)
    # the lattice texture passes bullets and sight, and Dystopia turrets ignore toolsblock_los (tested), so an
    # invisible solid layer inside the door stops lobby turrets from shooting through; it lifts with the gate
    g.solids.append(box(508, -192, 0, 516, 192, 256, NODRAW))
    # canopy over the gate approach with Corps turrets hanging from it
    m.detail(box(320, -256, 288, 448, 256, 304, "metal/metalwall003a"))
    for y in (-160, 160):
        turret(m, "tur_plaza", 384, y, 286, 180)
    # meatspace override screen inside the north guard post (north wall, facing south)
    scr = screen(m, "dys_screen", "gate_screen", "bi_gate_override", 288, 734, 72, "-y", w=40, h=40)
    scr.out("Button1", "gate_fp", "TestActivator")
    scr.out("Button2", "gate_fc", "TestActivator")
    f = kit.filter_team(m, "gate_fp", PUNKS)
    f.kv["origin"] = "288 700 64"
    f.out("OnPass", "gate_override", "Trigger")
    f = kit.filter_team(m, "gate_fc", CORPS)
    f.kv["origin"] = "288 700 80"
    f.out("OnPass", "gate_override", "CancelPending")
    f.out("OnPass", "msg_abort", "Display")
    f.out("OnPass", "snd_override", "StopSound")
    r = relay(m, "gate_override", 300, 700, 64)
    r.out("OnTrigger", "msg_override", "Display")
    r.out("OnTrigger", "snd_override", "PlaySound")
    r.out("OnTrigger", "msg_override10", "Display", delay=20)
    r.out("OnTrigger", "gate_done", "Trigger", delay=30)
    # alarm1.wav loops (cue chunk), so the entity must be flagged looped (spawnflags 16, not 48): a "not looped"
    # ambient_generic ignores StopSound and the alarm would sound forever after the gate falls
    m.ent("ambient_generic", (288, 600, 120), targetname="snd_override", message="ambient/alarms/alarm1.wav",
          health="7", radius="1800", spawnflags="16", pitch="100", pitchstart="100")
    r = relay(m, "gate_done", 320, 700, 64, once=True)
    for tgt, inp, delay in [("obj_gate", "SetPunks", 0), ("gate1", "Open", 0), ("ff_guard_n", "Disable", 0),
                            ("ff_guard_s", "Disable", 0), ("ff_service_n", "Disable", 0),
                            ("spawn_arcade", "SetPunks", 0),
                            ("ff_arcade_front", "Enable", 0), ("ff_arcade_back", "Enable", 0),
                            ("tur_plaza", "Disable", 0), ("msg_gate", "Display", 0), ("snd_override", "StopSound", 0),
                            ("gate_override", "Disable", 0),
                            ("cy_gateturrets_off", "Disable", 0), ("cy_gateturrets_on", "Disable", 0)]:
        r.out("OnTrigger", tgt, inp, delay=delay)

    # ============================================================ OBJ 2: security hub
    # console the deckers crack (visible block + info target)
    m.brush_ent("func_brush", box(1376, 1104, 192, 1440, 1152, 256, {"all": "metal/metalwall003a", "south": "dys_monitor2a"}),
                targetname="hub_console", Solidity="2", solidbsp="0", StartDisabled="0", spawnflags="2", InputFilter="0")
    crk = kit.trigger(m, "trigger_crackable", 1312, 1024, 192, 1504, 1152, 320, targetname="hub_crack",
                      filtername="f_punks", CrackTime="8", DelayBeforeReset="2", FilterFailText="1", spawnflags="1",
                      StartDisabled="0")
    crk.out("OnFinishCrack", "hub_done", "Trigger")
    crk.out("OnStartCrack", "snd_hub_alarm", "PlaySound")
    crk.out("OnStartCrack", "hub_alarm_light", "TurnOn")
    crk.out("OnStopCrack", "snd_hub_alarm", "StopSound")
    crk.out("OnStopCrack", "hub_alarm_light", "TurnOff")
    m.ent("ambient_generic", (1408, 960, 300), targetname="snd_hub_alarm", message="ambient/alarms/alarm_citizen_loop1.wav",
          health="6", radius="1500", spawnflags="16", pitch="100", pitchstart="100")      # looping wav: looped flag
    r = relay(m, "hub_done", 1408, 1000, 256, once=True)
    for tgt, inp, delay in [("obj_hub", "SetPunks", 0), ("spawn_corp_lobby", "SetPunks", 0),
                            ("ff_lobby_1", "SetPunks", 0), ("ff_lobby_2", "SetPunks", 0), ("ff_lobby_3", "SetPunks", 0),
                            ("spawn_corp_vault", "Enable", 0), ("blast1", "Open", 0), ("msg_hub", "Display", 0),
                            ("snd_hub_alarm", "StopSound", 0), ("hub_crack", "Disable", 0.1), ("hub_alarm_light", "TurnOff", 0),
                            ("maint_open", "Enable", 0), ("ff_cooling", "Disable", 0),
                            ("tur_lobby", "Disable", 0),
                            ("cy_lobbyturrets_off", "Disable", 0), ("cy_lobbyturrets_on", "Disable", 0)]:
        r.out("OnTrigger", tgt, inp, delay=delay)
    # blast doors between lobby and service lobby (open when the hub falls)
    kit.gate(m, "blast1", 1860, -128, 0, 1884, 128, 144, "metal/metalgate001a", speed=40, lip=8)

    # ============================================================ OBJ 3: core + shield
    core = m.brush_ent("func_breakable", ngon(4128, 0, 64, 12, -384, -96, "metal/metalwall003a"),
                       targetname="core", health="2600", material="2", damagefilter="f_nobody", explosion="0",
                       ExplodeDamage="0", ExplodeRadius="0", explodemagnitude="0", PerformanceMode="2",
                       minhealthdmg="0", spawnobject="0", nodamageforces="1", physdamagescale="0", spawnflags="0",
                       origin="4128 0 -240")
    core.out("OnHealthChanged", "obj_core", "SetHealth")
    core.out("OnBreak", "core_done", "Trigger")
    shield = m.brush_ent("func_brush", ngon(4128, 0, 112, 16, -384, -48, "effects/com_shield003a"),
                         targetname="core_shield", Solidity="2", solidbsp="0", StartDisabled="0", spawnflags="2",
                         InputFilter="0", rendermode="0", disableshadows="1", vrad_brush_cast_shadows="0")
    # timer relay for the temporary cyberspace drop
    r = relay(m, "shield_timer", 4000, 200, 0)
    r.out("OnTrigger", "shield_up", "Trigger", delay=40)
    r = relay(m, "shield_down", 4000, 220, 0)
    for tgt, inp, delay, p in [("core_shield", "Disable", 0, ""), ("core", "SetDamageFilter", 0, "f_punks"),
                               ("obj_shield", "SetPunks", 0, ""), ("msg_shield_down", "Display", 0, ""),
                               ("shield_timer", "CancelPending", 0, ""), ("shield_timer", "Trigger", 0.05, ""),
                               ("snd_shield", "PlaySound", 0, ""), ("vault_alarm", "TurnOn", 0, "")]:
        r.out("OnTrigger", tgt, inp, param=p, delay=delay)
    r = relay(m, "shield_up", 4000, 240, 0)
    for tgt, inp, delay, p in [("core_shield", "Enable", 0, ""), ("core", "SetDamageFilter", 0, "f_nobody"),
                               ("obj_shield", "SetCorps", 0, ""), ("msg_shield_up", "Display", 0, ""),
                               ("shield_timer", "CancelPending", 0, ""), ("vault_alarm", "TurnOff", 0, "")]:
        r.out("OnTrigger", tgt, inp, param=p, delay=delay)
    m.ent("ambient_generic", (4128, 0, 0), targetname="snd_shield", message="ambient/energy/whiteflash.wav",
          health="10", radius="2500", spawnflags="48", pitch="100", pitchstart="100")
    # two shield emitters: destroying both kills the shield for good
    cnt = m.ent("math_counter", (4000, 260, 0), targetname="emitter_count", min="0", max="2", startvalue="0")
    cnt.out("OnHitMax", "shield_dead", "Trigger")
    for i, (x, y) in enumerate(((3790, -480), (3790, 480))):
        e = m.brush_ent("func_breakable", box(x - 24, y - 24, -128, x + 24, y + 24, 16, "metal/metalwall003a"),
                        targetname=f"emitter{i}", health="900", material="2", damagefilter="f_punks",
                        explosion="1", ExplodeDamage="0", ExplodeRadius="0", PerformanceMode="0", spawnflags="0",
                        minhealthdmg="0", origin=f"{x} {y} -56")
        e.out("OnBreak", "emitter_count", "Add", param="1")
        e.out("OnBreak", "msg_emitter", "Display")
    r = relay(m, "shield_dead", 4000, 280, 0, once=True)
    for tgt, inp, delay, p in [("shield_up", "Disable", 0, ""), ("shield_timer", "CancelPending", 0, ""),
                               ("core_shield", "Disable", 0.05, ""), ("core", "SetDamageFilter", 0.05, "f_punks"),
                               ("obj_shield", "SetPunks", 0.05, ""), ("msg_shield_dead", "Display", 0, ""),
                               ("vault_alarm", "TurnOn", 0.1, "")]:
        r.out("OnTrigger", tgt, inp, param=p, delay=delay)
    r = relay(m, "core_done", 4000, 300, 0, once=True)
    r.out("OnTrigger", "obj_core", "SetPunks")
    r.out("OnTrigger", "msg_core", "Display")
    r.out("OnTrigger", "core_boom", "Explode")
    m.ent("env_explosion", (4128, 0, -200), targetname="core_boom", iMagnitude="0", spawnflags="1", fireballsprite="sprites/zerogxplode.spr")
    # vault + lobby turrets
    for y in (-256, 256):
        turret(m, "tur_vault", 4128, y, 318, 180)
    for y in (-448, 448):
        turret(m, "tur_lobby", 1216, y, 446, 90 if y < 0 else 270)
    # A freshly spawned npc_turret_ceiling ignores all damage until it receives Enable (verified in-game);
    # after that one boltgun bolt deals 82, so 800 hp = 10 bolts. Rebuilt turrets stay damageable.
    la = m.ent("logic_auto", (4000, 320, 0), spawnflags="0")
    for name in ("tur_plaza", "tur_lobby", "tur_vault"):
        la.out("OnMapSpawn", name, "Enable", delay=0.5)

    # maintenance door (server hall south) - opened from cyberspace, but only once the hub has fallen
    # (otherwise Punks could skip objective 2 and reach the vault early)
    kit.gate(m, "maint_door", 2560, -716, -128, 2688, -692, 32, "metal/metalgate001a", speed=80, lip=8)
    r = m.ent("logic_relay", (2624, -900, 0), targetname="maint_open", spawnflags="0", StartDisabled="1")
    r.out("OnTrigger", "maint_door", "Open")
    r.out("OnTrigger", "maint_door", "Close", delay=25)

    # --- jackpoints (meatspace -> cyberspace entry cameras)
    jack_terminal(m, "jp_hq", -5376, 512, -320, "-y", "cy_entry_punk")
    jack_terminal(m, "jp_hq2", -5632, 512, -320, "-y", "cy_entry_punk")
    jack_terminal(m, "jp_arcade", -2304, 640, 56, "+x", "cy_entry_punk")
    jack_terminal(m, "jp_hub", 1152, 976, 248, "+x", "cy_entry_mid", model="models/props/prop_jackin_dtrust.mdl")
    jack_terminal(m, "jp_lobby", 2432, -256, 248, "-x", "cy_entry_corp", model="models/props/prop_jackin_dtrust.mdl")
    jack_terminal(m, "jp_lobby2", 2432, 256, 248, "-x", "cy_entry_corp", model="models/props/prop_jackin_dtrust.mdl")
    jack_terminal(m, "jp_vault", 5056, 0, -72, "-x", "cy_entry_corp", model="models/props/prop_jackin_dtrust.mdl")

    # --- spectator / round cameras
    m.ent("info_player_start", (-800, -700, 520), angles="18 25 0")
    m.ent("info_camera_start", (-800, -700, 520), angles="18 25 0")
    m.ent("info_camera_corpswin", (-200, 400, 220), angles="8 -15 0")
    m.ent("info_camera_punkswin", (3800, 420, 120), angles="22 -40 0")

    return ents


PANELS = [
    {"name": "bi_gate_override", "type": "dys_screen", "title": "KURODA GATE CONTROL",
     "buttons": [("#dystopia_R_ManualOverride", "button1"), ("Abort Override", "button2")],
     "background": "vgui/screens/secorp_bg1"},
    {"name": "bi_cyber_gateturrets", "type": "dys_cyberscreen", "title": "#dystopia_R_TurretControl",
     "buttons": [("Disable", "button1"), ("Enable", "button2")],
     "background": "vgui/screens/cyberpanel_bg"},
    {"name": "bi_cyber_lobbyturrets", "type": "dys_cyberscreen", "title": "#dystopia_R_TurretControl",
     "buttons": [("Disable", "button1"), ("Enable", "button2")],
     "background": "vgui/screens/cyberpanel_bg"},
    {"name": "bi_cyber_core", "type": "dys_cyberscreen", "title": "BLACK ICE SHIELD",
     "buttons": [("#dystopia_R_DisableCore", "button1"), ("#dystopia_R_EnableCore", "button2")],
     "background": "vgui/screens/cyberpanel_bg"},
    {"name": "bi_cyber_vault", "type": "dys_cyberscreen", "title": "#dystopia_R_TurretControl",
     "buttons": [("Enable", "button1"), ("Disable", "button2"), ("#dystopia_R_CaptureTurrets", "button3")],
     "background": "vgui/screens/cyberpanel_bg"},
    {"name": "bi_cyber_maint", "type": "dys_cyberscreen", "title": "MAINTENANCE ACCESS",
     "buttons": [("#dystopia_R_OpenDoors", "button1"), ("#dystopia_R_LockDoor", "button2")],
     "background": "vgui/screens/cyberpanel_bg"},
]
