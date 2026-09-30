"""Monument concept "FIBRE TREE" -- quick 3D sketch for dys_blackice (Kuroda Plaza, sunken court).

A calm organic-tech 'tree of knowledge': twelve dark glossy cables twist around a core into a trunk, part into six
limbs and end in bundles of fibre-optic strands whose lit tips form a lumpy, rounded crown, with small translucent
data-leaf panels floating in it. It grows out of a black mirror pool in a raised hex planter whose rim carries the
Kuroda emblem and a red neon band; cable roots spill over the rim and plug into floor ports.

Run:  blender --background --factory-startup --python concept_tree.py
Units = Source units; base centre at the origin on z = 0; +X = east (tower), -X = west (players' approach).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import stage  # noqa: E402

import random  # noqa: E402
from math import asin, cos, pi, radians, sin  # noqa: E402

import bmesh  # noqa: E402
import bpy  # noqa: E402
from mathutils import Matrix, Vector  # noqa: E402

rng = random.Random(20260930)

# ----------------------------------------------------------------------------- dimensions
Z_POOL, Z_RIM, Z_PLINTH = 44.0, 50.0, 5.0
R_WALL, R_RIM, R_RIM_IN, R_PLINTH = 112.0, 116.0, 100.0, 118.0    # hex circumradii
PH = 30.0                                  # hex phase: flat faces look at 0/60/.../300 deg (one faces -X, the players)
C30 = cos(radians(30))
AP_WALL, AP_RIM, AP_RIM_IN = R_WALL * C30, R_RIM * C30, R_RIM_IN * C30
EMBLEM_FACES = (180, 60, 300)              # Kuroda emblems (west face = the approach)
ROOT_FACES = (0, 120, 240)                 # cable roots spill over these faces

K = 12                                     # cables in the trunk
Z_T0, Z_T1 = 52.0, 226.0                   # twisted part of the trunk
TWIST = radians(200)
PROFILE = [(52, 50), (64, 38), (84, 29), (110, 25), (140, 24), (170, 25), (196, 28), (214, 34), (226, 42)]
RC = [7.4, 6.6, 7.8, 6.8, 7.2, 6.4, 7.6, 7.0, 6.6, 7.8, 6.8, 7.2]   # cable radii
CROWN_C, CROWN_A, CROWN_B = Vector((0, 0, 262)), 158.0, 114.0       # crown ellipsoid (tips live on it)
N_LEAVES = 100
SIDES_CABLE, SIDES_FIBRE = 6, 3
SEG_CABLE = 13.0


# ----------------------------------------------------------------------------- materials
def glow_mat(name, base, emit_col, strength, rough=0.22, metal=0.8, spec=0.5):
    """Dark glossy surface whose emission follows the per-vertex 'glow' attribute (0..1) -- fibre-optic light."""
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*base, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if "Specular IOR Level" in b.inputs:
        b.inputs["Specular IOR Level"].default_value = spec
    b.inputs["Emission Color"].default_value = (*emit_col, 1)
    at = nt.nodes.new("ShaderNodeAttribute")
    at.attribute_name = "glow"
    mul = nt.nodes.new("ShaderNodeMath")
    mul.operation = "MULTIPLY"
    mul.inputs[1].default_value = strength
    nt.links.new(at.outputs["Fac"], mul.inputs[0])
    nt.links.new(mul.outputs[0], b.inputs["Emission Strength"])
    return m


def leaf_mat(name, color, strength=5.0):
    """Translucent data leaf: faint body, glowing rim (driven by the 'glow' attribute: 0 centre .. 1 rim)."""
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = (*color, 1)
    at = nt.nodes.new("ShaderNodeAttribute")
    at.attribute_name = "glow"
    pw = nt.nodes.new("ShaderNodeMath")          # steep falloff -> clear body, luminous edge
    pw.operation = "POWER"
    pw.inputs[1].default_value = 4.0
    nt.links.new(at.outputs["Fac"], pw.inputs[0])
    mul = nt.nodes.new("ShaderNodeMath")
    mul.operation = "MULTIPLY_ADD"
    mul.inputs[1].default_value = strength * 1.6
    mul.inputs[2].default_value = strength * 0.22
    nt.links.new(pw.outputs[0], mul.inputs[0])
    nt.links.new(mul.outputs[0], em.inputs["Strength"])
    fac = nt.nodes.new("ShaderNodeMath")
    fac.operation = "MULTIPLY_ADD"
    fac.inputs[1].default_value = 0.7
    fac.inputs[2].default_value = 0.16
    nt.links.new(pw.outputs[0], fac.inputs[0])
    tr = nt.nodes.new("ShaderNodeBsdfTransparent")
    mix = nt.nodes.new("ShaderNodeMixShader")
    nt.links.new(fac.outputs[0], mix.inputs[0])
    nt.links.new(tr.outputs[0], mix.inputs[1])
    nt.links.new(em.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], out.inputs[0])
    if hasattr(m, "surface_render_method"):
        m.surface_render_method = "BLENDED"
    if hasattr(m, "use_backface_culling"):
        m.use_backface_culling = False
    return m


# ----------------------------------------------------------------------------- geometry helpers
def pol(r, a, z):
    return Vector((r * cos(a), r * sin(a), z))


def face_pt(phi_deg, u, v, z):
    """Point in a planter-face frame: u = out along the face normal, v = along the face (CCW), z = up."""
    a = radians(phi_deg)
    return Vector((u * cos(a) - v * sin(a), u * sin(a) + v * cos(a), z))


def prof(z):
    for (z0, r0), (z1, r1) in zip(PROFILE, PROFILE[1:]):
        if z <= z1:
            return r0 + (r1 - r0) * (z - z0) / (z1 - z0)
    return PROFILE[-1][1]


def _cr(p0, p1, p2, p3, n):
    """Centripetal Catmull-Rom from p1 to p2 (n samples, p2 excluded) -- no loops/overshoot."""
    def nxt(t, a, b):
        return t + max((b - a).length, 1e-4) ** 0.5
    t0 = 0.0
    t1 = nxt(t0, p0, p1)
    t2 = nxt(t1, p1, p2)
    t3 = nxt(t2, p2, p3)
    out = []
    for s in range(n):
        t = t1 + (t2 - t1) * s / n
        a1 = p0 * ((t1 - t) / (t1 - t0)) + p1 * ((t - t0) / (t1 - t0))
        a2 = p1 * ((t2 - t) / (t2 - t1)) + p2 * ((t - t1) / (t2 - t1))
        a3 = p2 * ((t3 - t) / (t3 - t2)) + p3 * ((t - t2) / (t3 - t2))
        b1 = a1 * ((t2 - t) / (t2 - t0)) + a2 * ((t - t0) / (t2 - t0))
        b2 = a2 * ((t3 - t) / (t3 - t1)) + a3 * ((t - t1) / (t3 - t1))
        out.append(b1 * ((t2 - t) / (t2 - t1)) + b2 * ((t - t1) / (t2 - t1)))
    return out


def spline(ctrl, attrs, seg):
    """Smooth curve through ctrl; attrs (tuples per control point) are interpolated along it."""
    P = [Vector(p) for p in ctrl]
    ext = [P[0] * 2 - P[1]] + P + [P[-1] * 2 - P[-2]]
    pts, att = [], []
    for i in range(len(P) - 1):
        n = max(1, round((P[i + 1] - P[i]).length / seg))
        pts += _cr(ext[i], ext[i + 1], ext[i + 2], ext[i + 3], n)
        a, b = attrs[i], attrs[i + 1]
        att += [tuple(x + (y - x) * s / n for x, y in zip(a, b)) for s in range(n)]
    pts.append(P[-1])
    att.append(tuple(attrs[-1]))
    return pts, att


def bezier(p0, p1, p2, p3, n):
    return [p0 * (1 - t) ** 3 + p1 * (3 * (1 - t) ** 2 * t) + p2 * (3 * (1 - t) * t * t) + p3 * t ** 3
            for t in (i / n for i in range(n + 1))]


def tube(bm, pts, radii, glows=None, sides=6, cap_end=False):
    """Sweep a circle along pts (parallel-transport frames). Writes the 'glow' vertex layer if present."""
    glay = bm.verts.layers.float.get("glow")
    n = len(pts)
    tans = [(pts[min(n - 1, i + 1)] - pts[max(0, i - 1)]).normalized() for i in range(n)]
    ref = Vector((0, 0, 1)) if abs(tans[0].z) < 0.9 else Vector((1, 0, 0))
    nrm = tans[0].cross(ref).normalized()
    rings = []
    for i in range(n):
        t = tans[i]
        if i:
            nrm = tans[i - 1].rotation_difference(t) @ nrm
            nrm = (nrm - t * nrm.dot(t)).normalized()
        bi = t.cross(nrm)
        ring = []
        for k in range(sides):
            a = 2 * pi * k / sides
            v = bm.verts.new(pts[i] + (nrm * cos(a) + bi * sin(a)) * radii[i])
            if glay is not None:
                v[glay] = glows[i] if glows else 0.0
            ring.append(v)
        rings.append(ring)
    for i in range(n - 1):
        for k in range(sides):
            k2 = (k + 1) % sides
            bm.faces.new((rings[i][k], rings[i][k2], rings[i + 1][k2], rings[i + 1][k]))
    if cap_end:
        c = bm.verts.new(pts[-1] + tans[-1] * radii[-1] * 0.8)
        if glay is not None:
            c[glay] = glows[-1] if glows else 0.0
        for k in range(sides):
            bm.faces.new((rings[-1][k], rings[-1][(k + 1) % sides], c))


def hexpts(r, z, phase=PH, cx=0.0, cy=0.0):
    return [Vector((cx + r * cos(radians(phase + 60 * i)), cy + r * sin(radians(phase + 60 * i)), z)) for i in range(6)]


def prism_bm(bm, r, z0, z1, phase=PH, cx=0.0, cy=0.0, top=True, bottom=False):
    lo = [bm.verts.new(p) for p in hexpts(r, z0, phase, cx, cy)]
    hi = [bm.verts.new(p) for p in hexpts(r, z1, phase, cx, cy)]
    if top:
        bm.faces.new(hi)
    if bottom:
        bm.faces.new(list(reversed(lo)))
    for i in range(6):
        j = (i + 1) % 6
        bm.faces.new((lo[i], lo[j], hi[j], hi[i]))


def hex_ring_bm(bm, r_out, r_in, z0, z1, phase=PH, cx=0.0, cy=0.0, inner=True, top=True):
    lo_o = [bm.verts.new(p) for p in hexpts(r_out, z0, phase, cx, cy)]
    hi_o = [bm.verts.new(p) for p in hexpts(r_out, z1, phase, cx, cy)]
    hi_i = [bm.verts.new(p) for p in hexpts(r_in, z1, phase, cx, cy)]
    lo_i = [bm.verts.new(p) for p in hexpts(r_in, z0, phase, cx, cy)] if inner else None
    for i in range(6):
        j = (i + 1) % 6
        bm.faces.new((lo_o[i], lo_o[j], hi_o[j], hi_o[i]))
        if top:
            bm.faces.new((hi_o[i], hi_o[j], hi_i[j], hi_i[i]))
        if inner:
            bm.faces.new((lo_i[i], hi_i[i], hi_i[j], lo_i[j]))


def flat_hex_ring(bm, r_out, r_in, z, phase=0.0, cx=0.0, cy=0.0):
    o = [bm.verts.new(p) for p in hexpts(r_out, z, phase, cx, cy)]
    i_ = [bm.verts.new(p) for p in hexpts(r_in, z, phase, cx, cy)]
    for i in range(6):
        j = (i + 1) % 6
        bm.faces.new((o[i], o[j], i_[j], i_[i]))


def octa(bm, c, r):
    px, nx, py, ny, pz, nz = (bm.verts.new(c + Vector(d) * r)
                              for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)))
    for a, b in ((px, py), (py, nx), (nx, ny), (ny, px)):
        bm.faces.new((a, b, pz))
        bm.faces.new((b, a, nz))


def ico(bm, c, r):
    bmesh.ops.create_icosphere(bm, subdivisions=1, radius=r, matrix=Matrix.Translation(c))


def emblem(bm, phi_deg, u, zc, r):
    """Kuroda logo (pointy-top hexagon outline + vertical diamond) flat on a planter face, facing outward."""
    def P(x, y):
        return face_pt(phi_deg, u, x, zc + y)
    ri = r - 2.6 / C30
    o = [bm.verts.new(P(r * cos(radians(90 + 60 * k)), r * sin(radians(90 + 60 * k)))) for k in range(6)]
    i_ = [bm.verts.new(P(ri * cos(radians(90 + 60 * k)), ri * sin(radians(90 + 60 * k)))) for k in range(6)]
    for k in range(6):
        j = (k + 1) % 6
        bm.faces.new((o[k], o[j], i_[j], i_[k]))
    h, w = r * 0.62, r * 0.3
    bm.faces.new([bm.verts.new(P(x, y)) for x, y in ((w, 0), (0, h), (-w, 0), (0, -h))])


def band(bm, r, z0, z1, phase=PH):
    """Outer skin of a hex prism only (neon band wrapped round the rim)."""
    lo = [bm.verts.new(p) for p in hexpts(r, z0, phase)]
    hi = [bm.verts.new(p) for p in hexpts(r, z1, phase)]
    for i in range(6):
        j = (i + 1) % 6
        bm.faces.new((lo[i], lo[j], hi[j], hi[i]))


def leaf(bm, center, normal, length, width, curl=0.10):
    """Soft oval 'data leaf' panel, slightly cupped; glow layer 0.15 at the centre -> 1 at the rim."""
    glay = bm.verts.layers.float.get("glow")
    n = normal.normalized()
    ref = Vector((0, 0, 1)) if abs(n.z) < 0.9 else Vector((1, 0, 0))
    x = (Matrix.Rotation(rng.uniform(0, 2 * pi), 3, n) @ n.cross(ref)).normalized()
    y = n.cross(x)
    cv = bm.verts.new(center)
    cv[glay] = 0.0
    ring, rim = [], rng.uniform(0.88, 1.0)
    for k in range(12):
        a = 2 * pi * k / 12
        lx, ly = cos(a) * length / 2, sin(a) * width / 2
        v = bm.verts.new(center + x * lx + y * ly + n * (curl * length * 0.5 * (2 * lx / length) ** 2))
        v[glay] = rim
        ring.append(v)
    for k in range(12):
        bm.faces.new((cv, ring[k], ring[(k + 1) % 12]))


def new_bm(glow=False):
    bm = bmesh.new()
    if glow:
        bm.verts.layers.float.new("glow")
    return bm


def dome_point(d, f=1.0):
    """Point on the crown ellipsoid in unit direction d (scaled by f) and the surface normal there."""
    p = CROWN_C + Vector((CROWN_A * d.x, CROWN_A * d.y, CROWN_B * d.z)) * f
    nrm = Vector((d.x / CROWN_A, d.y / CROWN_A, d.z / CROWN_B)).normalized()
    return p, nrm


def dir_from(az, el):
    return Vector((cos(el) * cos(az), cos(el) * sin(az), sin(el)))


def cone_dirs(axis, half_angle, count, min_sep):
    """Up to count unit directions inside a cone round axis, at least min_sep (rad) apart."""
    axis = axis.normalized()
    ref = Vector((0, 0, 1)) if abs(axis.z) < 0.9 else Vector((1, 0, 0))
    u = axis.cross(ref).normalized()
    w = axis.cross(u)
    out = []
    tries = 0
    while len(out) < count and tries < 2000:
        tries += 1
        ca = 1 - rng.random() * (1 - cos(half_angle))
        sa = (1 - ca * ca) ** 0.5
        b = rng.uniform(0, 2 * pi)
        d = (axis * ca + u * (sa * cos(b)) + w * (sa * sin(b))).normalized()
        if all(d.angle(o) >= min_sep for o in out):
            out.append(d)
    return out


# ----------------------------------------------------------------------------- build
def build():
    M_CABLE = glow_mat("tree_cable", (0.010, 0.011, 0.014), stage.CYAN, 6.5, rough=0.16, metal=0.0, spec=0.18)
    M_PLANTER = stage.mat("tree_planter", (0.030, 0.031, 0.036), 0.32, metal=0.25)
    M_POOL = stage.mat("tree_pool", (0.003, 0.004, 0.006), 0.03, metal=0.0)
    M_RED = stage.neon("tree_kuroda_red", stage.RED, 14.0)
    M_CYAN = stage.neon("tree_cyan", stage.CYAN, 10.0)
    M_WHITE = stage.neon("tree_white", stage.WHITE, 9.0)
    M_LEAF = {"cyan": leaf_mat("tree_leaf_cyan", stage.CYAN, 1.9),
              "white": leaf_mat("tree_leaf_white", (0.85, 0.93, 1.0), 1.9),
              "red": leaf_mat("tree_leaf_red", stage.RED, 2.8)}

    cable = new_bm(glow=True)       # trunk cables, core, limbs, fibres (one material in the final prop)
    planter = new_bm()
    metal = new_bm()                # rim cap, floor ports
    pool = new_bm()
    red = new_bm()
    cyan = new_bm()
    white = new_bm()
    leaves = {k: new_bm(glow=True) for k in M_LEAF}

    # --- planter: plinth step, hex wall, black-metal rim cap with red band, mirror pool, emblems
    prism_bm(planter, R_PLINTH, 0.0, Z_PLINTH)
    prism_bm(planter, R_WALL, Z_PLINTH, Z_POOL)
    hex_ring_bm(metal, R_RIM, R_RIM_IN, Z_POOL - 2.0, Z_RIM)
    band(red, R_RIM + 0.35, Z_POOL + 1.4, Z_POOL + 4.4)
    pool.faces.new([pool.verts.new(p) for p in hexpts(R_RIM_IN + 1.0, Z_POOL + 0.02)])
    for f in EMBLEM_FACES:
        emblem(red, f, AP_WALL + 0.35, (Z_PLINTH + Z_POOL) / 2 - 1.0, 14.5)
    # data ripples on the pool: broken cyan arcs round the trunk
    for rr, arcs in ((64.0, ((10, 95), (130, 215), (250, 335))), (82.0, ((40, 150), (190, 300)))):
        for a0, a1 in arcs:
            n = max(3, int((a1 - a0) / 7.5))
            inner = [cyan.verts.new(pol(rr - 0.8, radians(a0 + (a1 - a0) * s / n), Z_POOL + 0.12)) for s in range(n + 1)]
            outer = [cyan.verts.new(pol(rr + 0.8, radians(a0 + (a1 - a0) * s / n), Z_POOL + 0.12)) for s in range(n + 1)]
            for s in range(n):
                cyan.faces.new((inner[s], outer[s], outer[s + 1], inner[s + 1]))

    # --- core (hidden inside the trunk) continuing up as the central leader, ending in the crown's heart node
    core_ctrl = [(0, 0, 38), (0, 0, 58), (0, 0, 90), (0, 0, 150), (0, 0, 205), (0, 0, 228),
                 (3, -2, 252), (-3, 2, 278), (1, -1, 300)]
    core_att = [(34, 0), (25, 0), (19, 0), (17, 0), (17.5, 0), (17, 0), (14, 0), (11, 0), (8.5, 0)]
    pts, att = spline(core_ctrl, core_att, SEG_CABLE)
    tube(cable, pts, [a[0] for a in att], [a[1] for a in att], sides=8, cap_end=True)
    hub = Vector((1, -1, 306))
    ico(white, hub, 4.5)

    # --- the twelve cables: root/dive -> twisted trunk -> limb (pairs) -> branch end
    zs = [z for z, _ in PROFILE]
    branch_ends = []                  # (position, outgoing direction, cable radius, tier)
    sockets = []
    limb_param = [dict(swirl=rng.uniform(8, 16), arch=rng.uniform(6, 12)) for _ in range(K // 2)]
    elev = [radians(rng.uniform(4, 13)) if i % 2 == 0 else radians(rng.uniform(30, 40)) for i in range(K)]
    for i in range(K):
        th_deg = 15 + 30 * i
        th = radians(th_deg)
        rc = RC[i]
        ctrl, att = [], []
        # bottom: root over a planter face, or dive into the pool
        face = next((f for f in ROOT_FACES if (th_deg - f) % 360 in (15, 345)), None)
        if face is not None:
            s = 1 if (th_deg - face) % 360 == 15 else -1
            end = face_pt(face, AP_RIM + 34, s * 28, rc * 0.5)
            sockets.append(end)
            ctrl += [end,
                     face_pt(face, AP_RIM + 23, s * 24, rc * 0.92),
                     face_pt(face, AP_RIM + rc + 3.5, s * 20, rc + 7),
                     face_pt(face, AP_RIM + rc * 0.95, s * 18.5, 27),
                     face_pt(face, AP_RIM + rc * 0.9, s * 18, Z_RIM - 3),
                     face_pt(face, AP_RIM - 6, s * 17, Z_RIM + rc * 0.9),
                     face_pt(face, AP_RIM_IN - 6, s * 16, Z_POOL + rc * 0.5),
                     face_pt(face, 68, s * 15, Z_POOL + rc * 0.45)]
            att += [(rc * 0.8, 0.06)] + [(rc, 0.0)] * 7
        else:
            ctrl += [pol(86, th - radians(5), Z_POOL - 14), pol(74, th - radians(2), Z_POOL - 1),
                     pol(62, th, Z_POOL + rc * 0.5)]
            att += [(rc, 0.0)] * 3
        # trunk
        for z in zs:
            ctrl.append(pol(prof(z), th + TWIST * (z - Z_T0) / (Z_T1 - Z_T0), z))
            att.append((rc, 0.0))
        # limb (cables 2L and 2L+1 travel together, twisting round each other) and the branch end
        L, side = i // 2, (-1 if i % 2 == 0 else 1)
        phi = radians(15 + 60 * L + 15) + TWIST
        p0 = pol(prof(Z_T1), phi, Z_T1)
        d_c = [dir_from(radians(15 + 30 * j) + TWIST, elev[j]) for j in (2 * L, 2 * L + 1)]
        b_c = [dome_point(d, 0.70)[0] for d in d_c]
        e_l = p0 + ((b_c[0] + b_c[1]) * 0.5 - p0) * 0.62 + Vector((0, 0, 6))
        dvec = (e_l - p0).normalized()
        lat = Vector((-sin(phi), cos(phi), 0))
        lat = (lat - dvec * lat.dot(dvec)).normalized()
        wv = dvec.cross(lat)
        lp = limb_param[L]
        for sfrac, rf, g in ((1 / 3, 0.86, 0.0), (2 / 3, 0.74, 0.0), (1.0, 0.64, 0.0)):
            axis = p0.lerp(e_l, sfrac) + Vector((0, 0, lp["arch"] * sin(pi * sfrac))) + lat * (lp["swirl"] * sfrac * sfrac)
            beta = (pi if side < 0 else 0.0) + pi * sfrac
            ro = 10.9 + (5.0 - 10.9) * sfrac
            ctrl.append(axis + (lat * cos(beta) + wv * sin(beta)) * ro)
            att.append((rc * rf, g))
        b_end = dome_point(d_c[0 if side < 0 else 1], 0.70)[0]
        ctrl.append(b_end)
        att.append((rc * 0.5, 0.05))
        pts, a = spline(ctrl, att, SEG_CABLE)
        tube(cable, pts, [x[0] for x in a], [x[1] for x in a], sides=SIDES_CABLE, cap_end=True)
        branch_ends.append((b_end, (pts[-1] - pts[-2]).normalized(), rc, d_c[0 if side < 0 else 1]))
        ico(white, b_end + (pts[-1] - pts[-2]).normalized() * rc * 0.3, rc * 0.34 + 0.6)

    # --- glowing data strands in the trunk grooves (light rising to the crown)
    for j in range(6):
        th = radians(60 * j)
        ctrl = [pol(prof(z) + 5.2, th + TWIST * (z - Z_T0) / (Z_T1 - Z_T0), z) for z in [58] + zs[2:-1]]
        att = [(1.2, 0.3 + 0.5 * (z - 58) / (zs[-2] - 58)) for z in [58] + zs[2:-1]]
        pts, a = spline(ctrl, att, 12.0)
        tube(cable, pts, [x[0] for x in a], [x[1] for x in a], sides=4)

    # --- floor ports where the roots plug in
    for p in sockets:
        prism_bm(metal, 10.5, 0.0, 2.2, phase=0.0, cx=p.x, cy=p.y)
        flat_hex_ring(cyan, 9.0, 7.0, 2.25, phase=0.0, cx=p.x, cy=p.y)

    # --- crown: fibre sprays from each branch end (+ the heart node) out to lit tips on the ellipsoid
    sources = [(b, d, 1.3, c, 7, radians(28)) for (b, d, rc, c) in branch_ends]
    sources.append((hub, Vector((0, 0, 1)), 1.5, Vector((0, 0, 1)), 14, radians(30)))
    tips = []
    for (S, dS, r0, cdir, count, half) in sources:
        for d in cone_dirs(cdir, half, count, radians(7.5)):
            T, nT = dome_point(d, rng.uniform(0.95, 1.06))
            ln = (T - S).length
            pts = bezier(S, S + dS * ln * 0.42, T - nT * ln * 0.32, T, 5)
            k = len(pts) - 1
            tube(cable, pts, [r0 + (0.7 - r0) * t / k for t in range(k + 1)],
                 [0.01 + 0.99 * (t / k) ** 5 for t in range(k + 1)], sides=SIDES_FIBRE)   # AgX: keep it low
            tips.append(T)
            octa(white if rng.random() < 0.3 else cyan, T, rng.uniform(2.2, 3.2))

    # --- floating data leaves: spread evenly through the crown shell (one soft volume), a few drifting down
    def pick():
        r = rng.random()
        return "cyan" if r < 0.70 else ("white" if r < 0.88 else "red")
    placed, tries = [], 0
    s_lo, s_hi = sin(radians(-26)), sin(radians(84))
    while len(placed) < N_LEAVES and tries < 6000:
        tries += 1
        el = asin(rng.uniform(s_lo, s_hi))
        P, nP = dome_point(dir_from(rng.uniform(0, 2 * pi), el), rng.uniform(0.72, 1.0))
        if any((P - q).length < 17 for q in placed):
            continue
        placed.append(P)
        tilt = Vector((rng.uniform(-1, 1), rng.uniform(-1, 1), rng.uniform(-0.6, 1))).normalized()
        ln = rng.uniform(17, 26)
        leaf(leaves[pick()], P, nP.lerp(tilt, rng.uniform(0.2, 0.55)), ln, ln * rng.uniform(0.6, 0.72))
    for k in range(5):                     # drifting down
        a = radians(200 + 72 * k + rng.uniform(-15, 15))
        P = pol(rng.uniform(62, 112), a, rng.uniform(150, 215))
        ln = rng.uniform(13, 18)
        leaf(leaves[pick()], P, Vector((rng.uniform(-1, 1), rng.uniform(-1, 1), rng.uniform(-0.3, 0.3))), ln, ln * 0.66)

    objs = [stage.obj_from_bmesh("tree_cables", cable, M_CABLE, smooth=True),
            stage.obj_from_bmesh("tree_planter", planter, M_PLANTER),
            stage.obj_from_bmesh("tree_metal", metal, M_CABLE),
            stage.obj_from_bmesh("tree_pool", pool, M_POOL),
            stage.obj_from_bmesh("tree_red", red, M_RED),
            stage.obj_from_bmesh("tree_cyan", cyan, M_CYAN, smooth=True),
            stage.obj_from_bmesh("tree_white", white, M_WHITE, smooth=True)]
    for k, bm in leaves.items():
        objs.append(stage.obj_from_bmesh(f"tree_leaves_{k}", bm, M_LEAF[k], smooth=True))
    return objs, sockets


def lights(sockets):
    L = stage.light
    tree, floor = stage.collection("concept"), stage.collection("stage")

    def tune(ob, soft=None, spec=None, only=None):
        if soft is not None:
            ob.data.shadow_soft_size = soft
        if spec is not None:
            ob.data.specular_factor = spec
        if only is not None and hasattr(ob, "light_linking"):
            ob.light_linking.receiver_collection = only       # light linking (EEVEE/Cycles, Blender 4.2+)
        return ob
    # a down-spot from above the crown throws dappled cyan light (the canopy's shadow) on the court
    tune(L("SPOT", "crown_down", (0, 0, 390), stage.CYAN, 3.5e6, target=(0, 0, 0), size=90, blend=0.9),
         soft=6, spec=0.0, only=floor)
    # warm uplights set in the pool, grazing the twisted trunk
    for n, a in enumerate((212, 148)):
        tune(L("SPOT", f"uplight_{n}", tuple(pol(84, radians(a), Z_POOL + 3)), stage.WHITE, 3e5,
               target=(0, 0, 150), size=30, blend=0.8), soft=3, only=tree)
    # cyan rim from the tower side for the silhouette
    tune(L("SPOT", "rim_east", (300, 60, 320), stage.CYAN, 2.5e6, target=(0, 0, 210), size=40, blend=0.5), only=tree)
    # Kuroda red spill from the emblems onto the wet floor (no specular: no hot-spot blobs in the wet floor)
    for f in EMBLEM_FACES:
        tune(L("POINT", f"kuroda_{f}", (126 * cos(radians(f)), 126 * sin(radians(f)), 16), stage.RED, 9e4),
             soft=10, spec=0.0)
    for n, p in enumerate(sockets):
        tune(L("POINT", f"port_{n}", (p.x, p.y, 9), stage.CYAN, 1.8e4), soft=6, spec=0.0)


def tri_count(objs):
    total = 0
    for ob in objs:
        t = sum(len(p.vertices) - 2 for p in ob.data.polygons)
        print(f"  {ob.name:22s} {t:6d} tris")
        total += t
    print(f"TREE_TRIS {total}")
    vs = [ob.matrix_world @ v.co for ob in objs for v in ob.data.vertices]
    rad = lambda v: (v.x * v.x + v.y * v.y) ** 0.5  # noqa: E731
    print(f"TREE_EXTENTS height {max(v.z for v in vs):.0f}  max radius {max(rad(v) for v in vs):.0f}  "
          f"max radius below z220 {max(rad(v) for v in vs if v.z < 220):.0f}  "
          f"lowest point beyond r150 {min((v.z for v in vs if rad(v) > 150), default=0):.0f}")
    return total


stage.reset()
objects, ports = build()
tri_count(objects)
stage.environment()
lights(ports)
stage.render("tree")
