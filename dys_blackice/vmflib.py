"""Minimal, dependable VMF authoring: brushes, entities, I/O, texture axes.

Conventions
- Units are Hammer units, +x east, +y north, +z up.
- Brush planes use Hammer's winding: three points clockwise seen from outside,
  so vbsp's normal (p0-p1) x (p2-p1) points out of the brush.
- Texture axes default to Hammer's world alignment at 0.25 scale.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

NODRAW = "tools/toolsnodraw"
SKYBOX = "tools/toolsskybox"
TRIGGER = "tools/toolstrigger"
PLAYERCLIP = "tools/toolsplayerclip"
CLIP = "tools/toolsclip"
HINT = "tools/toolshint"
SKIP = "tools/toolsskip"
AREAPORTAL = "tools/toolsareaportal"
BLACK = "tools/toolsblack"
INVISIBLE = "tools/toolsinvisible"
BLOCKLIGHT = "tools/toolsblocklight"
ORIGIN = "tools/toolsorigin"


def num(v: float) -> str:
    """Format a coordinate compactly; integers stay integers."""
    if abs(v - round(v)) < 1e-6:
        return str(int(round(v)))
    return f"{v:.3f}".rstrip("0").rstrip(".")


def vsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def vmul(a, s):
    return (a[0] * s, a[1] * s, a[2] * s)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def norm(a):
    length = math.sqrt(dot(a, a))
    return (a[0] / length, a[1] / length, a[2] / length) if length > 1e-12 else (0.0, 0.0, 0.0)


# --------------------------------------------------------------------------- textures

@dataclass
class Tex:
    """How a face is textured. `align` is 'world' (Hammer default) or 'face'."""
    material: str
    scale: float = 0.25
    uscale: float | None = None
    vscale: float | None = None
    uoff: float = 0.0
    voff: float = 0.0
    rotation: float = 0.0
    align: str = "world"
    lightmap: int = 16
    # Optional explicit axes (unit vectors); overrides align when given.
    uaxis: tuple | None = None
    vaxis: tuple | None = None

    def with_(self, **kw) -> "Tex":
        d = dict(self.__dict__)
        d.update(kw)
        return Tex(**d)


def as_tex(t) -> Tex:
    return t if isinstance(t, Tex) else Tex(t)


def world_axes(n):
    """Hammer world-aligned texture axes for a face normal."""
    ax, ay, az = abs(n[0]), abs(n[1]), abs(n[2])
    if az >= ax and az >= ay:
        return (1, 0, 0), (0, -1, 0)
    if ax >= ay:
        return (0, 1, 0), (0, 0, -1)
    return (1, 0, 0), (0, 0, -1)


def face_axes(n):
    """Face-aligned axes: u horizontal along the face, v down the face's slope."""
    if abs(n[2]) > 0.999:
        return world_axes(n)
    u = norm(cross((0, 0, 1), n))  # horizontal, lies in the face
    u = (-u[0], -u[1], -u[2])
    v = norm(cross(n, u))
    # v should point "down" the face like world-aligned walls do
    if v[2] > 0:
        v = (-v[0], -v[1], -v[2])
    return u, v


# --------------------------------------------------------------------------- brushes

@dataclass(eq=False)
class Side:
    p0: tuple
    p1: tuple
    p2: tuple
    tex: Tex
    normal: tuple = (0, 0, 1)
    smoothing: int = 0
    sid: int = 0


@dataclass
class Solid:
    sides: list
    color: str = "0 180 255"

    def materials(self):
        return {s.tex.material for s in self.sides}

    def retexture(self, fn):
        """fn(side) -> Tex | None; returns self for chaining."""
        for s in self.sides:
            t = fn(s)
            if t is not None:
                s.tex = as_tex(t)
        return self

    def bbox(self):
        pts = [p for s in self.sides for p in (s.p0, s.p1, s.p2)]
        xs, ys, zs = zip(*pts)
        return (min(xs), min(ys), min(zs), max(xs), max(ys), max(zs))


FACE_DIRS = {
    "top": (0, 0, 1),
    "bottom": (0, 0, -1),
    "west": (-1, 0, 0),
    "east": (1, 0, 0),
    "north": (0, 1, 0),
    "south": (0, -1, 0),
}


def _pick(mats, key, default):
    if isinstance(mats, dict):
        for k in (key, "sides" if key not in ("top", "bottom") else None, "all"):
            if k and k in mats:
                return mats[k]
        return default
    return mats if mats is not None else default


