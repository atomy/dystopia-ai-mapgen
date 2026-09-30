"""Kuroda monument: procedural Blender build -> SMDs + QC (+ .blend and preview renders).

Run:  blender --background --factory-startup --python build_monument.py -- [--out DIR] [--qc FILE] [--preview DIR]

Model space = Source units, base centre on the court floor at the origin, +X east (toward the Kuroda
tower), -X west (the players' approach). Every face is flat shaded and wound CCW seen from outside.
Design: stepped hex plinth with KURODA lettering, a tapering black hex shaft whose red neon grooves
converge up a pyramidion into the Kuroda emblem (hexagon ring + floating diamond, red/white neon),
a finial with a red beacon, and four clusters of "black ice" crystals (cyan edges) around the base.
"""
from __future__ import annotations

import json
import math
import os
import random
import sys
from math import cos, radians, sin
from pathlib import Path

import bmesh
import bpy
from mathutils import Vector

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import smd_export  # noqa: E402

GAME = Path(r"M:\SteamLibrary\steamapps\common\Dystopia\dystopia")
TEXSRC = GAME / "materialsrc" / "models" / "blackice"
NAME = "kuroda_monument"

# ----------------------------------------------------------------------------- dimensions (units)
T1, T2, PED, Z1, Z2, ZP = 144, 120, 96, 16, 32, 64         # plinth hex radii (flat faces toward +-X) / tops
COL_R, ZCOL = 78, 80                                        # collar under the shaft
PUCKS, PUCK_R = (30, 90, 150, 210, 270, 330), 86            # uplight pucks on the pedestal ledge corners
SH_R0, SH_R1, SH_Z1, SEGS = 72, 57, 240, 8                  # shaft radius bottom/top (vertex toward -X)
GROOVE_W, GROOVE_D = 2.0, 2.5                               # half width / depth of the neon grooves
ROOF_R, ROOF_Z, ROOF_SEGS = 16, 272, 2                      # pyramidion the emblem plugs into
EC, E_O, E_N1, E_N2, E_I, E_D = 326, 64, 62, 54, 52, 7      # emblem centre z, radii, half depth (x)
DIA_H, DIA_W, DIA_D = 34, 18, 12                            # diamond half height / width (y) / depth (x)
FIN_Z0, FIN_Z1, BEACON = 384, 410, 412
CLUSTERS = (30, 150, 210, 330)                              # crystal clusters at the plinth corners
CRYSTALS = (  # (azimuth offset, base radius, tilt, side tilt, radius, prism length, tip length)
    (0, 112, 11, 0, 15, 104, 24),
    (14, 112, 22, 8, 9, 56, 15),
    (-12, 114, 32, -6, 6, 36, 12),
)

# trim bands of kuroda_metal (v ranges) and kuroda_neon rows
BAND = {"A": (0.625, 1.0), "B": (0.375, 0.625), "C": (0.25, 0.375), "D": (0.125, 0.25), "E": (0.0, 0.125)}
NEON = {"red": (0.75, 1.0), "white": (0.5, 0.75), "cyan": (0.25, 0.5), "dim": (0.0, 0.25)}


def bv(band, t, pad=3 / 1024):
    """V inside a metal band; t=0 bottom row of the band, t=1 top row."""
    v0, v1 = BAND[band]
    return v0 + pad + (v1 - v0 - 2 * pad) * min(1.0, max(0.0, t))


def nv(band, t):
    v0, v1 = NEON[band]
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


class Part:
    """Polygons with per-corner UVs and a material; becomes one flat-shaded Blender object."""

    def __init__(self, name):
        self.name, self.verts, self.faces = name, [], []

    def poly(self, pts, mat, uvs, out):
        pts = [Vector(p) for p in pts]
        if _newell(pts).dot(Vector(out)) < 0:
            pts, uvs = pts[::-1], list(uvs)[::-1]
        i = len(self.verts)
        self.verts += pts
        self.faces.append((list(range(i, i + len(pts))), mat, list(uvs)))

    def build(self, coll):
        me = bpy.data.meshes.new(self.name)
        me.from_pydata([tuple(v) for v in self.verts], [], [f[0] for f in self.faces])
        names = sorted({f[1] for f in self.faces})
        for n in names:
            me.materials.append(bpy.data.materials.get(n) or bpy.data.materials.new(n))
        uv = me.uv_layers.new(name="UVMap")
        for p, (_, mat, uvs) in zip(me.polygons, self.faces):
            p.material_index = names.index(mat)
            p.use_smooth = False
            for k in range(p.loop_total):
                uv.data[p.loop_start + k].uv = uvs[k]
        ob = bpy.data.objects.new(self.name, me)
        coll.objects.link(ob)
        return ob


