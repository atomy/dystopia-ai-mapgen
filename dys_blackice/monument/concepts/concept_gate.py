"""HOLO GATE -- monument concept sketch for dys_blackice (sunken court, Kuroda Plaza).

A cyber-torii: two black-lacquer pillars, each split by a cyan data slit, rise out of two server-rack plinths
on a shallow stepped platform; a double top beam (kasagi + shimaki) with a red neon seam crowns it, and a
translucent cyan scanline membrane between the pillars shows the Kuroda emblem in red. The gate spans Y and
faces west (-X) toward the approaching players; it is walk-through (membrane = visual only, no collision).

Run:  blender --background --factory-startup --python concept_gate.py
"""
import random
import sys
from math import cos, pi, sin
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import stage  # noqa: E402

import bmesh  # noqa: E402
import bpy  # noqa: E402

# ----------------------------------------------------------------------------- dimensions (Source units)
Z_PLAT = 16                 # platform top (two 8 u steps)
PY = 108                    # pillar axis |y|
GAP = 6                     # data slit between the two pillar halves
R0, R1 = 19.0, 16.5         # pillar radius at the plinth top / at the pillar top
PZ0, PZ1 = 84, 352          # pillar z range (bottom hidden in the plinth, top hidden in the shimaki)
PB_X, PB_Y = 56, 34         # server-rack plinth half depth (x) / half width (y, around the pillar axis)
PLINTH_TOP = 92             # server-rack plinth cap top
NUKI = (284, 304)           # tie beam z range
NUKI_Y = 150                # tie beam half length
SHIMAKI = (340, 356)        # lower top beam
SEAM = 6                    # red neon seam between shimaki and kasagi
KASAGI = (362, 390)         # top beam bottom/top at the centre (curves up toward the ends)
KASAGI_L = 170              # top beam half length (= footprint limit)
SORI_B, SORI_T = 10, 20     # upsweep of the kasagi bottom / top line at the ends
MEM_Z = (26, 284)           # membrane z range
MEM_Y = 89                  # membrane half width (tucked into the pillars)
ZE, RE = 192, 50            # emblem centre z / hexagon radius

stage.reset()               # must run before any datablock (materials below) is created
COLL = stage.collection()


def rng_sori(y, amp, half=KASAGI_L):
    return amp * (min(abs(y), half) / half) ** 2.2


# ----------------------------------------------------------------------------- geometry helpers

def loft(name, p0, z0, p1, z1, material, smooth=lambda i: False):
    """Prism between two XY polygons (same vertex count) at z0 and z1."""
    bm = bmesh.new()
    lo = [bm.verts.new((x, y, z0)) for x, y in p0]
    hi = [bm.verts.new((x, y, z1)) for x, y in p1]
    n = len(lo)
    bm.faces.new(list(reversed(lo)))
    bm.faces.new(hi)
    for i in range(n):
        j = (i + 1) % n
        f = bm.faces.new((lo[i], lo[j], hi[j], hi[i]))
        f.smooth = smooth(i)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return stage.obj_from_bmesh(name, bm, material, COLL)


