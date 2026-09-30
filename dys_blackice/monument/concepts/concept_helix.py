"""DATA HELIX -- monument concept sketch for dys_blackice (sunken court, Kuroda Plaza).

Two broad, smooth black-glass ribbons wind around a translucent cyan data core like a DNA double helix. They flow
out of a round stepped plinth over a solid dark bell etched with cyan "data layer" lines (cover up to ~140u), lift
off the bell's shoulder around the light column, straighten up and dive into a collar that gathers into a slender
neck presenting the Kuroda emblem (red neon hexagon ring with the vertical diamond). The strands' edge light runs
from data cyan at the foot to Kuroda red at the crown: the data rises into the corporation. No spikes, no shards.

Run:  blender --background --factory-startup --python concept_helix.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import stage  # noqa: E402

import random  # noqa: E402
from math import cos, pi, radians, sin, sqrt, tan  # noqa: E402

import bmesh  # noqa: E402
import bpy  # noqa: E402
from mathutils import Matrix, Vector  # noqa: E402

# ----------------------------------------------------------------------------- parameters (Source units)
SEG = 48                                    # radial segments of the round parts
STEPS = ((140, 0, 12), (122, 12, 26), (104, 26, 40))   # round plinth: (radius, z0, z1)
BASE_TOP = 40
# centre surface the ribbons ride on, Rc(z): flared foot, pinched waist, opening again into the collar
RC_PTS = [(0, 96), (40, 88), (70, 78), (100, 68), (130, 60), (160, 54), (190, 51), (215, 50), (240, 52),
          (262, 55), (280, 57), (300, 58)]
BETA_MID, BETA_END = 28.0, 58.0             # helix inclination from horizontal (deg): DNA-like, steep at the collar
RAMP = (226.0, 274.0)                       # z range where the strands straighten up into the collar
TH, STRIP, GAP = 7.0, 3.0, 6.0              # ribbon thickness, neon strip along each outer edge, clearance to bell
W_K, W_END = 0.74, 0.5                      # ribbon width as a fraction of Rc (body / collar end)
Z_RIB0, Z_RIB1, N_RIB = 1.0, 292.0, 96      # ribbon centre-line range (overshoots; ends are cut flat) and samples
CUT_TOP = 274.0                             # strands are cut flat here, inside the crown
PHASE = radians(200)                        # rotation of the helix (composition toward the cameras)
BELL_Z1, SHOULDER_Z = 124.0, 142.0          # bell hugs the ribbons up to BELL_Z1, rounds into the core by SHOULDER_Z
BELL_LINES = (52, 64, 76, 88, 100, 112)     # etched cyan data-layer lines on the bell
CORE_R, CORE_Z0, CORE_Z1 = 28.0, 130.0, 280.0
COLLAR_Z0 = 256.0
# collar + neck as one flowing lathe profile (r, dz above COLLAR_Z0): a cup the strands flow into, a rolled rim,
# then inward and up the concave neck to the emblem socket (solid on the left of the walk)
CROWN = [(0.5, 0), (30, 0), (42, 2.5), (50, 6), (57, 11), (62, 17), (65, 23), (65.5, 27), (63, 30.5), (56, 32.5),
         (46, 34.5), (35, 37.5), (26, 42), (18, 47), (13, 52), (10.5, 57), (9.5, 60), (0.5, 61)]
RIM_Z, RIM_R = 26.0, 65.8                   # crown rim neon (height above COLLAR_Z0, radius)
EC, E_O, E_I, E_D = 362.0, 52.0, 41.0, 6.0  # emblem centre z, outer / inner vertex radius, half depth (x)
DIA_H, DIA_W, DIA_D = 31.0, 16.5, 8.0       # diamond half height / half width (y) / half depth (x)
GRAD = (160.0, 245.0)                       # strand edge light: cyan below, Kuroda red above


# ----------------------------------------------------------------------------- math helpers
def hermite(pts):
    """Smooth interpolating curve through (x, y) points (cubic Hermite, finite-difference slopes)."""
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    n = len(pts)
    ms = [(ys[min(i + 1, n - 1)] - ys[max(i - 1, 0)]) / (xs[min(i + 1, n - 1)] - xs[max(i - 1, 0)]) for i in range(n)]

    def f(x):
        if x <= xs[0]:
            return ys[0] + ms[0] * (x - xs[0])
        if x >= xs[-1]:
            return ys[-1] + ms[-1] * (x - xs[-1])
        i = max(k for k in range(n - 1) if xs[k] <= x)
        h = xs[i + 1] - xs[i]
        t = (x - xs[i]) / h
        return ((2 * t ** 3 - 3 * t ** 2 + 1) * ys[i] + (t ** 3 - 2 * t ** 2 + t) * h * ms[i]
                + (-2 * t ** 3 + 3 * t ** 2) * ys[i + 1] + (t ** 3 - t ** 2) * h * ms[i + 1])
    return f


Rc = hermite(RC_PTS)


def dRc(z):
    return Rc(z + 0.5) - Rc(z - 0.5)


def smooth01(z, z0, z1):
    t = min(1.0, max(0.0, (z - z0) / (z1 - z0)))
    return t * t * (3 - 2 * t)


def beta(z):
    return radians(BETA_MID + (BETA_END - BETA_MID) * smooth01(z, *RAMP))


def width(z):
    return Rc(z) * (W_K + (W_END - W_K) * smooth01(z, *RAMP))


def theta_table(z0, z1, step=0.5):
    """theta(z) = integral of cot(beta) / Rc dz  (constant inclination on the curved envelope)."""
    tab, th, z = [(z0, 0.0)], 0.0, z0
    while z < z1:
        th += step / (tan(beta(z + step / 2)) * Rc(z + step / 2))
        z += step
        tab.append((z, th))
    return tab


THETA = theta_table(Z_RIB0 - 1, Z_RIB1 + 1)


def theta(z):
    i = min(int((z - THETA[0][0]) / 0.5), len(THETA) - 2)
    (za, ta), (zb, tb) = THETA[i], THETA[i + 1]
    return ta + (tb - ta) * (z - za) / (zb - za)


def bell_r(z):
    off = TH / 2 + GAP
    return Rc(z) - off * sqrt(1 + dRc(z) ** 2)


# ----------------------------------------------------------------------------- materials
def neon_gradient(name, c0, c1, z0, z1, strength):
    """Emission blending c0 -> c1 with object-space height (a gradient band of the neon atlas in the real prop)."""
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    tc = nt.nodes.new("ShaderNodeTexCoord")
    sep = nt.nodes.new("ShaderNodeSeparateXYZ")
    mr = nt.nodes.new("ShaderNodeMapRange")
    ramp = nt.nodes.new("ShaderNodeValToRGB")
    mr.interpolation_type = "SMOOTHSTEP"
    mr.inputs["From Min"].default_value = z0
    mr.inputs["From Max"].default_value = z1
    ramp.color_ramp.elements[0].color = (*c0, 1)
    ramp.color_ramp.elements[1].color = (*c1, 1)
    nt.links.new(tc.outputs["Object"], sep.inputs[0])
    nt.links.new(sep.outputs["Z"], mr.inputs["Value"])
    nt.links.new(mr.outputs["Result"], ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"], em.inputs["Color"])
    em.inputs["Strength"].default_value = strength
    nt.links.new(em.outputs[0], out.inputs[0])
    return m


# ----------------------------------------------------------------------------- mesh helpers
def finish(name, bm, mats, smooth=True, sharp=None, shadow=True):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    for m in mats:
        me.materials.append(m)
    if smooth:
        for p in me.polygons:
            p.use_smooth = True
        if sharp is not None and hasattr(me, "set_sharp_from_angle"):
            me.set_sharp_from_angle(angle=radians(sharp))
    ob = bpy.data.objects.new(name, me)
    stage.collection().objects.link(ob)
    if not shadow:
        ob.visible_shadow = False
    return ob


def lathe(name, prof, mat, segs=SEG, closed=False, cap_top=False, cap_bottom=False, sharp=35, shadow=True):
    """Surface of revolution; walk the (r, z) profile with the solid on the left (outward normal to the right)."""
    bm = bmesh.new()
    rings = [[bm.verts.new((r * cos(2 * pi * i / segs), r * sin(2 * pi * i / segs), z)) for i in range(segs)]
             for (r, z) in prof]
    n = len(rings)
    for k in range(n - 1 + (1 if closed else 0)):
        a, b = rings[k], rings[(k + 1) % n]
        for i in range(segs):
            j = (i + 1) % segs
            bm.faces.new((a[i], a[j], b[j], b[i]))
    if cap_bottom:
        bm.faces.new(list(reversed(rings[0])))
    if cap_top:
        bm.faces.new(rings[-1])
    return finish(name, bm, [mat], sharp=sharp, shadow=shadow)


def band(name, r0, z0, r1, z1, mat, segs=SEG):
    """Thin light band lying on a surface of revolution between (r0, z0) and (r1, z1)."""
    return lathe(name, [(r0, z0), (r1, z1)], mat, segs, sharp=None, shadow=False)


# ----------------------------------------------------------------------------- the ribbons
BLACK_I, NEON_I = 0, 1


def ribbon_profile(w, n_w=3, cap_n=3):
    """Closed cross-section loop [(a, b, material)] -- a across the width, b through the thickness (+ = outward).
    Rounded edges; the outer face carries a neon strip along each edge. The edge i->i+1 uses the material of i."""
    h = TH / 2
    aw = w / 2 - h
    a0, a1 = -aw + STRIP, aw - STRIP
    pts = [(a0 + (a1 - a0) * i / n_w, h, BLACK_I) for i in range(n_w)]
    pts.append((a1, h, NEON_I))
    pts += [(aw + h * cos(radians(90 - 180 * j / cap_n)), h * sin(radians(90 - 180 * j / cap_n)), NEON_I)
            for j in range(cap_n)]
    pts += [(aw - 2 * aw * i / (n_w + 1), -h, BLACK_I) for i in range(n_w + 1)]
    pts += [(-aw + h * cos(radians(270 - 180 * j / cap_n)), h * sin(radians(270 - 180 * j / cap_n)), NEON_I)
            for j in range(cap_n)]
    pts.append((-aw, h, NEON_I))
    return pts


def ribbon_point(zc, th0, a, b):
    """Wrap profile point (a, b) onto the envelope of revolution around the centre-line point at height zc."""
    R = Rc(zc)
    cb = 1 / tan(beta(zc))                 # = R * dtheta/dz
    L = sqrt(cb * cb + 1)
    nu, nz = -1 / L, cb / L                # width direction in the unrolled (R*theta, z) plane
    zp = zc + a * nz
    th = th0 + a * nu / R
    d = dRc(zp)
    s = sqrt(1 + d * d)
    r = Rc(zp) + b / s                     # thickness along the envelope normal
    z = zp - b * d / s
    return Vector((r * cos(th), r * sin(th), z))


def ribbon(name, phase, black, edge):
    bm = bmesh.new()
    rings = []
    for s in range(N_RIB + 1):
        zc = Z_RIB0 + (Z_RIB1 - Z_RIB0) * s / N_RIB
        th0 = theta(zc) + phase
        rings.append([bm.verts.new(ribbon_point(zc, th0, a, b)) for (a, b, _) in ribbon_profile(width(zc))])
    mids = [m for (_, _, m) in ribbon_profile(width(Z_RIB0))]
    n = len(mids)
    for s in range(N_RIB):
        A, B = rings[s], rings[s + 1]
        for i in range(n):
            j = (i + 1) % n
            bm.faces.new((A[i], A[j], B[j], B[i])).material_index = mids[i]
    bm.faces.new(list(reversed(rings[0])))
    bm.faces.new(rings[-1])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    # clean horizontal ends: flush with the plinth top, and cut inside the crown
    bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, 0, CUT_TOP),
                           plane_no=(0, 0, 1), clear_outer=True)
    bmesh.ops.bisect_plane(bm, geom=bm.verts[:] + bm.edges[:] + bm.faces[:], plane_co=(0, 0, BASE_TOP - 3),
                           plane_no=(0, 0, 1), clear_inner=True)
    return finish(name, bm, [black, edge])


# ----------------------------------------------------------------------------- the rest
def bell_profile():
    prof = []
    z = BASE_TOP
    while z < BELL_Z1:
        prof.append((bell_r(z), z))
        z += 7
    p0 = Vector((bell_r(BELL_Z1), BELL_Z1))
    ctrl = Vector((p0.x + dRc(BELL_Z1) * (SHOULDER_Z - BELL_Z1), SHOULDER_Z))
    p1 = Vector((CORE_R + 3, SHOULDER_Z))
    for i in range(7):                     # quadratic Bezier shoulder rolling inward to the core
        t = i / 6
        q = (1 - t) ** 2 * p0 + 2 * (1 - t) * t * ctrl + t * t * p1
        prof.append((q.x, q.y))
    prof.append((CORE_R - 1, SHOULDER_Z))
    return prof


def data_streaks(mat):
    """Short vertical light dashes around the core: packets of data rising (a scrolling texture in the real prop)."""
    rng = random.Random(11)
    bm = bmesh.new()
    cols = 20
    for c in range(cols):
        ang = 2 * pi * c / cols + rng.uniform(-0.05, 0.05)
        t, e = Vector((-sin(ang), cos(ang), 0)), Vector((cos(ang), sin(ang), 0))
        z = SHOULDER_Z + rng.uniform(4, 40)
        while True:
            length = rng.uniform(3, 16)
            if z + length > COLLAR_Z0 - 6:
                break
            ctr = e * (CORE_R + 0.6)
            vs = [bm.verts.new(ctr + t * sx * 0.6 + e * sy * 0.5 + Vector((0, 0, zz)))
                  for zz in (z, z + length) for (sx, sy) in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
            for f in ((0, 1, 2, 3), (7, 6, 5, 4), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)):
                bm.faces.new([vs[k] for k in f])
            z += length + rng.uniform(10, 44)
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return finish("core_data", bm, [mat], smooth=False, shadow=False)


def emblem(black, red, hot, white):
    """Kuroda emblem in the YZ plane (faces west to the approach and east to the tower): pointy-top hexagon ring,
    neon on both faces, black rims; floating diamond on light rods."""
    def P(r, k, x):
        a = radians(90 + 60 * k)
        return Vector((x, r * cos(a), EC + r * sin(a)))

    bm = bmesh.new()
    V = {}
    for k in range(6):
        for (r, x) in ((E_O, -E_D), (E_O, E_D), (E_I, E_D), (E_I, -E_D)):
            V[(k, r, x)] = bm.verts.new(P(r, k, x))
    for k in range(6):
        l = (k + 1) % 6
        quads = (((k, E_O, E_D), (l, E_O, E_D), (l, E_I, E_D), (k, E_I, E_D), 1),      # west face: neon
                 ((k, E_I, -E_D), (l, E_I, -E_D), (l, E_O, -E_D), (k, E_O, -E_D), 1),  # east face: neon
                 ((k, E_O, -E_D), (l, E_O, -E_D), (l, E_O, E_D), (k, E_O, E_D), 0),    # outer rim
                 ((k, E_I, E_D), (l, E_I, E_D), (l, E_I, -E_D), (k, E_I, -E_D), 0))    # inner rim
        for q in quads:
            bm.faces.new([V[q[i]] for i in range(4)]).material_index = q[4]
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    finish("emblem_ring", bm, [black, red], smooth=False)

    bm = bmesh.new()
    c = Vector((0, 0, EC))
    top, bot = bm.verts.new(c + Vector((0, 0, DIA_H))), bm.verts.new(c - Vector((0, 0, DIA_H)))
    eq = [bm.verts.new(c + v) for v in (Vector((-DIA_D, 0, 0)), Vector((0, DIA_W, 0)),
                                        Vector((DIA_D, 0, 0)), Vector((0, -DIA_W, 0)))]
    for i in range(4):
        j = (i + 1) % 4
        bm.faces.new((top, eq[i], eq[j]))
        bm.faces.new((bot, eq[j], eq[i]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    finish("emblem_diamond", bm, [hot], smooth=False, shadow=False)

    bm = bmesh.new()
    for z0, z1 in ((EC - E_I - 2, EC - DIA_H + 3), (EC + DIA_H - 3, EC + E_I + 2)):
        bmesh.ops.create_cone(bm, cap_ends=True, segments=8, radius1=1.3, radius2=1.3, depth=z1 - z0,
                              matrix=Matrix.Translation((0, 0, (z0 + z1) / 2)))
    finish("emblem_rods", bm, [white], smooth=True, shadow=False)


def build():
    black = stage.mat("helix_black_lacquer", (0.02, 0.021, 0.025), rough=0.32, metal=0.0)   # dark base ...
    bsdf = black.node_tree.nodes["Principled BSDF"]
    for key, val in (("Coat Weight", 1.0), ("Coat Roughness", 0.05)):                       # ... under a gloss coat
        if key in bsdf.inputs:
            bsdf.inputs[key].default_value = val
    plinth = stage.mat("helix_plinth", (0.05, 0.052, 0.06), rough=0.3, metal=0.25)
    red = stage.neon("helix_neon_red", stage.RED, 3.6)
    cyan = stage.neon("helix_neon_cyan", stage.CYAN, 3.5)
    white = stage.neon("helix_neon_white", stage.WHITE, 6)
    hot = stage.neon("helix_neon_hot", (1.0, 0.45, 0.45), 8)
    core = stage.hologram("helix_core", stage.CYAN, 2.0, 0.36)
    edge = neon_gradient("helix_edge", stage.CYAN, stage.RED, *GRAD, 3.5)

    # round stepped plinth with light lines in the risers
    for i, (r, z0, z1) in enumerate(STEPS):
        lathe(f"step{i + 1}", [(r, z0), (r, z1), (0.5, z1)], plinth, cap_bottom=True)
    band("step1_line", STEPS[0][0] + 0.4, 5, STEPS[0][0] + 0.4, 7, cyan)
    band("step3_line", STEPS[2][0] + 0.4, 32, STEPS[2][0] + 0.4, 34.5, red)

    # solid bell the strands ride on (cover), etched with data-layer lines, rounding into the core
    lathe("bell", bell_profile(), plinth, sharp=None)
    for z in BELL_LINES:
        band(f"bell_line{z}", bell_r(z - 0.9) + 0.35, z - 0.9, bell_r(z + 0.9) + 0.35, z + 0.9, cyan)
    stage.torus("bell_lip", CORE_R + 2, 2.2, cyan, loc=(0, 0, SHOULDER_Z), major_seg=SEG, minor_seg=6)

    # the double helix: identical black strands, edge light rising from data cyan to Kuroda red
    ribbon("strand_a", PHASE, black, edge)
    ribbon("strand_b", PHASE + pi, black, edge)

    # translucent data core with a hot filament and rising data packets
    lathe("core", [(CORE_R, CORE_Z0), (CORE_R, CORE_Z1)], core, segs=32, cap_top=True, cap_bottom=True,
          sharp=None, shadow=False)
    lathe("core_filament", [(6, CORE_Z0), (6, CORE_Z1)], stage.neon("helix_filament", (0.7, 0.95, 1.0), 8),
          segs=12, sharp=None, shadow=False)
    data_streaks(stage.neon("helix_data", (0.6, 0.93, 1.0), 3))

    # collar gathering into the neck that presents the emblem
    lathe("crown", [(r, COLLAR_Z0 + dz) for (r, dz) in CROWN], black, sharp=38)
    stage.torus("crown_neon", RIM_R, 2.0, red, loc=(0, 0, COLLAR_Z0 + RIM_Z), major_seg=SEG, minor_seg=6)
    stage.torus("crown_lip", CORE_R + 2, 2.0, cyan, loc=(0, 0, COLLAR_Z0), major_seg=SEG, minor_seg=6)
    stage.torus("socket_clasp", 10.2, 1.4, red, loc=(0, 0, COLLAR_Z0 + CROWN[-2][1] - 1), major_seg=24,
                minor_seg=6)
    emblem(black, red, hot, white)

    # uplight pucks on the second step
    for i in range(4):
        a = radians(45 + 90 * i)
        stage.prism(f"puck{i}", 5, STEPS[1][2], STEPS[1][2] + 2, white, sides=12, cx=113 * cos(a), cy=113 * sin(a))


def lights():
    # red wash from the emblem over the crown and the tops of the strands
    stage.light("POINT", "emblem_red", (0, 0, EC), stage.RED, 6e5)
    stage.light("POINT", "crown_red_w", (-120, 0, COLLAR_Z0 + 30), stage.RED, 1.5e5)
    # the core lights the inner faces of the strands and the bell shoulder
    for z in (170, 210, 250):
        ob = stage.light("POINT", f"core_{z}", (0, 0, z), stage.CYAN, 1.6e5)
        ob.data.shadow_soft_size = 8
    # cool uplights from the pucks graze the strands
    for i in range(4):
        a = radians(45 + 90 * i)
        p = (113 * cos(a), 113 * sin(a), STEPS[1][2] + 3)
        stage.light("SPOT", f"uplight{i}", p, (0.75, 0.9, 1.0), 9e5, target=(0.25 * p[0], 0.25 * p[1], 200),
                    size=30, blend=0.7)
    # soft plaza fill from the approach side, range-limited to the court (so the shared stage stays comparable)
    ob = stage.light("AREA", "west_fill", (-360, -60, 260), (0.8, 0.85, 1.0), 6e5, target=(0, 0, 170))
    ob.data.size = 220
    if hasattr(ob.data, "use_custom_distance"):
        ob.data.use_custom_distance = True
        ob.data.cutoff_distance = 700
    # reflection probe = the court's env_cubemap, so the black lacquer shows the city like $envmap will in game
    pd = bpy.data.lightprobes.new("helix_cubemap", "SPHERE")
    for attr, val in (("influence_distance", 700.0), ("clip_start", 60.0), ("clip_end", 6000.0)):
        if hasattr(pd, attr):
            setattr(pd, attr, val)
    ob = bpy.data.objects.new("helix_cubemap", pd)
    ob.location = (-160, 0, 180)
    stage.collection("lights").objects.link(ob)


def report():
    tot = 0
    for ob in stage.collection().objects:
        if ob.type == "MESH":
            t = sum(len(p.vertices) - 2 for p in ob.data.polygons)
            tot += t
            print(f"  {ob.name:18s} {t:6d} tris")
    print(f"HELIX_TRIS {tot}")


def main(tag="helix", views=("eye", "approach", "wide"), save_blend=True):
    stage.reset()
    build()
    lights()
    report()
    stage.environment()
    return stage.render(tag, views=views, save_blend=save_blend)


if __name__ == "__main__":
    main()