def ring(r, phase, z, n=6):
    return [Vector((r * cos(radians(phase + 360 / n * i)), r * sin(radians(phase + 360 / n * i)), z)) for i in range(n)]


def prism_sides(p: Part, r, phase, z0, z1, band, per_face=False, tile=128.0, cols=1):
    """Six vertical faces of a hex prism on a metal band (V = height); cols splits faces for vertex lighting."""
    lo, hi = ring(r, phase, z0), ring(r, phase, z1)
    for i in range(6):
        j = (i + 1) % 6
        u0, u1 = (0.0, 1.0) if per_face else (i * r / tile, (i + 1) * r / tile)
        mid = (lo[i] + lo[j]) / 2
        for c in range(cols):
            f0, f1 = c / cols, (c + 1) / cols
            ua, ub = u0 + (u1 - u0) * f0, u0 + (u1 - u0) * f1
            p.poly([lo[i].lerp(lo[j], f0), lo[i].lerp(lo[j], f1), hi[i].lerp(hi[j], f1), hi[i].lerp(hi[j], f0)],
                   "kuroda_metal", [(ua, bv(band, 0)), (ub, bv(band, 0)), (ub, bv(band, 1)), (ua, bv(band, 1))],
                   (mid.x, mid.y, 0))


def ring_face(p: Part, r_out, r_in, phase, z, band="D", up=True, depth_scale=32.0, tile=128.0, cols=1):
    """Horizontal hex annulus; V runs from the outer edge (band top) inward, U wraps around."""
    o, n = ring(r_out, phase, z), ring(r_in, phase, z)
    t_in = 1 - (r_out - r_in) * cos(radians(30)) / depth_scale
    k = max(1, round(3 * (r_out + r_in) / tile))
    for i in range(6):
        j = (i + 1) % 6
        for c in range(cols):
            f0, f1 = c / cols, (c + 1) / cols
            ua, ub = (i + f0) / 6 * k, (i + f1) / 6 * k
            p.poly([o[i].lerp(o[j], f0), o[i].lerp(o[j], f1), n[i].lerp(n[j], f1), n[i].lerp(n[j], f0)], "kuroda_metal",
                   [(ua, bv(band, 1)), (ub, bv(band, 1)), (ub, bv(band, t_in)), (ua, bv(band, t_in))],
                   (0, 0, 1 if up else -1))


# ----------------------------------------------------------------------------- parts

def plinth(p: Part):
    for r_out, r_in, z0, z1 in ((T1, T2 - 2, 0, Z1), (T2, PED - 2, Z1, Z2)):
        prism_sides(p, r_out, 30, z0, z1, "C", cols=3)
        ring_face(p, r_out, r_in, 30, z1, cols=3)
    prism_sides(p, PED, 30, Z2, ZP, "B", per_face=True, cols=2)  # KURODA lettering on all six faces
    ring_face(p, PED, 66, 30, ZP, cols=2)
    prism_sides(p, COL_R, 0, ZP, ZCOL, "C", cols=2)                # collar
    ring_face(p, COL_R, 66, 0, ZCOL, cols=2)
    for az in PUCKS:                                               # uplight pucks on the pedestal corners
        c = Vector((PUCK_R * cos(radians(az)), PUCK_R * sin(radians(az)), 0))
        lo = [q + c for q in ring(5, 30, ZP - 1)]
        hi = [q + c for q in ring(4, 30, ZP + 3.5)]
        for i in range(6):
            j = (i + 1) % 6
            mid = (lo[i] + lo[j]) / 2 - c
            p.poly([lo[i], lo[j], hi[j], hi[i]], "kuroda_metal",
                   [(0, bv("E", 0.2)), (0.04, bv("E", 0.2)), (0.04, bv("E", 0.8)), (0, bv("E", 0.8))], (mid.x, mid.y, 0.2))
        p.poly(hi, "kuroda_neon", [(0.5, nv("cyan", 0.5 + (q - c).y / 10)) for q in hi], (0, 0, 1))