def slab_x(name, poly_yz, x0, x1, material):
    """Extrude a convex polygon drawn in the YZ plane (the gate plane) along X."""
    bm = bmesh.new()
    a = [bm.verts.new((x0, y, z)) for y, z in poly_yz]
    b = [bm.verts.new((x1, y, z)) for y, z in poly_yz]
    n = len(a)
    bm.faces.new(a)
    bm.faces.new(list(reversed(b)))
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((a[i], b[i], b[j], a[j]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return stage.obj_from_bmesh(name, bm, material, COLL)


def sweep_y(name, half, section, material, n=24):
    """Beam along Y from -half to +half; section(y) -> closed polygon [(x, z), ...]."""
    bm = bmesh.new()
    rings = []
    for i in range(n + 1):
        y = -half + 2 * half * i / n
        rings.append([bm.verts.new((x, y, z)) for x, z in section(y)])
    m = len(rings[0])
    for a, b in zip(rings, rings[1:]):
        for j in range(m):
            k = (j + 1) % m
            bm.faces.new((a[j], a[k], b[k], b[j]))
    bm.faces.new(rings[0])
    bm.faces.new(list(reversed(rings[-1])))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return stage.obj_from_bmesh(name, bm, material, COLL)


def box(name, x0, y0, z0, x1, y1, z1, material):
    return stage.box(name, min(x0, x1), min(y0, y1), min(z0, z1), max(x0, x1), max(y0, y1), max(z0, z1),
                     material, COLL)


def octagon(hx, hy, c):
    return [(hx - c, -hy), (hx, -hy + c), (hx, hy - c), (hx - c, hy),
            (-hx + c, hy), (-hx, hy - c), (-hx, -hy + c), (-hx + c, -hy)]


def d_shape(cy, r, s, k=8):
    """Half-pillar outline in XY: semicircle bulging toward s (+1 = +y), flat side on y = cy."""
    return [(r * cos(pi * i / k), cy + s * r * sin(pi * i / k)) for i in range(k + 1)]


def stadium(cy, r, gap, k=8):
    """Full pillar outline: two semicircles pulled apart by the slit width."""
    a = [(r * cos(pi * i / k), cy + gap / 2 + r * sin(pi * i / k)) for i in range(k + 1)]
    b = [(r * cos(pi + pi * i / k), cy - gap / 2 + r * sin(pi + pi * i / k)) for i in range(k + 1)]
    return a + b


def pillar_r(z):
    return R0 + (R1 - R0) * (z - PZ0) / (PZ1 - PZ0)


class Quads:
    """Collects small emissive quads (status LEDs) per material into one object each."""

    def __init__(self):
        self.polys = {}

    def add(self, material, pts):
        self.polys.setdefault(material, []).append(pts)

    def led_x(self, material, x, y, z, w=2.6, h=1.4):       # on a face whose normal is +-X
        self.add(material, [(x, y - w / 2, z - h / 2), (x, y + w / 2, z - h / 2), (x, y + w / 2, z + h / 2),
                            (x, y - w / 2, z + h / 2)])

    def led_y(self, material, x, y, z, w=2.6, h=1.4):       # on a face whose normal is +-Y
        self.add(material, [(x - w / 2, y, z - h / 2), (x + w / 2, y, z - h / 2), (x + w / 2, y, z + h / 2),
                            (x - w / 2, y, z + h / 2)])

    def build(self, prefix):
        for material, polys in self.polys.items():
            bm = bmesh.new()
            for pts in polys:
                bm.faces.new([bm.verts.new(p) for p in pts])
            ob = stage.obj_from_bmesh(f"{prefix}_{material.name}", bm, material, COLL)
            ob.visible_shadow = False


# ----------------------------------------------------------------------------- materials

def lacquer(name, base, rough, metal, coat=0.8):
    m = stage.mat(name, base, rough, metal)
    b = m.node_tree.nodes["Principled BSDF"]
    for key, val in (("Coat Weight", coat), ("Coat Roughness", 0.05)):
        if key in b.inputs:
            b.inputs[key].default_value = val
    return m


def membrane_material():
    """Cyan scanline field: fades in above the floor, glows along the pillars and under the emitter beam,
    turns red around the emblem."""
    m = bpy.data.materials.new("gate_membrane")
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    new, link = nt.nodes.new, nt.links.new

    def feed(src, dst):
        if isinstance(src, (int, float)):
            dst.default_value = src
        else:
            link(src, dst)

    def op(kind, a, b=None, clamp=False):
        n = new("ShaderNodeMath")
        n.operation = kind
        n.use_clamp = clamp
        feed(a, n.inputs[0])
        if b is not None:
            feed(b, n.inputs[1])
        return n.outputs[0]

    def remap(v, a, b, c=0.0, d=1.0, smooth=True):
        n = new("ShaderNodeMapRange")
        n.interpolation_type = "SMOOTHSTEP" if smooth else "LINEAR"
        feed(v, n.inputs[0])
        for i, x in enumerate((a, b, c, d), start=1):
            n.inputs[i].default_value = x
        return n.outputs[0]

    def add(*vals):
        out = vals[0]
        for v in vals[1:]:
            out = op("ADD", out, v)
        return out

    def mul(*vals):
        out = vals[0]
        for v in vals[1:]:
            out = op("MULTIPLY", out, v)
        return out

    tc = new("ShaderNodeTexCoord")
    sep = new("ShaderNodeSeparateXYZ")
    link(tc.outputs["Object"], sep.inputs[0])
    y, z = sep.outputs["Y"], sep.outputs["Z"]
    ay = op("ABSOLUTE", y)
    lines = remap(op("SINE", mul(z, 2 * pi / 4.5)), 0.25, 1.0)            # fine scanlines ...
    dxyz = new("ShaderNodeCombineXYZ")                                      # ... broken into data dashes per line
    feed(mul(y, 0.07), dxyz.inputs[0])
    feed(mul(op("FLOOR", mul(z, 1 / 4.5)), 1.73), dxyz.inputs[1])
    dn = new("ShaderNodeTexNoise")
    dn.inputs["Scale"].default_value = 1.0
    dn.inputs["Detail"].default_value = 0.0
    link(dxyz.outputs[0], dn.inputs["Vector"])
    lines = mul(lines, op("ADD", 0.3, mul(remap(dn.outputs["Fac"], 0.44, 0.58), 0.7)))
    # slow horizontal streaks ("signal" bands), static
    cxyz = new("ShaderNodeCombineXYZ")
    feed(mul(y, 0.008), cxyz.inputs[0])
    feed(mul(z, 0.07), cxyz.inputs[1])
    nz = new("ShaderNodeTexNoise")
    nz.inputs["Scale"].default_value = 1.0
    nz.inputs["Detail"].default_value = 1.0
    link(cxyz.outputs[0], nz.inputs["Vector"])
    streak = remap(nz.outputs["Fac"], 0.35, 0.68, 0.3, 1.0, smooth=False)
    fb = remap(z, MEM_Z[0] + 8, MEM_Z[0] + 125)                   # hangs from the beam, dissolves toward the floor
    ft = remap(z, MEM_Z[1] - 70, MEM_Z[1])                        # curtain projected from the tie beam
    fc = remap(ay, MEM_Y, 12)                                     # fuller in the middle than at the pillars
    fe = remap(ay, MEM_Y - 5, MEM_Y)                              # thin attachment glow at the pillars
    dz = op("SUBTRACT", z, ZE)
    adz = op("ABSOLUTE", dz)
    dist = op("SQRT", op("ADD", mul(y, y), mul(dz, dz)))
    fr = remap(dist, RE * 1.85, RE * 0.7)                         # red halo around the emblem
    # faint "portal" ring: a larger pointy-top hexagon around the emblem (hex distance = apothem)
    hexd = op("MAXIMUM", ay, op("ADD", mul(ay, 0.5), mul(adz, 0.866)))
    ring = remap(op("ABSOLUTE", op("SUBTRACT", hexd, RE * 1.45 * 0.866)), 1.8, 0.0)
    ls = mul(lines, streak)
    # opacity (how much of the background it veils) and radiance are set separately so the cyan stays saturated
    ftc = mul(ft, op("ADD", 0.25, mul(fc, 0.75)))                 # top glow concentrated in the middle (no hard frame)
    opacity = mul(fb, add(0.08, mul(fc, 0.08), mul(ls, 0.09), mul(ftc, 0.22), mul(fe, 0.06), mul(fr, 0.14),
                          mul(ring, 0.25)))
    opacity = op("MINIMUM", opacity, 0.85)
    rad_c = mul(fb, add(mul(op("ADD", 0.045, mul(ls, 0.19)), op("ADD", 0.3, mul(fc, 0.7))), mul(ftc, ft, 0.9),
                        mul(fe, 0.12), mul(ring, 0.55)), op("SUBTRACT", 1.0, mul(fr, 0.8)))
    rad_r = mul(fb, fr, op("ADD", 0.22, mul(lines, 0.32)))
    safe = op("MAXIMUM", opacity, 0.02)
    sc = op("DIVIDE", rad_c, safe)
    sr = op("DIVIDE", rad_r, safe)
    alpha = opacity
    ec = new("ShaderNodeEmission")
    ec.inputs["Color"].default_value = (*stage.CYAN, 1)
    link(sc, ec.inputs["Strength"])
    er = new("ShaderNodeEmission")
    er.inputs["Color"].default_value = (*stage.RED, 1)
    link(sr, er.inputs["Strength"])
    both = new("ShaderNodeAddShader")
    link(ec.outputs[0], both.inputs[0])
    link(er.outputs[0], both.inputs[1])
    tr = new("ShaderNodeBsdfTransparent")
    mix = new("ShaderNodeMixShader")
    link(alpha, mix.inputs[0])
    link(tr.outputs[0], mix.inputs[1])
    link(both.outputs[0], mix.inputs[2])
    out = new("ShaderNodeOutputMaterial")
    link(mix.outputs[0], out.inputs[0])
    if hasattr(m, "surface_render_method"):
        m.surface_render_method = "BLENDED"
    if hasattr(m, "use_backface_culling"):
        m.use_backface_culling = False
    return m


M_FRAME = lacquer("gate_black_lacquer", (0.04, 0.042, 0.048), 0.3, 0.75, coat=1.0)
M_RACK = lacquer("gate_rack_glass", (0.008, 0.01, 0.013), 0.12, 0.2, coat=0.5)
M_BASE = stage.mat("gate_platform", (0.03, 0.031, 0.036), 0.3, metal=0.2)
M_CYAN = stage.neon("gate_cyan", stage.CYAN, 9.0)
M_CYAN_DIM = stage.neon("gate_cyan_dim", stage.CYAN, 3.0)
M_RED = stage.neon("gate_red", stage.RED, 16.0)
M_WHITE = stage.neon("gate_warm_white", stage.WHITE, 10.0)
M_MEMBRANE = membrane_material()


# ----------------------------------------------------------------------------- build

def platform():
    loft("step_1", octagon(108, 168, 26), 0, octagon(108, 168, 26), 8, M_BASE)
    loft("step_2", octagon(94, 154, 20), 8, octagon(94, 154, 20), Z_PLAT, M_BASE)
    band = loft("step_2_line", octagon(94.7, 154.7, 20.3), 10.5, octagon(94.7, 154.7, 20.3), 12, M_CYAN_DIM)
    band.visible_shadow = False
    py = PY - PB_Y                                                                      # membrane floor slot
    slot = box("floor_emitter", -3.5, -py, Z_PLAT - 0.5, 3.5, py, Z_PLAT + 1.2, M_CYAN)
    slot.visible_shadow = False


def plinth(s, leds, rnd):
    """Server-rack plinth around the pillar at y = s*PY: toe, body, cap, rack doors with status LEDs."""
    cy = s * PY
    zc = PLINTH_TOP - 7                                  # cap plate bottom
    box(f"plinth_toe_{s}", -(PB_X - 4), cy - (PB_Y - 4), Z_PLAT, PB_X - 4, cy + PB_Y - 4, Z_PLAT + 6, M_BASE)
    box(f"plinth_body_{s}", -PB_X, cy - PB_Y, Z_PLAT + 6, PB_X, cy + PB_Y, zc, M_FRAME)
    box(f"plinth_cap_{s}", -(PB_X + 3), cy - (PB_Y + 3), zc, PB_X + 3, cy + PB_Y + 3, PLINTH_TOP, M_FRAME)
    colors = [M_CYAN] * 7 + [M_WHITE] * 2 + [M_RED] * 2
    dz0, dz1 = Z_PLAT + 10, zc - 4                       # rack door z range

    def door_leds(put, u0, u1):
        z = dz0 + 6.0
        while z < dz1 - 3:
            count = rnd.choice((0, 1, 1, 2, 2, 3))
            for k in range(count):
                put(rnd.choice(colors), u1 - 4.5 - 4.2 * k, z)
            z += 6.5

    # west / east ends: two rack doors each
    for sx in (-1, 1):
        xf = sx * PB_X
        for (u0, u1) in ((cy - PB_Y + 3, cy - 1.5), (cy + 1.5, cy + PB_Y - 3)):
            box(f"door_{s}_{sx}", xf - sx * 0.5, u0, dz0, xf + sx * 1.0, u1, dz1, M_RACK)
            door_leds(lambda m, u, z: leds.led_x(m, xf + sx * 1.25, u, z), u0, u1)
    # outer side: three doors along X
    yf = cy + s * PB_Y
    w = (2 * PB_X - 8) / 3
    for k in range(3):
        u0 = -PB_X + 4 + k * w
        u1 = u0 + w - 3
        box(f"side_door_{s}", u0, yf - s * 0.5, dz0, u1, yf + s * 1.0, dz1, M_RACK)
        door_leds(lambda m, u, z: leds.led_y(m, u, yf + s * 1.25, z), u0, u1)
    # passage side: a cyan guide line under the cap
    yi = cy - s * PB_Y
    line = box(f"inner_line_{s}", -(PB_X - 4), yi - s * 0.8, zc - 3.5, PB_X - 4, yi + s * 0.4, zc - 1.5, M_CYAN)
    line.visible_shadow = False


def pillar(s):
    cy = s * PY
    for half in (-1, 1):                               # two D-section halves; the data slit runs full height
        c = cy + half * GAP / 2
        loft(f"pillar_{s}_{half}", d_shape(c, R0, half), PZ0, d_shape(c, R1, half), PZ1, M_FRAME,
             smooth=lambda i: i < 8)
    slit = box(f"pillar_slit_{s}", -(R1 - 1.5), cy - 1.2, PZ0, R1 - 1.5, cy + 1.2, SHIMAKI[0] + 2, M_CYAN)
    slit.visible_shadow = False
    # socket collar where the pillar plugs into the rack plinth, with a thin light line
    loft(f"socket_{s}", stadium(cy, R0 + 5, GAP), PLINTH_TOP - 1, stadium(cy, R0 + 4, GAP), PLINTH_TOP + 9, M_FRAME,
         smooth=lambda i: True)
    ring = loft(f"socket_line_{s}", stadium(cy, R0 + 5.0, GAP), PLINTH_TOP + 2.5, stadium(cy, R0 + 4.8, GAP),
                PLINTH_TOP + 4.5, M_CYAN)
    ring.visible_shadow = False


def beams():
    box("nuki", -11, -NUKI_Y, NUKI[0], 11, NUKI_Y, NUKI[1], M_FRAME)
    em = box("nuki_emitter", -3.5, -(MEM_Y - 2), NUKI[0] - 2.5, 3.5, MEM_Y - 2, NUKI[0], M_CYAN)
    em.visible_shadow = False
    zm = (NUKI[0] + NUKI[1]) / 2                     # thin light line along the tie beam (front and back)
    box("nuki_line", -11.6, -(NUKI_Y - 3), zm - 1.1, 11.6, NUKI_Y - 3, zm + 1.1, M_CYAN_DIM).visible_shadow = False
    box("gakuzuka", -9, -13, NUKI[1], 9, 13, SHIMAKI[0] + 1, M_FRAME)
    zg = (NUKI[1] + SHIMAKI[0]) / 2                  # small emblem diamond on the centre strut
    slab_x("gakuzuka_diamond", [(0, zg - 11), (5.5, zg), (0, zg + 11), (-5.5, zg)], -9.8, 9.8,
           M_RED).visible_shadow = False

    def shimaki(y):
        o = rng_sori(y, SORI_B)
        z0, z1 = SHIMAKI[0] + o, SHIMAKI[1] + o
        return [(-12, z0), (12, z0), (12, z1), (-12, z1)]

    def seam(y):
        o = rng_sori(y, SORI_B)
        z0, z1 = SHIMAKI[1] + o - 0.5, SHIMAKI[1] + SEAM + o + 0.5
        return [(-10, z0), (10, z0), (10, z1), (-10, z1)]

    def kasagi(y):
        zb, zt = KASAGI[0] + rng_sori(y, SORI_B), KASAGI[1] + rng_sori(y, SORI_T)
        return [(-16, zb), (16, zb), (16, zt - 6), (10, zt), (-10, zt), (-16, zt - 6)]

    sweep_y("shimaki", KASAGI_L - 14, shimaki, M_FRAME)
    sweep_y("red_seam", KASAGI_L - 12, seam, M_RED).visible_shadow = False
    sweep_y("kasagi", KASAGI_L, kasagi, M_FRAME)


def emblem():
    """Kuroda logo in the membrane plane: pointy-top hexagon ring + vertical diamond with a white-hot ridge."""
    w = 7.0
    ri = RE - w / cos(pi / 6)
    hexo = [(RE * cos(pi / 2 + i * pi / 3), ZE + RE * sin(pi / 2 + i * pi / 3)) for i in range(6)]
    hexi = [(ri * cos(pi / 2 + i * pi / 3), ZE + ri * sin(pi / 2 + i * pi / 3)) for i in range(6)]
    for i in range(6):
        j = (i + 1) % 6
        slab_x(f"emblem_ring_{i}", [hexo[i], hexo[j], hexi[j], hexi[i]], -2, 2, M_RED).visible_shadow = False
    dh, dw = RE * 0.62, RE * 0.30
    slab_x("emblem_diamond", [(0, ZE - dh), (dw, ZE), (0, ZE + dh), (-dw, ZE)], -3, 3, M_RED).visible_shadow = False
    slab_x("emblem_ridge", [(-1.1, ZE - dh * 0.7), (1.1, ZE - dh * 0.7), (1.1, ZE + dh * 0.7), (-1.1, ZE + dh * 0.7)],
           -3.6, 3.6, M_WHITE).visible_shadow = False


def membrane():
    bm = bmesh.new()
    vs = [bm.verts.new(p) for p in ((0, -MEM_Y, MEM_Z[0]), (0, MEM_Y, MEM_Z[0]), (0, MEM_Y, MEM_Z[1]),
                                    (0, -MEM_Y, MEM_Z[1]))]
    bm.faces.new(vs)
    ob = stage.obj_from_bmesh("membrane", bm, M_MEMBRANE, COLL)
    ob.visible_shadow = False


def area(name, loc, target, color, power, sx, sy):
    ld = bpy.data.lights.new(name, "AREA")
    ld.shape = "RECTANGLE"
    ld.size, ld.size_y = sx, sy
    ld.color, ld.energy = color, power
    ob = bpy.data.objects.new(name, ld)
    ob.location = loc
    stage.collection("lights").objects.link(ob)
    stage.aim(ob, target)
    return ob


def lights():
    zc = (MEM_Z[0] + MEM_Z[1]) / 2 + 20
    for sx in (-1, 1):                                                   # the membrane lights the court
        a = area(f"membrane_light_{sx}", (sx * 3, 0, zc), (sx * 100, 0, zc), stage.CYAN, 7e5, 170, 220)
        if hasattr(a.data, "specular_factor"):
            a.data.specular_factor = 0.15
        stage.light("POINT", f"emblem_light_{sx}", (sx * 30, 0, ZE), stage.RED, 2.5e5)
        for s in (-1, 1):                                                # floor uplights grazing the pillars
            stage.light("SPOT", f"uplight_{sx}_{s}", (sx * 84, s * PY, Z_PLAT + 4), (0.75, 0.9, 1.0), 3e6,
                        target=(sx * 12, s * PY, 380), size=16, blend=0.7)
    zs = SHIMAKI[1] + SEAM / 2
    for sx in (-1, 1):                                                   # red spill of the seam onto the beams
        a = area(f"seam_spill_{sx}", (sx * 30, 0, zs - 4), (0, 0, zs - 4), stage.RED, 2.2e5, 330, 16)
        if hasattr(a.data, "specular_factor"):
            a.data.specular_factor = 0.4
    stage.light("SPOT", "top", (-260, -120, 1300), (0.75, 0.85, 1.0), 2.5e7, target=(0, 0, 370), size=26, blend=0.5)
    stage.light("SPOT", "rim_east", (560, 200, 820), (0.6, 0.8, 1.0), 4e7, target=(0, 0, 320), size=30, blend=0.5)
    stage.light("SPOT", "key_west", (-700, -300, 420), (0.65, 0.8, 1.0), 2e7, target=(0, 0, 250), size=26, blend=0.6)


def tri_count():
    t = 0
    for ob in COLL.objects:
        if ob.type == "MESH":
            t += sum(len(p.vertices) - 2 for p in ob.data.polygons)
    return t


rnd = random.Random(7)
leds = Quads()
platform()
for side in (-1, 1):
    plinth(side, leds, rnd)
    pillar(side)
leds.build("leds")
beams()
emblem()
membrane()
lights()
print("GATE_TRIS", tri_count())
stage.environment()
stage.render("gate")
