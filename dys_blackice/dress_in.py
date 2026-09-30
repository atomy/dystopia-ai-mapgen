"""Interior dressing for dys_blackice: metro, tower lobby, hub, spawns, server hall, vault."""
from __future__ import annotations

import random

import kit
from dress import neon, panel, blade, wall_overlay, floor_overlay, wall_lamp, FACING
from vmflib import VMF, Tex, box, ngon, NODRAW


def light_panel(m: VMF, cx, cy, z, w=64, d=64, mat="vaccinert/dys_vaccleanlight", color=(220, 235, 255), bright=375, style=None):
    """Recessed ceiling light panel at ceiling height z + light below."""
    m.detail(box(cx - w / 2, cy - d / 2, z - 4, cx + w / 2, cy + d / 2, z, {"all": "metal/metalwall003a", "bottom": mat}))
    kit.light(m, cx, cy, z - 24, color=color, bright=bright, style=style)


def tube(m: VMF, x, y, zc, along="x", color=(190, 230, 215), bright=24, style=None):
    """Hanging fluorescent tube fixture (model) + light."""
    kit.prop(m, "models/props_wasteland/prison_flourescentlight002b.mdl", x, y, zc, yaw=90 if along == "x" else 0,
             solid=0, on_floor=False, disableshadows="1")
    kit.light(m, x, y, zc - 20, color=color, bright=bright, style=style)


def rail_glass(m: VMF, x0, y0, x1, y1, z, h=40):
    """Glass balustrade with metal cap along an axis-aligned line."""
    if abs(x1 - x0) >= abs(y1 - y0):
        kit.glass(m, min(x0, x1), y0 - 1, z, max(x0, x1), y0 + 1, z + h - 4, mat="glass/glasswindow007a")
        m.detail(box(min(x0, x1), y0 - 3, z + h - 4, max(x0, x1), y0 + 3, z + h, "metal/metalwall003a"))
    else:
        kit.glass(m, x0 - 1, min(y0, y1), z, x0 + 1, max(y0, y1), z + h - 4, mat="glass/glasswindow007a")
        m.detail(box(x0 - 3, min(y0, y1), z + h - 4, x0 + 3, max(y0, y1), z + h, "metal/metalwall003a"))
    # stop players from hopping onto the thin cap
    kit.clip_box(m, min(x0, x1) - (3 if x0 == x1 else 0), min(y0, y1) - (3 if y0 == y1 else 0), z + h,
                 max(x0, x1) + (3 if x0 == x1 else 0), max(y0, y1) + (3 if y0 == y1 else 0), z + h + 24)


def round_pillar(m: VMF, x, y, z0, z1, r=24, mat="vaccinert/dys_vactrim2", ring="vaccinert/dys_vactrim3light"):
    m.detail(ngon(x, y, r, 12, z0, z1, {"all": mat}))
    if ring:
        m.detail(ngon(x, y, r + 2, 12, z1 - 20, z1 - 12, {"all": ring}))


# ============================================================================ metro