def shaft(p: Part):
    """Chamfered hex shaft (vertex toward -X) that tapers into a pyramidion; a red neon groove runs up the
    middle of every face and converges on the emblem."""
    zs = [ZCOL + (SH_Z1 - ZCOL) * k / SEGS for k in range(SEGS + 1)]
    zs += [SH_Z1 + (ROOF_Z - SH_Z1) * k / ROOF_SEGS for k in range(1, ROOF_SEGS + 1)]

    def radius(z):
        if z <= SH_Z1:
            return SH_R0 + (SH_R1 - SH_R0) * (z - ZCOL) / (SH_Z1 - ZCOL)
        return SH_R1 + (ROOF_R - SH_R1) * (z - SH_Z1) / (ROOF_Z - SH_Z1)

    def section(z):
        r = radius(z)
        v, t = ring(r, 0, z), 0.05 * r
        return ([v[i] + (v[i - 1] - v[i]).normalized() * t for i in range(6)],
                [v[i] + (v[(i + 1) % 6] - v[i]).normalized() * t for i in range(6)])

    secs = [section(z) for z in zs]
    ta = lambda s_: bv("A", 0.5 + s_ / 80)
    E3, E7 = bv("E", 0.3), bv("E", 0.7)
    for i in range(6):
        j = (i + 1) % 6
        cvert = ring(1, 0, 0)[i]                                    # chamfer outward direction
        rows, u = [], 0.0
        for kk in range(len(zs)):
            b, a = secs[kk][1][i], secs[kk][0][j]
            h, m, w = (a - b).normalized(), (a + b) / 2, (a - b).length
            if rows:
                u += (m - rows[-1]["m"]).length / 256
            rows.append({"b": b, "a": a, "m": m, "w": w, "h": h, "u": u})
        for k in range(len(zs) - 1):
            r0, r1 = rows[k], rows[k + 1]
            quad = [r0["b"], r0["a"], r1["a"], r1["b"]]
            n = _newell(quad).normalized()
            n = n if n.dot(Vector((r0["m"].x, r0["m"].y, 0))) > 0 else -n
            for r in (r0, r1):
                r["gl"], r["gr"] = r["m"] - r["h"] * GROOVE_W, r["m"] + r["h"] * GROOVE_W
                r["glb"], r["grb"] = r["gl"] - n * GROOVE_D, r["gr"] - n * GROOVE_D
            u0, u1 = r0["u"], r1["u"]
            p.poly([r0["b"], r0["gl"], r1["gl"], r1["b"]], "kuroda_metal",
                   [(u0, ta(-r0["w"] / 2)), (u0, ta(-GROOVE_W)), (u1, ta(-GROOVE_W)), (u1, ta(-r1["w"] / 2))], n)
            p.poly([r0["gr"], r0["a"], r1["a"], r1["gr"]], "kuroda_metal",
                   [(u0, ta(GROOVE_W)), (u0, ta(r0["w"] / 2)), (u1, ta(r1["w"] / 2)), (u1, ta(GROOVE_W))], n)
            p.poly([r0["gl"], r0["glb"], r1["glb"], r1["gl"]], "kuroda_metal", [(u0, E3), (u0, E7), (u1, E7), (u1, E3)], r0["h"])
            p.poly([r0["gr"], r0["grb"], r1["grb"], r1["gr"]], "kuroda_metal", [(u0, E3), (u0, E7), (u1, E7), (u1, E3)], -r0["h"])
            p.poly([r0["glb"], r0["grb"], r1["grb"], r1["glb"]], "kuroda_neon",
                   [(u0, nv("red", 0)), (u0, nv("red", 1)), (u1, nv("red", 1)), (u1, nv("red", 0))], n)
            a0, b0, a1, b1 = secs[k][0][i], secs[k][1][i], secs[k + 1][0][i], secs[k + 1][1][i]
            p.poly([a0, b0, b1, a1], "kuroda_metal",
                   [(u0, bv("E", 0.15)), (u0, bv("E", 0.85)), (u1, bv("E", 0.85)), (u1, bv("E", 0.15))],
                   (cvert.x, cvert.y, 0.3))
    top = [q for i in range(6) for q in (secs[-1][0][i], secs[-1][1][i])]
    p.poly(top, "kuroda_metal", [(0.1 + v.x / 64, bv("E", 0.5 + v.y / 64)) for v in top], (0, 0, 1))


