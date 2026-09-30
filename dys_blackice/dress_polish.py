"""Polish pass: shop interiors, arcade, alleys, lobby hologram, clips."""
from __future__ import annotations

import random

import kit
from dress import neon, panel, blade, wall_overlay, floor_overlay, wall_lamp
from vmflib import VMF, Tex, box, NODRAW, PLAYERCLIP


def shops(b):
    m: VMF = b.m
    # --- noodle bar (x -3328..-2944, y 320..704, z 0..224), back passage x -3136..-3008
    for (x0, x1) in ((-3312, -3152), (-2992, -2960)):
        m.detail(box(x0, 600, 0, x1, 648, 42, {"all": "metal/metalwall017a", "top": "dys_cybernetic/floor_black_glossy"}))
    panel(m, -3232, 599, 8, 20, "-y", 150, "neon/dog_neon13", depth=1)
    for x in (-3290, -3240, -3190):
        kit.prop(m, "models/props_c17/chair_stool01a.mdl", x, 560, 0, yaw=90, solid=6)
    for x in (-3240, -3060):
        kit.prop(m, "models/props_c17/light_domelight02_on.mdl", x, 520, 222, solid=0, on_floor=False)
        kit.light(m, x, 520, 196, color=(255, 170, 110), bright=90)
        kit.sprite(m, x, 520, 213, color=(255, 170, 110), scale=0.25, alpha=120)
    neon(m, -3232, 702, 130, 194, "-y", 128, "neon/neon_thdsm", (255, 70, 90), bright=40, reach=160, sprite=False)
    # --- DATASMITH electronics (x -3072..-2560, y -704..-320), back door x -2688..-2560
    for y in (-660, -590, -520, -450):
        kit.prop(m, "models/props/cs_office/shelves_metal.mdl", -3056, y, 0, yaw=0, solid=6)
    m.detail(box(-2900, -560, 0, -2780, -520, 40, {"all": "vaccinert/dys_vacextwall4", "top": "metal/metalwall003a"}))
    for x in (-2872, -2808):
        kit.prop(m, "models/termi/t_monitor.mdl", x, -548, 40, yaw=90, solid=0)
        kit.prop(m, "models/props_c17/computer01_keyboard.mdl", x, -528, 40, yaw=90, solid=0)
    kit.light(m, -2816, -512, 190, color=(170, 210, 255), bright=110)
    neon(m, -2816, -702, 120, 184, "+y", 256, "neon/neon_datasmith", (255, 90, 200), bright=35, reach=150, sprite=False)
    # --- NetExcess arcade (punk fwd spawn, x -2304..-1792, y 384..896, z 0..288)
    for y in (440, 520, 600, 680, 760, 840):
        m.detail(box(-1840, y - 22, 0, -1796, y + 22, 96, {"all": "metal/metalwall002a", "top": "metal/metalwall003a"}))
        panel(m, -1841, y, 44, 84, "-x", 40, "adverts/adverts_cyberfight_001", depth=1, cls="func_illusionary")
        kit.sprite(m, -1846, y, 64, color=(255, 80, 220), scale=0.25, alpha=90)
    for (x, y) in ((-2176, 520), (-2176, 760), (-1920, 640)):
        kit.light(m, x, y, 250, color=(255, 90, 210), bright=80)
    for x in range(-2272, -1800, 128):
        panel(m, x, 894, 250, 262, "-y", 112, "neon/dog_neon8", depth=1)
    kit.light(m, -2048, 860, 250, color=(80, 220, 255), bright=60)