def metro(b):
    m: VMF = b.m
    rng = random.Random(21)
    F = -384  # platform floor
    # pilasters on the back wall + edge columns
    for x in range(-5952, -4500, 256):
        m.detail(box(x - 20, 480, F, x + 20, 512, -64, {"all": "tile/tilewall006b", "bottom": NODRAW}))
    for x in (-5760, -5376, -4992, -4672):
        m.detail(box(x - 20, -236, F, x + 20, -196, -64, {"all": "tile/tilewall006b", "bottom": NODRAW}))
    # platform edge hazard strip (walkable, 2u)
    m.detail(box(-6016, -256, F, -4480, -236, F + 2, {"all": "concrete/concretewall008a",
                                                      "top": Tex("props/hazardstrip001a", scale=0.3125)}))
    # rails in the track bed, running on into both tunnels
    tw, te = b.TUNNEL_W, b.TUNNEL_E
    for y in (-520, -376):
        m.detail(box(tw + 8, y - 3, -448, te - 8, y + 3, -440, "metal/metaltrack001a"))
    # tunnels: sleepers every 64u, dim lamps that fade out, black far ends
    for x in range(int(tw) + 32, int(te) - 32, 64):
        if -6016 <= x <= -4480:
            continue
        m.detail(box(x - 8, -560, -448, x + 8, -336, -444, "concrete/concretefloor008a"))
    for x in (-6400, -7000, -4050, -3550):
        wall_lamp(m, x, -256, -250, "-y", (255, 120, 60), bright=45, glow=0.15)
    for x in (tw, te - 8):
        m.detail(box(x, -640, -448, x + 8, -256, -192, "tools/toolsblack"))
    # derelict train car on the tracks
    cx0, cx1, cy0, cy1 = -5600, -4880, -600, -296
    body = {"all": "metal/metalwall002a", "top": "metal/metalwall003a"}
    m.detail(box(cx0, cy0, -440, cx1, cy1, -344, body))                         # lower body
    m.detail(box(cx0, cy0, -280, cx1, cy1, -216, body))                         # roof band
    for x in range(cx0, cx1, 120):                                              # window posts
        m.detail(box(x, cy0, -344, x + 16, cy1, -280, "metal/metalwall002a"))
    kit.glass(m, cx0, cy1 - 3, -344, cx1, cy1 - 1, -280, mat="glass/glasswindow007a")
    kit.glass(m, cx0, cy0 + 1, -344, cx1, cy0 + 3, -280, mat="glass/glasswindow007a")
    kit.light(m, (cx0 + cx1) / 2, (cy0 + cy1) / 2, -300, color=(255, 200, 120), bright=100, style=10)
    # ceiling fluorescent rows (a few flicker)
    for i, x in enumerate(range(-5888, -4600, 256)):
        for y in (40, 320):
            tube(m, x, y, -72, style=10 if (i * 7 + y) % 5 == 0 else None)
    # red emergency lamps at the tunnel mouths
    for x in (-6096, -4400):
        wall_lamp(m, x, -256, -236, "-y", (255, 30, 20), bright=110)
    # signage
    neon(m, -4736, 510, -276, -148, "-y", 128, "neon/s_neon_monorail", (80, 200, 255), bright=240, reach=260)
    for x in (-5376, -5632):
        neon(m, x, 510, -250, -218, "-y", 96, "detonate/exo_pubjipneon", (80, 255, 120), bright=120, reach=150, sprite=False)
    # lintel over the stairwell arch carries the station sign (in front of the spawn forcefield)
    m.detail(box(-4480, -192, -160, -4464, 192, -64, {"all": "tile/tilewall006b", "bottom": "concrete/concreteceiling004a"}))
    panel(m, -4480, 0, -150, -118, "-x", 128, "props/sign_trainstation03", depth=2)
    kit.light(m, -4520, 0, -130, color=(200, 220, 255), bright=135)
    # benches, bins, a vending machine
    for x in (-5888, -5504, -5120 + 256, -4864):
        kit.prop(m, "models/props_trainstation/bench_indoor001a.mdl", x, 470, F, yaw=90, solid=6)
    kit.prop(m, "models/props/dys_vendingmachine01.mdl", -4580, 478, F, yaw=270, solid=6)
    for (x, y) in [(-5990, 300), (-4520, -120)]:
        kit.prop(m, "models/props_junk/trashbin01a.mdl", x, y, F, yaw=rng.randint(0, 359), solid=6)
    for (x, y) in [(-5300, -500), (-4700, -560), (-5900, -420)]:
        kit.prop(m, "models/props_junk/garbage256_composite001a.mdl", x, y, -448, yaw=rng.randint(0, 359), solid=0)
    # graffiti & posters on the tiles
    for (x, mat) in [(-5760, "graffiti/decal_graffiti_space"), (-5008, "graffiti/decal_graffiti_vice"),
                     (-4880, "decals/decal_posters002a"), (-6000 + 40, "graffiti/decal_graffiti_rage")]:
        wall_overlay(m, mat, x, 512, F + 150, "-y", 128, 128)
    # stairwell: blue accent lights up the flight (stairs rise 1:2 from x=-4448)
    for x in range(-4400, -3700, 128):
        kit.light(m, x, 170, -384 + (x + 4448) / 2 + 96, color=(90, 170, 255), bright=135)
    # maintenance tunnel: caged lamps, then up the flight (rises 1:2 from x=-4736)
    wall_lamp(m, -4992, 780, -270, "-x", (255, 190, 120), bright=120)
    for x in (-4600, -4300, -4050):
        wall_lamp(m, x, 1152, -384 + (x + 4736) / 2 + 110, "-y", (255, 190, 120), bright=120)


# ============================================================================ tower lobby