def emblem(p: Part):
    def P(r, k, x):
        a = radians(90 + 60 * k)
        return Vector((x, r * cos(a), EC + r * sin(a)))

    for k in range(6):
        l = (k + 1) % 6
        u0, u1 = k * 0.5, (k + 1) * 0.5
        for x in (-E_D, E_D):
            out = (1 if x > 0 else -1, 0, 0)
            p.poly([P(E_O, k, x), P(E_O, l, x), P(E_N1, l, x), P(E_N1, k, x)], "kuroda_metal",
                   [(u0, bv("E", 0.9)), (u1, bv("E", 0.9)), (u1, bv("E", 0.6)), (u0, bv("E", 0.6))], out)
            p.poly([P(E_N1, k, x), P(E_N1, l, x), P(E_N2, l, x), P(E_N2, k, x)], "kuroda_neon",
                   [(u0, nv("red", 0)), (u1, nv("red", 0)), (u1, nv("red", 1)), (u0, nv("red", 1))], out)
            p.poly([P(E_N2, k, x), P(E_N2, l, x), P(E_I, l, x), P(E_I, k, x)], "kuroda_metal",
                   [(u0, bv("E", 0.4)), (u1, bv("E", 0.4)), (u1, bv("E", 0.1)), (u0, bv("E", 0.1))], out)
        mo = (P(E_O, k, 0) + P(E_O, l, 0)) / 2 - Vector((0, 0, EC))
        p.poly([P(E_O, k, -E_D), P(E_O, l, -E_D), P(E_O, l, E_D), P(E_O, k, E_D)], "kuroda_metal",
               [(u0, bv("E", 0.1)), (u1, bv("E", 0.1)), (u1, bv("E", 0.9)), (u0, bv("E", 0.9))], mo)
        p.poly([P(E_I, k, -E_D), P(E_I, l, -E_D), P(E_I, l, E_D), P(E_I, k, E_D)], "kuroda_metal",
               [(u0, bv("E", 0.1)), (u1, bv("E", 0.1)), (u1, bv("E", 0.9)), (u0, bv("E", 0.9))], -mo)
    # the floating diamond: white-hot along the vertical ridge, red toward the side tips
    c = Vector((0, 0, EC))
    top, bot = c + Vector((0, 0, DIA_H)), c - Vector((0, 0, DIA_H))
    eq = [c + Vector((-DIA_D, 0, 0)), c + Vector((0, DIA_W, 0)), c + Vector((DIA_D, 0, 0)), c + Vector((0, -DIA_W, 0))]
    tv = [0.5, 0.0, 0.5, 1.0]
    for i in range(4):
        j = (i + 1) % 4
        for pole in (top, bot):
            p.poly([pole, eq[i], eq[j]], "kuroda_neon", [(0.5, nv("white", 0.5)), (0.5, nv("white", tv[i])), (0.5, nv("white", tv[j]))],
                   (pole + eq[i] + eq[j]) / 3 - c)
    # light rods tying the diamond to the ring (the logo's vertical line)
    for z0, z1 in ((EC + DIA_H - 4, EC + E_I + 3), (EC - E_I - 3, EC - DIA_H + 4)):
        sq = [(-1.2, -1.2), (1.2, -1.2), (1.2, 1.2), (-1.2, 1.2)]
        for i in range(4):
            a, b = sq[i], sq[(i + 1) % 4]
            p.poly([(a[0], a[1], z0), (b[0], b[1], z0), (b[0], b[1], z1), (a[0], a[1], z1)], "kuroda_neon",
                   [(0.2, nv("white", 0.5))] * 4, ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0))
    # finial spike + red beacon
    base = [Vector((-E_D, -8, FIN_Z0)), Vector((E_D, -8, FIN_Z0)), Vector((E_D, 8, FIN_Z0)), Vector((-E_D, 8, FIN_Z0))]
    apex = Vector((0, 0, FIN_Z1))
    for i in range(4):
        a, b = base[i], base[(i + 1) % 4]
        p.poly([a, b, apex], "kuroda_metal", [(0, bv("E", 0.1)), (0.12, bv("E", 0.1)), (0.06, bv("E", 0.9))],
               (a + b) / 2 - Vector((0, 0, FIN_Z0)) + Vector((0, 0, 4)))
    bc = Vector((0, 0, BEACON))
    bt, bb = bc + Vector((0, 0, 5)), bc - Vector((0, 0, 5))
    be = [bc + Vector((2.8 * cos(radians(45 + 90 * i)), 2.8 * sin(radians(45 + 90 * i)), 0)) for i in range(4)]
    for i in range(4):
        for pole in (bt, bb):
            p.poly([pole, be[i], be[(i + 1) % 4]], "kuroda_neon", [(0.5, nv("red", 0.5))] * 3, (pole + be[i] + be[(i + 1) % 4]) / 3 - bc)


