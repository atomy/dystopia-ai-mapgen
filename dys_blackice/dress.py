"""Set dressing for dys_blackice: signage, street furniture, props, lighting, weather.

All geometry here is func_detail / brush entities / props, never sealing world.
"""
from __future__ import annotations

import math
import random

import assets
import kit
from vmflib import (VMF, Tex, box, hull, ngon, wedge, NODRAW, TRIGGER, INVISIBLE, PLAYERCLIP, cross, num)

FACING = {"+x": (1, 0, 0), "-x": (-1, 0, 0), "+y": (0, 1, 0), "-y": (0, -1, 0)}
FACE_KEY = {"+x": "east", "-x": "west", "+y": "north", "-y": "south"}


def fit_tex(mat, facing, left_pt, top_z, w, h, lm=16):
    """Texture fitted exactly to a w x h panel, reading correctly for a viewer facing it."""
    f = FACING[facing]
    r = cross((-f[0], -f[1], -f[2]), (0, 0, 1))          # viewer's right
    r = (round(r[0]), round(r[1]), round(r[2]))
    tw, th = assets.texture_size(mat) or (512, 512)
    us, vs = w / tw, h / th
    uoff = -(left_pt[0] * r[0] + left_pt[1] * r[1]) / us
    voff = top_z / vs
    return Tex(mat, uscale=us, vscale=vs, uoff=uoff, voff=voff, uaxis=r, vaxis=(0, 0, -1), lightmap=lm)


def panel(m: VMF, cx, cy, z0, z1, facing, w, mat, depth=2, back=NODRAW, cls="func_detail", **kv):
    """Flat panel centred at (cx, cy) on a wall, front face toward `facing`, fitted texture."""
    f = FACING[facing]
    r = cross((-f[0], -f[1], -f[2]), (0, 0, 1))
    left = (cx - r[0] * w / 2, cy - r[1] * w / 2)
    tex = fit_tex(mat, facing, left, z1, w, z1 - z0)
    if f[0]:
        x0, x1 = sorted((cx, cx + f[0] * depth))
        s = box(x0, cy - w / 2, z0, x1, cy + w / 2, z1, {"all": back, FACE_KEY[facing]: tex})
    else:
        y0, y1 = sorted((cy, cy + f[1] * depth))
        s = box(cx - w / 2, y0, z0, cx + w / 2, y1, z1, {"all": back, FACE_KEY[facing]: tex})
    if cls == "func_detail":
        return m.detail(s)
    return m.brush_ent(cls, s, **kv)


def neon(m: VMF, cx, cy, z0, z1, facing, w, mat, color, bright=60, reach=160, sprite=True):
    """Glowing sign on a wall + coloured light pooled in front of it."""
    panel(m, cx, cy, z0, z1, facing, w, mat, depth=2, cls="func_brush", Solidity="1", solidbsp="0",
          StartDisabled="0", disableshadows="1", vrad_brush_cast_shadows="0", spawnflags="2", InputFilter="0")
    f = FACING[facing]
    kit.light(m, cx + f[0] * 48, cy + f[1] * 48, (z0 + z1) / 2, color=color, bright=bright,
              fifty=reach * 0.45, hundred=reach * 1.6)
    if sprite:
        kit.sprite(m, cx + f[0] * 6, cy + f[1] * 6, (z0 + z1) / 2, color=color, scale=0.6, alpha=70)