def lobby(b):
    m: VMF = b.m
    # pillars along mezzanine edges, full height
    for x in (704, 960, 1472):
        round_pillar(m, x, 480, 0, 448)
        round_pillar(m, x, -480, 0, 448)
    for y in (-320, 320):
        round_pillar(m, 1600, y, 0, 448)
    # glass balustrades (gaps for the stairs)
    rail_glass(m, 576, 484, 1152, 484, 192)
    rail_glass(m, 1280, 484, 1600, 484, 192)
    rail_glass(m, 576, -484, 1152, -484, 192)
    rail_glass(m, 1280, -484, 1600, -484, 192)
    rail_glass(m, 1596, -480, 1596, 480, 192)
    # reception desk
    m.detail(box(900, -160, 0, 964, 160, 42, {"all": "vaccinert/dys_vacextwall4", "top": "dys_cybernetic/floor_black_glossy"}))
    m.detail(box(964, -160, 0, 1040, -128, 42, {"all": "vaccinert/dys_vacextwall4", "top": "dys_cybernetic/floor_black_glossy"}))
    m.detail(box(964, 128, 0, 1040, 160, 42, {"all": "vaccinert/dys_vacextwall4", "top": "dys_cybernetic/floor_black_glossy"}))
    panel(m, 899, 0, 6, 22, "-x", 300, "vaccinert/dys_vactrim3light", depth=1)
    for y in (-80, 0, 80):
        kit.prop(m, "models/props/monitor01.mdl", 940, y, 42, yaw=180, solid=0)
        kit.prop(m, "models/spire/s_chair1a.mdl", 1000, y, 0, yaw=180, solid=6)
    kit.light(m, 960, 0, 120, color=(255, 220, 180), bright=205)
    # Kuroda logo above the gate (inside), elevators on the north/south walls
    neon(m, 578, 0, 272, 368, "+x", 384, "blackice/kuroda_wide", (255, 70, 80), bright=205, reach=300, sprite=False)
    for (x, y, fac) in [(704, 766, "-y"), (864, 766, "-y"), (704, -766, "+y"), (864, -766, "+y")]:
        panel(m, x, y, 0, 128, fac, 96, "vaccinert/dys_vacdoor7_fixed", depth=2)
        kit.light(m, x, y + (-20 if fac == "-y" else 20), 150, color=(120, 220, 255), bright=85)
    # ceiling light grid over the atrium + under the mezzanines
    for x in (768, 1024, 1280):
        for y in (-256, 0, 256):
            light_panel(m, x, y, 448, bright=410)
    for x in (704, 960, 1216, 1472):
        for y in (-624, 624):
            light_panel(m, x, y, 176, w=48, d=48, bright=155)
    for y in (-320, 0, 320):
        light_panel(m, 1728, y, 176, w=48, d=48, bright=155)
    # plants by the entrance
    for (x, y) in [(640, -300), (640, 300), (1520, -680), (1520, 680)]:
        m.detail(box(x - 28, y - 28, 0, x + 28, y + 28, 24, {"all": "vaccinert/dys_vacextwall4", "top": "nature/dirtfloor006a"}))
        kit.prop(m, "models/props_foliage/shrub_01a.mdl", x, y, 24, solid=0, fade=(1500, 2000))
    # mezzanine seating
    for (x, y, yaw) in [(720, 640, 0), (870, 640, 180), (720, -640, 0), (870, -640, 180)]:
        kit.prop(m, "models/spire/s_chair1b.mdl", x, y, 192, yaw=yaw, solid=6)
    # security hub: node screens, desks, sign, alarm light
    for (x, mat) in [(1216, "vaccinert/dys_camnode"), (1312, "vaccinert/dys_turretnode")]:
        panel(m, x, 1150, 240, 320, "-y", 80, mat, depth=2)
    for (y, mat) in [(848, "vaccinert/dys_mainnode"), (1088, "vaccinert/dys_corenode")]:   # east wall
        panel(m, 1662, y, 240, 320, "-x", 80, mat, depth=2)
    kit.prop(m, "models/props_wasteland/controlroom_desk001a.mdl", 1248, 1080, 192, yaw=270, solid=6)
    kit.prop(m, "models/props_wasteland/controlroom_monitor001a.mdl", 1248, 1090, 226, yaw=270, solid=0)
    panel(m, 1408, 766, 332, 396, "-y", 128, "vaccine2/vac_sign9", depth=2)
    kit.light(m, 1408, 740, 360, color=(120, 200, 255), bright=135)
    for x in (1280, 1536):
        light_panel(m, x, 976, 400, bright=270)
    kit.light(m, 1408, 1000, 360, color=(255, 30, 30), bright=475, name="hub_alarm_light",
              spawnflags="1")
    # corps spawn: lockers + lights
    for y in range(-448, 449, 64):
        if abs(y) < 96 or 160 < abs(y) < 352:      # keep the jack-in terminals at y +-256 clear
            continue
        kit.prop(m, "models/props_lab/lockers.mdl", 2410, y, 192, yaw=180, solid=6)
    for (x, y) in [(2000, -256), (2000, 256), (2300, 0)]:
        light_panel(m, x, y, 448, bright=305)
    neon(m, 2430, 0, 320, 416, "-x", 384, "blackice/kuroda_wide", (255, 70, 80), bright=135, reach=240, sprite=False)
    # service lobby: crates + hazard framing around the blast doors
    for (x, y, yaw) in [(2000, -420, 0), (2060, -420, 10), (2300, 420, 0), (2350, 360, 30)]:
        kit.prop(m, "models/termi/t_dtrustcrate48.mdl", x, y, 0, yaw=yaw, solid=6)
    kit.prop(m, "models/termi/t_dtrustcrate128.mdl", 2250, -430, 0, yaw=0, solid=6)
    for y in (-136, 136):
        m.detail(box(1888, y - 8, 0, 1904, y + 8, 152, Tex("props/hazardstrip001a", scale=0.25)))
    for (x, y) in [(2000, 0), (2300, -250), (2300, 250)]:
        kit.light(m, x, y, 140, color=(255, 214, 160), bright=240)
    # maintenance corridor + shaft
    for x in range(1300, 2700, 256):
        kit.light(m, x, -1088, 300, color=(255, 180, 110), bright=100)
    kit.light(m, 2624, -900, 100, color=(255, 180, 110), bright=135)