def crystal(p: Part, base, axis, r, length, tip, spin):
    """Hex prism crystal with a pointed tip; kuroda_ice glows along every edge."""
    axis = axis.normalized()
    u = axis.cross(Vector((0, 0, 1)))
    u = (u if u.length > 1e-6 else Vector((1, 0, 0))).normalized()
    v = axis.cross(u)
    ang = [radians(spin + 60 * i) for i in range(6)]
    lo = [base + (u * cos(a) + v * sin(a)) * r for a in ang]
    hi = [q + axis * length for q in lo]
    apex = base + axis * (length + tip)
    ut, ua = length / 128, (length + tip) / 128
    for i in range(6):
        j = (i + 1) % 6
        out = (lo[i] + lo[j]) / 2 - base
        p.poly([lo[i], lo[j], hi[j], hi[i]], "kuroda_ice", [(0, 0.0), (0, 1.0), (ut, 1.0), (ut, 0.0)], out)
        m = (hi[i] + hi[j]) / 2
        tout = (m + apex) / 2 - (base + axis * length * 0.5)
        p.poly([hi[i], m, apex], "kuroda_ice", [(ut, 0.0), (ut, 0.5), (ua, 0.0)], tout)
        p.poly([m, hi[j], apex], "kuroda_ice", [(ut, 0.5), (ut, 1.0), (ua, 1.0)], tout)
    return lo + hi + [apex]


def crystal_axis(az, tilt, side):
    radial = Vector((cos(radians(az)), sin(radians(az)), 0))
    tang = Vector((-radial.y, radial.x, 0))
    d = radial * cos(radians(side)) + tang * sin(radians(side))
    return Vector((0, 0, cos(radians(tilt)))) + d * sin(radians(tilt))


def crystals(p: Part):
    rng = random.Random(5)
    clusters = []
    for n, az in enumerate(CLUSTERS):
        hand = 1 if n % 2 == 0 else -1
        pts = []
        for daz, r0, tilt, side, rad, ln, tip in CRYSTALS:
            a = az + daz * hand
            base = Vector((r0 * cos(radians(a)), r0 * sin(radians(a)), 4))
            pts += crystal(p, base, crystal_axis(a, tilt, side * hand), rad, ln, tip, rng.uniform(0, 60))
        clusters.append((az, pts))
    return clusters


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


