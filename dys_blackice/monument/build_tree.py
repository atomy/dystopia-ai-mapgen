"""Kuroda fibre tree: procedural Blender build -> SMDs + QC (+ .blend and preview renders).

Run:  blender --background --factory-startup --python build_tree.py -- [--out DIR] [--qc FILE] [--preview DIR]

Model space = Source units, base centre on the court floor at the origin, +X east (toward the Kuroda tower),
-X west (the players' approach).
Design:
- Trunk: twelve black glossy cables twist 200 deg round a core. Cyan light strands run in its grooves.
- Crown: the trunk parts into six limbs, which end in tufts of fibre-optic strands. Their lit tips and floating
  additive data leaves form a rounded crown.
- Base: the tree grows from a black mirror pool in a hex planter. The planter has a red neon band and three
  Kuroda emblems.
- Roots: cable roots spill over the rim into cyan-ringed floor ports.
Materials:
- kuroda_tree_cable: trim sheet, see tree_textures.py.
- kuroda_tree_concrete: planter.
- kuroda_tree_neon: unlit.
- kuroda_tree_leaf: additive, $nocull.
"""
from __future__ import annotations

import json
import math
import os
import random
import sys
from math import asin, cos, pi, radians, sin
from pathlib import Path

import bmesh
import bpy
from mathutils import Matrix, Vector

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import smd_export  # noqa: E402

GAME = Path(r"M:\SteamLibrary\steamapps\common\Dystopia\dystopia")
TEXSRC = GAME / "materialsrc" / "models" / "blackice"
NAME = "kuroda_tree"
CABLE, CONC, NEON, LEAF = "kuroda_tree_cable", "kuroda_tree_concrete", "kuroda_tree_neon", "kuroda_tree_leaf"
rng = random.Random(20260930)

# ----------------------------------------------------------------------------- dimensions (units)
Z_POOL, Z_RIM, Z_PLINTH = 44.0, 50.0, 5.0
R_WALL, R_RIM, R_RIM_IN, R_PLINTH = 112.0, 116.0, 100.0, 118.0    # hex circumradii
PH = 30.0                                  # hex phase: flat faces look at 0/60/.../300 deg (one faces -X, the players)
C30 = cos(radians(30))
AP_WALL, AP_RIM, AP_RIM_IN = R_WALL * C30, R_RIM * C30, R_RIM_IN * C30
EMBLEM_FACES = (180, 60, 300)              # Kuroda emblems (west face = the approach)
ROOT_FACES = (0, 120, 240)                 # cable roots spill over these faces into floor ports
EMBLEM_Z, EMBLEM_R = 23.5, 14.5

K = 12                                     # cables in the trunk
Z_T0, Z_T1 = 52.0, 226.0                   # twisted part of the trunk
TWIST = radians(200)
PROFILE = [(52, 50), (64, 38), (84, 29), (110, 25), (140, 24), (170, 25), (196, 28), (214, 34), (226, 42)]
RC = [7.4, 6.6, 7.8, 6.8, 7.2, 6.4, 7.6, 7.0, 6.6, 7.8, 6.8, 7.2]   # cable radii
CROWN_C, CROWN_A, CROWN_B = Vector((0, 0, 262)), 158.0, 114.0       # crown ellipsoid (tips live on it)
FIBRES_PER_END, HUB_FIBRES, N_LEAVES = 5, 10, 130
CULL_Z = (70.0, 200.0)                     # trunk zone where the inward faces of the cables are hidden
SIDES_CABLE, SIDES_FIBRE = 6, 3
TILE = 128.0                               # concrete: units per texture tile

# texture layout (mirrors tree_textures.py)
CBAND = {"A": (0.5, 1.0), "B": (0.25, 0.5), "C": (0.125, 0.25), "D": (0.0, 0.125)}
NROW = {"red": (0.75, 1.0), "cyan": (0.5, 0.75), "white": (0.25, 0.5), "ramp": (0.0, 0.25)}
LEAF_PX = {"cyan_a": (0, 0, 256), "cyan_b": (256, 0, 256), "white": (0, 256, 256), "red": (256, 256, 128),
           "glow_cyan": (384, 256, 128), "glow_red": (256, 384, 128), "glow_white": (384, 384, 128)}
LEAF_CELLS = {k: (x / 512, 1 - (y + s) / 512, (x + s) / 512, 1 - y / 512) for k, (x, y, s) in LEAF_PX.items()}


def cband(b, t, pad=2 / 512):
    v0, v1 = CBAND[b]
    return v0 + pad + (v1 - v0 - 2 * pad) * min(1.0, max(0.0, t))


def nrow(r, t):
    v0, v1 = NROW[r]
    return v0 + 2 / 256 + (v1 - v0 - 4 / 256) * min(1.0, max(0.0, t))


def _args():
    a = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    opt = {"out": HERE.parent / "build" / "monument", "qc": HERE / f"{NAME}.qc", "preview": None}
    for i in range(0, len(a) - 1, 2):
        opt[a[i].lstrip("-")] = Path(a[i + 1])
    return opt


# ----------------------------------------------------------------------------- mesh builder

def _newell(pts):
    n = Vector((0.0, 0.0, 0.0))
    for i, a in enumerate(pts):
        b = pts[(i + 1) % len(pts)]
        n.x += (a.y - b.y) * (a.z + b.z)
        n.y += (a.z - b.z) * (a.x + b.x)
        n.z += (a.x - b.x) * (a.y + b.y)
    return n


class Mesh:
    """bmesh with one UV layer and per-face materials; becomes one Blender object."""

    def __init__(self, name, smooth=True):
        self.name, self.smooth, self.mats = name, smooth, []
        self.bm = bmesh.new()
        self.uv = self.bm.loops.layers.uv.new("UVMap")

    def v(self, co):
        return self.bm.verts.new(Vector(co))

    def f(self, verts, uvs, mat):
        if mat not in self.mats:
            self.mats.append(mat)
        face = self.bm.faces.new(verts)
        face.material_index = self.mats.index(mat)
        face.smooth = self.smooth
        for lp, uv in zip(face.loops, uvs):
            lp[self.uv].uv = uv
        return face

    def poly(self, pts, uvs, mat, out):
        """Flat polygon with its own vertices, wound CCW seen from the 'out' side."""
        pts = [Vector(p) for p in pts]
        uvs = list(uvs)
        if _newell(pts).dot(Vector(out)) < 0:
            pts, uvs = pts[::-1], uvs[::-1]
        return self.f([self.v(p) for p in pts], uvs, mat)

    def build(self, coll):
        loose = [v for v in self.bm.verts if not v.link_faces]
        if loose:
            bmesh.ops.delete(self.bm, geom=loose, context="VERTS")
        me = bpy.data.meshes.new(self.name)
        self.bm.to_mesh(me)
        self.bm.free()
        for n in self.mats:
            me.materials.append(bpy.data.materials.get(n) or bpy.data.materials.new(n))
        ob = bpy.data.objects.new(self.name, me)
        coll.objects.link(ob)
        return ob


