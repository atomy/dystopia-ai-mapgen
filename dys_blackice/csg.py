"""Box-CSG shell builder.

A level is an ordered list of operations. Each op paints an axis-aligned box as
SOLID or AIR with a style; later ops overwrite earlier ones (like painting).

build() turns the painted volume into world brushes:
  * every solid op becomes its box minus all later ops (fragments),
  * fragments that touch no air are dropped (they are invisible and seal nothing),
  * each fragment face is partitioned by what lies just outside it, fragments are
    split where that changes, and each face is textured by resolver(solid, air, dir),
  * faces against solid or void become nodraw.
Because every visible surface is a face of a solid that borders air, and air only
exists where painted, the shell is sealed as long as the painted air is enclosed.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from vmflib import Solid, Side, Tex, as_tex, NODRAW

DIRS = ("east", "west", "north", "south", "top", "bottom")
AXIS = {"east": 0, "west": 0, "north": 1, "south": 1, "top": 2, "bottom": 2}
SIGN = {"east": 1, "west": -1, "north": 1, "south": -1, "top": 1, "bottom": -1}


@dataclass(frozen=True)
class Box:
    x0: int
    y0: int
    z0: int
    x1: int
    y1: int
    z1: int

    @staticmethod
    def of(x0, y0, z0, x1, y1, z1):
        return Box(min(x0, x1), min(y0, y1), min(z0, z1), max(x0, x1), max(y0, y1), max(z0, z1))

    def lo(self, a):
        return (self.x0, self.y0, self.z0)[a]

    def hi(self, a):
        return (self.x1, self.y1, self.z1)[a]

    def valid(self):
        return self.x1 > self.x0 and self.y1 > self.y0 and self.z1 > self.z0

    def intersects(self, o: "Box"):
        return self.x0 < o.x1 and o.x0 < self.x1 and self.y0 < o.y1 and o.y0 < self.y1 and self.z0 < o.z1 and o.z0 < self.z1

    def inter(self, o: "Box"):
        b = Box(max(self.x0, o.x0), max(self.y0, o.y0), max(self.z0, o.z0), min(self.x1, o.x1), min(self.y1, o.y1), min(self.z1, o.z1))
        return b if b.valid() else None

    def contains(self, o: "Box"):
        return self.x0 <= o.x0 and self.y0 <= o.y0 and self.z0 <= o.z0 and self.x1 >= o.x1 and self.y1 >= o.y1 and self.z1 >= o.z1

    def subtract(self, o: "Box"):
        if not self.intersects(o):
            return [self]
        out = []
        x0, y0, z0, x1, y1, z1 = self.x0, self.y0, self.z0, self.x1, self.y1, self.z1
        if o.x0 > x0:
            out.append(Box(x0, y0, z0, o.x0, y1, z1)); x0 = o.x0
        if o.x1 < x1:
            out.append(Box(o.x1, y0, z0, x1, y1, z1)); x1 = o.x1
        if o.y0 > y0:
            out.append(Box(x0, y0, z0, x1, o.y0, z1)); y0 = o.y0
        if o.y1 < y1:
            out.append(Box(x0, o.y1, z0, x1, y1, z1)); y1 = o.y1
        if o.z0 > z0:
            out.append(Box(x0, y0, z0, x1, y1, o.z0)); z0 = o.z0
        if o.z1 < z1:
            out.append(Box(x0, y0, o.z1, x1, y1, z1)); z1 = o.z1
        return out

    def split(self, axis, c):
        if not (self.lo(axis) < c < self.hi(axis)):
            return [self]
        a = list((self.x0, self.y0, self.z0, self.x1, self.y1, self.z1))
        b = list(a)
        a[3 + axis] = c
        b[axis] = c
        return [Box(*a), Box(*b)]

    def face_slab(self, d, eps=1):
        """Thin box just outside face d."""
        a = AXIS[d]
        lo = list((self.x0, self.y0, self.z0))
        hi = list((self.x1, self.y1, self.z1))
        if SIGN[d] > 0:
            lo[a], hi[a] = hi[a], hi[a] + eps
        else:
            lo[a], hi[a] = lo[a] - eps, lo[a]
        return Box(*lo, *hi)


@dataclass
class Op:
    idx: int
    kind: str  # 'solid' | 'air'
    box: Box
    style: str
    tags: dict = field(default_factory=dict)


@dataclass
class Face:
    """A visible face of a shell brush."""
    box: Box          # the brush box
    d: str            # direction the face points
    solid: Op
    air: Op | None    # what it looks onto (None = void, or solid op)
    other: Op | None

    def rect(self):
        """(axis, plane coord, (u0, v0, u1, v1) in the other two axes)."""
        a = AXIS[self.d]
        c = self.box.hi(a) if SIGN[self.d] > 0 else self.box.lo(a)
        ax = [i for i in range(3) if i != a]
        return a, c, (self.box.lo(ax[0]), self.box.lo(ax[1]), self.box.hi(ax[0]), self.box.hi(ax[1]))


class Level:
    def __init__(self, cell=512):
        self.ops: list[Op] = []
        self.cell = cell
        self._grid: dict = {}

    # ---- painting
    def _add(self, kind, box, style, tags):
        op = Op(len(self.ops), kind, box, style, tags)
        assert box.valid(), f"invalid box {box}"
        self.ops.append(op)
        c = self.cell
        for gx in range(box.x0 // c, (box.x1 - 1) // c + 1):
            for gy in range(box.y0 // c, (box.y1 - 1) // c + 1):
                for gz in range(box.z0 // c, (box.z1 - 1) // c + 1):
                    self._grid.setdefault((gx, gy, gz), []).append(op)
        return op

    def solid(self, x0, y0, z0, x1, y1, z1, style, **tags):
        return self._add("solid", Box.of(x0, y0, z0, x1, y1, z1), style, tags)

    def air(self, x0, y0, z0, x1, y1, z1, style, **tags):
        return self._add("air", Box.of(x0, y0, z0, x1, y1, z1), style, tags)

    def query(self, box: Box):
        """Ops intersecting box, in paint order."""
        c = self.cell
        seen = {}
        for gx in range(box.x0 // c, (box.x1 - 1) // c + 1):
            for gy in range(box.y0 // c, (box.y1 - 1) // c + 1):
                for gz in range(box.z0 // c, (box.z1 - 1) // c + 1):
                    for op in self._grid.get((gx, gy, gz), ()):
                        if op.idx not in seen and op.box.intersects(box):
                            seen[op.idx] = op
        return [seen[k] for k in sorted(seen)]

    def label_at(self, x, y, z):
        pt = Box(x, y, z, x + 1, y + 1, z + 1)
        ops = self.query(pt)
        return ops[-1] if ops else None

    # ---- face partition
    @staticmethod
    def _paint2d(pieces, rect, label):
        u0, v0, u1, v1 = rect
        out = []
        for (a0, b0, a1, b1), lab in pieces:
            if a0 >= u1 or u0 >= a1 or b0 >= v1 or v0 >= b1:
                out.append(((a0, b0, a1, b1), lab))
                continue
            if a0 < u0:
                out.append(((a0, b0, u0, b1), lab)); a0 = u0
            if u1 < a1:
                out.append(((u1, b0, a1, b1), lab)); a1 = u1
            if b0 < v0:
                out.append(((a0, b0, a1, v0), lab)); b0 = v0
            if v1 < b1:
                out.append(((a0, v1, a1, b1), lab)); b1 = v1
        out.append((rect, label))
        return out

    def face_partition(self, box: Box, d: str):
        """Partition face d of box into rects labelled by the op just outside."""
        slab = box.face_slab(d)
        a = AXIS[d]
        ax = [i for i in range(3) if i != a]
        full = (box.lo(ax[0]), box.lo(ax[1]), box.hi(ax[0]), box.hi(ax[1]))
        pieces = [(full, None)]
        for op in self.query(slab):
            r = (max(full[0], op.box.lo(ax[0])), max(full[1], op.box.lo(ax[1])),
                 min(full[2], op.box.hi(ax[0])), min(full[3], op.box.hi(ax[1])))
            if r[2] > r[0] and r[3] > r[1]:
                pieces = self._paint2d(pieces, r, op)
        return ax, pieces

    def air_fragments(self, op: Op):
        pieces = [op.box]
        for later in self.query(op.box):
            if later.idx <= op.idx:
                continue
            nxt = []
            for p in pieces:
                nxt.extend(p.subtract(later.box))
            pieces = nxt
        return pieces

    def check_leaks(self):
        """Air that touches the void (nothing painted) leaks. Returns [(op, d, rect)]."""
        leaks = []
        for op in self.ops:
            if op.kind != "air":
                continue
            for frag in self.air_fragments(op):
                for d in DIRS:
                    ax, pieces = self.face_partition(frag, d)
                    for rect, lab in pieces:
                        if lab is None:
                            leaks.append((op, d, rect))
        return leaks

    # ---- build
    def fragments(self):
        """Solid fragments: (Box, Op) with later ops removed."""
        frags = []
        for op in self.ops:
            if op.kind != "solid":
                continue
            pieces = [op.box]
            for later in self.query(op.box):
                if later.idx <= op.idx:
                    continue
                nxt = []
                for p in pieces:
                    nxt.extend(p.subtract(later.box))
                pieces = nxt
                if not pieces:
                    break
            pieces = self._merge(pieces)
            frags.extend((p, op) for p in pieces)
        return frags

    @staticmethod
    def _merge(boxes):
        """Greedy merge of boxes that share a full face."""
        boxes = list(boxes)
        changed = True
        while changed and len(boxes) > 1:
            changed = False
            for i in range(len(boxes)):
                bi = boxes[i]
                for j in range(i + 1, len(boxes)):
                    bj = boxes[j]
                    m = None
                    if (bi.y0, bi.y1, bi.z0, bi.z1) == (bj.y0, bj.y1, bj.z0, bj.z1) and (bi.x1 == bj.x0 or bj.x1 == bi.x0):
                        m = Box(min(bi.x0, bj.x0), bi.y0, bi.z0, max(bi.x1, bj.x1), bi.y1, bi.z1)
                    elif (bi.x0, bi.x1, bi.z0, bi.z1) == (bj.x0, bj.x1, bj.z0, bj.z1) and (bi.y1 == bj.y0 or bj.y1 == bi.y0):
                        m = Box(bi.x0, min(bi.y0, bj.y0), bi.z0, bi.x1, max(bi.y1, bj.y1), bi.z1)
                    elif (bi.x0, bi.x1, bi.y0, bi.y1) == (bj.x0, bj.x1, bj.y0, bj.y1) and (bi.z1 == bj.z0 or bj.z1 == bi.z0):
                        m = Box(bi.x0, bi.y0, min(bi.z0, bj.z0), bi.x1, bi.y1, max(bi.z1, bj.z1))
                    if m is not None:
                        boxes[i] = m
                        boxes.pop(j)
                        changed = True
                        break
                if changed:
                    break
        return boxes

    @staticmethod
    def _zsplit(pieces, ax, cuts_for):
        """Split vertical-face pieces at z cut levels supplied per label."""
        if ax[1] != 2:
            return pieces
        out = []
        for rect, lab in pieces:
            cuts = sorted(c for c in cuts_for(lab) if rect[1] < c < rect[3]) if lab is not None else []
            lo = rect[1]
            for c in cuts:
                out.append(((rect[0], lo, rect[2], c), lab))
                lo = c
            out.append(((rect[0], lo, rect[2], rect[3]), lab))
        return out

    def build(self, resolver, lightmap=None, zcuts=None):
        """resolver(solid_op, air_op, d, box, zr) -> material/Tex or None (nodraw).
        zr is the (z0, z1) span of the face piece. zcuts(op) -> z levels at which
        vertical faces bordering / belonging to that op are split (texture bands).
        Returns (list[Solid], list[Face])."""
        out_solids, faces = [], []
        work = self.fragments()
        guard = 0
        cuts_for = (lambda lab: list(zcuts(lab)) + list(zcuts(op_now[0]))) if zcuts else (lambda lab: [])
        op_now = [None]
        while work:
            guard += 1
            assert guard < 2_000_000, "csg split runaway"
            box, op = work.pop()
            op_now[0] = op
            touches_air = False
            split_done = False
            face_info = {}
            for d in DIRS:
                ax, pieces = self.face_partition(box, d)
                if zcuts and d not in ("top", "bottom"):
                    pieces = self._zsplit(pieces, ax, cuts_for)
                keyed = []
                for rect, lab in pieces:
                    air = lab if (lab is not None and lab.kind == "air") else None
                    if air is not None:
                        touches_air = True
                    zr = (rect[1], rect[3]) if d not in ("top", "bottom") else (box.z0, box.z1)
                    mat = resolver(op, air, d, box, zr) if air is not None else None
                    key = (mat.material, mat.uoff, mat.voff, mat.scale, mat.rotation, mat.lightmap) if isinstance(mat, Tex) else mat
                    keyed.append((rect, lab, air, mat, key))
                keys = {k[4] for k in keyed}
                if len(keys) > 1:
                    # split the box along the first boundary where the outcome changes
                    cut = None
                    for rect, lab, air, mat, key in keyed:
                        for i, axis in enumerate(ax):
                            for c in (rect[i], rect[i + 2]):
                                if box.lo(axis) < c < box.hi(axis):
                                    cut = (axis, c)
                                    break
                            if cut:
                                break
                        if cut:
                            break
                    if cut:
                        work.extend((b, op) for b in box.split(*cut))
                        split_done = True
                        break
                face_info[d] = keyed[0] if keyed else (None, None, None, None, None)
            if split_done:
                continue
            if not touches_air:
                continue
            sides = []
            from vmflib import box as mkbox
            mats = {}
            for d in DIRS:
                rect, lab, air, mat, key = face_info[d]
                if mat is None:
                    mats[d] = NODRAW
                else:
                    mats[d] = mat
                    faces.append(Face(box, d, op, air, lab))
            s = mkbox(box.x0, box.y0, box.z0, box.x1, box.y1, box.z1, mats)
            if lightmap:
                for side in s.sides:
                    if side.tex.material != NODRAW:
                        lm = lightmap(op, side)
                        if lm:
                            side.tex = side.tex.with_(lightmap=lm)
            s.color = op.tags.get("color", "0 180 255")
            out_solids.append(s)
        return out_solids, faces
