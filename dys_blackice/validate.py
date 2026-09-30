"""Static checks on the generated VMF before compiling."""
from __future__ import annotations

import collections

import assets

SPECIAL = {"!activator", "!caller", "!self", "!player", "!picker", "!pvsplayer"}
NAME_KEYS = ("filtername", "damagefilter", "objtarget", "target", "icename", "parentname", "SourceEntityName")


POINT_OK_IN_SOLID = {"light_environment", "env_fog_controller", "sky_camera", "info_overlay", "infodecal"}
PROPS = ("prop_static", "prop_dynamic", "prop_dynamic_override", "prop_physics_multiplayer")
NOT_GEOMETRY = ("trigger_", "dys_forcefield", "cyber_ice", "dys_jackpoint", "func_areaportal")


def _geometry(m):
    """Bounding boxes of everything a prop can visibly rest on besides the CSG shell."""
    def visible(s):
        return any(not side.tex.material.lower().startswith("tools/") for side in s.sides)
    boxes = [s.bbox() for s in m.world if visible(s)]
    for e in m.entities:
        if e.solids and not e.classname.startswith(NOT_GEOMETRY):
            boxes += [s.bbox() for s in e.solids if visible(s)]
    return boxes


def _prop_box(e):
    import math
    info = assets.mdl_info(e.kv["model"])
    if not info:
        return None
    x, y, z = (float(c) for c in str(e.kv["origin"]).split())
    yaw = math.radians(float(str(e.kv.get("angles", "0 0 0")).split()[1]))
    (x0, y0, z0), (x1, y1, z1) = info["hull_min"], info["hull_max"]
    c, s = math.cos(yaw), math.sin(yaw)
    xs = [x + px * c - py * s for px in (x0, x1) for py in (y0, y1)]
    ys = [y + px * s + py * c for px in (x0, x1) for py in (y0, y1)]
    return min(xs), min(ys), z + z0, max(xs), max(ys), z + z1