# ----------------------------------------------------------------------------- curve helpers

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
    """Centripetal Catmull-Rom from p1 to p2 (n samples, p2 excluded) -- no loops or overshoot."""
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


def spline(ctrl, radii, segs):
    """Smooth curve through ctrl; radii interpolated; segs[i] = target segment length of span i."""
    P = [Vector(p) for p in ctrl]
    ext = [P[0] * 2 - P[1]] + P + [P[-1] * 2 - P[-2]]
    pts, rad = [], []
    for i in range(len(P) - 1):
        n = max(1, round((P[i + 1] - P[i]).length / segs[i]))
        pts += _cr(ext[i], ext[i + 1], ext[i + 2], ext[i + 3], n)
        rad += [radii[i] + (radii[i + 1] - radii[i]) * s / n for s in range(n)]
    pts.append(P[-1])
    rad.append(radii[-1])
    return pts, rad


def bezier(p0, p1, p2, p3, n):
    return [p0 * (1 - t) ** 3 + p1 * (3 * (1 - t) ** 2 * t) + p2 * (3 * (1 - t) * t * t) + p3 * t ** 3
            for t in (i / n for i in range(n + 1))]


def arclen(pts, scale):
    u = [0.0]
    for a, b in zip(pts, pts[1:]):
        u.append(u[-1] + (b - a).length / scale)
    return u


def tube(mesh: Mesh, pts, radii, sides, mat, vfun, u, cap=False, cull=None):
    """Sweep a circle along pts (parallel-transport frames). u = U per point; vfun(t) maps 0..1 around to V.
    cull(centre, outward) -> True drops that face (hidden inside the trunk). Returns the ring vertex positions."""
    n = len(pts)
    tans = [(pts[min(n - 1, i + 1)] - pts[max(0, i - 1)]).normalized() for i in range(n)]
    ref = Vector((0, 0, 1)) if abs(tans[0].z) < 0.9 else Vector((1, 0, 0))
    nrm = tans[0].cross(ref).normalized()
    rings, dirs = [], []
    for i in range(n):
        t = tans[i]
        if i:
            nrm = tans[i - 1].rotation_difference(t) @ nrm
            nrm = (nrm - t * nrm.dot(t)).normalized()
        bi = t.cross(nrm)
        dr = [nrm * cos(2 * pi * k / sides) + bi * sin(2 * pi * k / sides) for k in range(sides)]
        rings.append([mesh.v(pts[i] + d * radii[i]) for d in dr])
        dirs.append(dr)
    for i in range(n - 1):
        for k in range(sides):
            k2 = (k + 1) % sides
            if cull is not None and cull((pts[i] + pts[i + 1]) * 0.5, (dirs[i][k] + dirs[i][k2]).normalized()):
                continue
            ta, tb = k / sides, (k + 1) / sides
            mesh.f((rings[i][k], rings[i][k2], rings[i + 1][k2], rings[i + 1][k]),
                   ((u[i], vfun(ta)), (u[i], vfun(tb)), (u[i + 1], vfun(tb)), (u[i + 1], vfun(ta))), mat)
    if cap:
        c = mesh.v(pts[-1] + tans[-1] * radii[-1] * 0.8)
        for k in range(sides):
            k2 = (k + 1) % sides
            mesh.f((rings[-1][k], rings[-1][k2], c),
                   ((u[-1], vfun(k / sides)), (u[-1], vfun((k + 1) / sides)), (u[-1] + 0.05, vfun((k + 0.5) / sides))), mat)
    return [v.co.copy() for r in rings for v in r]


def trunk_cull(c, o):
    if not (CULL_Z[0] <= c.z <= CULL_Z[1]):
        return False
    radial = Vector((c.x, c.y, 0.0))
    return radial.length > 1e-6 and o.dot(radial.normalized()) < -0.25


def octa(mesh: Mesh, c, r, mat, uv):
    px, nx, py, ny, pz, nz = (mesh.v(c + Vector(d) * r)
                              for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)))
    for a, b in ((px, py), (py, nx), (nx, ny), (ny, px)):
        mesh.f((a, b, pz), (uv, uv, uv), mat)
        mesh.f((b, a, nz), (uv, uv, uv), mat)


def icosa(mesh: Mesh, c, r, mat, uv):
    g = (1 + 5 ** 0.5) / 2
    raw = [(-1, g, 0), (1, g, 0), (-1, -g, 0), (1, -g, 0), (0, -1, g), (0, 1, g), (0, -1, -g), (0, 1, -g),
           (g, 0, -1), (g, 0, 1), (-g, 0, -1), (-g, 0, 1)]
    vs = [mesh.v(c + Vector(p).normalized() * r) for p in raw]
    for a, b, d in ((0, 11, 5), (0, 5, 1), (0, 1, 7), (0, 7, 10), (0, 10, 11), (1, 5, 9), (5, 11, 4), (11, 10, 2),
                    (10, 7, 6), (7, 1, 8), (3, 9, 4), (3, 4, 2), (3, 2, 6), (3, 6, 8), (3, 8, 9), (4, 9, 5),
                    (2, 4, 11), (6, 2, 10), (8, 6, 7), (9, 8, 1)):
        mesh.f((vs[a], vs[b], vs[d]), (uv, uv, uv), mat)


def card(mesh: Mesh, c, x, y, cell):
    """Flat additive quad centred on c, half-extents x (width, U) and y (length, V) as vectors."""
    u0, v0, u1, v1 = LEAF_CELLS[cell]
    pu, pv = (u1 - u0) * 0.01, (v1 - v0) * 0.01
    mesh.f((mesh.v(c - x - y), mesh.v(c + x - y), mesh.v(c + x + y), mesh.v(c - x + y)),
           ((u0 + pu, v0 + pv), (u1 - pu, v0 + pv), (u1 - pu, v1 - pv), (u0 + pu, v1 - pv)), LEAF)