# ============================================================================ server hall + vault

def server_vault(b):
    m: VMF = b.m
    rng = random.Random(33)
    F = -128
    rack_tex = Tex("t_asmwalls/t_techsupport01", scale=0.125)
    # server rack rows (two segments per row, cross aisle at x 3072..3200)
    for yc in (-416, -160, 160, 416):
        for (x0, x1) in ((2688, 3072), (3200, 3584)):
            m.detail(box(x0, yc - 24, F, x1, yc + 24, F + 128,
                         {"all": "metal/metalwall002a", "north": rack_tex, "south": rack_tex, "top": "metal/metalwall003a"}))
            for x in range(x0 + 48, x1, 96):         # status LEDs
                kit.sprite(m, x, yc + 26, F + 100, color=rng.choice([(60, 255, 120), (80, 160, 255), (60, 255, 120)]),
                           scale=0.08, alpha=200)
                kit.sprite(m, x, yc - 26, F + 100, color=(80, 160, 255), scale=0.08, alpha=200)
    # blue aisle lighting + white work lights
    for x in (2752, 3136, 3520):
        for y in (-560, -288, 0, 288, 560):
            kit.light(m, x, y, 150, color=(90, 150, 255), bright=155)
    for x in (2880, 3392):
        light_panel(m, x, 0, 192, w=128, d=32, mat="dys_cybernetic/ceiling_lights", color=(210, 230, 255), bright=240)
    # cable trays along the ceiling
    for y in (-288, 288):
        for x in (2600, 3112):
            kit.prop(m, "models/props_pipes/pipeset08d_512_001a.mdl", x + 256, y, 176, yaw=0, solid=0, on_floor=False)
    # rack models by the entrance + cooling tank
    for y in (-560, 560):
        kit.prop(m, "models/twincannon/dys_serverrack.mdl", 2600, y, F, yaw=0 if y < 0 else 180, solid=6)
    kit.prop(m, "models/props_wasteland/horizontalcoolingtank04.mdl", 3520, 580, F + 61, yaw=0, solid=6, on_floor=False)

    # ---------------- vault
    cx, cy = 4128, 0
    # animated reactor core (the func_breakable made in gameplay uses this material via retexture)
    for e in m.entities:
        if e.name == "core":
            for s in e.solids:
                s.retexture(lambda side: "dys_cybernetic/cybersyn_core_ani" if abs(side.normal[2]) < 0.5 else "metal/metalcombine001")
        if e.name == "core_shield":
            for s in e.solids:
                s.retexture(lambda side: "vaccine/vacshield_002")
        if e.name and e.name.startswith("emitter"):
            for s in e.solids:
                s.retexture(lambda side: "vaccinert/dys_vactrim3light" if abs(side.normal[2]) < 0.5 else "metal/metalcombine001")
    # glowing floor ring under the core
    m.detail(box(cx - 224, cy - 224, -384, cx + 224, cy + 224, -382,
                 {"all": "metal/metalwall003a", "top": Tex("dys_cybernetic/cyber_floor_ring_ani", scale=1.75)}))
    # energy conduit from core to ceiling
    m.detail(ngon(cx, cy, 20, 8, -40, 320, {"all": Tex("vaccine/coresfx2", scale=0.25)}))
    m.detail(ngon(cx, cy, 72, 12, 280, 320, {"all": "metal/metalcombine001"}))
    kit.light(m, cx, cy, -200, color=(100, 220, 255), bright=885)
    kit.light(m, cx, cy, 200, color=(100, 220, 255), bright=305)
    kit.sprite(m, cx, cy, -240, color=(120, 230, 255), scale=1.4, alpha=90)
    # emitter glow caps
    for (x, y) in ((3790, -480), (3790, 480)):
        kit.sprite(m, x, y, 24, color=(120, 230, 255), scale=0.6, alpha=160)
        kit.light(m, x, y, 40, color=(100, 220, 255), bright=205)
    # railings on the walkway edges (the stairs along the walls have their own balustrades)
    rail_glass(m, 3904, -224, 3904, 224, -128)
    rail_glass(m, 4352, -224, 4352, 224, -128)
    rail_glass(m, 4384, -512, 4384, -224, -128)
    rail_glass(m, 3872, 224, 3872, 512, -128)
    # alarm lights (off until the shield drops)
    for (x, y) in ((3760, -480), (3760, 480), (4496, -480), (4496, 480)):
        kit.light(m, x, y, 200, color=(255, 30, 30), bright=410, name="vault_alarm", spawnflags="1")
    for (x, y) in ((3800, -300), (3800, 300), (4450, -300), (4450, 300)):
        light_panel(m, x, y, 320, bright=205)
    # signage
    panel(m, 3746, -384, 40, 104, "+x", 128, "vaccine2/vac_sign3", depth=2)
    panel(m, 3746, 384, 40, 104, "+x", 128, "vaccine2/vac_sign3", depth=2)
    neon(m, 4510, 0, 120, 184, "-x", 128, "blackice/ice_warning", (255, 40, 40), bright=135, reach=200, sprite=False)
    # final corps spawn: monitors + lights
    for y in (-300, 300):
        kit.prop(m, "models/props_wasteland/controlroom_desk001a.mdl", 5000, y, -128, yaw=180, solid=6)
    for (x, y) in [(4700, -200), (4700, 200), (4950, 0)]:
        light_panel(m, x, y, 128, bright=270)


