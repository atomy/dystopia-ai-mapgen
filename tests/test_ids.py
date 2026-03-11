"""Unique and monotonic ID allocation."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from vmf_writer import VmfWriter
from vmf_primitives import add_box
from validate_map import validate_vmf_text, validate_writer


def test_unique_ids_after_write() -> None:
    w = VmfWriter()
    add_box(w, 0, 0, 0, 64, 64, 64)
    add_box(w, 128, 0, 0, 64, 64, 64)
    out = w.write()
    errors = validate_vmf_text(out)
    assert not [e for e in errors if "Duplicate" in e], errors


def test_validate_writer_no_duplicate_ids() -> None:
    w = VmfWriter()
    add_box(w, 0, 0, 0, 64, 64, 64)
    add_box(w, 128, 0, 0, 64, 64, 64)
    errors = validate_writer(w)
    assert not errors, errors


def test_ids_are_numeric_strings() -> None:
    w = VmfWriter()
    add_box(w, 0, 0, 0, 64, 64, 64)
    out = w.write()
    for m in re.finditer(r'"id"\s+"([^"]+)"', out):
        val = m.group(1)
        assert val.isdigit(), f"ID must be numeric: {val!r}"