def collision(coll, clusters):
    def prism(r, phase, z0, z1, r1=None):
        return ring(r, phase, z0) + ring(r if r1 is None else r1, phase, z1)

    parts = [("tier1", prism(T1, 30, 0, Z1)), ("tier2", prism(T2, 30, 0, Z2)), ("pedestal", prism(PED, 30, 0, ZP)),
             ("collar", prism(COL_R, 0, 40, ZCOL)),
             ("shaft", ring(SH_R0, 0, 76) + ring(SH_R1, 0, SH_Z1) + ring(ROOF_R, 0, ROOF_Z))]

    def P(r, k, x):
        a = radians(90 + 60 * k)
        return Vector((x, r * cos(a), EC + r * sin(a)))

    for k in range(6):                   # six ring bars, pulled 0.3u apart at the mitres
        l = (k + 1) % 6
        q = [P(E_O, k, 0), P(E_O, l, 0), P(E_I, l, 0), P(E_I, k, 0)]
        q = [q[0] + (q[1] - q[0]).normalized() * 0.3, q[1] + (q[0] - q[1]).normalized() * 0.3,
             q[2] + (q[3] - q[2]).normalized() * 0.3, q[3] + (q[2] - q[3]).normalized() * 0.3]
        parts.append((f"ring{k}", [v + Vector((x, 0, 0)) for v in q for x in (-E_D, E_D)]))
    parts.append(("diamond", [Vector((0, 0, EC + s * DIA_H)) for s in (-1, 1)] +
                  [Vector((s * DIA_D, 0, EC)) for s in (-1, 1)] + [Vector((0, s * DIA_W, EC)) for s in (-1, 1)]))
    parts.append(("finial", [Vector((x, y, FIN_Z0 - 4)) for x in (-E_D, E_D) for y in (-8, 8)] + [Vector((0, 0, BEACON + 5))]))
    for az, pts in clusters:
        # fill the narrow gap between the crystals and the pedestal corner so nothing can wedge in it
        fill = []
        for z in (Z2, ZP):
            c = Vector((PED * cos(radians(az)), PED * sin(radians(az)), z))
            for s in (-1, 1):
                nb = Vector((PED * cos(radians(az + 60 * s)), PED * sin(radians(az + 60 * s)), z))
                fill += [c * 0.98, c + (nb - c).normalized() * 18]
        parts.append((f"crystals{az}", [q for q in pts if q.z >= 0] + fill))
    return [hull_obj(f"phys_{n}", pts, coll) for n, pts in parts]


def walkable_report(objs, min_z=70):
    """Upward faces (normal z > 0.7) above min_z in the collision model: places a player could stand."""
    out = []
    for ob in objs:
        for f in ob.data.polygons:
            if f.normal.z > 0.7:
                zs = [ob.data.vertices[i].co.z for i in f.vertices]
                if max(zs) > min_z:
                    out.append((ob.name, round(min(zs)), round(max(zs)), round(f.area)))
    return out


# ----------------------------------------------------------------------------- preview scene

def _img(name, non_color=False):
    img = bpy.data.images.load(str(TEXSRC / f"{name}.tga"), check_existing=True)
    if non_color:
        img.colorspace_settings.name = "Non-Color"
    return img


def preview_materials():
    for name in ("kuroda_metal", "kuroda_ice"):
        m = bpy.data.materials[name]
        m.use_nodes = True
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
        rough.inputs["To Min"].default_value = 0.55 if name == "kuroda_metal" else 0.25
        rough.inputs["To Max"].default_value = 0.16 if name == "kuroda_metal" else 0.05
        emi = nt.nodes.new("ShaderNodeMath")
        emi.operation = "MULTIPLY"
        emi.inputs[1].default_value = 7.0
        L = nt.links.new
        L(tex.outputs["Color"], bsdf.inputs["Base Color"])
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
        bsdf.inputs["Metallic"].default_value = 0.7 if name == "kuroda_metal" else 0.2
        L(bsdf.outputs[0], out.inputs[0])
    m = bpy.data.materials["kuroda_neon"]
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    tex = nt.nodes.new("ShaderNodeTexImage")
    tex.image = _img("kuroda_neon")
    em.inputs["Strength"].default_value = 9.0
    nt.links.new(tex.outputs["Color"], em.inputs["Color"])
    nt.links.new(em.outputs[0], out.inputs[0])


def _mat(name, color, rough, emit=None, image=None, tile=1.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
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


def _light(kind, name, loc, color, power, coll, rot=None, size=None, blend=0.3):
    ld = bpy.data.lights.new(name, kind)
    ld.color = color
    ld.energy = power
    if kind == "SPOT":
        ld.spot_size = radians(size or 50)
        ld.spot_blend = blend
    ob = bpy.data.objects.new(name, ld)
    ob.location = loc
    if rot is not None:
        ob.rotation_euler = rot
    coll.objects.link(ob)
    return ob


def _aim(ob, target):
    ob.rotation_euler = (Vector(target) - ob.location).to_track_quat("-Z", "Y").to_euler()


def preview_scene(sc):
    """Rough stand-in for the plaza: sunken court, plaza deck, tower facade, lights like place() adds."""
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
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0.006, 0.008, 0.016, 1)
    bg.inputs["Strength"].default_value = 1.0
    sc.world = world
    for x in (-40, 40):
        _light("POINT", "emblem_red", (x, 0, EC), (1.0, 0.24, 0.27), 2.5e6, coll)
    for az in PUCKS:                     # same layout as monument.place(): one uplight per pedestal corner
        d = Vector((cos(radians(az)), sin(radians(az)), 0))
        ob = _light("SPOT", f"uplight{az}", d * PUCK_R + Vector((0, 0, ZP + 8)), (0.55, 0.82, 1.0), 5e5, coll, size=70)
        _aim(ob, d * 50 + Vector((0, 0, 230)))
    for az in CLUSTERS:
        _light("POINT", f"ice_glow{az}", (150 * cos(radians(az)), 150 * sin(radians(az)), 24), (0.35, 0.86, 1.0), 1.5e5, coll)
    sun = _light("SUN", "moon", (0, 0, 2000), (0.5, 0.6, 1.0), 0.03, coll)
    sun.rotation_euler = (radians(50), 0, radians(-120))


