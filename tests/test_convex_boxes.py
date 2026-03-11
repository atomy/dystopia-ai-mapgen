"""Six-face box generation sanity checks."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from vmf_writer import VmfWriter
from vmf_primitives import add_box


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
        "DEV/DEV_MEASUREGENERIC01",
        "BRICK/WALL_A",
        "BRICK/WALL_B",
        "BRICK/WALL_C",
        "BRICK/WALL_D",
    ]
    add_box(w, 0, 0, 0, 64, 64, 64, face_materials=face_materials)
    assert [side["material"] for side in w.world_solids[0]["sides"]] == face_materials