def alleys(b):
    m: VMF = b.m
    rng = random.Random(5)
    # fire escape grating panels + drain pipes on the rear facades of the market blocks
    for x in (-3300, -2900, -2500, -2100):
        for z in (224, 416, 608):
            if (x, z) == (-2500, 224):
                continue                # would hang over the fire-escape flight
            backed = [b.L.label_at(xx, 1020, z + 4) for xx in (x - 90, x, x + 90)]
            if not all(lab is not None and lab.kind == "solid" for lab in backed):
                continue                # no wall behind it (the roof walkway is open above z 320)
            m.brush_ent("func_brush", box(x - 96, 1024, z, x + 96, 1072, z + 8,
                                          {"all": "metal/metalwall003a", "top": "metal/metalfireescape002a"}),
                        Solidity="2", solidbsp="0", StartDisabled="0", spawnflags="2", InputFilter="0")
            kit.rail(m, x - 96, 1070, x + 96, 1070, z + 8, h=36, mat="metal/metalwall003a")
    # pipe bundles lie flat against solid wall (never across a door or passage); 243 wide, 511 tall
    for (x, y, fac) in [(-3700, 1024, "+y"), (-3050, 1216, "-y"), (-3450, -1024, "-y"), (-2950, -1024, "-y"),
                        (-2200, -1024, "-y"), (-1800, -1024, "-y")]:
        f = 1 if fac == "+y" else -1
        kit.prop(m, "models/props_pipes/pipecluster08d_006a.mdl", x, y + f * 7, 256, yaw=90, solid=0, on_floor=False)
    for (x, y, mat) in [(-3400, 1216, "graffiti/decal_graffiti_bash"), (-2700, 1216, "graffiti/decal_graffiti_sista"),
                        (-3000, -1216, "graffiti/decal_graffiti_die"), (-2200, -1216, "decals/decal_posters005a")]:
        wall_overlay(m, mat, x, y, 90, "-y" if y > 0 else "+y", 160, 160)
    for (x, y) in [(-3300, 1120), (-2500, 1140), (-3100, -1110), (-2400, -1120)]:
        floor_overlay(m, "overlays/puddle001a", x, y, 0, 200, 140, yaw=rng.randint(0, 180))
    # readable flank lighting: caged wall lamps over the back doors and along the walls
    for (x, y, fac, c) in [(-3800, 1216, "-y", (255, 150, 90)), (-3072, 1024, "+y", (120, 190, 255)),
                           (-2860, 1216, "-y", (255, 120, 60)), (-2350, 1216, "-y", (255, 120, 200)),
                           (-1856, 1024, "+y", (255, 170, 90)),
                           (-3700, -1216, "+y", (255, 150, 90)), (-3300, -1216, "+y", (255, 80, 160)),
                           (-2624, -1024, "-y", (120, 190, 255)), (-2200, -1216, "+y", (255, 170, 80)),
                           (-1900, -1216, "+y", (255, 120, 200))]:
        wall_lamp(m, x, y, 196, fac, c)
    for (x, y, fac) in [(-2600, 1214, "-y"), (-2000, 1214, "-y")]:
        neon(m, x, y, 150, 214, fac, 128, "decals/sign_arrow_tech", (90, 220, 255), bright=40, reach=160, sprite=False)


def tower_extras(b):
    m: VMF = b.m
    # rotating holo ring over the reception desk
    cx, cy, z = 1024, 0, 360
    glow = Tex("dys_cybernetic/trim_lights", scale=0.1)
    ring = [box(cx - 150, cy - 150, z, cx + 150, cy - 138, z + 10, glow),
            box(cx - 150, cy + 138, z, cx + 150, cy + 150, z + 10, glow),
            box(cx - 150, cy - 138, z, cx - 138, cy + 138, z + 10, glow),
            box(cx + 138, cy - 138, z, cx + 150, cy + 138, z + 10, glow)]
    m.brush_ent("func_rotating", ring, targetname="lobby_ring", origin=(cx, cy, z + 5), maxspeed="12",
                fanfriction="20", spawnflags="65", solidbsp="0", volume="0", dmg="0")
    kit.light(m, cx, cy, z - 20, color=(90, 220, 255), bright=140)
    # keep players off the tower setback ledge (sniper perch over the whole plaza)
    kit.clip_box(m, 448, -1216, 480, 576, 1216, 1280)
    # north guard post = obj 1 control booth: desk + monitors under the override screen
    m.detail(box(208, 660, 0, 368, 700, 36, {"all": "vaccinert/dys_vacextwall4", "top": "dys_cybernetic/floor_black_glossy"}))
    for x in (236, 340):
        kit.prop(m, "models/props/monitor01.mdl", x, 684, 36, yaw=90, solid=0)
    kit.light(m, 288, 620, 150, color=(255, 214, 170), bright=70)
    # rooftop dishes / antennas on the guard posts
    for y in (576, -576):
        kit.prop(m, "models/props_rooftop/roof_dish001.mdl", 288, y + (80 if y > 0 else -80), 256, yaw=180, solid=6)