def blade(m: VMF, x, y, z0, z1, out_dir, w, mat, color, bright=50):
    """Double-sided blade sign projecting from a wall along out_dir ('+x' etc.)."""
    o = FACING[out_dir]
    # sign plane is perpendicular to the wall: faces point along the wall direction
    if o[0]:   # wall runs along y, blade extends along x, faces +-y
        cx = x + o[0] * (w / 2 + 8)
        t_n = fit_tex(mat, "+y", (cx + w / 2, 0), z1, w, z1 - z0)
        t_s = fit_tex(mat, "-y", (cx - w / 2, 0), z1, w, z1 - z0)
        s = box(cx - w / 2, y - 2, z0, cx + w / 2, y + 2, z1, {"all": NODRAW, "north": t_n, "south": t_s})
        arm = box(x, y - 2, z1 - 4, cx + o[0] * w / 2, y + 2, z1, "metal/metalwall003a")
    else:
        cy = y + o[1] * (w / 2 + 8)
        t_e = fit_tex(mat, "+x", (0, cy - w / 2), z1, w, z1 - z0)
        t_w = fit_tex(mat, "-x", (0, cy + w / 2), z1, w, z1 - z0)
        s = box(x - 2, cy - w / 2, z0, x + 2, cy + w / 2, z1, {"all": NODRAW, "east": t_e, "west": t_w})
        arm = box(x - 2, y, z1 - 4, x + 2, cy + o[1] * w / 2, z1, "metal/metalwall003a")
    m.brush_ent("func_brush", s, Solidity="1", solidbsp="0", StartDisabled="0", disableshadows="1",
                vrad_brush_cast_shadows="0", spawnflags="2", InputFilter="0")
    m.detail(arm)
    bx, by, _, bx1, by1, _ = s.bbox()
    kit.light(m, (bx + bx1) / 2, (by + by1) / 2, (z0 + z1) / 2, color=color, bright=bright, fifty=70, hundred=260)


def shutter(m: VMF, cx, cy, z0, z1, facing, w, mat="metal/metaldoor032a"):
    panel(m, cx, cy, z0, z1, facing, w, mat, depth=4, back="metal/metalwall003a")


def sidewalk(m: VMF, x0, x1, y0, y1, h=8, top="urban/sidewalk", curb="concrete/concretewall008a", curb_side=None):
    mats = {"all": curb, "top": Tex(top, lightmap=32), "bottom": NODRAW}
    m.detail(box(x0, y0, 0, x1, y1, h, mats))


def lamppost(m: VMF, x, y, arm_dir, color=(210, 200, 255), bright=230):
    """HL2 street lamp; arm reaches ~96u toward arm_dir."""
    yaw = {"+y": 0, "-x": 90, "-y": 180, "+x": 270}[arm_dir]
    kit.prop(m, "models/props_c17/lamppost03a_on.mdl", x, y, 0, yaw=yaw, solid=6, fade=(3500, 4500))
    ox, oy = {"+y": (0, 1), "-y": (0, -1), "+x": (1, 0), "-x": (-1, 0)}[arm_dir]
    hx, hy = x + ox * 88, y + oy * 88
    kit.spot(m, hx, hy, 424, pitch=-90, color=color, bright=bright, inner=40, outer=68)
    kit.sprite(m, hx, hy, 426, color=color, scale=0.45, alpha=110)


def cable(m: VMF, name, p0, p1, slack=120, width=2, mat="cable/cable.vmt"):
    end = m.ent("keyframe_rope", p1, targetname=f"{name}_b", Slack=str(slack), Subdiv="4", Width=str(width),
                RopeMaterial=mat, TextureScale="1", MoveSpeed="64", Type="0", Barbed="0", Breakable="0",
                Collide="0", Dangling="0", spawnflags="0")
    m.ent("move_rope", p0, targetname=f"{name}_a", NextKey=f"{name}_b", Slack=str(slack), Subdiv="4",
          Width=str(width), RopeMaterial=mat, TextureScale="1", MoveSpeed="64", Type="0", Barbed="0",
          Breakable="0", Collide="0", Dangling="0", PositionInterpolator="2", spawnflags="0")


def floor_overlay(m: VMF, mat, x, y, z, w, h, yaw=0, order=0):
    sides = m.find_sides((x, y, z), (0, 0, 1))
    if not sides:
        return None
    a = math.radians(yaw)
    u = (round(math.cos(a), 4), round(math.sin(a), 4), 0)
    return m.overlay(mat, (x, y, z), (0, 0, 1), u, w, h, sides, render_order=order)


def wall_overlay(m: VMF, mat, x, y, z, facing, w, h, order=0):
    n = FACING[facing]
    sides = m.find_sides((x, y, z), n)
    if not sides:
        return None
    r = cross((-n[0], -n[1], -n[2]), (0, 0, 1))
    return m.overlay(mat, (x, y, z), n, (round(r[0]), round(r[1]), 0), w, h, sides, render_order=order)


def rain(m: VMF, x0, y0, z0, x1, y1, z1, density=40):
    m.brush_ent("func_precipitation", box(x0, y0, z0, x1, y1, z1, TRIGGER), preciptype="0",
                renderamt=str(density), rendercolor="140 160 190")


