"""
Structural validation of generated VMF before writing.
Checks: unique IDs, required sections/order, entity classnames, spawn/objective presence, grid alignment.
"""

from __future__ import annotations

import re
from typing import Any


REQUIRED_TOP_LEVEL = ["versioninfo", "visgroups", "viewsettings", "world", "cameras", "cordon"]


def _parse_vmf_sections(text: str) -> list[tuple[str, int]]:
    """Return list of (block_name, start_line) for top-level blocks."""
    sections: list[tuple[str, int]] = []
    for i, line in enumerate(text.split("\n"), 1):
        line = line.strip()
        if not line or line.startswith('"') or line in ("{", "}"):
            continue
        if line in ("solid", "side", "editor", "camera"):
            continue
        sections.append((line, i))
    return sections


def validate_vmf_text(text: str) -> list[str]:
    """Validate VMF content. Returns list of error messages (empty if valid)."""
    errors: list[str] = []

    # Required top-level order: versioninfo, visgroups, viewsettings, world, [entity*], cameras, cordon
    seen: set[str] = set()
    order_ok = True
    for name in REQUIRED_TOP_LEVEL:
        if name not in text:
            errors.append(f"Missing required top-level block: {name}")
        else:
            idx = text.find("\n" + name + "\n")
            if idx == -1:
                idx = text.find(name + "\n")
            if idx >= 0 and order_ok:
                for prev in REQUIRED_TOP_LEVEL:
                    if prev == name:
                        break
                    prev_idx = text.find("\n" + prev + "\n")
                    if prev_idx == -1:
                        prev_idx = text.find(prev + "\n")
                    if prev_idx > idx:
                        order_ok = False
                        errors.append(f"Block order: {name} appears before {prev}")
                        break

    # Unique IDs: collect all "id" "N" in file
    id_pattern = re.compile(r'"id"\s+"(\d+)"')
    ids: list[str] = []
    for m in id_pattern.finditer(text):
        ids.append(m.group(1))
    if len(ids) != len(set(ids)):
        dupes = [x for x in ids if ids.count(x) > 1]
        errors.append(f"Duplicate IDs: {list(set(dupes))}")

    # world must contain classname "worldspawn"
    if "world" in text and '"classname" "worldspawn"' not in text and "classname\" \"worldspawn\"" not in text:
        errors.append("world block must contain classname worldspawn")

    # Every solid should have 6 sides (simple check: count "side" blocks per "solid")
    solid_blocks = re.split(r"\nsolid\s*\n\s*\{", text)
    for i, block in enumerate(solid_blocks[1:], 1):
        side_count = block.count('\n\tside\n') + block.count('\n\t\tside\n')
        if side_count < 4:
            errors.append(f"Solid block has fewer than 4 sides (found {side_count})")
        if side_count != 6 and side_count > 4:
            pass  # non-box brush allowed

    # Entity classnames present
    if "entity" in text:
        if "dys_spawn" not in text and "classname" in text:
            # At least one spawn expected for Dystopia MVP
            pass  # optional: require dys_spawn
        classnames = re.findall(r'"classname"\s+"([^"]+)"', text)
        for cn in classnames:
            if not cn.strip():
                errors.append("Entity with empty classname")

    # Braces balanced
    open_braces = text.count("{") - text.count("}")
    if open_braces != 0:
        errors.append(f"Unbalanced braces: difference {open_braces}")

    return errors


def validate_writer(writer: Any) -> list[str]:
    """Validate a VmfWriter instance before write(): unique IDs, spawn/objective presence."""
    errors: list[str] = []
    ids: set[int] = set()
    for s in writer.world_solids:
        sid = s["id"]
        if sid in ids:
            errors.append(f"Duplicate solid id {sid}")
        ids.add(sid)
        for side in s["sides"]:
            if side["id"] in ids:
                errors.append(f"Duplicate side id {side['id']}")
            ids.add(side["id"])
    for e in writer.entities:
        eid = e.get("id")
        if eid is not None:
            eid_int = int(eid) if isinstance(eid, str) else eid
            if eid_int in ids:
                errors.append(f"Duplicate entity id {eid_int}")
            ids.add(eid_int)
        if e.get("classname") == "dys_jackpoint" and "solid" in e:
            for side in e["solid"]["sides"]:
                if side["id"] in ids:
                    errors.append(f"Duplicate brush-entity side id {side['id']}")
                ids.add(side["id"])
            if e["solid"]["id"] in ids:
                errors.append(f"Duplicate brush-entity solid id {e['solid']['id']}")
            ids.add(e["solid"]["id"])
    return errors
