"""
Catalog Dystopia material definitions for map editing.
"""

from __future__ import annotations

import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path


LINE_RE = re.compile(r'^\s*"(?P<key>[^"]+)"\s+(?:"(?P<quoted>[^"]*)"|(?P<bare>\S+))')
MATERIAL_RE = re.compile(r'^\s*"material"\s+"(?P<material>[^"]+)"', re.IGNORECASE)
MAPPING_EXCLUDE_PREFIXES = (
    "vgui/",
    "models/",
    "particles/",
    "sprites/",
    "effects/",
)


def resolve_game_dir() -> Path:
    env_value = os.environ.get("DYSTOPIA_GAME_DIR")
    if env_value:
        return Path(env_value)

    return Path(__file__).resolve().parents[3]


def normalize_material_path(path: Path, material_root: Path) -> str:
    return path.relative_to(material_root).as_posix()


def normalize_material_name(material_name: str) -> str:
    normalized = material_name.replace("\\", "/").strip().lower()
    if normalized.endswith(".vmt"):
        normalized = normalized[:-4]
    return normalized


def normalize_model_name(model_name: str) -> str:
    return model_name.replace("\\", "/").strip().lower()


def parse_vmt(path: Path, material_root: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()

    shader = "Unknown"
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('"') and stripped.count('"') >= 2:
            shader = stripped.split('"')[1]
            break

    props: dict[str, str] = {}
    for line in lines:
        match = LINE_RE.match(line)
        if not match:
            continue
        key = match.group("key").lower()
        value = match.group("quoted") if match.group("quoted") is not None else match.group("bare")
        props[key] = value

    material_rel = normalize_material_path(path, material_root)
    material_name = material_rel[:-4] if material_rel.endswith(".vmt") else material_rel
    group = material_name.split("/", 1)[0] if "/" in material_name else material_name

    usage = classify_material(material_name, shader)
    basetexture = props.get("$basetexture", "")

    return {
        "material": material_name,
        "material_key": normalize_material_name(material_name),
        "vmt_path": material_rel,
        "group": group,
        "shader": shader,
        "surfaceprop": props.get("$surfaceprop", ""),
        "basetexture": basetexture.replace("\\", "/"),
        "usage": usage,
        "map_usable": usage in {"map", "skybox", "decal", "overlay"},
        "flags": {
            "translucent": props.get("$translucent", "0"),
            "alphatest": props.get("$alphatest", "0"),
            "nocull": props.get("$nocull", "0"),
            "selfillum": props.get("$selfillum", "0"),
        },
    }


def _iter_vmf_keyvalues(vmf_path: Path):
    block_stack: list[str] = []
    pending_block: str | None = None

    with vmf_path.open("r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped == "{":
                block_stack.append(pending_block or "")
                pending_block = None
                continue
            if stripped == "}":
                if block_stack:
                    block_stack.pop()
                pending_block = None
                continue
            if stripped.startswith('"'):
                match = LINE_RE.match(line)
                if match:
                    value = match.group("quoted") if match.group("quoted") is not None else match.group("bare")
                    yield ("keyvalue", list(block_stack), match.group("key").lower(), value)
                continue

            pending_block = stripped
            yield ("block", list(block_stack), stripped, None)


def scan_vmf_material_usage(vmf_dir: Path) -> dict[str, object]:
    vmf_paths = sorted(vmf_dir.rglob("*.vmf"))
    usage_by_material: dict[str, set[str]] = defaultdict(set)
    usage_by_map: dict[str, set[str]] = {}

    for vmf_path in vmf_paths:
        material_names: set[str] = set()
        for event_type, block_stack, key, value in _iter_vmf_keyvalues(vmf_path):
            if event_type != "keyvalue":
                continue
            if key != "material" or "side" not in block_stack:
                continue
            material_name = normalize_material_name(value or "")
            material_names.add(material_name)

        map_name = vmf_path.stem
        usage_by_map[map_name] = material_names
        for material_name in material_names:
            usage_by_material[material_name].add(map_name)

    return {
        "vmf_dir": str(vmf_dir),
        "vmf_count": len(vmf_paths),
        "map_names": sorted(usage_by_map.keys()),
        "unique_material_count": len(usage_by_material),
        "usage_by_material": {
            material: sorted(map_names)
            for material, map_names in sorted(usage_by_material.items())
        },
        "usage_by_map": {
            map_name: sorted(material_names)
            for map_name, material_names in sorted(usage_by_map.items())
        },
    }


def scan_vmf_entities_and_models(vmf_dir: Path, game_dir: Path | None = None) -> dict[str, object]:
    vmf_paths = sorted(vmf_dir.rglob("*.vmf"))
    game_dir = game_dir or resolve_game_dir()

    entity_usage: dict[str, dict[str, object]] = {}
    model_usage: dict[str, dict[str, object]] = {}
    entities_by_map: dict[str, list[dict[str, object]]] = {}
    entity_instance_count = 0
    external_model_refs = 0

    for vmf_path in vmf_paths:
        map_name = vmf_path.stem
        entities_by_map[map_name] = []

        current_entity: dict[str, object] | None = None
        current_entity_depth: int | None = None
        entity_counter = 0

        for event_type, block_stack, key, value in _iter_vmf_keyvalues(vmf_path):
            if current_entity is not None and len(block_stack) < (current_entity_depth or 0):
                finalize_entity_record(current_entity, entities_by_map, entity_usage, model_usage, game_dir)
                entity_instance_count += 1
                if current_entity.get("external_models"):
                    external_model_refs += len(current_entity["external_models"])
                current_entity = None
                current_entity_depth = None

            if event_type == "block":
                if key == "entity":
                    current_entity = {
                        "map": map_name,
                        "order": entity_counter,
                        "keyvalues": {},
                    }
                    current_entity_depth = len(block_stack) + 1
                    entity_counter += 1
                continue

            if current_entity is None:
                continue

            if len(block_stack) == current_entity_depth:
                current_entity["keyvalues"][key] = value

        if current_entity is not None:
            finalize_entity_record(current_entity, entities_by_map, entity_usage, model_usage, game_dir)
            entity_instance_count += 1
            if current_entity.get("external_models"):
                external_model_refs += len(current_entity["external_models"])

    return {
        "vmf_dir": str(vmf_dir),
        "vmf_count": len(vmf_paths),
        "map_names": sorted(entities_by_map.keys()),
        "entity_instance_count": entity_instance_count,
        "unique_entity_classes": len(entity_usage),
        "unique_external_models": len(model_usage),
        "external_model_ref_count": external_model_refs,
        "entities_by_class": dict(sorted(entity_usage.items())),
        "models": dict(sorted(model_usage.items())),
        "entities_by_map": entities_by_map,
    }


def finalize_entity_record(
    current_entity: dict[str, object],
    entities_by_map: dict[str, list[dict[str, object]]],
    entity_usage: dict[str, dict[str, object]],
    model_usage: dict[str, dict[str, object]],
    game_dir: Path,
) -> None:
    keyvalues = current_entity["keyvalues"]
    classname = str(keyvalues.get("classname", "")).strip().lower()
    if not classname:
        return

    map_name = str(current_entity["map"])
    model_value = str(keyvalues.get("model", "")).strip()
    normalized_model = normalize_model_name(model_value) if model_value else ""
    external_models = [normalized_model] if normalized_model and not normalized_model.startswith("*") else []
    current_entity["external_models"] = external_models

    entity_summary = {
        "classname": classname,
        "has_model": bool(model_value),
        "model": normalized_model,
        "origin": str(keyvalues.get("origin", "")),
        "targetname": str(keyvalues.get("targetname", "")),
    }
    entities_by_map[map_name].append(entity_summary)

    entity_info = entity_usage.setdefault(
        classname,
        {
            "count": 0,
            "maps": set(),
            "keys": Counter(),
            "external_models": set(),
        },
    )
    entity_info["count"] += 1
    entity_info["maps"].add(map_name)
    for key in keyvalues.keys():
        entity_info["keys"][key] += 1
    for model_name in external_models:
        entity_info["external_models"].add(model_name)

    for model_name in external_models:
        model_path = game_dir / model_name
        model_info = model_usage.setdefault(
            model_name,
            {
                "count": 0,
                "maps": set(),
                "classnames": set(),
                "exists_in_game": model_path.exists(),
            },
        )
        model_info["count"] += 1
        model_info["maps"].add(map_name)
        model_info["classnames"].add(classname)


def normalize_entity_scan(entity_scan: dict[str, object]) -> dict[str, object]:
    normalized_entities_by_class: dict[str, dict[str, object]] = {}
    for classname, info in entity_scan["entities_by_class"].items():
        normalized_entities_by_class[classname] = {
            "count": info["count"],
            "maps": sorted(info["maps"]),
            "common_keys": [key for key, _ in info["keys"].most_common(12)],
            "external_models": sorted(info["external_models"]),
        }

    normalized_models: dict[str, dict[str, object]] = {}
    for model_name, info in entity_scan["models"].items():
        normalized_models[model_name] = {
            "count": info["count"],
            "maps": sorted(info["maps"]),
            "classnames": sorted(info["classnames"]),
            "exists_in_game": info["exists_in_game"],
        }

    normalized_by_map = {
        map_name: sorted(entries, key=lambda entry: (entry["classname"], entry["model"], entry["origin"]))
        for map_name, entries in sorted(entity_scan["entities_by_map"].items())
    }

    normalized_scan = dict(entity_scan)
    normalized_scan["entities_by_class"] = normalized_entities_by_class
    normalized_scan["models"] = normalized_models
    normalized_scan["entities_by_map"] = normalized_by_map
    return normalized_scan


def enrich_catalog_with_vmf_usage(catalog: dict[str, object], usage_scan: dict[str, object]) -> dict[str, object]:
    usage_by_material = usage_scan["usage_by_material"]
    all_used_materials = set(usage_by_material.keys())

    enriched_materials: list[dict[str, object]] = []
    for entry in catalog["materials"]:
        material_key = entry["material_key"]
        used_in_maps = usage_by_material.get(material_key, [])
        enriched_entry = dict(entry)
        enriched_entry["used_in_maps"] = used_in_maps
        enriched_entry["used_in_map_count"] = len(used_in_maps)
        enriched_entry["used_in_mapsrc"] = bool(used_in_maps)
        enriched_materials.append(enriched_entry)

    known_materials = {entry["material_key"] for entry in enriched_materials}
    missing_materials = sorted(all_used_materials - known_materials)
    used_counter = Counter(
        entry["group"] for entry in enriched_materials if entry["used_in_mapsrc"]
    )

    grouped_entries: dict[str, list[dict[str, object]]] = defaultdict(list)
    for entry in enriched_materials:
        grouped_entries[str(entry["group"])].append(entry)

    for group in grouped_entries.values():
        group.sort(key=lambda entry: str(entry["material"]))

    enriched_catalog = dict(catalog)
    enriched_catalog["materials"] = enriched_materials
    enriched_catalog["materials_by_group"] = dict(sorted(grouped_entries.items()))
    enriched_catalog["vmf_usage"] = {
        "vmf_dir": usage_scan["vmf_dir"],
        "vmf_count": usage_scan["vmf_count"],
        "map_names": usage_scan["map_names"],
        "unique_used_materials": usage_scan["unique_material_count"],
        "catalog_materials_used": sum(1 for entry in enriched_materials if entry["used_in_mapsrc"]),
        "missing_materials": missing_materials,
        "used_groups": dict(sorted(used_counter.items())),
        "usage_by_map": usage_scan["usage_by_map"],
    }
    return enriched_catalog


def usage_scan_to_markdown(usage_scan: dict[str, object]) -> str:
    lines = [
        "# VMF Used Texture Report",
        "",
        f"- VMF source dir: `{usage_scan['vmf_dir']}`",
        f"- VMF files scanned: `{usage_scan['vmf_count']}`",
        f"- Unique referenced materials: `{usage_scan['unique_material_count']}`",
        "",
        "## Maps",
        "",
    ]

    for map_name in usage_scan["map_names"]:
        material_count = len(usage_scan["usage_by_map"][map_name])
        lines.append(f"- `{map_name}`: `{material_count}` unique materials")

    lines.extend([
        "",
        "## Referenced Materials",
        "",
        "| Material | Used By Maps |",
        "|---|---|",
    ])

    for material_name, map_names in usage_scan["usage_by_material"].items():
        lines.append(f"| `{material_name}` | `{len(map_names)}` |")

    return "\n".join(lines)


def entity_scan_to_markdown(entity_scan: dict[str, object]) -> str:
    lines = [
        "# VMF Entity And Model Report",
        "",
        f"- VMF source dir: `{entity_scan['vmf_dir']}`",
        f"- VMF files scanned: `{entity_scan['vmf_count']}`",
        f"- Entity instances: `{entity_scan['entity_instance_count']}`",
        f"- Unique entity classes: `{entity_scan['unique_entity_classes']}`",
        f"- Unique external models: `{entity_scan['unique_external_models']}`",
        f"- External model references: `{entity_scan['external_model_ref_count']}`",
        "",
        "## Entity Classes",
        "",
        "| Classname | Count | Maps | External Models |",
        "|---|---|---|---|",
    ]

    for classname, info in entity_scan["entities_by_class"].items():
        lines.append(
            f"| `{classname}` | `{info['count']}` | `{len(info['maps'])}` | `{len(info['external_models'])}` |"
        )

    lines.extend([
        "",
        "## Models",
        "",
        "| Model | Count | Maps | Classnames | Exists In Game |",
        "|---|---|---|---|---|",
    ])

    for model_name, info in entity_scan["models"].items():
        lines.append(
            f"| `{model_name}` | `{info['count']}` | `{len(info['maps'])}` | "
            f"`{', '.join(info['classnames'])}` | `{info['exists_in_game']}` |"
        )

    return "\n".join(lines)


def classify_material(material_name: str, shader: str) -> str:
    lower_name = material_name.lower()
    lower_shader = shader.lower()

    if lower_name.startswith("skybox/"):
        return "skybox"
    if lower_name.startswith(MAPPING_EXCLUDE_PREFIXES):
        if lower_name.startswith("models/"):
            return "model"
        if lower_name.startswith("vgui/"):
            return "ui"
        if lower_name.startswith("particles/"):
            return "particle"
        if lower_name.startswith("sprites/"):
            return "sprite"
        return "effect"
    if "decal" in lower_shader or "decal" in lower_name:
        return "decal"
    if "overlay" in lower_name:
        return "overlay"
    return "map"


def build_catalog(game_dir: Path | None = None) -> dict[str, object]:
    game_dir = game_dir or resolve_game_dir()
    material_root = game_dir / "materials"
    materials = sorted(material_root.rglob("*.vmt"))

    entries = [parse_vmt(path, material_root) for path in materials]
    group_counts = Counter(entry["group"] for entry in entries)
    usage_counts = Counter(entry["usage"] for entry in entries)

    grouped_entries: dict[str, list[dict[str, object]]] = defaultdict(list)
    for entry in entries:
        grouped_entries[str(entry["group"])].append(entry)

    for group in grouped_entries.values():
        group.sort(key=lambda entry: str(entry["material"]))

    return {
        "game_dir": str(game_dir),
        "material_root": str(material_root),
        "summary": {
            "total_materials": len(entries),
            "map_usable_materials": sum(1 for entry in entries if entry["map_usable"]),
            "groups": dict(sorted(group_counts.items())),
            "usage": dict(sorted(usage_counts.items())),
        },
        "materials": entries,
        "materials_by_group": dict(sorted(grouped_entries.items())),
    }


def catalog_to_markdown(catalog: dict[str, object]) -> str:
    summary = catalog["summary"]
    materials_by_group = catalog["materials_by_group"]

    lines = [
        "# Dystopia Texture Catalog",
        "",
        f"- Game dir: `{catalog['game_dir']}`",
        f"- Material root: `{catalog['material_root']}`",
        f"- Total materials: `{summary['total_materials']}`",
        f"- Map-usable materials: `{summary['map_usable_materials']}`",
        "",
        "## Usage Summary",
        "",
    ]

    for usage, count in summary["usage"].items():
        lines.append(f"- `{usage}`: `{count}`")

    vmf_usage = catalog.get("vmf_usage")
    if vmf_usage:
        lines.extend([
            "",
            "## VMF Usage",
            "",
            f"- VMF source dir: `{vmf_usage['vmf_dir']}`",
            f"- VMF files scanned: `{vmf_usage['vmf_count']}`",
            f"- Unique materials referenced by VMFs: `{vmf_usage['unique_used_materials']}`",
            f"- Catalog materials used by scanned VMFs: `{vmf_usage['catalog_materials_used']}`",
        ])
        if vmf_usage["missing_materials"]:
            lines.append(f"- Referenced materials missing from this install: `{len(vmf_usage['missing_materials'])}`")

    lines.extend([
        "",
        "## Notes",
        "",
        "- `map` is a default mapping-friendly bucket.",
        "- `skybox` materials are usable for sky brushes.",
        "- `decal` and `overlay` are often useful in detailing passes.",
        "- `ui`, `model`, `particle`, `sprite`, and `effect` entries are cataloged for completeness but are usually not brush-face textures.",
        "",
        "## Materials By Group",
        "",
    ])

    for group_name, group_entries in materials_by_group.items():
        lines.append(f"### `{group_name}`")
        lines.append("")
        lines.append("| Material | Shader | Surface | Usage | Used In Maps | Base Texture |")
        lines.append("|---|---|---|---|---|---|")
        for entry in group_entries:
            lines.append(
                "| "
                f"`{entry['material']}` | "
                f"`{entry['shader']}` | "
                f"`{entry['surfaceprop'] or '-'}` | "
                f"`{entry['usage']}` | "
                f"`{entry.get('used_in_map_count', 0)}` | "
                f"`{entry['basetexture'] or '-'}` |"
            )
        lines.append("")

    return "\n".join(lines)


def write_catalog_outputs(
    game_dir: Path | None = None,
    output_dir: Path | None = None,
    vmf_dir: Path | None = None,
    file_prefix: str = "texture_catalog",
) -> tuple[Path, Path]:
    catalog = build_catalog(game_dir)
    if vmf_dir is not None:
        usage_scan = scan_vmf_material_usage(vmf_dir)
        catalog = enrich_catalog_with_vmf_usage(catalog, usage_scan)
    if output_dir is None:
        output_dir = Path(__file__).resolve().parents[1] / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / f"{file_prefix}.json"
    md_path = output_dir / f"{file_prefix}.md"

    json_path.write_text(json.dumps(catalog, indent=2), encoding="utf-8")
    md_path.write_text(catalog_to_markdown(catalog), encoding="utf-8")
    return json_path, md_path
