"""Cyberspace for dys_blackice: a sealed node network north of the city (y 3300..6100).

      [G gate node] ===== top link ===== [C core node]
            |                 |                 |
      [P punk entry] ====== [M mid] ====== [E corp entry]
"""
from __future__ import annotations

import kit
from gameplay import screen, PUNKS, CORPS
from vmflib import VMF, box, NODRAW, TRIGGER

ICE_MAT = "cyberspace/scroller_gibberish"
FLOOR_MAT = "termitex/cysp_floor04_blue"

NODES = {
    #        x0     y0    x1    y1
    "P": (-2048, 3840, -1536, 4352),
    "M": (-256, 3840, 256, 4352),
    "E": (1536, 3840, 2048, 4352),
    "G": (-2048, 5120, -1536, 5632),
    "C": (1536, 5120, 2048, 5632),
}
NODE_Z = (0, 384)
TUBES = [
    (-1856, 4352, -1728, 5120),   # P-G
    (-1536, 4032, -256, 4160),    # P-M
    (256, 4032, 1536, 4160),      # M-E
    (1728, 4352, 1856, 5120),     # E-C
    (-1536, 5312, 1536, 5440),    # G-C
    (-64, 4352, 64, 5312),        # M-top link
]
TUBE_Z = (0, 192)
NODE_STYLE = {"P": "cy_green", "M": "cy_yellow", "E": "cy_purple", "G": "cy_purple", "C": "cy_black"}


def shell(b):
    S, A = b.solid, b.air
    S(-2560, 3328, -256, 2560, 6144, 768, "cyrock")
    for k, (x0, y0, x1, y1) in NODES.items():
        A(x0, y0, NODE_Z[0], x1, y1, NODE_Z[1], NODE_STYLE[k])
    for (x0, y0, x1, y1) in TUBES:
        A(x0, y0, TUBE_Z[0], x1, y1, TUBE_Z[1], "cy_tube")


def ice(m: VMF, name, x0, y0, z0, x1, y1, z1, team=CORPS, hackable=True):
    return m.brush_ent("cyber_ice", box(x0, y0, z0, x1, y1, z1, ICE_MAT), targetname=name, team=str(team),
                       spawnflags="9" if hackable else "1", WedgeDelay="5")


