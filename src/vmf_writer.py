"""
Deterministic VMF writer: monotonic ID allocation, required top-level sections.
Emits only known-good convex brushes (via add_brush). Do not generate arbitrary planes here.
"""

from __future__ import annotations

from typing import Any


def _plane_string(p1: tuple[float, float, float], p2: tuple[float, float, float], p3: tuple[float, float, float]) -> str:
    def fmt(v: float) -> str:
        return str(int(round(v)))
    return f'({fmt(p1[0])} {fmt(p1[1])} {fmt(p1[2])}) ({fmt(p2[0])} {fmt(p2[1])} {fmt(p2[2])}) ({fmt(p3[0])} {fmt(p3[1])} {fmt(p3[2])})'


def _uaxis_vaxis_for_plane(normal_axis: str) -> tuple[str, str]:
    """Return (uaxis, vaxis) strings for lightmap alignment. Scale 0.25, no offset."""
    # Standard axis-aligned faces
    if normal_axis == "z-":
        return '[1 0 0 0] 0.25', '[0 -1 0 0] 0.25'
    if normal_axis == "z+":
        return '[1 0 0 0] 0.25', '[0 -1 0 0] 0.25'
    if normal_axis == "x-":
        return '[0 1 0 0] 0.25', '[0 0 -1 0] 0.25'
    if normal_axis == "x+":
        return '[0 1 0 0] 0.25', '[0 0 -1 0] 0.25'
    if normal_axis == "y-":
        return '[1 0 0 0] 0.25', '[0 0 -1 0] 0.25'
    if normal_axis == "y+":
        return '[1 0 0 0] 0.25', '[0 0 -1 0] 0.25'
    return '[1 0 0 0] 0.25', '[0 -1 0 0] 0.25'


def _normal_axis_for_plane(p1: tuple[float, float, float], p2: tuple[float, float, float], p3: tuple[float, float, float]) -> str:
    """Infer face axis from plane points (which form bottom/top/walls)."""
    # Vectors in plane
    ax = p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]
    bx = p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]
    # Normal = ax x bx (right-hand rule)
    nx = ax[1] * bx[2] - ax[2] * bx[1]
    ny = ax[2] * bx[0] - ax[0] * bx[2]
    nz = ax[0] * bx[1] - ax[1] * bx[0]
    if abs(nz) >= abs(nx) and abs(nz) >= abs(ny):
        return "z+" if nz > 0 else "z-"
    if abs(nx) >= abs(ny) and abs(nx) >= abs(nz):
        return "x+" if nx > 0 else "x-"
    return "y+" if ny > 0 else "y-"


