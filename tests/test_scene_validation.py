"""Layout-level validation for high-risk prop placement."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from layout_rules import Bounds, Building, District, Objective, PropPlacement, Scene, Spawns, Street
from validate_map import validate_scene_layout


def _base_scene(*props: PropPlacement) -> Scene:
    return Scene(
        map_name="dys_validation",
        grid=64,
        districts=[
            District(
                name="test_district",
                type="corporate",
                bounds=Bounds(-1024, -1024, 1024, 1024),
            )
        ],
        streets=[Street(name="main", path=[(-1024, 0), (1024, 0)], width=256)],
        buildings=[],
        objectives=[Objective(type="datacore", position=(0, 0, 128))],
        spawns=Spawns(
            corp=[
                (-768, -320, -64),
                (-768, -192, -64),
                (-768, -64, -64),
                (-768, 64, -64),
                (-768, 192, -64),
                (-768, 320, -64),
            ],
            punk=[
                (768, -320, -64),
                (768, -192, -64),
                (768, -64, -64),
                (768, 64, -64),
                (768, 192, -64),
                (768, 320, -64),
            ],
        ),
        props=list(props),
        entities=[],
    )


def test_blocks_low_z_skyline_prop() -> None:
    scene = _base_scene(
        PropPlacement(
            id="bad_hitech",
            model="models/buildings/hitech.mdl",
            origin=(0, 0, 0),
        )
    )
    errors = validate_scene_layout(scene)
    assert any("minimum placement z" in error for error in errors), errors


def test_blocks_skyline_prop_near_boundary() -> None:
    scene = _base_scene(
        PropPlacement(
            id="edge_hitech",
            model="models/buildings/hitech.mdl",
            origin=(-1100, 0, 640),
        )
    )
    errors = validate_scene_layout(scene)
    assert any("arena boundary" in error for error in errors), errors


def test_allows_curated_skyline_prop_with_safe_offset() -> None:
    scene = _base_scene(
        PropPlacement(
            id="good_hitech",
            model="models/buildings/hitech.mdl",
            origin=(0, 0, 640),
        )
    )
    errors = validate_scene_layout(scene)
    assert not errors, errors


def test_blocks_spawn_blocking_prop_on_spawn_pad() -> None:
    scene = _base_scene(
        PropPlacement(
            id="bad_spawn_crate",
            model="models/termi/t_spawncrate_closed.mdl",
            origin=(-768, 0, 0),
            purpose="spawn_cover",
        )
    )
    errors = validate_scene_layout(scene)
    assert any("too close to spawn position" in error for error in errors), errors


def test_ceiling_prop_without_ceiling_fails_validation() -> None:
    """Prison lamp (ceiling-attached) in open space must fail validation."""
    scene = _base_scene(
        PropPlacement(
            id="floating_lamp",
            model="models/props_wasteland/prison_lamp001b.mdl",
            origin=(-832, 0, 96),
            purpose="spawn_lighting",
        )
    )
    errors = validate_scene_layout(scene)
    assert any("requires a ceiling" in error for error in errors), errors


def test_allows_overhead_prop_near_spawn_when_under_ceiling() -> None:
    """Ceiling lamp near spawn is allowed when a building ceiling exists above it."""
    # Building with ceiling above (-832, 0): base_z=-31, height=160 -> ceiling_underside=97 >= 96
    building = Building(
        id="lamp_ceiling",
        style="block",
        base=(-896, -64),
        size=(128, 128),
        height=160,
        archetype="solid",
    )
    scene = _base_scene(
        PropPlacement(
            id="spawn_lamp",
            model="models/props_wasteland/prison_lamp001b.mdl",
            origin=(-832, 0, 96),
            purpose="spawn_lighting",
        )
    )
    scene.buildings.append(building)
    errors = validate_scene_layout(scene)
    assert not errors, errors


def test_lifts_vending_machine_off_floor_boundary() -> None:
    scene = _base_scene(
        PropPlacement(
            id="floor_vendor",
            model="models/props/dys_vendingmachine01c.mdl",
            origin=(0, 256, -32),
            purpose="landmark",
        )
    )
    errors = validate_scene_layout(scene)
    assert not errors, errors


def test_blocks_vending_machine_inside_generated_platform() -> None:
    scene = _base_scene(
        PropPlacement(
            id="platform_vendor",
            model="models/props/dys_vendingmachine01c.mdl",
            origin=(256, 256, 0),
            purpose="landmark",
        )
    )
    scene.buildings.append(
        Building(
            id="test_platform",
            style="platform",
            base=(256, 256),
            size=(256, 256),
            height=128,
        )
    )
    errors = validate_scene_layout(scene)
    assert any("inside solid building" in error for error in errors), errors


def test_allows_prop_inside_enterable_building() -> None:
    scene = _base_scene(
        PropPlacement(
            id="interior_vendor",
            model="models/props/dys_vendingmachine01c.mdl",
            origin=(320, 320, 48),
            purpose="landmark",
        )
    )
    scene.buildings.append(
        Building(
            id="test_enterable",
            style="block",
            base=(256, 256),
            size=(256, 256),
            height=128,
            archetype="spawn_block",
        )
    )
    errors = validate_scene_layout(scene)
    assert not any("inside solid building" in error for error in errors), errors


def test_requires_six_spawn_pads_per_team() -> None:
    scene = _base_scene()
    scene.spawns = Spawns(
        corp=[(-768, -64, -64)] * 5,
        punk=[(768, -64, -64)] * 5,
    )

    errors = validate_scene_layout(scene)

    assert any("Corp team must define at least 6 spawn pads" in error for error in errors), errors
    assert any("Punk team must define at least 6 spawn pads" in error for error in errors), errors