def halo(mesh: Mesh, c, r, cell):
    """Three perpendicular additive glow cards: reads as a soft light from any side."""
    for x, y in ((Vector((r, 0, 0)), Vector((0, 0, r))), (Vector((0, r, 0)), Vector((0, 0, r))),
                 (Vector((r, 0, 0)), Vector((0, r, 0)))):
        card(mesh, c, x, y, cell)


def dome_point(d, f=1.0):
    p = CROWN_C + Vector((CROWN_A * d.x, CROWN_A * d.y, CROWN_B * d.z)) * f
    return p, Vector((d.x / CROWN_A, d.y / CROWN_A, d.z / CROWN_B)).normalized()


def dir_from(az, el):
    return Vector((cos(el) * cos(az), cos(el) * sin(az), sin(el)))


def cone_dirs(axis, half_angle, count, min_sep):
    axis = axis.normalized()
    ref = Vector((0, 0, 1)) if abs(axis.z) < 0.9 else Vector((1, 0, 0))
    u = axis.cross(ref).normalized()
    w = axis.cross(u)
    out, tries = [], 0
    while len(out) < count and tries < 4000:
        tries += 1
        ca = 1 - rng.random() * (1 - cos(half_angle))
        sa = (1 - ca * ca) ** 0.5
        b = rng.uniform(0, 2 * pi)
        d = (axis * ca + u * (sa * cos(b)) + w * (sa * sin(b))).normalized()
        if all(d.angle(o) >= min_sep for o in out):
            out.append(d)
    return out


def hexpts(r, z, phase=PH, cx=0.0, cy=0.0):
    return [Vector((cx + r * cos(radians(phase + 60 * i)), cy + r * sin(radians(phase + 60 * i)), z)) for i in range(6)]


# ----------------------------------------------------------------------------- planter

def planter(flat: Mesh):
    """Plinth step, board-formed concrete wall, black metal rim cap with a red neon band, emblems, mirror pool,
    data ripples. Faces are split so static-prop vertex lighting has vertices to work with."""
    def wall(r, z0, z1, mat, vb=None, cols=1, rows=1, off=0.0):
        lo, hi = hexpts(r, z0), hexpts(r, z1)
        for i in range(6):
            j = (i + 1) % 6
            mid = (lo[i] + lo[j]) / 2
            side = (lo[j] - lo[i]).length
            for c in range(cols):
                for rr in range(rows):
                    f0, f1, g0, g1 = c / cols, (c + 1) / cols, rr / rows, (rr + 1) / rows
                    q = [lo[i].lerp(lo[j], f0).lerp(hi[i].lerp(hi[j], f0), g0), lo[i].lerp(lo[j], f1).lerp(hi[i].lerp(hi[j], f1), g0),
                         lo[i].lerp(lo[j], f1).lerp(hi[i].lerp(hi[j], f1), g1), lo[i].lerp(lo[j], f0).lerp(hi[i].lerp(hi[j], f0), g1)]
                    if mat == CONC:
                        us = [(off + (i + f) * side) / TILE for f in (f0, f1, f1, f0)]
                        uvs = [(us[k], q[k].z / TILE) for k in range(4)]
                    else:
                        us = [(i + f) * side / 64 for f in (f0, f1, f1, f0)]
                        uvs = [(us[k], vb((q[k].z - z0) / (z1 - z0))) for k in range(4)]
                    flat.poly(q, uvs, mat, (mid.x, mid.y, 0))

    def ring(r_out, r_in, z, up, mat, vb=None):
        o, n = hexpts(r_out, z), hexpts(r_in, z)
        for i in range(6):
            j = (i + 1) % 6
            q = [o[i], o[j], n[j], n[i]]
            if mat == CONC:
                uvs = [(p.x / TILE, p.y / TILE) for p in q]
            else:
                uvs = [(i * 0.9, vb(1)), ((i + 1) * 0.9, vb(1)), ((i + 1) * 0.9, vb(0)), (i * 0.9, vb(0))]
            flat.poly(q, uvs, mat, (0, 0, 1 if up else -1))

    metal = lambda t: cband("C", t)  # noqa: E731
    wall(R_PLINTH, 0, Z_PLINTH, CONC, cols=2)
    ring(R_PLINTH, R_WALL, Z_PLINTH, True, CONC)
    wall(R_WALL, Z_PLINTH, Z_POOL, CONC, cols=3, rows=2)
    wall(R_RIM, Z_POOL, Z_RIM, CABLE, metal, cols=2)
    ring(R_RIM, R_RIM_IN, Z_RIM, True, CABLE, metal)
    ring(R_RIM, R_WALL, Z_POOL, False, CABLE, metal)                  # overhang under the cap
    lo, hi = hexpts(R_RIM_IN, Z_POOL), hexpts(R_RIM_IN, Z_RIM)       # inner face of the cap, toward the pool
    for i in range(6):
        j = (i + 1) % 6
        mid = (lo[i] + lo[j]) / 2
        flat.poly([lo[i], lo[j], hi[j], hi[i]], [(i, metal(0)), (i + 1, metal(0)), (i + 1, metal(1)), (i, metal(1))],
                  CABLE, (-mid.x, -mid.y, 0))
    # red neon band round the rim cap
    lo, hi = hexpts(R_RIM + 0.35, Z_POOL + 1.4), hexpts(R_RIM + 0.35, Z_POOL + 4.4)
    for i in range(6):
        j = (i + 1) % 6
        mid = (lo[i] + lo[j]) / 2
        flat.poly([lo[i], lo[j], hi[j], hi[i]], [(0.1, nrow("red", 0)), (0.9, nrow("red", 0)), (0.9, nrow("red", 1)),
                                                 (0.1, nrow("red", 1))], NEON, (mid.x, mid.y, 0))
    # Kuroda emblems: pointy-top hex outline + vertical diamond, flat on three wall faces
    for f in EMBLEM_FACES:
        n = face_pt(f, 1, 0, 0)

        def P(x, y):
            return face_pt(f, AP_WALL + 0.35, x, EMBLEM_Z + y)
        ri = EMBLEM_R - 2.6 / C30
        for k in range(6):
            a, b = radians(90 + 60 * k), radians(90 + 60 * (k + 1))
            q = [P(EMBLEM_R * cos(a), EMBLEM_R * sin(a)), P(EMBLEM_R * cos(b), EMBLEM_R * sin(b)),
                 P(ri * cos(b), ri * sin(b)), P(ri * cos(a), ri * sin(a))]
            flat.poly(q, [(0.3, nrow("red", 0)), (0.7, nrow("red", 0)), (0.7, nrow("red", 1)), (0.3, nrow("red", 1))],
                      NEON, n)
        h, w = EMBLEM_R * 0.62, EMBLEM_R * 0.3
        flat.poly([P(w, 0), P(0, h), P(-w, 0), P(0, -h)], [(0.5, nrow("red", 0.5))] * 4, NEON, n)
    # black mirror pool + broken cyan data ripples on it
    pool = hexpts(R_RIM_IN + 1.0, Z_POOL + 0.02)
    flat.poly(pool, [(0.5 + p.x / 400, cband("D", 0.5 + p.y / 400)) for p in pool], CABLE, (0, 0, 1))
    for rr, arcs in ((64.0, ((10, 95), (130, 215), (250, 335))), (82.0, ((40, 150), (190, 300)))):
        for a0, a1 in arcs:
            n = max(3, int((a1 - a0) / 9))
            for s in range(n):
                b0, b1 = radians(a0 + (a1 - a0) * s / n), radians(a0 + (a1 - a0) * (s + 1) / n)
                q = [pol(rr - 0.8, b0, Z_POOL + 0.12), pol(rr + 0.8, b0, Z_POOL + 0.12),
                     pol(rr + 0.8, b1, Z_POOL + 0.12), pol(rr - 0.8, b1, Z_POOL + 0.12)]
                flat.poly(q, [(0.2, nrow("cyan", 0)), (0.2, nrow("cyan", 1)), (0.8, nrow("cyan", 1)), (0.8, nrow("cyan", 0))],
                          NEON, (0, 0, 1))