# ============================================================================ alternative routes

def routes(b):
    """North service route to the hub and the cooling route from the hub to the vault."""
    m: VMF = b.m
    # north service door: hazard frame + sign on the plaza side, lights up the stair hall
    for y in (1016, 1152):
        m.detail(box(440, y, 0, 448, y + 8, 136, Tex("props/hazardstrip001a", scale=0.25)))
    m.detail(box(440, 1016, 128, 448, 1160, 136, Tex("props/hazardstrip001a", scale=0.25)))
    panel(m, 448, 1088, 150, 182, "-x", 128, "vaccine2/vac_sign9", depth=2)         # SECURITY
    for x in (640, 832, 1024):
        kit.light(m, x, 1088, 120 + (x - 704) // 2 if x > 704 else 110, color=(255, 214, 160), bright=150)
    # duct from the hub to the cooling plant: caged lamps on the south wall
    for x in (1760, 2016, 2272):
        wall_lamp(m, x, 1152, 290, "+y", (255, 180, 110), bright=180)
    for x in (2432, 2688, 2880):
        wall_lamp(m, x, 1152, 192 - (x - 2304) // 2 + 90, "+y", (255, 180, 110), bright=180)
    # cooling plant: tanks as cover, transformer boxes, cold blue light
    F = -128
    # (the strip y 1152..1280 at the foot of the stairs stays clear)
    for (x, y) in ((3200, 1040), (3520, 1040)):
        kit.prop(m, "models/props_wasteland/coolingtank01.mdl", x, y, F, solid=6)
    kit.prop(m, "models/props_wasteland/horizontalcoolingtank04.mdl", 3480, 880, F + 61, yaw=0, solid=6, on_floor=False)
    for (x, y) in ((3040, 800), (3660, 1216)):          # (the approach to the server-hall door stays open)
        kit.prop(m, "models/props_c17/substation_stripebox01a.mdl", x, y, F, solid=6)
    for x in (3072, 3328, 3584):
        for y in (864, 1152):
            kit.light(m, x, y, 200, color=(120, 190, 255), bright=200)
    panel(m, 3710, 1000, 60, 124, "-x", 128, "vaccine2/vac_sign3", depth=2)         # CORE ROOM, by the vault corridor
    # corridor to the vault
    for x in (3840, 4096, 4352):
        wall_lamp(m, x, 896, 0, "-y", (120, 190, 255), bright=150)
    kit.light(m, 4448, 640, -40, color=(120, 190, 255), bright=150)
