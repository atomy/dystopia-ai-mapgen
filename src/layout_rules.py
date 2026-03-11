"""
MVP arena layout schema and fixed gameplay rules.
Scene is grid-snapped (128 units). Defines districts, streets, buildings, objectives, spawns.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# Grid and arena bounds for MVP
GRID = 128
ARENA_SIZE = 2048  # X/Y extent (symmetric around 0 or offset)
FLOOR_Z = 0
CEILING_HEIGHT = 256
TOWER_HEIGHT = 512
ROOF_OFFSET = 64  # height of rooftop platform above building top


@dataclass
class Bounds:
    """Axis-aligned 2D bounds [x_min, y_min, x_max, y_max] or 3D."""
    x_min: int
    y_min: int
    x_max: int
    y_max: int

    def to_list_2d(self) -> list[int]:
        return [self.x_min, self.y_min, self.x_max, self.y_max]


@dataclass
class District:
    name: str
    type: str  # corporate, slums, transit, etc.
    bounds: Bounds
    materials: list[str] = field(default_factory=list)
    height_range: tuple[int, int] = (128, 512)
    street_width_range: tuple[int, int] = (192, 320)
    density: float = 0.7
    material_theme: str | None = None
    preferred_material_groups: list[str] = field(default_factory=list)


@dataclass
class Street:
    name: str
    path: list[tuple[int, int]]  # [(x,y), ...]
    width: int


@dataclass
class Building:
    id: str
    style: str  # tower, block, etc.
    base: tuple[int, int]  # (x, y) bottom-left
    size: tuple[int, int]   # (width, depth)
    height: int
    floors: int = 1
    roof_access: bool = False
    materials: dict[str, str] = field(default_factory=dict)


@dataclass
class Objective:
    type: str  # datacore, etc.
    position: tuple[int, int, int]


@dataclass
class Spawns:
    corp: list[tuple[int, int, int]]
    punk: list[tuple[int, int, int]]


@dataclass
class PropPlacement:
    id: str
    model: str
    origin: tuple[int, int, int]
    angles: tuple[int, int, int] | None = None
    zone: str | None = None
    purpose: str | None = None


@dataclass
class EntityHint:
    classname: str
    origin: tuple[int, int, int]
    angles: tuple[int, int, int] | None = None
    properties: dict[str, str | int | float | bool] = field(default_factory=dict)


@dataclass
class Scene:
    map_name: str
    grid: int
    districts: list[District]
    streets: list[Street]
    buildings: list[Building]
    objectives: list[Objective]
    spawns: Spawns
    props: list[PropPlacement] = field(default_factory=list)
    entities: list[EntityHint] = field(default_factory=list)

    def to_json_dict(self) -> dict[str, Any]:
        return {
            "map_name": self.map_name,
            "grid": self.grid,
            "districts": [
                {
                    "name": d.name,
                    "type": d.type,
                    "bounds": d.bounds.to_list_2d(),
                    "materials": d.materials,
                    "height_range": list(d.height_range),
                    "street_width_range": list(d.street_width_range),
                    "density": d.density,
                    "material_theme": d.material_theme,
                    "preferred_material_groups": d.preferred_material_groups,
                }
                for d in self.districts
            ],
            "streets": [
                {"name": s.name, "path": list(s.path), "width": s.width}
                for s in self.streets
            ],
            "buildings": [
                {
                    "id": b.id,
                    "style": b.style,
                    "base": list(b.base),
                    "size": list(b.size),
                    "height": b.height,
                    "floors": b.floors,
                    "roof_access": b.roof_access,
                    "materials": b.materials,
                }
                for b in self.buildings
            ],
            "objectives": [
                {"type": o.type, "position": list(o.position)}
                for o in self.objectives
            ],
            "spawns": {
                "corp": list(self.spawns.corp),
                "punk": list(self.spawns.punk),
            },
            "props": [
                {
                    "id": p.id,
                    "model": p.model,
                    "origin": list(p.origin),
                    "angles": list(p.angles) if p.angles is not None else None,
                    "zone": p.zone,
                    "purpose": p.purpose,
                }
                for p in self.props
            ],
            "entities": [
                {
                    "classname": e.classname,
                    "origin": list(e.origin),
                    "angles": list(e.angles) if e.angles is not None else None,
                    "properties": e.properties,
                }
                for e in self.entities
            ],
        }


def snap_to_grid(value: int | float, grid: int = GRID) -> int:
    return int(round(value / grid) * grid)


def _tuple2(values: list[int]) -> tuple[int, int]:
    return int(values[0]), int(values[1])


def _tuple3(values: list[int]) -> tuple[int, int, int]:
    return int(values[0]), int(values[1]), int(values[2])


def scene_from_json_dict(data: dict[str, Any]) -> Scene:
    districts = [
        District(
            name=d["name"],
            type=d["type"],
            bounds=Bounds(*d["bounds"]),
            material_theme=d.get("material_theme"),
            preferred_material_groups=list(d.get("preferred_material_groups", [])),
        )
        for d in data.get("districts", [])
    ]
    streets = [
        Street(
            name=s["name"],
            path=[_tuple2(point) for point in s["path"]],
            width=int(s["width"]),
        )
        for s in data.get("streets", [])
    ]
    buildings = [
        Building(
            id=b["id"],
            style=b["style"],
            base=_tuple2(b["base"]),
            size=_tuple2(b["size"]),
            height=int(b["height"]),
            floors=int(b.get("floors", 1)),
            roof_access=bool(b.get("roof_access", False)),
            materials={str(k): str(v) for k, v in b.get("materials", {}).items()},
        )
        for b in data.get("buildings", [])
    ]
    objectives = [
        Objective(type=o["type"], position=_tuple3(o["position"]))
        for o in data.get("objectives", [])
    ]
    corp_list = [_tuple3(p) for p in data["spawns"]["corp"]]
    punk_list = [_tuple3(p) for p in data["spawns"]["punk"]]
    # Ensure at least one spawn per team so the map always has spawns
    if not corp_list:
        corp_list = [(-768, 0, -64)]
    if not punk_list:
        punk_list = [(768, 0, -64)]
    spawns = Spawns(corp=corp_list, punk=punk_list)
    props = [
        PropPlacement(
            id=p["id"],
            model=p["model"],
            origin=_tuple3(p["origin"]),
            angles=_tuple3(p["angles"]) if p.get("angles") is not None else None,
            zone=p.get("zone"),
            purpose=p.get("purpose"),
        )
        for p in data.get("props", [])
    ]
    entities = [
        EntityHint(
            classname=e["classname"],
            origin=_tuple3(e["origin"]),
            angles=_tuple3(e["angles"]) if e.get("angles") is not None else None,
            properties=dict(e.get("properties", {})),
        )
        for e in data.get("entities", [])
    ]
    return Scene(
        map_name=data["map_name"],
        grid=int(data["grid"]),
        districts=districts,
        streets=streets,
        buildings=buildings,
        objectives=objectives,
        spawns=spawns,
        props=props,
        entities=entities,
    )
