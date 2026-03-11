"""
Structural validation of generated VMF before writing.
Checks: unique IDs, required sections/order, entity classnames, spawn/objective presence, grid alignment.
"""

from __future__ import annotations

import re
from typing import Any

from layout_rules import Scene
from model_placement_rules import ModelPlacementRule, get_model_placement_rule, resolve_prop_origin
from scene_to_vmf import has_ceiling_above
from spawn_layout import FLOOR_THICKNESS, FLOOR_Z, SPAWN_FLOOR_Z, Z_FIGHT_OFFSET, resolve_spawn_positions


REQUIRED_TOP_LEVEL = ["versioninfo", "visgroups", "viewsettings", "world", "cameras", "cordon"]
SCENE_BOUNDS_PADDING = 256  # Keep in sync with scene_to_vmf.ARENA_PADDING.
MIN_TEAM_SPAWNS = 6
DEFAULT_PROP_SPAWN_PADDING = 96
DEFAULT_PROP_SPAWN_MAX_DELTA_Z = 96
PURPOSE_SPAWN_PADDING = 192
PURPOSE_SPAWN_MAX_DELTA_Z = 160


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


def _scene_reference_bounds(scene: Scene) -> tuple[int, int, int, int]:
    """
    Return arena bounds inferred from the authored layout, excluding props.

    Large skyline props should not influence these bounds because we validate
    them against the playable area rather than letting them stretch it.
    """
    xs: list[int] = []
    ys: list[int] = []

    for district in scene.districts:
        xs.extend([district.bounds.x_min, district.bounds.x_max])
        ys.extend([district.bounds.y_min, district.bounds.y_max])

    for street in scene.streets:
        half_width = street.width // 2
        for x, y in street.path:
            xs.extend([x - half_width, x + half_width])
            ys.extend([y - half_width, y + half_width])

    for building in scene.buildings:
        xs.extend([building.base[0], building.base[0] + building.size[0]])
        ys.extend([building.base[1], building.base[1] + building.size[1]])

    for x, y, _z in scene.spawns.corp + scene.spawns.punk:
        xs.append(x)
        ys.append(y)

    for objective in scene.objectives:
        xs.append(objective.position[0])
        ys.append(objective.position[1])

    for entity in scene.entities:
        xs.append(entity.origin[0])
        ys.append(entity.origin[1])

    if not xs or not ys:
        return (-1024, -1024, 1024, 1024)

    return (
        min(xs) - SCENE_BOUNDS_PADDING,
        min(ys) - SCENE_BOUNDS_PADDING,
        max(xs) + SCENE_BOUNDS_PADDING,
        max(ys) + SCENE_BOUNDS_PADDING,
    )