def stall(m: VMF, cx, cy, yaw_out, canopy="neon/dog_neon14", light_color=(255, 120, 90)):
    """Street food stall: counter + posts + striped canopy, open toward yaw_out ('+y'/'-y')."""
    w, d = 160, 88
    x0, x1, y0, y1 = cx - w / 2, cx + w / 2, cy - d / 2, cy + d / 2
    s = []
    s.append(box(x0, y0, 0, x1, y1, 44, {"all": "metal/metalwall017a", "top": "metal/metalwall003a"}))
    for (px, py) in [(x0, y0), (x1 - 6, y0), (x0, y1 - 6), (x1 - 6, y1 - 6)]:
        s.append(box(px, py, 44, px + 6, py + 6, 128, "metal/metalwall003a"))
    s.append(box(x0 - 12, y0 - 16, 128, x1 + 12, y1 + 16, 134, {"all": "metal/metalwall003a", "bottom": canopy, "top": "metal/metalwall017a"}))
    m.detail(s)
    kit.light(m, cx, cy, 110, color=light_color, bright=70, fifty=60, hundred=220)


# ============================================================================= zones

def street(b):
    m: VMF = b.m
    rng = random.Random(7)
    # --- sidewalks with curbs (road is y -192..192)
    sidewalk(m, -3456, -1664, 192, 320)
    sidewalk(m, -3456, -1664, -320, -192)
    # --- road markings
    for x in range(-3392, -1700, 256):
        floor_overlay(m, "concrete/concrete_paintline_medium", x + 64, 0, 0, 128, 12)
    # crosswalk near the plaza
    for i in range(6):
        floor_overlay(m, "concrete/concrete_paintline_large", -1760, -150 + i * 60, 0, 180, 28, yaw=0)

    # --- north side shop fronts (facade at y=320 faces -y)
    neon(m, -3136, 316, 236, 292, "-y", 384, "neon/neon_thdsm", (255, 70, 90), bright=70)            # noodle bar
    neon(m, -2688, 316, 150, 246, "-y", 96, "neon/s_neon1", (255, 50, 50), bright=60)                 # pawn shop
    shutter(m, -2816, 316, 0, 144, "-y", 128)
    shutter(m, -2560, 316, 0, 144, "-y", 128, "urban/oldgarage")
    neon(m, -2048, 316, 176, 240, "-y", 256, "signs/sign_netexcess02", (120, 160, 255), bright=70)     # arcade
    neon(m, -1760, 316, 150, 246, "-y", 96, "neon/s_neon_netexcess", (255, 60, 70), bright=50)
    blade(m, -2656, 320, 360, 872, "-y", 128, "props/sign_hotel01a", (255, 200, 150), bright=90)        # HOTEL
    # --- south side (facade at y=-320 faces +y)
    neon(m, -3264, -316, 150, 246, "+y", 96, "neon/s_neon2", (60, 220, 255), bright=60)               # liquor
    shutter(m, -3392, -316, 0, 144, "+y", 96)
    neon(m, -2816, -316, 236, 300, "+y", 256, "neon/neon_datasmith", (255, 90, 200), bright=70)       # electronics
    neon(m, -2304, -316, 150, 246, "+y", 96, "neon/s_neon_diner", (80, 220, 255), bright=60)          # diner
    shutter(m, -2432, -316, 0, 144, "+y", 128, "detonate/detrollerdoor02")
    shutter(m, -2176, -316, 0, 144, "+y", 128)
    neon(m, -1856, -316, 150, 246, "+y", 96, "neon/s_neon3", (255, 150, 40), bright=60)               # SoyKaf
    neon(m, -1856, -316, 290, 354, "+y", 128, "neon/dog_neon17", (90, 200, 255), bright=40, sprite=False)
    blade(m, -2240, -320, 420, 932, "+y", 128, "signs/osaka_sign01", (255, 90, 220), bright=90)
    # metro entrance sign over the kiosk mouth (kiosk opens east at x=-3456)
    neon(m, -3452, 0, 330, 458, "+x", 128, "neon/s_neon_monorail", (80, 200, 255), bright=80)

    # --- street lamps
    for (x, y, d) in [(-3200, 272, "-y"), (-2432, 272, "-y"), (-2816, -272, "+y"), (-2016, -272, "+y")]:
        lamppost(m, x, y, d)

    # --- overhead cables and wires
    for i, x in enumerate(range(-3380, -1700, 210)):
        z0 = 380 + rng.randint(0, 160)
        z1 = 380 + rng.randint(0, 160)
        cable(m, f"st_cable{i}", (x, 318, z0), (x + rng.randint(-120, 120), -318, z1), slack=rng.randint(60, 160))
    for i, x in enumerate(range(-3300, -1800, 380)):
        cable(m, f"st_cable_l{i}", (x, 318, 560), (x + 360, 318, 520), slack=90, width=3)

    # --- cover & clutter
    stall(m, -2880, -40, "+y")
    stall(m, -2240, 60, "-y", light_color=(120, 200, 255))
    kit.prop(m, "models/props_vehicles/car005a.mdl", -2560, -90, 0, yaw=12, solid=6, fade=(2500, 3500))
    kit.prop(m, "models/props_vehicles/car002b.mdl", -3180, 120, 0, yaw=-170, solid=6, fade=(2500, 3500))
    for (x, y, yaw) in [(-3000, 250, 5), (-2930, 262, 40), (-2100, -262, 10), (-3330, -250, 80), (-2490, 256, 0)]:
        kit.prop(m, "models/termi/t_dtrustcrate48.mdl", x, y, 8, yaw=yaw, solid=6)
    for (x, y) in [(-3300, 290), (-2720, 290), (-2000, -290), (-2620, -290), (-1820, 290)]:
        kit.prop(m, "models/props_junk/trashcluster01a.mdl", x, y, 8, yaw=rng.randint(0, 359), solid=0)
    for (x, y) in [(-3050, -280), (-2360, 280)]:
        kit.prop(m, "models/props/dys_vendingmachine01c.mdl", x, y, 8, yaw=90 if y < 0 else 270, solid=6)
    for (x, y) in [(-2960, 60), (-2150, -130), (-3350, -40)]:
        floor_overlay(m, "overlays/puddle001a", x, y, 0, 220, 160, yaw=rng.randint(0, 180))
    # steam from a manhole
    floor_overlay(m, "urban/osaka_sewer_lid", -2688, 40, 0, 48, 48)
    m.ent("env_steam", (-2688, 40, 2), angles="-90 0 0", InitialState="1", type="0", SpreadSpeed="18", Speed="60",
          StartSize="18", EndSize="60", Rate="14", rendercolor="170 180 200", JetLength="160", renderamt="120",
          rollspeed="6", spawnflags="0")

    # --- alleys: dumpsters, trash, a light each
    for (x, y, yaw) in [(-3600, 1090, 0), (-2400, 1150, 180), (-3200, -1090, 0), (-2000, -1150, 180)]:
        kit.prop(m, "models/props_junk/trashdumpster02.mdl", x, y, 0, yaw=yaw, solid=6)
    for (x, y) in [(-3000, 1120), (-2600, -1120)]:
        kit.prop(m, "models/props_junk/garbage256_composite002a.mdl", x, y, 0, yaw=90, solid=0)
    for (x, y, c) in [(-3500, 1120, (255, 120, 60)), (-2600, 1120, (80, 160, 255)), (-3300, -1120, (255, 80, 160)),
                      (-2200, -1120, (255, 170, 80))]:
        kit.light(m, x, y, 180, color=c, bright=60, fifty=120, hundred=420)
        kit.prop(m, "models/props_c17/light_cagelight01_on.mdl", x, y + (60 if y > 0 else -60) * 0, 200, solid=0, on_floor=False)

    # --- rain over the market
    rain(m, -3456, -320, 0, -1664, 320, 1100)
    rain(m, -3968, 1024, 0, -1664, 1216, 1100)
    rain(m, -3968, -1216, 0, -1664, -1024, 1100)


