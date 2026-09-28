"""Static checks on the generated VMF before compiling."""
from __future__ import annotations

import collections

import assets

SPECIAL = {"!activator", "!caller", "!self", "!player", "!picker", "!pvsplayer"}
NAME_KEYS = ("filtername", "damagefilter", "objtarget", "target", "icename", "parentname", "SourceEntityName")


POINT_OK_IN_SOLID = {"light_environment", "env_fog_controller", "sky_camera", "info_overlay", "infodecal"}


def check(m, panels=(), level=None):
    problems = []
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