class VmfWriter:
    def __init__(self) -> None:
        self.next_id = 2  # 1 reserved for world
        self.world_solids: list[dict[str, Any]] = []
        self.entities: list[dict[str, Any]] = []

    def alloc_id(self) -> int:
        i = self.next_id
        self.next_id += 1
        return i

    def add_brush(self, planes: list[tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]], material: str) -> None:
        """Add one solid (6 sides) from list of 3-point planes. Order: bottom, top, x-, x+, y-, y+."""
        solid_id = self.alloc_id()
        sides = []
        axis_order = ["z+", "z-", "x-", "x+", "y+", "y-"]  # matches plane order: top, bottom, x-, x+, y+, y-
        for i, (p1, p2, p3) in enumerate(planes):
            side_id = self.alloc_id()
            axis = axis_order[i] if i < len(axis_order) else _normal_axis_for_plane(p1, p2, p3)
            uaxis, vaxis = _uaxis_vaxis_for_plane(axis)
            sides.append({
                "id": side_id,
                "plane": _plane_string(p1, p2, p3),
                "material": material,
                "uaxis": uaxis,
                "vaxis": vaxis,
                "rotation": "0",
                "lightmapscale": "16",
                "smoothing_groups": "0",
            })
        self.world_solids.append({
            "id": solid_id,
            "sides": sides,
        })

    def add_entity(self, classname: str, **kwargs: Any) -> None:
        e = {"classname": classname, **kwargs}
        if "id" not in e:
            e["id"] = str(self.alloc_id())
        self.entities.append(e)

    def _emit_block(self, lines: list[str], name: str, keyvalues: dict[str, str], children: list[str]) -> None:
        lines.append(name)
        lines.append("{")
        for k, v in keyvalues.items():
            lines.append(f'\t"{k}" "{v}"')
        for c in children:
            for line in c.split("\n"):
                lines.append("\t" + line)
        lines.append("}")

    def _emit_side(self, side: dict[str, Any]) -> str:
        lines = [
            "side",
            "{",
            f'\t"id" "{side["id"]}"',
            f'\t"plane" "{side["plane"]}"',
            f'\t"material" "{side["material"]}"',
            f'\t"uaxis" "{side["uaxis"]}"',
            f'\t"vaxis" "{side["vaxis"]}"',
            f'\t"rotation" "{side["rotation"]}"',
            f'\t"lightmapscale" "{side["lightmapscale"]}"',
            f'\t"smoothing_groups" "{side["smoothing_groups"]}"',
            "}",
        ]
        return "\n".join(lines)

    def _emit_solid(self, solid: dict[str, Any]) -> str:
        children = [self._emit_side(s) for s in solid["sides"]]
        children.append("editor\n{\n\t\"color\" \"0 136 185\"\n\t\"visgroupshown\" \"1\"\n\t\"visgroupautoshown\" \"1\"\n}")
        lines = [
            "solid",
            "{",
            f'\t"id" "{solid["id"]}"',
        ]
        for s in solid["sides"]:
            lines.append("\t" + self._emit_side(s).replace("\n", "\n\t"))
        lines.append("\teditor")
        lines.append("\t{")
        lines.append('\t\t"color" "0 136 185"')
        lines.append('\t\t"visgroupshown" "1"')
        lines.append('\t\t"visgroupautoshown" "1"')
        lines.append("\t}")
        lines.append("}")
        return "\n".join(lines)

    def _emit_entity(self, e: dict[str, Any]) -> str:
        lines = ["entity", "{"]
        eid = e.get("id")
        if eid is not None:
            lines.append(f'\t"id" "{eid}"')
        for k, v in e.items():
            if k == "id":
                continue
            if k == "solid" and isinstance(v, dict):
                continue
            if isinstance(v, dict):
                continue
            lines.append(f'\t"{k}" "{str(v)}"')
        # Nested solid for brush entities (e.g. dys_jackpoint)
        if isinstance(e.get("solid"), dict):
            lines.append("\t" + self._emit_solid(e["solid"]).replace("\n", "\n\t"))
        lines.append("\teditor")
        lines.append("\t{")
        lines.append('\t\t"visgroupshown" "1"')
        lines.append('\t\t"visgroupautoshown" "1"')
        lines.append("\t}")
        lines.append("}")
        return "\n".join(lines)

    def write(self) -> str:
        """Build full VMF text: versioninfo, visgroups, viewsettings, world, entities, cameras, cordon."""
        lines: list[str] = []

        # versioninfo
        self._emit_block(lines, "versioninfo", {
            "editorversion": "400",
            "editorbuild": "8357",
            "mapversion": "1",
            "formatversion": "100",
            "prefab": "0",
        }, [])

        # visgroups
        lines.append("visgroups")
        lines.append("{")
        lines.append("}")

        # viewsettings
        self._emit_block(lines, "viewsettings", {
            "bSnapToGrid": "1",
            "bShowGrid": "1",
            "bShowLogicalGrid": "0",
            "nGridSpacing": "16",
            "bShow3DGrid": "0",
        }, [])

        # world
        world_children = [self._emit_solid(s) for s in self.world_solids]
        world_kv = {
            "id": "1",
            "mapversion": "1",
            "classname": "worldspawn",
            "detailmaterial": "detail/detailsprites",
            "detailvbsp": "detail.vbsp",
            "maxpropscreenwidth": "-1",
            "skyname": "sky_day01_01_hdr",
        }
        lines.append("world")
        lines.append("{")
        for k, v in world_kv.items():
            lines.append(f'\t"{k}" "{v}"')
        for solid in self.world_solids:
            lines.append("\t" + self._emit_solid(solid).replace("\n", "\n\t"))
        lines.append("}")

        # entities
        for e in self.entities:
            lines.append(self._emit_entity(e))

        # cameras
        self._emit_block(lines, "cameras", {"activecamera": "-1"}, [])

        # cordon
        self._emit_block(lines, "cordon", {
            "mins": "(-1024 -1024 -1024)",
            "maxs": "(1024 1024 1024)",
            "active": "0",
        }, [])

        return "\n".join(lines)