def plaza(b):
    m: VMF = b.m
    rng = random.Random(11)
    # --- planters with trees (cover), concrete sides
    for (cx, cy) in [(-1280, -704), (-1280, 704), (-256, -832), (-256, 832)]:
        m.detail(box(cx - 128, cy - 96, 0, cx + 128, cy + 96, 48,
                     {"all": "concrete/concretewall060c", "top": "nature/dirtfloor006a"}))
        kit.prop(m, "models/props_foliage/tree_deciduous_03b.mdl", cx, cy, 48, yaw=rng.randint(0, 359), solid=6,
                 fade=(3000, 4000))
    # --- central monument in the sunken court: black obelisk + light strips + rotating ring
    ox, oy = -512, 0
    m.detail(box(ox - 48, oy - 48, -64, ox + 48, oy + 48, 320, {"all": "vaccinert/dys_vacextwall4", "top": "metal/metalwall003a"}))
    for (sx, sy, fac) in [(ox + 49, oy, "+x"), (ox - 49, oy, "-x")]:
        panel(m, sx, sy, -40, 300, fac, 12, "vaccinert/dys_vactrim3light", depth=1)
    ring = [box(ox - 132, oy - 132, 360, ox + 132, oy - 120, 372, "vaccinert/dys_vactrim3light"),
            box(ox - 132, oy + 120, 360, ox + 132, oy + 132, 372, "vaccinert/dys_vactrim3light"),
            box(ox - 132, oy - 120, 360, ox - 120, oy + 120, 372, "vaccinert/dys_vactrim3light"),
            box(ox + 120, oy - 120, 360, ox + 132, oy + 120, 372, "vaccinert/dys_vactrim3light")]
    m.brush_ent("func_rotating", ring, targetname="monument_ring", origin=(ox, oy, 366), maxspeed="18",
                fanfriction="20", spawnflags="1", solidbsp="0", volume="0", dmg="0", rendercolor="255 255 255")
    kit.light(m, ox, oy, 380, color=(90, 220, 255), bright=120, fifty=180, hundred=700)
    kit.light(m, ox + 120, oy, 40, color=(90, 220, 255), bright=40, fifty=60, hundred=240)
    kit.light(m, ox - 120, oy, 40, color=(90, 220, 255), bright=40, fifty=60, hundred=240)
    # --- concrete barriers as cover near the gate
    for (x, y, yaw) in [(96, -336, 0), (96, 336, 0), (64, 0, 90), (-60, -560, 60), (-60, 560, 120)]:
        kit.prop(m, "models/props_c17/concrete_barrier001a.mdl", x, y, 0, yaw=yaw, solid=6)
    # wrecked transport on the south side (big cover piece)
    kit.prop(m, "models/props/brute_destroyed.mdl", -1024, -1000, 0, yaw=20, solid=6, fade=(3500, 4500))
    kit.prop(m, "models/props_vehicles/van001a.mdl", -960, 980, 0, yaw=-8, solid=6, fade=(3500, 4500))
    # --- tower facade: vertical light pilasters + floodlights toward the plaza
    for y in (-960, -704, 704, 960):
        panel(m, 450, y, 32, 1200, "-x", 16, "vaccinert/dys_vactrim5light", depth=2)
    for y in (-1024, -512, 512, 1024):
        kit.spot(m, 430, y, 600, pitch=35, yaw=180, color=(200, 220, 255), bright=500, inner=25, outer=45)
    # KURODA banner over the entrance + wide logos on the setback ledge
    neon(m, 574, 0, 320, 1216, "-x", 224, "blackice/kuroda_banner", (255, 60, 70), bright=180, reach=640)
    m.detail(box(448, -1216, 472, 576, 1216, 480, {"all": "vaccinert/dys_vactrim2", "top": "metal/metalfloor_001e"}))
    for y in (-760, 760):
        neon(m, 574, y, 600, 696, "-x", 384, "blackice/kuroda_wide", (255, 70, 80), bright=70, reach=300, sprite=False)
    # guard post glass (breakable) in the window slits
    for gy in (1, -1):
        for (y0, y1) in ((432, 496), (656, 720)):
            kit.glass(m, 142, gy * y0 if gy > 0 else -y1, 72, 146, gy * y1 if gy > 0 else -y0, 144, breakable=True)
        kit.glass(m, 192, gy * 398 if gy > 0 else -402, 72, 384, gy * 402 if gy > 0 else -398, 144, breakable=True)
        kit.light(m, 288, gy * 576, 170, color=(200, 225, 255), bright=110, fifty=90, hundred=320)
    # lamps along the plaza edges
    for (x, y, d) in [(-1536, -1120, "+y"), (-512, -1120, "+y"), (-1536, 1120, "-y"), (-512, 1120, "-y")]:
        lamppost(m, x, y, d, color=(200, 220, 255), bright=320)
    rain(m, -1664, -1216, 0, 448, 1216, 1100, density=35)