def floor_port(flat: Mesh, p):
    """Low black metal hex plate with a cyan light ring, where a root plugs into the court floor."""
    lo, hi = hexpts(10.5, 0.0, 0.0, p.x, p.y), hexpts(10.5, 2.2, 0.0, p.x, p.y)
    for i in range(6):
        j = (i + 1) % 6
        mid = (lo[i] + lo[j]) / 2 - Vector((p.x, p.y, 0))
        flat.poly([lo[i], lo[j], hi[j], hi[i]], [(0, cband("C", 0.1)), (0.16, cband("C", 0.1)), (0.16, cband("C", 0.9)),
                                                 (0, cband("C", 0.9))], CABLE, (mid.x, mid.y, 0.1))
    o, n = hexpts(9.0, 2.25, 0.0, p.x, p.y), hexpts(7.0, 2.25, 0.0, p.x, p.y)
    for i in range(6):
        j = (i + 1) % 6
        flat.poly([o[i], o[j], n[j], n[i]], [(0.3, nrow("cyan", 0)), (0.7, nrow("cyan", 0)), (0.7, nrow("cyan", 1)),
                                             (0.3, nrow("cyan", 1))], NEON, (0, 0, 1))
    top = hexpts(10.5, 2.2, 0.0, p.x, p.y)
    flat.poly(top, [(0.1 + i * 0.05, cband("C", 0.5)) for i in range(6)], CABLE, (0, 0, 1))


# ----------------------------------------------------------------------------- tree

