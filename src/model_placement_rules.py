"""
Curated placement rules for models that need extra validation.

These rules are intentionally small and conservative. They are meant to catch
obviously bad placements for large skyline props before a VMF is written.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelPlacementRule:
    min_z: int | None = None
    border_padding: int = 0
    spawn_padding: int = 0
    max_spawn_delta_z: int = 96
    export_z_offset: int = 0
    category: str = "skyline"


MODEL_PLACEMENT_RULES: dict[str, ModelPlacementRule] = {
    "models/buildings/hitech.mdl": ModelPlacementRule(min_z=512, border_padding=768, category="skyline"),
    "models/buildings/tall01.mdl": ModelPlacementRule(min_z=512, border_padding=768, category="skyline"),
    "models/buildings/tall_lab.mdl": ModelPlacementRule(min_z=384, border_padding=640, category="skyline"),
    "models/dys_cybernetic/building_archology1.mdl": ModelPlacementRule(min_z=-128, border_padding=512, category="skyline"),
    "models/dys_cybernetic/cybertech_base.mdl": ModelPlacementRule(min_z=-128, border_padding=512, category="skyline"),
    "models/dys_cybernetic/cybertech_tower_half.mdl": ModelPlacementRule(min_z=0, border_padding=512, category="skyline"),
    "models/termi/t_spawncrate_closed.mdl": ModelPlacementRule(
        spawn_padding=192,
        max_spawn_delta_z=128,
        category="spawn_blocker",
    ),
    "models/props/dock_station_nopipes.mdl": ModelPlacementRule(
        spawn_padding=224,
        max_spawn_delta_z=128,
        category="ground_cover",
    ),
    "models/props_junk/trashdumpster02.mdl": ModelPlacementRule(
        spawn_padding=192,
        max_spawn_delta_z=128,
        category="ground_cover",
    ),
    "models/props_junk/plasticcrate01a.mdl": ModelPlacementRule(
        spawn_padding=128,
        max_spawn_delta_z=128,
        category="ground_cover",
    ),
    "models/props_junk/wood_crate001a.mdl": ModelPlacementRule(
        spawn_padding=128,
        max_spawn_delta_z=128,
        category="ground_cover",
    ),
    "models/props_junk/wood_crate002a.mdl": ModelPlacementRule(
        spawn_padding=128,
        max_spawn_delta_z=128,
        category="ground_cover",
    ),
    "models/props/dys_vendingmachine01.mdl": ModelPlacementRule(
        export_z_offset=32,
        category="ground_fixture",
    ),
    "models/props/dys_vendingmachine01b.mdl": ModelPlacementRule(
        export_z_offset=32,
        category="ground_fixture",
    ),
    "models/props/dys_vendingmachine01c.mdl": ModelPlacementRule(
        export_z_offset=32,
        category="ground_fixture",
    ),
    "models/props/dys_vendingmachine01d.mdl": ModelPlacementRule(
        export_z_offset=32,
        category="ground_fixture",
    ),
}


def normalize_model_path(model: str) -> str:
    return model.strip().replace("\\", "/").removeprefix("./").lower()


def get_model_placement_rule(model: str) -> ModelPlacementRule | None:
    return MODEL_PLACEMENT_RULES.get(normalize_model_path(model))


def resolve_prop_origin(model: str, origin: tuple[int, int, int]) -> tuple[int, int, int]:
    rule = get_model_placement_rule(model)
    if rule is None or rule.export_z_offset == 0:
        return origin
    x, y, z = origin
    return (x, y, z + rule.export_z_offset)