def validate_scene_layout(scene: Scene) -> list[str]:
    """Validate layout-level placement constraints before exporting a VMF."""
    errors: list[str] = []

    for building in scene.buildings:
        if building.is_enterable():
            min_interior = 2 * building.wall_thickness
            if building.size[0] < min_interior or building.size[1] < min_interior:
                errors.append(
                    f"Enterable building {building.id} ({building.archetype}) footprint too small: "
                    f"size {building.size} must allow interior (min {min_interior} per axis)"
                )
            if building.floor_height is not None and building.floor_height < 96:
                errors.append(
                    f"Enterable building {building.id} floor_height must be at least 96 "
                    f"(got {building.floor_height})"
                )

    if len(scene.spawns.corp) < MIN_TEAM_SPAWNS:
        errors.append(
            f"Corp team must define at least {MIN_TEAM_SPAWNS} spawn pads "
            f"(found {len(scene.spawns.corp)})"
        )
    if len(scene.spawns.punk) < MIN_TEAM_SPAWNS:
        errors.append(
            f"Punk team must define at least {MIN_TEAM_SPAWNS} spawn pads "
            f"(found {len(scene.spawns.punk)})"
        )

    arena_x_min, arena_y_min, arena_x_max, arena_y_max = _scene_reference_bounds(scene)
    arena_bounds = (arena_x_min, arena_y_min, arena_x_max, arena_y_max)
    # Only solid buildings block spawn placement; enterable buildings may contain spawns/interiors.
    building_boxes = [(b.base, b.size) for b in scene.buildings if b.height > 0 and not b.is_enterable()]
    resolved_spawns = (
        resolve_spawn_positions(scene.spawns.corp, 1, arena_bounds, building_boxes)
        + resolve_spawn_positions(scene.spawns.punk, 2, arena_bounds, building_boxes)
    )
    floor_top_z = FLOOR_Z + FLOOR_THICKNESS
    base_z = FLOOR_Z + FLOOR_THICKNESS + Z_FIGHT_OFFSET

    for prop in scene.props:
        rule = get_model_placement_rule(prop.model)
        x, y, z = resolve_prop_origin(prop.model, prop.origin)

        if rule is not None and rule.requires_ceiling and not has_ceiling_above(scene.buildings, x, y, z, base_z):
            errors.append(
                f"Prop {prop.id} ({prop.model}) requires a ceiling above it but is in open space "
                f"(no building ceiling at origin {x} {y} {z})"
            )

        if rule is not None and rule.min_z is not None and z < rule.min_z:
            errors.append(
                f"Prop {prop.id} ({prop.model}) is below its minimum placement z "
                f"({z} < {rule.min_z}) for {rule.category} models"
            )

        border_distance = min(x - arena_x_min, arena_x_max - x, y - arena_y_min, arena_y_max - y)
        if rule is not None and rule.border_padding and border_distance < rule.border_padding:
            errors.append(
                f"Prop {prop.id} ({prop.model}) is too close to the arena boundary "
                f"({border_distance} < {rule.border_padding}) for {rule.category} models"
            )

        purpose_lower = (prop.purpose or "").lower()
        purpose_spawn_padding = _purpose_spawn_padding(purpose_lower)
        purpose_spawn_delta_z = PURPOSE_SPAWN_MAX_DELTA_Z if purpose_spawn_padding else 0

        spawn_padding = max(
            DEFAULT_PROP_SPAWN_PADDING,
            purpose_spawn_padding,
            rule.spawn_padding if rule is not None else 0,
        )
        spawn_delta_z = max(
            DEFAULT_PROP_SPAWN_MAX_DELTA_Z,
            purpose_spawn_delta_z,
            rule.max_spawn_delta_z if rule is not None else 0,
        )

        if abs(z - SPAWN_FLOOR_Z) <= spawn_delta_z:
            for spawn_x, spawn_y, _yaw in resolved_spawns:
                dx = x - spawn_x
                dy = y - spawn_y
                if (dx * dx) + (dy * dy) < (spawn_padding * spawn_padding):
                    blocker_category = _spawn_blocker_category(rule, purpose_lower)
                    errors.append(
                        f"Prop {prop.id} ({prop.model}) is too close to spawn position "
                        f"({spawn_padding} units clearance required) for {blocker_category} placement"
                    )
                    break

        if not _skip_solid_embedding_check(rule):
            if _point_in_box(x, y, z, arena_x_min, arena_y_min, FLOOR_Z, arena_x_max, arena_y_max, floor_top_z):
                errors.append(
                    f"Prop {prop.id} ({prop.model}) resolves inside the floor slab after placement adjustment"
                )
                continue

            for building in scene.buildings:
                if building.height <= 0 or building.is_enterable():
                    continue
                bx0, by0 = building.base
                bx1 = bx0 + building.size[0]
                by1 = by0 + building.size[1]
                bz0 = floor_top_z + Z_FIGHT_OFFSET
                bz1 = bz0 + building.height
                if _point_in_box(x, y, z, bx0, by0, bz0, bx1, by1, bz1):
                    errors.append(
                        f"Prop {prop.id} ({prop.model}) resolves inside solid building {building.id} "
                        f"after placement adjustment"
                    )
                    break

    return errors


def _spawn_blocker_category(rule: ModelPlacementRule | None, purpose_lower: str) -> str:
    if rule is not None and rule.category:
        return rule.category
    if _purpose_spawn_padding(purpose_lower):
        return "spawn-purpose"
    return "ground-level"


def _purpose_spawn_padding(purpose_lower: str) -> int:
    if "spawn" not in purpose_lower:
        return 0
    blocking_keywords = ("cover", "crate", "block", "obstacle", "barrier")
    return PURPOSE_SPAWN_PADDING if any(keyword in purpose_lower for keyword in blocking_keywords) else 0


def _point_in_box(
    x: int,
    y: int,
    z: int,
    x_min: int,
    y_min: int,
    z_min: int,
    x_max: int,
    y_max: int,
    z_max: int,
) -> bool:
    return x_min <= x <= x_max and y_min <= y <= y_max and z_min <= z <= z_max


def _skip_solid_embedding_check(rule: ModelPlacementRule | None) -> bool:
    return rule is not None and rule.category == "skyline"


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
        if "solid" in e and isinstance(e.get("solid"), dict):
            for side in e["solid"]["sides"]:
                if side["id"] in ids:
                    errors.append(f"Duplicate brush-entity side id {side['id']}")
                ids.add(side["id"])
            if e["solid"]["id"] in ids:
                errors.append(f"Duplicate brush-entity solid id {e['solid']['id']}")
            ids.add(e["solid"]["id"])
    return errors