def _bloom(sc):
    try:
        tree = bpy.data.node_groups.new("comp", "CompositorNodeTree")
        sc.compositing_node_group = tree
        rl = tree.nodes.new("CompositorNodeRLayers")
        gl = tree.nodes.new("CompositorNodeGlare")
        out = tree.nodes.new("NodeGroupOutput")
        tree.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
        if "Type" in gl.inputs:
            gl.inputs["Type"].default_value = "Bloom"
        else:
            gl.glare_type = "BLOOM"
        for key, val in (("Threshold", 0.6), ("Strength", 0.6), ("Size", 0.7)):
            if key in gl.inputs:
                gl.inputs[key].default_value = val
        tree.links.new(rl.outputs["Image"], gl.inputs["Image"])
        tree.links.new(gl.outputs["Image"], out.inputs[0])
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
    for n in ("kuroda_metal", "kuroda_ice", "kuroda_neon"):
        bpy.data.materials.new(n)
    model = bpy.data.collections.new("monument")
    phys = bpy.data.collections.new("collision")
    sc.collection.children.link(model)
    sc.collection.children.link(phys)

    parts = {n: Part(n) for n in ("plinth", "shaft", "emblem", "crystals")}
    plinth(parts["plinth"])
    shaft(parts["shaft"])
    emblem(parts["emblem"])
    clusters = crystals(parts["crystals"])
    ref = [p.build(model) for p in parts.values()]
    cols = collision(phys, clusters)

    out = opt["out"]
    out.mkdir(parents=True, exist_ok=True)
    info = smd_export.export_ref(out / f"{NAME}_ref.smd", ref)
    info["pieces"] = smd_export.export_phys(out / f"{NAME}_phys.smd", cols)
    smd_export.export_idle(out / f"{NAME}_idle.smd")
    pts = [v for p in parts.values() for v in p.verts]
    info["bbox"] = [[round(min(v[i] for v in pts), 2) for i in range(3)], [round(max(v[i] for v in pts), 2) for i in range(3)]]
    info["max_radius"] = round(max(math.hypot(v.x, v.y) for v in pts), 2)
    info["walkable_high"] = walkable_report(cols)

    rel = os.path.relpath(out, opt["qc"].parent).replace("\\", "/")
    opt["qc"].write_text(
        f"// Kuroda monument (dys_blackice). Generated by build_monument.py; SMDs live in {rel}/\n"
        f'$modelname "blackice/{NAME}.mdl"\n'
        '$cdmaterials "models/blackice/"\n'
        "$staticprop\n"
        '$surfaceprop "metal"\n'
        '$contents "solid"\n'
        "$illumposition 0 0 160\n"
        f'$body monument "{rel}/{NAME}_ref.smd"\n'
        f'$sequence idle "{rel}/{NAME}_idle.smd" fps 1\n'
        f'$collisionmodel "{rel}/{NAME}_phys.smd"\n'
        "{\n\t$concave\n\t$maxconvexpieces 24\n\t$mass 20000\n}\n", encoding="ascii")

    phys.hide_render = True
    preview_materials()
    if opt["preview"]:
        preview_scene(sc)
        bpy.ops.wm.save_as_mainfile(filepath=str(out / f"{NAME}.blend"))
        info["previews"], info["bloom"] = render_previews(sc, opt["preview"])
    else:
        bpy.ops.wm.save_as_mainfile(filepath=str(out / f"{NAME}.blend"))
    print("MONUMENT_INFO " + json.dumps(info))


if __name__ == "__main__":
    main()
