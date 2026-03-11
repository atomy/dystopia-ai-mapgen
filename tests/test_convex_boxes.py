"""Six-face box generation sanity checks and enterable building primitives."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from vmf_writer import VmfWriter
from vmf_primitives import (
    add_box,
    add_floor_slab,
    add_glass_panel,
    add_hollow_shell,
    add_wall_with_door,
)


def test_box_has_six_sides() -> None:
    w = VmfWriter()
    add_box(w, 0, 0, 0, 100, 100, 100)
    assert len(w.world_solids) == 1
    assert len(w.world_solids[0]["sides"]) == 6


def test_box_plane_format() -> None:
    w = VmfWriter()
    add_box(w, 0, 0, 0, 64, 64, 64)
    for side in w.world_solids[0]["sides"]:
        plane = side["plane"]
        assert "(" in plane and ")" in plane
        assert plane.count("(") == 3 and plane.count(")") == 3
        assert "material" in side
        assert "uaxis" in side and "vaxis" in side


def test_multiple_boxes_distinct_solids() -> None:
    w = VmfWriter()
    add_box(w, 0, 0, 0, 64, 64, 64)
    add_box(w, 128, 128, 0, 64, 64, 64)
    assert len(w.world_solids) == 2
    id1 = w.world_solids[0]["id"]
    id2 = w.world_solids[1]["id"]
    assert id1 != id2


def test_box_supports_per_face_materials() -> None:
    w = VmfWriter()
    face_materials = [
        "TOOLS/TOOLSSKYBOX",
        "urban/conc_clean2",
        "BRICK/WALL_A",
        "BRICK/WALL_B",
        "BRICK/WALL_C",
        "BRICK/WALL_D",
    ]
    add_box(w, 0, 0, 0, 64, 64, 64, face_materials=face_materials)
    assert [side["material"] for side in w.world_solids[0]["sides"]] == face_materials


def test_hollow_shell_emits_six_pieces() -> None:
    w = VmfWriter()
    add_hollow_shell(w, 0, 0, 0, 256, 256, 128, wall_thickness=32)
    assert len(w.world_solids) == 6
    for solid in w.world_solids:
        assert len(solid["sides"]) == 6


def test_wall_with_door_emits_multiple_brushes() -> None:
    w = VmfWriter()
    add_wall_with_door(w, "x_min", 0, 0, 0, 32, 128, 128, 32, 64, 64, 96, "BRICK/WALL")
    assert len(w.world_solids) >= 3


def test_glass_panel_emits_one_brush() -> None:
    w = VmfWriter()
    add_glass_panel(w, 0, 0, 0, 4, 64, 64)
    assert len(w.world_solids) == 1
    assert len(w.world_solids[0]["sides"]) == 6


def test_floor_slab_emits_one_brush() -> None:
    w = VmfWriter()
    add_floor_slab(w, 0, 0, 64, 128, 128, 16)
    assert len(w.world_solids) == 1