def tree(cab: Mesh, glow: Mesh, add: Mesh):
    """Cables, core, strands, fibres, tips, nodes (cab = smooth lit + neon), glow = unlit neon bits, add = additive."""
    va = lambda t: cband("A", t)  # noqa: E731
    vb = lambda t: cband("B", t)  # noqa: E731
    white, cyan = (0.5, nrow("white", 0.5)), (0.5, nrow("cyan", 0.5))
    info = {"roots": {f: [] for f in ROOT_FACES}, "ports_by_face": {f: [] for f in ROOT_FACES}, "divers": {},
            "ports": [], "ends": []}

    # core (hidden inside the trunk) continuing up as the central leader
    core_ctrl = [(0, 0, 38), (0, 0, 58), (0, 0, 90), (0, 0, 150), (0, 0, 205), (0, 0, 228), (3, -2, 252), (-3, 2, 278),
                 (1, -1, 300)]
    pts, rad = spline(core_ctrl, [34, 25, 19, 17, 17.5, 17, 14, 11, 8.5], [30, 30, 40, 40, 30, 16, 16, 16])
    tube(cab, pts, rad, 8, CABLE, va, arclen(pts, 64), cap=True)
    hub = Vector((1, -1, 306))
    icosa(glow, hub, 4.5, NEON, white)

    zs = [z for z, _ in PROFILE]
    limb_param = [dict(swirl=rng.uniform(8, 16), arch=rng.uniform(6, 12)) for _ in range(K // 2)]
    elev = [radians(rng.uniform(4, 13)) if i % 2 == 0 else radians(rng.uniform(30, 40)) for i in range(K)]
    for i in range(K):
        th_deg = 15 + 30 * i
        th = radians(th_deg)
        rc = RC[i]
        ctrl, rad, segs = [], [], []
        face = next((f for f in ROOT_FACES if (th_deg - f) % 360 in (15, 345)), None)
        if face is not None:                    # root: floor port -> up the wall -> over the rim -> across the pool
            s = 1 if (th_deg - face) % 360 == 15 else -1
            port = face_pt(face, AP_RIM + 34, s * 28, 0)
            info["ports"].append(port)
            info["ports_by_face"][face].append(port)
            ctrl += [port + Vector((0, 0, -3)), face_pt(face, AP_RIM + 32, s * 27, rc * 0.55),
                     face_pt(face, AP_RIM + 23, s * 24, rc * 0.92), face_pt(face, AP_RIM + rc + 3.5, s * 20, rc + 7),
                     face_pt(face, AP_RIM + rc * 0.95, s * 18.5, 27), face_pt(face, AP_RIM + rc * 0.9, s * 18, Z_RIM - 3),
                     face_pt(face, AP_RIM - 6, s * 17, Z_RIM + rc * 0.9), face_pt(face, AP_RIM_IN - 6, s * 16, Z_POOL + rc * 0.5),
                     face_pt(face, 68, s * 15, Z_POOL + rc * 0.45)]
            rad += [rc * 0.75, rc * 0.8] + [rc] * 7
            segs += [6, 9, 10, 10, 10, 8, 9, 12, 12]
        else:                                   # diver: rises out of the pool
            ctrl += [pol(86, th - radians(5), Z_POOL - 14), pol(74, th - radians(2), Z_POOL - 1), pol(62, th, Z_POOL + rc * 0.5)]
            rad += [rc] * 3
            segs += [20, 12, 12]
        for z in zs:                            # twisted trunk
            ctrl.append(pol(prof(z), th + TWIST * (z - Z_T0) / (Z_T1 - Z_T0), z))
            rad.append(rc)
        segs += [13] * (len(zs) - 1)
        # limb: cables 2L and 2L+1 travel together, twisting round each other, then part to their branch ends
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
        for sfrac, rf in ((1 / 3, 0.86), (2 / 3, 0.74), (1.0, 0.64)):
            axis = p0.lerp(e_l, sfrac) + Vector((0, 0, lp["arch"] * sin(pi * sfrac))) + lat * (lp["swirl"] * sfrac * sfrac)
            beta = (pi if side < 0 else 0.0) + pi * sfrac
            ro = 10.9 + (5.0 - 10.9) * sfrac
            ctrl.append(axis + (lat * cos(beta) + wv * sin(beta)) * ro)
            rad.append(rc * rf)
        b_end = b_c[0 if side < 0 else 1]
        ctrl.append(b_end)
        rad.append(rc * 0.5)
        segs += [17, 17, 17, 16]
        pts, r = spline(ctrl, rad, segs)
        ring_pts = tube(cab, pts, r, SIDES_CABLE, CABLE, va, arclen(pts, 64), cap=True, cull=trunk_cull)
        low = [q for q in ring_pts if q.z < 70 and math.hypot(q.x, q.y) >= 48]     # the part outside the trunk base
        if face is not None:
            info["roots"][face] += low
        else:
            info["divers"].setdefault(round(th_deg / 60) * 60 % 360, []).extend(low)
        tan = (pts[-1] - pts[-2]).normalized()
        octa(glow, b_end + tan * rc * 0.3, rc * 0.34 + 0.6, NEON, white)
        info["ends"].append((b_end, tan, d_c[0 if side < 0 else 1]))

    # cyan light strands in the trunk grooves, rising dim -> bright (unlit neon ribbons facing outward)
    for j in range(6):
        th = radians(60 * j)
        zz = [58] + zs[2:-1]
        ctrl = [pol(prof(z) + 5.0, th + TWIST * (z - Z_T0) / (Z_T1 - Z_T0), z) for z in zz]
        pts, _ = spline(ctrl, [1] * len(ctrl), [13] * (len(ctrl) - 1))
        u = arclen(pts, 1.0)
        rows = []
        for k, p in enumerate(pts):
            t = (pts[min(len(pts) - 1, k + 1)] - pts[max(0, k - 1)]).normalized()
            radial = Vector((p.x, p.y, 0)).normalized()
            wdir = t.cross(radial).normalized() * 1.2
            uu = 0.12 + 0.86 * u[k] / u[-1]
            rows.append((glow.v(p - wdir), glow.v(p + wdir), uu))
        for k in range(len(rows) - 1):
            a, b = rows[k], rows[k + 1]
            glow.f((a[0], a[1], b[1], b[0]), ((a[2], nrow("ramp", 0)), (a[2], nrow("ramp", 1)), (b[2], nrow("ramp", 1)),
                                              (b[2], nrow("ramp", 0))), NEON)

    # crown: fibre tufts from each branch end (+ the hub) out to lit tips on the ellipsoid
    sources = [(b, d, 1.7, c, FIBRES_PER_END, radians(28)) for (b, d, c) in info["ends"]]
    sources.append((hub, Vector((0, 0, 1)), 1.9, Vector((0, 0, 1)), HUB_FIBRES, radians(30)))
    tips = []
    for (S, dS, r0, cdir, count, half) in sources:
        for d in cone_dirs(cdir, half, count, radians(9)):
            T, nT = dome_point(d, rng.uniform(0.95, 1.06))
            ln = (T - S).length
            pts = bezier(S, S + dS * ln * 0.42, T - nT * ln * 0.32, T, 4)
            k = len(pts) - 1
            tube(cab, pts, [r0 + (1.0 - r0) * q / k for q in range(k + 1)], SIDES_FIBRE, CABLE, vb,
                 [0.02 + 0.97 * q / k for q in range(k + 1)])
            hot = rng.random() < 0.35
            octa(glow, T, rng.uniform(2.4, 3.2), NEON, white if hot else cyan)
            halo(add, T, rng.uniform(4.5, 6.0), "glow_white" if hot else "glow_cyan")
            tips.append((T, hot))
    info["tips"], info["hub"] = tips, hub

    # floating data leaves: spread evenly through the crown shell, a few drifting down round the trunk
    def pick():
        r = rng.random()
        return "cyan_a" if r < 0.35 else ("cyan_b" if r < 0.70 else ("white" if r < 0.88 else "red"))

    def leaf(P, nrm, ln, wd):
        n = nrm.normalized()
        ref = Vector((0, 0, 1)) if abs(n.z) < 0.9 else Vector((1, 0, 0))
        x = (Matrix.Rotation(rng.uniform(0, 2 * pi), 3, n) @ n.cross(ref)).normalized()
        y = n.cross(x)
        card(add, P, x * (wd / 2), y * (ln / 2), pick())

    placed, tries = [], 0
    s_lo, s_hi = sin(radians(-26)), sin(radians(84))
    while len(placed) < N_LEAVES and tries < 6000:
        tries += 1
        P, nP = dome_point(dir_from(rng.uniform(0, 2 * pi), asin(rng.uniform(s_lo, s_hi))), rng.uniform(0.72, 1.0))
        if any((P - q).length < 15 for q in placed):
            continue
        placed.append(P)
        tilt = Vector((rng.uniform(-1, 1), rng.uniform(-1, 1), rng.uniform(-0.6, 1))).normalized()
        ln = rng.uniform(17, 26)
        leaf(P, nP.lerp(tilt, rng.uniform(0.2, 0.55)), ln, ln * rng.uniform(0.6, 0.72))
    for k in range(5):
        a = radians(200 + 72 * k + rng.uniform(-15, 15))
        ln = rng.uniform(13, 18)
        leaf(pol(rng.uniform(62, 112), a, rng.uniform(150, 215)),
             Vector((rng.uniform(-1, 1), rng.uniform(-1, 1), rng.uniform(-0.3, 0.3))), ln, ln * 0.66)
    info["leaves"] = len(placed) + 5
    return info


# ----------------------------------------------------------------------------- collision

def hull_obj(name, pts, coll):
    bm = bmesh.new()
    for q in pts:
        bm.verts.new(q)
    res = bmesh.ops.convex_hull(bm, input=bm.verts)
    junk = list({g for g in res["geom_interior"] + res["geom_unused"] if isinstance(g, bmesh.types.BMVert)})
    if junk:
        bmesh.ops.delete(bm, geom=junk, context="VERTS")
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    coll.objects.link(ob)
    return ob


def circle(r, z, n=12):
    return [Vector((r * cos(2 * pi * k / n), r * sin(2 * pi * k / n), z)) for k in range(n)]


def collision(coll, info):
    """Convex pieces: planter body, six rim bars, trunk (base cone, shaft, top flare) and low hulls over the roots.
    Crown, fibres and leaves have no collision."""
    parts = [("planter", hexpts(R_PLINTH, 0) + hexpts(R_PLINTH, Z_PLINTH) + hexpts(R_WALL, Z_POOL))]
    o0, o1, n0, n1 = hexpts(R_RIM, Z_POOL - 2), hexpts(R_RIM, Z_RIM), hexpts(R_RIM_IN, Z_POOL - 2), hexpts(R_RIM_IN, Z_RIM)
    for i in range(6):                               # rim bars, pulled 0.3u apart at the mitres
        j = (i + 1) % 6
        q = []
        for a, b in ((o0, o0), (o1, o1), (n0, n0), (n1, n1)):
            q += [a[i] + (a[j] - a[i]).normalized() * 0.3, b[j] + (b[i] - b[j]).normalized() * 0.3]
        parts.append((f"rim{i}", q))
    parts += [("trunk_base", circle(54, Z_POOL - 1) + circle(33, 108)),
              ("trunk_shaft", circle(33, 104) + circle(33.5, 180)),
              ("trunk_top", circle(34, 176) + circle(42, 214) + circle(47, 226))]
    for f in ROOT_FACES:
        # each root pair: a low floor ramp (cables lying on the court floor + the two ports, steppable) and a bridge
        # from the pool over the rim and down the wall; both span the pair so nothing can wedge between the cables
        pts = info["roots"][f]
        nf = Vector((cos(radians(f)), sin(radians(f)), 0.0))
        floor = [Vector((q.x, q.y, max(0.0, q.z))) for q in pts if q.z < 16 and q.dot(nf) >= AP_WALL + 4]
        floor += [p + Vector(d) for p in info["ports_by_face"][f]
                  for d in ((10.5, 0, 0), (-10.5, 0, 0), (0, 10.5, 0), (0, -10.5, 0), (0, 0, 2.2))]
        parts.append((f"root_floor{f}", floor))
        parts.append((f"root_bridge{f}", [q for q in pts if q.z >= 12 and q.dot(nf) >= 50]))
    for a, pts in sorted(info["divers"].items()):
        parts.append((f"diver{a}", [q for q in pts if q.z >= Z_POOL - 1]))
    return [hull_obj(f"phys_{n}", pts, coll) for n, pts in parts if len(pts) >= 4]


def walkable_report(objs, min_z=70):
    out = []
    for ob in objs:
        for f in ob.data.polygons:
            if f.normal.z > 0.7:
                zs = [ob.data.vertices[i].co.z for i in f.vertices]
                if max(zs) > min_z:
                    out.append((ob.name, round(min(zs)), round(max(zs)), round(f.area)))
    return out


# ----------------------------------------------------------------------------- preview scene

def _nodes(idb):
    """Enable nodes only where needed (Blender 5 always has them; the setter is deprecated there)."""
    if getattr(idb, "node_tree", None) is None:
        idb.use_nodes = True


def _img(name, non_color=False):
    img = bpy.data.images.load(str(TEXSRC / f"{name}.tga"), check_existing=True)
    if non_color:
        img.colorspace_settings.name = "Non-Color"
    return img


def _lit_material(name, rough_lo, rough_hi, selfillum=0.0, spec=0.35):
    """Source VertexLitGeneric stand-in: base, DirectX normal map (green flipped), phong mask -> roughness,
    base alpha -> selfillum."""
    m = bpy.data.materials[name]
    _nodes(m)
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    bsdf = nt.nodes.new("ShaderNodeBsdfPrincipled")
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.image = _img(name)
    ntex = nt.nodes.new("ShaderNodeTexImage")
    ntex.image = _img(name + "_n", True)
    sep = nt.nodes.new("ShaderNodeSeparateColor")
    inv = nt.nodes.new("ShaderNodeMath")
    inv.operation = "SUBTRACT"
    inv.inputs[0].default_value = 1.0
    comb = nt.nodes.new("ShaderNodeCombineColor")
    nmap = nt.nodes.new("ShaderNodeNormalMap")
    rough = nt.nodes.new("ShaderNodeMapRange")
    rough.inputs["To Min"].default_value = rough_lo
    rough.inputs["To Max"].default_value = rough_hi
    L = nt.links.new
    L(tex.outputs["Color"], bsdf.inputs["Base Color"])
    if selfillum:
        emi = nt.nodes.new("ShaderNodeMath")
        emi.operation = "MULTIPLY"
        emi.inputs[1].default_value = selfillum
        L(tex.outputs["Color"], bsdf.inputs["Emission Color"])
        L(tex.outputs["Alpha"], emi.inputs[0])
        L(emi.outputs[0], bsdf.inputs["Emission Strength"])
    L(ntex.outputs["Color"], sep.inputs[0])
    L(sep.outputs[1], inv.inputs[1])
    L(sep.outputs[0], comb.inputs[0])
    L(inv.outputs[0], comb.inputs[1])
    L(sep.outputs[2], comb.inputs[2])
    L(comb.outputs[0], nmap.inputs["Color"])
    L(nmap.outputs["Normal"], bsdf.inputs["Normal"])
    L(ntex.outputs["Alpha"], rough.inputs["Value"])
    L(rough.outputs[0], bsdf.inputs["Roughness"])
    bsdf.inputs["Metallic"].default_value = 0.0
    if "Specular IOR Level" in bsdf.inputs:
        bsdf.inputs["Specular IOR Level"].default_value = spec
    L(bsdf.outputs[0], out.inputs[0])


def preview_materials():
    _lit_material(CABLE, 0.55, 0.12, selfillum=5.0, spec=0.3)
    _lit_material(CONC, 0.75, 0.35, spec=0.4)
    m = bpy.data.materials[NEON]
    _nodes(m)
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.image = _img(NEON)
    em.inputs["Strength"].default_value = 5.0
    nt.links.new(tex.outputs["Color"], em.inputs["Color"])
    nt.links.new(em.outputs[0], out.inputs[0])
    m = bpy.data.materials[LEAF]                 # additive: transparent + emission
    _nodes(m)
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.image = _img(LEAF)
    em.inputs["Strength"].default_value = 2.2
    tr = nt.nodes.new("ShaderNodeBsdfTransparent")
    add = nt.nodes.new("ShaderNodeAddShader")
    nt.links.new(tex.outputs["Color"], em.inputs["Color"])
    nt.links.new(tr.outputs[0], add.inputs[0])
    nt.links.new(em.outputs[0], add.inputs[1])
    nt.links.new(add.outputs[0], out.inputs[0])
    if hasattr(m, "surface_render_method"):
        m.surface_render_method = "BLENDED"
    if hasattr(m, "use_backface_culling"):
        m.use_backface_culling = False


def _mat(name, color, rough, emit=None, image=None, tile=1.0):
    m = bpy.data.materials.new(name)
    _nodes(m)
    nt = m.node_tree
    bsdf = nt.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*color, 1)
    bsdf.inputs["Roughness"].default_value = rough
    if image:
        tex = nt.nodes.new("ShaderNodeTexImage")
        tex.image = bpy.data.images.load(str(image), check_existing=True)
        tex.projection = "BOX"
        mapn = nt.nodes.new("ShaderNodeMapping")
        mapn.inputs["Scale"].default_value = (tile, tile, tile)
        tc = nt.nodes.new("ShaderNodeTexCoord")
        nt.links.new(tc.outputs["Object"], mapn.inputs[0])
        nt.links.new(mapn.outputs[0], tex.inputs[0])
        nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
        nt.links.new(tex.outputs["Color"], bsdf.inputs["Emission Color"])
        bsdf.inputs["Emission Strength"].default_value = emit or 0
    return m


def _box(name, x0, y0, z0, x1, y1, z1, mat, coll):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector(((x0 + x1) / 2 + v.co.x * (x1 - x0), (y0 + y1) / 2 + v.co.y * (y1 - y0), (z0 + z1) / 2 + v.co.z * (z1 - z0)))
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    me.materials.append(mat)
    ob = bpy.data.objects.new(name, me)
    coll.objects.link(ob)
    return ob


def _light(kind, name, loc, color, power, coll, size=None, blend=0.3, soft=None, spec=None):
    ld = bpy.data.lights.new(name, kind)
    ld.color = color
    ld.energy = power
    if kind == "SPOT":
        ld.spot_size = radians(size or 50)
        ld.spot_blend = blend
    if soft is not None:
        ld.shadow_soft_size = soft
    if spec is not None:
        ld.specular_factor = spec
    ob = bpy.data.objects.new(name, ld)
    ob.location = loc
    coll.objects.link(ob)
    return ob


def _aim(ob, target):
    ob.rotation_euler = (Vector(target) - ob.location).to_track_quat("-Z", "Y").to_euler()


def preview_scene(sc, info):
    """Rough stand-in for the plaza (sunken court, deck, lit tower facade) with lights like monument.place()."""
    coll = bpy.data.collections.new("preview_env")
    sc.collection.children.link(coll)
    wet = _mat("prev_wet_concrete", (0.035, 0.036, 0.042), 0.22)
    deck = _mat("prev_plaza", (0.05, 0.05, 0.058), 0.35)
    wins = GAME / "materialsrc" / "blackice" / "lit_windows.tga"
    facade = _mat("prev_facade", (0.02, 0.02, 0.03), 0.4, emit=1.2, image=wins if wins.exists() else None, tile=1 / 256)
    _box("court_floor", -384, -448, -8, 384, 448, 0, wet, coll)
    for (x0, y0, x1, y1) in ((-2200, -1300, -384, 1300), (384, -1300, 1100, 1300), (-384, 448, 384, 1300), (-384, -1300, 384, -448)):
        _box("plaza", x0, y0, 0, x1, y1, 64, deck, coll)
    _box("tower", 960, -1216, 0, 1088, 1216, 3200, facade, coll)
    for y in (-1500, 1500):
        _box("block", -2200, y - 200, 0, 1100, y + 200, 1800, facade, coll)
    world = bpy.data.worlds.new("night")
    _nodes(world)
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0.006, 0.008, 0.016, 1)
    bg.inputs["Strength"].default_value = 1.0
    sc.world = world
    # same layout as monument.place()
    ob = _light("SPOT", "canopy_down", (0, 0, 640), (0.72, 0.9, 1.0), 6e6, coll, size=100, blend=0.6, soft=4)
    _aim(ob, (0, 0, 0))
    for f in EMBLEM_FACES:
        _light("POINT", f"emblem_red{f}", (128 * cos(radians(f)), 128 * sin(radians(f)), 22), (1.0, 0.24, 0.27), 1.2e5,
               coll, soft=10, spec=0.0)
    for n, p in enumerate(info["ports"]):
        _light("POINT", f"port{n}", (p.x, p.y, 10), (0.35, 0.86, 1.0), 2.2e4, coll, soft=6, spec=0.0)
    for n, a in enumerate((212, 148)):
        ob = _light("SPOT", f"uplight{n}", pol(84, radians(a), Z_POOL + 3), (1.0, 0.93, 0.85), 3e5, coll, size=30, blend=0.8, soft=3)
        _aim(ob, (0, 0, 150))
    sun = _light("SUN", "moon", (0, 0, 2000), (0.5, 0.6, 1.0), 0.03, coll)
    sun.rotation_euler = (radians(50), 0, radians(-120))


