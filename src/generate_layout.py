"""
Build a structured JSON scene for the MVP arena.
Deterministic layout: 2 spawn buildings, central plaza, 2 alleys, objective tower, rooftop bypass.
"""

from __future__ import annotations

import json
from pathlib import Path

from layout_rules import (
    Bounds,
    Building,
    District,
    GRID,
    EntityHint,
    PropPlacement,
    Scene,
    Spawns,
    Objective,
    Street,
    snap_to_grid,
)


def generate_mvp_arena() -> Scene:
    """Fixed MVP layout: symmetric arena with plaza, alleys, tower, rooftop route."""
    half = 1024
    g = GRID

    # One district covering the arena
    districts = [
        District(
            name="corp_plaza",
            type="corporate",
            bounds=Bounds(-half, -half, half, half),
            materials=["concrete", "metal"],
            height_range=(256, 512),
            street_width_range=(192, 384),
            density=0.6,
            material_theme="clean_corporate",
            preferred_material_groups=["urban", "twincannon", "vaccinecore"],
        ),
    ]

    # Main avenue (horizontal through center), two flank alleys
    streets = [
        Street(name="main_avenue", path=[(-half, 0), (half, 0)], width=384),
        Street(name="alley_north", path=[(-half, 384), (0, 384), (half, 384)], width=192),
        Street(name="alley_south", path=[(-half, -384), (0, -384), (half, -384)], width=192),
    ]

    # Corp spawn building (west), Punk spawn building (east), central plaza, objective tower (center), rooftop bypass
    # Enterable archetypes: spawn_block, small_shop, office_midrise, warehouse. solid = legacy solid block.
    buildings = [
        Building(
            id="corp_spawn_building",
            style="block",
            base=(-half - 384, -256),
            size=(384, 512),
            height=256,
            floors=2,
            roof_access=True,
            materials={
                "floor": "urban/conc_clean2",
                "wall": "twincannon/dys_office/office_wall2",
                "roof": "vaccine/dys_metalroof",
            },
            archetype="spawn_block",
            entrance_sides=["x_max"],
        ),
        Building(
            id="punk_spawn_building",
            style="block",
            base=(half, -256),
            size=(384, 512),
            height=256,
            floors=2,
            roof_access=True,
            materials={
                "floor": "urban/conc_clean2",
                "wall": "urban/dys_urban_chipboard_04",
                "roof": "vaccine/dys_metalroof",
            },
            archetype="spawn_block",
            entrance_sides=["x_min"],
        ),
        Building(
            id="plaza",
            style="open",
            base=(-512, -384),
            size=(1024, 768),
            height=0,  # ground only, no volume
            floors=1,
            roof_access=False,
        ),
        Building(
            id="objective_tower",
            style="tower",
            base=(-256, -256),
            size=(512, 512),
            height=512,
            floors=4,
            roof_access=True,
            materials={
                "floor": "urban/conc_clean2",
                "wall": "vaccinecore/metal_panelwall_001",
                "roof": "vaccine/dys_metalroof",
            },
            archetype="office_midrise",
            entrance_sides=["x_min", "x_max"],
        ),
        Building(
            id="rooftop_bypass_north",
            style="platform",
            base=(-384, 256),
            size=(768, 128),
            height=320,
            floors=1,
            roof_access=True,
            materials={
                "floor": "twincannon/concretefloor009a_fixed",
                "wall": "twincannon/concretefloor009a_fixed",
                "roof": "twincannon/concretefloor009a_fixed",
            },
        ),
        Building(
            id="rooftop_bypass_south",
            style="platform",
            base=(-384, -384),
            size=(768, 128),
            height=320,
            floors=1,
            roof_access=True,
            materials={
                "floor": "twincannon/concretefloor009a_fixed",
                "wall": "twincannon/concretefloor009a_fixed",
                "roof": "twincannon/concretefloor009a_fixed",
            },
        ),
    ]

    objectives = [
        Objective(type="datacore", position=(0, 0, 256)),
    ]

    # Spawn positions: corp west, punk east; at least 6 per team for validation
    spawn_floor_z = -64
    spawns = Spawns(
        corp=[
            (-768, -192, spawn_floor_z),
            (-768, -64, spawn_floor_z),
            (-768, 64, spawn_floor_z),
            (-768, 192, spawn_floor_z),
            (-768, -128, spawn_floor_z),
            (-768, 128, spawn_floor_z),
        ],
        punk=[
            (768, -192, spawn_floor_z),
            (768, -64, spawn_floor_z),
            (768, 64, spawn_floor_z),
            (768, 192, spawn_floor_z),
            (768, -128, spawn_floor_z),
            (768, 128, spawn_floor_z),
        ],
    )

    # Ceiling-attached lamps omitted in open plazas; add under buildings if desired.
    props: list[PropPlacement] = []

    entities = [
        EntityHint(
            classname="env_cubemap",
            origin=(0, 0, 192),
        ),
    ]

    return Scene(
        map_name="dys_ai",
        grid=g,
        districts=districts,
        streets=streets,
        buildings=buildings,
        objectives=objectives,
        spawns=spawns,
        props=props,
        entities=entities,
    )


def main() -> None:
    scene = generate_mvp_arena()
    out_dir = Path(__file__).resolve().parent.parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "layout.json"
    with open(path, "w") as f:
        json.dump(scene.to_json_dict(), f, indent=2)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
