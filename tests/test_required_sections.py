"""Verify required VMF sections and order."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from vmf_writer import VmfWriter
from vmf_primitives import add_box
from validate_map import validate_vmf_text, REQUIRED_TOP_LEVEL


def test_required_sections_present() -> None:
    w = VmfWriter()
    add_box(w, 0, 0, 0, 256, 256, 128)
    out = w.write()
    for name in REQUIRED_TOP_LEVEL:
        assert name in out, f"Missing block: {name}"


def test_section_order() -> None:
    w = VmfWriter()
    add_box(w, 0, 0, 0, 64, 64, 64)
    out = w.write()
    errors = validate_vmf_text(out)
    assert not errors, f"Validation errors: {errors}"


def test_world_has_worldspawn() -> None:
    w = VmfWriter()
    add_box(w, 0, 0, 0, 64, 64, 64)
    out = w.write()
    assert "world" in out
    assert "worldspawn" in out
    assert '"classname" "worldspawn"' in out


def test_has_solid_in_world() -> None:
    w = VmfWriter()
    add_box(w, 0, 0, 0, 64, 64, 64)
    out = w.write()
    assert out.count("solid") >= 1
    assert "side" in out