def _bloom(sc):
    try:
        tree_ = bpy.data.node_groups.new("comp", "CompositorNodeTree")
        sc.compositing_node_group = tree_
        rl = tree_.nodes.new("CompositorNodeRLayers")
        gl = tree_.nodes.new("CompositorNodeGlare")
        out = tree_.nodes.new("NodeGroupOutput")
        tree_.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
        if "Type" in gl.inputs:
            gl.inputs["Type"].default_value = "Bloom"
        else:
            gl.glare_type = "BLOOM"
        for key, val in (("Threshold", 0.6), ("Strength", 0.6), ("Size", 0.7)):
            if key in gl.inputs:
                gl.inputs[key].default_value = val
        tree_.links.new(rl.outputs["Image"], gl.inputs["Image"])
        tree_.links.new(gl.outputs["Image"], out.inputs[0])
        return True
    except Exception as e:  # compositor API differs between Blender versions; previews still render
        print("bloom disabled:", e)
        return False


def render_previews(sc, outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)
    sc.render.engine = "BLENDER_EEVEE"
    sc.render.resolution_x, sc.render.resolution_y = 1600, 900
    sc.render.image_settings.file_format = "PNG"
    for attr, val in (("taa_render_samples", 64), ("use_raytracing", True), ("use_shadows", True)):
        if hasattr(sc.eevee, attr):
            setattr(sc.eevee, attr, val)
    sc.view_settings.view_transform = "AgX"
    bloom = _bloom(sc)
    views = {  # name: (eye position, look-at, horizontal fov)
        "eye": ((-370, -230, 64), (0, 0, 184), 90),                 # player standing in the sunken court
        "approach": ((-1152, -40, 128), (0, 0, 200), 90),           # entering the plaza from the market street
        "wide": ((-780, -600, 430), (0, 0, 175), 50),
    }
    done = []
    for name, (loc, target, fov) in views.items():
        cd = bpy.data.cameras.new(name)
        cd.angle = radians(fov)
        cd.clip_start, cd.clip_end = 4, 20000
        ob = bpy.data.objects.new(f"cam_{name}", cd)
        sc.collection.objects.link(ob)
        ob.location = loc
        _aim(ob, target)
        sc.camera = ob
        sc.render.filepath = str(outdir / f"monument_preview_{name}.png")
        bpy.ops.render.render(write_still=True)
        done.append(sc.render.filepath)
    return done, bloom