def box(x0, y0, z0, x1, y1, z1, mats=NODRAW) -> Solid:
    """Axis-aligned box. mats: material/Tex, or dict with keys
    top/bottom/north/south/east/west/sides/all."""
    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0
    if z0 > z1:
        z0, z1 = z1, z0
    assert x1 > x0 and y1 > y0 and z1 > z0, f"degenerate box {(x0, y0, z0, x1, y1, z1)}"
    planes = {
        "top": ((x0, y1, z1), (x1, y1, z1), (x1, y0, z1)),
        "bottom": ((x0, y0, z0), (x1, y0, z0), (x1, y1, z0)),
        "west": ((x0, y1, z1), (x0, y0, z1), (x0, y0, z0)),
        "east": ((x1, y1, z0), (x1, y0, z0), (x1, y0, z1)),
        "north": ((x1, y1, z1), (x0, y1, z1), (x0, y1, z0)),
        "south": ((x1, y0, z0), (x0, y0, z0), (x0, y0, z1)),
    }
    sides = []
    for key, (a, b, c) in planes.items():
        sides.append(Side(a, b, c, as_tex(_pick(mats, key, NODRAW)), FACE_DIRS[key]))
    return Solid(sides)


def _hull_faces(points):
    """Faces of the convex hull of a small point set: list of (normal, [verts ccw from outside])."""
    pts = list({(round(p[0], 4), round(p[1], 4), round(p[2], 4)) for p in points})
    n = len(pts)
    faces = []
    seen = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                nrm = cross(vsub(pts[j], pts[i]), vsub(pts[k], pts[i]))
                if dot(nrm, nrm) < 1e-9:
                    continue
                nrm = norm(nrm)
                d = dot(nrm, pts[i])
                side = [dot(nrm, p) - d for p in pts]
                if all(s <= 1e-4 for s in side):
                    pass
                elif all(s >= -1e-4 for s in side):
                    nrm = (-nrm[0], -nrm[1], -nrm[2])
                    d = -d
                else:
                    continue
                if any(abs(dot(nrm, m) - 1) < 1e-6 and abs(dm - d) < 1e-3 for m, dm in seen):
                    continue
                seen.append((nrm, d))
                on = [p for p in pts if abs(dot(nrm, p) - d) < 1e-3]
                c = vmul((sum(p[0] for p in on), sum(p[1] for p in on), sum(p[2] for p in on)), 1 / len(on))
                ref = norm(vsub(on[0], c))
                ref2 = cross(nrm, ref)
                on.sort(key=lambda p: math.atan2(dot(vsub(p, c), ref2), dot(vsub(p, c), ref)))
                faces.append((nrm, on))
    return faces


