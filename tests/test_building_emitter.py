"""Building emitter: solid vs enterable brush count."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from layout_rules import Building
from vmf_writer import VmfWriter
from building_emitter import emit_building

FLOOR_Z = -64
FLOOR_THICKNESS = 32
BASE_Z = FLOOR_Z + FLOOR_THICKNESS


def test_solid_building_emits_one_brush() -> None:
    w = VmfWriter()
    b = Building(
        id="solid_block",
        style="block",
        base=(0, 0),
        size=(256, 256),
        height=128,
        archetype="solid",
    )
    emit_building(w, b, BASE_Z)
    assert len(w.world_solids) == 1
    assert len(w.world_solids[0]["sides"]) == 6


def test_enterable_building_emits_many_brushes() -> None:
    w = VmfWriter()
    b = Building(
        id="enterable_block",
        style="block",
        base=(0, 0),
        size=(256, 256),
        height=128,
        floors=2,
        archetype="spawn_block",
    )
    emit_building(w, b, BASE_Z)
    # Floor, roof, 4 walls (possibly with door/window segments), interior slabs, maybe stair core
    assert len(w.world_solids) >= 8, "enterable building should emit many brushes (shell + floors + walls)"
    for solid in w.world_solids:
        assert len(solid["sides"]) >= 4, "each solid must have valid side count"


def test_enterable_building_emits_door_entities() -> None:
    """Enterable buildings with entrances emit paired func_door entities per entrance."""
    w = VmfWriter()
    b = Building(
        id="shop",
        style="block",
        base=(0, 0),
        size=(256, 256),
        height=128,
        archetype="small_shop",
        entrance_sides=["y_max"],
    )
    emit_building(w, b, BASE_Z)
    doors = [e for e in w.entities if e.get("classname") == "func_door"]
    # One entrance (y_max) -> two leaves (_l, _r)
    assert len(doors) == 2, "one entrance should emit two door leaves"
    targetnames = {e.get("targetname") for e in doors}
    assert targetnames == {"shop_y_max_door_l", "shop_y_max_door_r"}
    movedirs = {e.get("movedir") for e in doors}
    # y_max entrance: doors slide along X
    assert movedirs == {"0 0 0", "0 180 0"}
    for e in doors:
        assert "solid" in e and "sides" in e["solid"]
        assert len(e["solid"]["sides"]) == 6


def test_enterable_building_two_entrances_emits_four_doors() -> None:
    """Spawn_block has two entrance sides -> four func_door entities."""
    w = VmfWriter()
    b = Building(
        id="spawn",
        style="block",
        base=(0, 0),
        size=(256, 256),
        height=128,
        archetype="spawn_block",
    )
    emit_building(w, b, BASE_Z)
    doors = [e for e in w.entities if e.get("classname") == "func_door"]
    assert len(doors) == 4, "spawn_block has x_min and x_max -> 4 door leaves"
    targetnames = [e.get("targetname") for e in doors]
    assert "spawn_x_min_door_l" in targetnames and "spawn_x_min_door_r" in targetnames
    assert "spawn_x_max_door_l" in targetnames and "spawn_x_max_door_r" in targetnames