# ----------------------------------------------------------------------------- main

def main():
    opt = _args()
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.context.preferences.filepaths.save_version = 0        # no .blend1 backups in build/
    sc = bpy.context.scene
    for n in (CABLE, CONC, NEON, LEAF):
        bpy.data.materials.new(n)
    model = bpy.data.collections.new("tree")
    phys = bpy.data.collections.new("collision")
    sc.collection.children.link(model)
    sc.collection.children.link(phys)

    flat, cab, glow, add = Mesh("planter", smooth=False), Mesh("cables"), Mesh("neon"), Mesh("leaves", smooth=False)
    planter(flat)
    info = tree(cab, glow, add)
    for p in info["ports"]:
        floor_port(flat, p)
    ref = [m.build(model) for m in (flat, cab, glow, add)]
    cols = collision(phys, info)

    out = opt["out"]
    out.mkdir(parents=True, exist_ok=True)
    res = smd_export.export_ref(out / f"{NAME}_ref.smd", ref)
    res["pieces"] = smd_export.export_phys(out / f"{NAME}_phys.smd", cols)
    smd_export.export_idle(out / f"{NAME}_idle.smd")
    pts = [ob.matrix_world @ v.co for ob in ref for v in ob.data.vertices]
    res["bbox"] = [[round(min(v[i] for v in pts), 1) for i in range(3)], [round(max(v[i] for v in pts), 1) for i in range(3)]]
    res["max_radius"] = round(max(math.hypot(v.x, v.y) for v in pts), 1)
    res["max_radius_below_220"] = round(max(math.hypot(v.x, v.y) for v in pts if v.z < 220), 1)
    res["tris_by_object"] = {ob.name: sum(len(p.vertices) - 2 for p in ob.data.polygons) for ob in ref}
    res["tips"], res["leaves"] = len(info["tips"]), info["leaves"]
    res["collision"] = [ob.name for ob in cols]
    res["walkable_high"] = walkable_report(cols)
    # light anchors for monument.place(): floor ports + the outermost tip in each 45-degree sector (env_sprites)
    sprites = []
    for k in range(8):
        sec = [(T, hot) for T, hot in info["tips"] if int((math.degrees(math.atan2(T.y, T.x)) % 360) // 45) == k]
        if sec:
            T, hot = max(sec, key=lambda t: (t[0] - CROWN_C).length)
            sprites.append({"pos": [round(c, 1) for c in T], "white": hot})
    anchors = {"ports": [[round(p.x, 1), round(p.y, 1), 0.0] for p in info["ports"]], "sprites": sprites,
               "hub": [round(c, 1) for c in info["hub"]], "top": res["bbox"][1][2]}
    (opt["qc"].parent / f"{NAME}_lights.json").write_text(json.dumps(anchors, indent=1), encoding="ascii")
    res["anchors"] = anchors

    rel = os.path.relpath(out, opt["qc"].parent).replace("\\", "/")
    opt["qc"].write_text(
        f"// Kuroda fibre tree (dys_blackice). Generated by build_tree.py; SMDs live in {rel}/\n"
        f'$modelname "blackice/{NAME}.mdl"\n'
        '$cdmaterials "models/blackice/"\n'
        "$staticprop\n"
        "$mostlyopaque\n"
        '$surfaceprop "metal"\n'
        '$contents "solid"\n'
        "$illumposition 0 0 200\n"
        f'$body tree "{rel}/{NAME}_ref.smd"\n'
        f'$sequence idle "{rel}/{NAME}_idle.smd" fps 1\n'
        f'$collisionmodel "{rel}/{NAME}_phys.smd"\n'
        "{\n\t$concave\n\t$maxconvexpieces 24\n\t$mass 20000\n}\n", encoding="ascii")

    phys.hide_render = True
    preview_materials()
    if opt["preview"]:
        preview_scene(sc, info)
        bpy.ops.wm.save_as_mainfile(filepath=str(out / f"{NAME}.blend"))
        res["previews"], res["bloom"] = render_previews(sc, opt["preview"])
    else:
        bpy.ops.wm.save_as_mainfile(filepath=str(out / f"{NAME}.blend"))
    print("MONUMENT_INFO " + json.dumps(res))


if __name__ == "__main__":
    main()