def hull(points, mats=NODRAW, face_mat=None) -> Solid:
    """Convex brush from vertices. face_mat(normal) -> material/Tex overrides `mats`."""
    sides = []
    for nrm, verts in _hull_faces(points):
        # verts are CCW seen from outside; Hammer wants clockwise -> reverse.
        a, b, c = verts[0], verts[1], verts[2]
        # choose three well-spread vertices for precision
        if len(verts) > 3:
            b = verts[len(verts) // 3]
            c = verts[(2 * len(verts)) // 3]
        p0, p1, p2 = c, b, a
        if dot(cross(vsub(p0, p1), vsub(p2, p1)), nrm) < 0:
            p0, p2 = p2, p0
        if face_mat is not None:
            m = face_mat(nrm)
        else:
            key = max(FACE_DIRS, key=lambda k: dot(FACE_DIRS[k], nrm))
            m = _pick(mats, key, NODRAW)
        sides.append(Side(p0, p1, p2, as_tex(m), nrm))
    return Solid(sides)


def prism(poly2d, z0, z1, mats=NODRAW) -> Solid:
    """Vertical prism from a convex 2D polygon (any winding)."""
    pts = [(x, y, z0) for x, y in poly2d] + [(x, y, z1) for x, y in poly2d]
    return hull(pts, mats)


def ngon(cx, cy, r, sides, z0, z1, mats=NODRAW, rot=0.0, snap=1.0) -> Solid:
    poly = []
    for i in range(sides):
        a = math.radians(rot + 360.0 * i / sides)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        if snap:
            x, y = round(x / snap) * snap, round(y / snap) * snap
        poly.append((x, y))
    return prism(poly, z0, z1, mats)


def wedge(x0, y0, z0, x1, y1, z1, rise="+x", mats=NODRAW) -> Solid:
    """Ramp: full height on the `rise` side, zero height on the opposite side."""
    if rise == "+x":
        pts = [(x0, y0, z0), (x0, y1, z0), (x1, y0, z0), (x1, y1, z0), (x1, y0, z1), (x1, y1, z1)]
    elif rise == "-x":
        pts = [(x0, y0, z0), (x0, y1, z0), (x1, y0, z0), (x1, y1, z0), (x0, y0, z1), (x0, y1, z1)]
    elif rise == "+y":
        pts = [(x0, y0, z0), (x1, y0, z0), (x0, y1, z0), (x1, y1, z0), (x0, y1, z1), (x1, y1, z1)]
    elif rise == "-y":
        pts = [(x0, y0, z0), (x1, y0, z0), (x0, y1, z0), (x1, y1, z0), (x0, y0, z1), (x1, y0, z1)]
    else:
        raise ValueError(rise)
    return hull(pts, mats)


# --------------------------------------------------------------------------- entities

@dataclass
class Entity:
    classname: str
    kv: dict = field(default_factory=dict)
    solids: list = field(default_factory=list)
    outputs: list = field(default_factory=list)

    def out(self, output, target, inp, param="", delay=0.0, times=-1):
        self.outputs.append((output, target, inp, param, delay, times))
        return self

    @property
    def name(self):
        return self.kv.get("targetname")


class VMF:
    def __init__(self, **world_kv):
        self.world_kv = {"classname": "worldspawn", "mapversion": "1", **world_kv}
        self.world: list[Solid] = []
        self.entities: list[Entity] = []
        self._id = 0

    # -- building
    def add(self, *solids):
        for s in solids:
            if isinstance(s, (list, tuple)):
                self.add(*s)
            elif s is not None:
                self.world.append(s)
        return solids

    def ent(self, classname, origin=None, **kv) -> Entity:
        d = {}
        for k, v in kv.items():
            if v is None:
                continue
            d[k] = v
        if origin is not None:
            d["origin"] = origin if isinstance(origin, str) else " ".join(num(c) for c in origin)
        e = Entity(classname, d)
        self.entities.append(e)
        return e

    def brush_ent(self, classname, solids, **kv) -> Entity:
        solids = list(solids) if isinstance(solids, (list, tuple)) else [solids]
        if "origin" not in kv and classname != "func_detail":
            # Hammer always stores the bounds centre; game code measures ranges from it
            bbs = [s.bbox() for s in solids]
            kv["origin"] = ((min(b[0] for b in bbs) + max(b[3] for b in bbs)) / 2,
                            (min(b[1] for b in bbs) + max(b[4] for b in bbs)) / 2,
                            (min(b[2] for b in bbs) + max(b[5] for b in bbs)) / 2)
        e = self.ent(classname, **kv)
        e.solids = solids
        return e

    def detail(self, *solids) -> Entity | None:
        flat = []
        for s in solids:
            if isinstance(s, (list, tuple)):
                flat.extend(x for x in s if x is not None)
            elif s is not None:
                flat.append(s)
        if not flat:
            return None
        return self.brush_ent("func_detail", flat)

    # -- serialisation
    def _nid(self):
        self._id += 1
        return self._id

    def _kv_value(self, v):
        if isinstance(v, float):
            return num(v)
        if isinstance(v, (tuple, list)):
            return " ".join(num(c) if isinstance(c, (int, float)) else str(c) for c in v)
        return str(v)

    def _write_solid(self, out, s: Solid, indent):
        i1 = "\t" * indent
        i2 = "\t" * (indent + 1)
        i3 = "\t" * (indent + 2)
        out.append(f"{i1}solid\n{i1}{{\n{i2}\"id\" \"{self._nid()}\"\n")
        for side in s.sides:
            t = side.tex
            n = norm(cross(vsub(side.p0, side.p1), vsub(side.p2, side.p1)))
            if t.uaxis is not None and t.vaxis is not None:
                u, v = t.uaxis, t.vaxis
            elif t.align == "face":
                u, v = face_axes(n)
            else:
                u, v = world_axes(n)
            if t.rotation:
                a = math.radians(t.rotation)
                ca, sa = math.cos(a), math.sin(a)
                u, v = (vadd(vmul(u, ca), vmul(v, sa)), vadd(vmul(v, ca), vmul(u, -sa)))
            us = t.uscale if t.uscale is not None else t.scale
            vs = t.vscale if t.vscale is not None else t.scale
            plane = " ".join(f"({num(p[0])} {num(p[1])} {num(p[2])})" for p in (side.p0, side.p1, side.p2))
            out.append(
                f"{i2}side\n{i2}{{\n"
                f"{i3}\"id\" \"{self._nid()}\"\n"
                f"{i3}\"plane\" \"{plane}\"\n"
                f"{i3}\"material\" \"{t.material}\"\n"
                f"{i3}\"uaxis\" \"[{num(u[0])} {num(u[1])} {num(u[2])} {num(t.uoff)}] {num(us)}\"\n"
                f"{i3}\"vaxis\" \"[{num(v[0])} {num(v[1])} {num(v[2])} {num(t.voff)}] {num(vs)}\"\n"
                f"{i3}\"rotation\" \"{num(t.rotation)}\"\n"
                f"{i3}\"lightmapscale\" \"{t.lightmap}\"\n"
                f"{i3}\"smoothing_groups\" \"{side.smoothing}\"\n"
                f"{i2}}}\n"
            )
        out.append(f"{i2}editor\n{i2}{{\n{i3}\"color\" \"{s.color}\"\n{i3}\"visgroupshown\" \"1\"\n{i3}\"visgroupautoshown\" \"1\"\n{i2}}}\n")
        out.append(f"{i1}}}\n")

    def _assign_side_ids(self):
        n = 1_000_000
        for s in self.world:
            for side in s.sides:
                n += 1
                side.sid = n
        for e in self.entities:
            for s in e.solids:
                for side in s.sides:
                    n += 1
                    side.sid = n

    def find_sides(self, point, normal, tol=0.5, solids=None):
        """World (or given) brush sides lying in the plane through `point` with outward
        `normal` whose brush bounds contain the point."""
        out = []
        pool = solids if solids is not None else self.world
        for s in pool:
            bb = s.bbox()
            if not (bb[0] - tol <= point[0] <= bb[3] + tol and bb[1] - tol <= point[1] <= bb[4] + tol
                    and bb[2] - tol <= point[2] <= bb[5] + tol):
                continue
            for side in s.sides:
                n = norm(cross(vsub(side.p0, side.p1), vsub(side.p2, side.p1)))
                if dot(n, normal) > 0.999 and abs(dot(n, vsub(point, side.p1))) < tol:
                    out.append(side)
        return out

    def overlay(self, material, origin, normal, u, width, height, sides, render_order=0, name=None):
        """info_overlay centred on origin; u = in-plane horizontal axis."""
        v = norm(cross(normal, u))
        e = self.ent("info_overlay", origin, material=material, BasisOrigin=" ".join(num(c) for c in origin),
                     BasisNormal=" ".join(num(c) for c in normal), BasisU=" ".join(num(c) for c in u),
                     BasisV=" ".join(num(c) for c in v), StartU="0", EndU="1", StartV="0", EndV="1",
                     uv0=f"{num(-width / 2)} {num(-height / 2)} 0", uv1=f"{num(-width / 2)} {num(height / 2)} 0",
                     uv2=f"{num(width / 2)} {num(height / 2)} 0", uv3=f"{num(width / 2)} {num(-height / 2)} 0",
                     RenderOrder=str(render_order), fademindist="-1", targetname=name)
        e.overlay_sides = list(sides)
        return e

    def text(self) -> str:
        self._id = 0
        self._assign_side_ids()
        out = [
            "versioninfo\n{\n\t\"editorversion\" \"400\"\n\t\"editorbuild\" \"8864\"\n\t\"mapversion\" \"1\"\n"
            "\t\"formatversion\" \"100\"\n\t\"prefab\" \"0\"\n}\n",
            "visgroups\n{\n}\n",
            "viewsettings\n{\n\t\"bSnapToGrid\" \"1\"\n\t\"bShowGrid\" \"1\"\n\t\"bShowLogicalGrid\" \"0\"\n"
            "\t\"nGridSpacing\" \"16\"\n\t\"bShow3DGrid\" \"0\"\n}\n",
        ]
        out.append("world\n{\n")
        out.append(f"\t\"id\" \"{self._nid()}\"\n")
        for k, v in self.world_kv.items():
            out.append(f"\t\"{k}\" \"{self._kv_value(v)}\"\n")
        for s in self.world:
            self._write_solid(out, s, 1)
        out.append("}\n")
        for e in self.entities:
            out.append("entity\n{\n")
            out.append(f"\t\"id\" \"{self._nid()}\"\n")
            out.append(f"\t\"classname\" \"{e.classname}\"\n")
            for k, v in e.kv.items():
                out.append(f"\t\"{k}\" \"{self._kv_value(v)}\"\n")
            if e.outputs:
                out.append("\tconnections\n\t{\n")
                for (o, tgt, inp, param, delay, times) in e.outputs:
                    out.append(f"\t\t\"{o}\" \"{tgt},{inp},{param},{num(delay)},{times}\"\n")
                out.append("\t}\n")
            for s in e.solids:
                self._write_solid(out, s, 1)
            out.append("}\n")
        out.append("cameras\n{\n\t\"activecamera\" \"-1\"\n}\n")
        out.append("cordon\n{\n\t\"mins\" \"(-1024 -1024 -1024)\"\n\t\"maxs\" \"(1024 1024 1024)\"\n\t\"active\" \"0\"\n}\n")
        return "".join(out)