class _Grid:
    """Coarse spatial hash over boxes for point-in-box queries."""

    def __init__(self, boxes, cell=256):
        self.cell, self.cells = cell, {}
        for i, b in enumerate(boxes):
            for gx in range(int(b[0] // cell), int(b[3] // cell) + 1):
                for gy in range(int(b[1] // cell), int(b[4] // cell) + 1):
                    self.cells.setdefault((gx, gy), []).append(b)

    def hit(self, p, skip=None):
        for b in self.cells.get((int(p[0] // self.cell), int(p[1] // self.cell)), ()):
            if b is not skip and b[0] <= p[0] <= b[3] and b[1] <= p[1] <= b[4] and b[2] <= p[2] <= b[5]:
                return True
        return False


def _face_samples(bb, tol):
    """3x3 sample points just outside each of the six faces of a box."""
    x0, y0, z0, x1, y1, z1 = bb
    xs, ys, zs = (x0, (x0 + x1) / 2, x1), (y0, (y0 + y1) / 2, y1), (z0, (z0 + z1) / 2, z1)
    return [[(x0 - tol, y, z) for y in ys for z in zs], [(x1 + tol, y, z) for y in ys for z in zs],
            [(x, y0 - tol, z) for x in xs for z in zs], [(x, y1 + tol, z) for x in xs for z in zs],
            [(x, y, z0 - tol) for x in xs for y in ys], [(x, y, z1 + tol) for x in xs for y in ys]]


DETAIL = ("func_detail", "func_illusionary", "func_brush", "func_breakable", "func_door", "cyber_floor")
FLOAT_OK = ("vaccinert/dys_", "termitex/icon_", "cyspfinal/circlet")    # cyberspace holograms float on purpose


def _touch(a, b, tol):
    return all(a[i] - tol <= b[i + 3] and b[i] - tol <= a[i + 3] for i in range(3))


def _floating_clusters(m, level, props, tol=2):
    """Detail brushes are grouped into clusters of touching pieces (a balcony and its railing are one); every
    cluster must touch the CSG shell, a world brush or a prop somewhere. Floating clusters are reported."""
    def visible(s):
        return any(not sd.tex.material.lower().startswith("tools/") for sd in s.sides)
    items = []                        # (bbox, entity, solid)
    for e in m.entities:
        if e.classname in DETAIL:
            items += [(s.bbox(), e, s) for s in e.solids if visible(s)]
    world = _Grid([s.bbox() for s in m.world if visible(s)])
    grid, cell = {}, 256
    for i, (b, e, s) in enumerate(items):
        for gx in range(int((b[0] - tol) // cell), int((b[3] + tol) // cell) + 1):
            for gy in range(int((b[1] - tol) // cell), int((b[4] + tol) // cell) + 1):
                grid.setdefault((gx, gy), []).append(i)
    parent = list(range(len(items)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for cell_items in grid.values():
        for a in range(len(cell_items)):
            for b in range(a + 1, len(cell_items)):
                i, j = cell_items[a], cell_items[b]
                if find(i) != find(j) and _touch(items[i][0], items[j][0], tol):
                    parent[find(i)] = find(j)

    def anchored(b):
        for face in _face_samples(b, tol):
            for p in face:
                lab = level.label_at(int(p[0]), int(p[1]), int(p[2]))
                if (lab is not None and lab.kind == "solid") or world.hit(p) or props.hit(p):
                    return True
        return False
    groups = {}
    for i in range(len(items)):
        groups.setdefault(find(i), []).append(i)
    problems = []
    for idx in groups.values():
        boxes = [items[i][0] for i in idx]
        if any(anchored(b) for b in boxes):
            continue
        mats = sorted({sd.tex.material for i in idx for sd in items[i][2].sides
                       if not sd.tex.material.lower().startswith("tools/")})
        if min(b[1] for b in boxes) < -6000 or any(mt.lower().startswith(FLOAT_OK) for mt in mats):
            continue                  # 3D skybox, cyberspace holograms
        c = [(min(b[k] for b in boxes) + max(b[k + 3] for b in boxes)) / 2 for k in range(3)]
        problems.append(f"floating {items[idx[0]][1].classname} x{len(idx)} ({', '.join(mats[:3])}) "
                        f"at ({c[0]:.0f} {c[1]:.0f} {c[2]:.0f})")
    return problems


def floating(m, level, tol=6, glow_reach=24):
    """Props not mounted on anything (no face mostly backed by geometry or another prop), thin sign panels
    with nothing behind them, and glow sprites with nothing near them."""
    geo = _Grid(_geometry(m))
    pboxes = [(e, _prop_box(e)) for e in m.entities if e.classname in PROPS]
    pboxes = [(e, bb) for e, bb in pboxes if bb is not None]
    props = _Grid([bb for e, bb in pboxes])

    def solid(p, skip=None):
        lab = level.label_at(int(p[0]), int(p[1]), int(p[2]))
        if lab is not None and lab.kind == "solid":
            return True
        return geo.hit(p) or props.hit(p, skip)

    problems = []
    for e, bb in pboxes:
        faces = _face_samples(bb, tol)
        if max(sum(solid(p, bb) for p in face) for face in faces) < 5 and not solid(faces[4][4], bb):
            problems.append(f"floating prop {e.kv['model']} at ({e.kv['origin']})")
    problems += _floating_clusters(m, level, props)
    for e in m.entities:
        if e.classname != "env_sprite":
            continue
        x, y, z = (float(c) for c in str(e.kv["origin"]).split())
        near_geo = any(solid((x + dx * r, y + dy * r, z + dz * r)) for r in (8, 16, glow_reach)
                       for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)))
        near_prop = any(b[0] - glow_reach <= x <= b[3] + glow_reach and b[1] - glow_reach <= y <= b[4] + glow_reach
                        and b[2] - glow_reach <= z <= b[5] + glow_reach for e2, b in pboxes)
        if not (near_geo or near_prop):
            problems.append(f"glow sprite in mid-air at ({e.kv['origin']})")
    return problems


def check(m, panels=(), level=None):
    problems = []
    if level is not None:
        problems += floating(m, level)
    # every point entity must sit in painted air (vbsp floods from entities: void origins leak)
    if level is not None:
        for e in m.entities:
            if e.solids or e.classname in POINT_OK_IN_SOLID or "origin" not in e.kv:
                continue
            try:
                x, y, z = (float(c) for c in str(e.kv["origin"]).split())
            except ValueError:
                continue
            lab = level.label_at(int(x), int(y), int(z + 1))
            if lab is None or lab.kind != "air":
                where = "void" if lab is None else f"solid '{lab.style}'"
                problems.append(f"{e.classname} '{e.name or ''}' at ({x:.0f} {y:.0f} {z:.0f}) is in {where}")
    names = collections.Counter(e.kv.get("targetname") for e in m.entities if e.kv.get("targetname"))
    # I/O targets
    for e in m.entities:
        for (o, tgt, inp, param, delay, times) in e.outputs:
            if tgt not in names and tgt not in SPECIAL:
                problems.append(f"{e.classname} '{e.name}' {o} -> missing target '{tgt}'")
        for k in NAME_KEYS:
            v = e.kv.get(k)
            if v and v not in names and not (e.classname == "prop_static") and not (k == "filtername" and e.classname == "filter_activator_name"):
                problems.append(f"{e.classname} '{e.name}' {k}='{v}' not found")
        if e.classname in ("prop_static", "prop_dynamic", "prop_physics_multiplayer", "prop_dynamic_override") \
                and not assets.model_exists(e.kv["model"]):
            problems.append(f"missing model {e.kv['model']}")
    # materials
    mats = collections.Counter()
    for s in m.world:
        for side in s.sides:
            mats[side.tex.material] += 1
    for e in m.entities:
        for s in e.solids:
            for side in s.sides:
                mats[side.tex.material] += 1
    for mat in mats:
        if not assets.material_exists(mat):
            problems.append(f"missing material {mat} (x{mats[mat]})")
        if mat.lower().startswith("dev/"):
            problems.append(f"dev texture in use: {mat}")
    # translucent materials never seal: forbid them on world brushes
    for s in m.world:
        for side in s.sides:
            if side.tex.material.lower().startswith("tools/"):
                continue
            kv = assets.vmt(side.tex.material) or {}
            if any(kv.get(k) in ("1", 1) for k in ("$translucent", "$additive", "$alphatest")):
                problems.append(f"translucent material on world brush: {side.tex.material}")
                break
    # panels
    pn = {p["name"] for p in panels}
    for e in m.entities:
        if e.classname in ("dys_screen", "dys_cyberscreen") and e.kv.get("panelname") not in pn:
            problems.append(f"{e.classname} '{e.name}' uses unregistered panel {e.kv.get('panelname')}")
    for p in panels:
        for label, cmd in p["buttons"]:
            pass
    # spawns
    ids = {e.kv.get("spawnid") for e in m.entities if e.classname == "dys_spawn"}
    for e in m.entities:
        if e.classname == "dys_spawn_point" and e.kv.get("spawnid") not in ids:
            problems.append(f"spawn point with orphan spawnid {e.kv.get('spawnid')}")
    return problems