def add(b):
    m: VMF = b.m
    # walkable cyber floors (brush entities over the world floor)
    for k, (x0, y0, x1, y1) in NODES.items():
        m.brush_ent("cyber_floor", box(x0, y0, 0, x1, y1, 16, {"all": NODRAW, "top": FLOOR_MAT}))
    for (x0, y0, x1, y1) in TUBES:
        m.brush_ent("cyber_floor", box(x0, y0, 0, x1, y1, 16, {"all": NODRAW, "top": FLOOR_MAT}))

    # entry cameras (decker spawn points in cyberspace)
    for name, (x, y), yaw in [("cy_entry_punk", (-1792, 3968), 90), ("cy_entry_mid", (0, 3968), 90),
                              ("cy_entry_corp", (1792, 3968), 90)]:
        m.ent("point_camera", (x, y, 88), targetname=name, angles=f"0 {yaw} 0", FOV="90", renderTarget="camera1",
              UseScreenAspectRatio="0", fogEnable="0", fogColor="0 0 0", fogStart="2048", fogEnd="4096", spawnflags="0")

    # --- gate node: gate lock + plaza turrets (north wall, facing south)
    gx0, gy0, gx1, gy1 = NODES["G"]
    s = screen(m, "dys_cyberscreen", "cy_gate_screen", "bi_cyber_gate", -1888, gy1, 112, "-y", w=64, h=64,
               team=str(CORPS), protection="1", icename="ice_gate")
    s.out("Button1", "cy_gate_fp", "TestActivator")
    ice(m, "ice_gate", -1952, gy1 - 48, 64, -1824, gy1 - 16, 176)
    s = screen(m, "dys_cyberscreen", "cy_plaza_screen", "bi_cyber_plaza", -1696, gy1, 112, "-y", w=64, h=64,
               team=str(CORPS), protection="1", icename="ice_plaza")
    s.out("Button1", "tur_plaza", "Enable")
    s.out("Button2", "tur_plaza", "Disable")
    s.out("Button3", "tur_plaza", "SetTeamTouched")
    ice(m, "ice_plaza", -1760, gy1 - 48, 64, -1632, gy1 - 16, 176)

    # --- core node: core shield (encrypted) + vault turrets
    cx0, cy0, cx1, cy1 = NODES["C"]
    s = screen(m, "dys_cyberscreen", "cy_core_screen", "bi_cyber_core", 1696, cy1, 112, "-y", w=64, h=64,
               team=str(CORPS), protection="2", icename="ice_core")
    s.out("Button1", "cy_core_fp", "TestActivator")
    s.out("Button2", "cy_core_fc", "TestActivator")
    ice(m, "ice_core", 1632, cy1 - 48, 64, 1760, cy1 - 16, 176)
    f = kit.filter_team(m, "cy_core_fp", PUNKS)
    f.kv["origin"] = "1700 5500 64"
    f.out("OnPass", "shield_down", "Trigger")
    f = kit.filter_team(m, "cy_core_fc", CORPS)
    f.kv["origin"] = "1700 5500 96"
    f.out("OnPass", "shield_up", "Trigger")
    s = screen(m, "dys_cyberscreen", "cy_vault_screen", "bi_cyber_vault", 1888, cy1, 112, "-y", w=64, h=64,
               team=str(CORPS), protection="1", icename="ice_vault")
    s.out("Button1", "tur_vault", "Enable")
    s.out("Button2", "tur_vault", "Disable")
    s.out("Button3", "tur_vault", "SetTeamTouched")
    ice(m, "ice_vault", 1824, cy1 - 48, 64, 1952, cy1 - 16, 176)

    # --- mid node: maintenance door
    mx0, my0, mx1, my1 = NODES["M"]
    s = screen(m, "dys_cyberscreen", "cy_maint_screen", "bi_cyber_maint", 160, my1, 112, "-y", w=64, h=64,
               team=str(CORPS), protection="1", icename="ice_maint")
    s.out("Button1", "maint_open", "Trigger")
    s.out("Button2", "maint_door", "Close")
    ice(m, "ice_maint", 96, my1 - 48, 64, 224, my1 - 16, 176)

    # energy crystals
    for (x, y) in [(-1792, 4224), (0, 4224), (1792, 4224), (-1792, 5376), (1792, 5376), (0, 5376), (-800, 5376), (800, 5376)]:
        m.ent("cyber_crystal", (x, y, 40), EnergyRestore="10", RespawnDelay="30", model="models/props/cyber_shard.mdl")

    # ---- art: rotating circlet rings, bitstream columns on tube walls, terminal frames
    from dress import panel
    from vmflib import Tex
    for k, (x0, y0, x1, y1) in NODES.items():
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        ring = box(cx - 160, cy - 160, 300, cx + 160, cy + 160, 301,
                   {"all": NODRAW, "top": Tex("cyspfinal/circlet1", scale=320 / 512), "bottom": Tex("cyspfinal/circlet1", scale=320 / 512)})
        m.brush_ent("func_rotating", ring, origin=(cx, cy, 300.5), maxspeed="24", fanfriction="20", spawnflags="65",
                    solidbsp="0", volume="0", dmg="0", rendermode="0")
    for (x0, y0, x1, y1) in TUBES:
        along_x = (x1 - x0) > (y1 - y0)
        n = int(((x1 - x0) if along_x else (y1 - y0)) // 384)
        for i in range(max(1, n)):
            if along_x:
                x = x0 + (i + 0.5) * (x1 - x0) / max(1, n)
                for (y, fac) in ((y1 - 1, "-y"), (y0 + 1, "+y")):
                    panel(m, x, y, 16, 176, fac, 96, "cyspfinal/bitstream1a", depth=1, cls="func_illusionary")
            else:
                y = y0 + (i + 0.5) * (y1 - y0) / max(1, n)
                for (x, fac) in ((x1 - 1, "-x"), (x0 + 1, "+x")):
                    panel(m, x, y, 16, 176, fac, 96, "cyspfinal/bitstream1a", depth=1, cls="func_illusionary")
    # terminal frames behind every cyberscreen (wall-mounted slabs)
    for e in list(m.entities):
        if e.classname == "dys_cyberscreen":
            ox, oy, oz = map(float, e.kv["origin"].split())
            yaw = int(e.kv["angles"].split()[1])
            if yaw == 270:   # faces -y, spans +x from origin; 1u in front of the wall at oy + 1
                wy = oy + 1
                fm = {"all": "cyberspace/t_cyspwall1_black", "south": "termitex/cysp_scroller02"}
                m.detail([box(ox - 10, wy - 5, oz - 10, ox + 74, wy, oz, fm),          # bottom bar
                          box(ox - 10, wy - 5, oz + 64, ox + 74, wy, oz + 74, fm),     # top bar
                          box(ox - 10, wy - 5, oz, ox, wy, oz + 64, fm),               # left bar
                          box(ox + 64, wy - 5, oz, ox + 74, wy, oz + 64, fm)])         # right bar
    # core node: BLACK ICE warning + red plasma pillars
    cx0, cy0, cx1, cy1 = NODES["C"]
    panel(m, (cx0 + cx1) / 2, cy0 + 1, 220, 348, "+y", 256, "blackice/ice_warning", depth=1, cls="func_illusionary")
    for (x, y) in ((cx0 + 64, cy0 + 64), (cx1 - 64, cy0 + 64)):
        m.detail(box(x - 24, y - 24, 16, x + 24, y + 24, 384, "dys_nameless/redplasma2"))

    # light + soundscapes
    for k, (x0, y0, x1, y1) in NODES.items():
        kit.light(m, (x0 + x1) / 2, (y0 + y1) / 2, 300, color=(160, 120, 255), bright=150)
        m.ent("env_soundscape", ((x0 + x1) / 2, (y0 + y1) / 2, 160), radius="900",
              soundscape={"P": "CyberSpace.Node1", "M": "CyberSpace.Node2", "E": "CyberSpace.Node3",
                          "G": "CyberSpace.Node2", "C": "CyberSpace.Node3"}[k], StartDisabled="0")
