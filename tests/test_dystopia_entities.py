"""Tests for dystopia_entities helpers (func_door, func_breakable, etc.)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from vmf_writer import VmfWriter
from dystopia_entities import add_func_door, DEFAULT_DOOR_MATERIAL


def test_add_func_door_emits_one_entity() -> None:
    w = VmfWriter()
    add_func_door(w, 0, 0, 0, 32, 64, 128, movedir="0 0 0", targetname="door1")
    assert len(w.entities) == 1
    e = w.entities[0]
    assert e["classname"] == "func_door"
    assert e["targetname"] == "door1"
    assert e["movedir"] == "0 0 0"
    assert e["speed"] == "100"
    assert e["wait"] == "4"
    assert e["lip"] == "0"
    assert e["spawnpos"] == "0"
    assert e["forceclosed"] == "0"
    assert e["spawnflags"] == "1024"


def test_add_func_door_brush_has_six_sides() -> None:
    w = VmfWriter()
    add_func_door(w, 0, 0, 0, 16, 64, 96, material=DEFAULT_DOOR_MATERIAL)
    e = w.entities[0]
    assert "solid" in e
    assert "sides" in e["solid"]
    assert len(e["solid"]["sides"]) == 6
    for side in e["solid"]["sides"]:
        assert "plane" in side and "material" in side
        assert side["material"] == DEFAULT_DOOR_MATERIAL


def test_add_func_door_origin_at_center() -> None:
    w = VmfWriter()
    add_func_door(w, 100, 200, 300, 132, 264, 428)  # center (116, 232, 364)
    e = w.entities[0]
    assert e["origin"] == "116 232 364"
