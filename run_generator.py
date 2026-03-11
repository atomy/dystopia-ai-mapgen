#!/usr/bin/env python3
"""
Entrypoint: generate map layout (LLM JSON or static MVP), export to VMF, and optionally compile.

Build chain (LLM layout):
  1. Run prepare_llm_request.py; open output/llm_layout_request.md and catalogs in Cursor.
  2. Run the LLM; save response as output/layout.json.
  3. Run this script with --use-llm-layout (or --layout-json path) from the maps folder.

Fallback (static map): run without --layout-json and without --use-llm-layout,
or with --use-llm-layout when output/layout.json is missing; uses hardcoded MVP arena.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

# Run from project root (dystopia_citygen)
script_dir = Path(__file__).resolve().parent
src = script_dir / "src"
sys.path.insert(0, str(src))

from generate_layout import generate_mvp_arena
from compile_tools import compile_map
from scene_to_vmf import scene_to_vmf
from layout_rules import scene_from_json_dict
from validate_map import validate_vmf_text, validate_writer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate the MVP Dystopia VMF.")
    parser.add_argument(
        "--compile",
        action="store_true",
        help="Run vbsp, vvis, and vrad after writing the VMF.",
    )
    parser.add_argument(
        "--map-name",
        default=None,
        help="Base map name to write, without the .vmf extension. Defaults to the scene map_name.",
    )
    parser.add_argument(
        "--layout-json",
        help="Optional path to a JSON layout matching city_layout_schema.json.",
    )
    parser.add_argument(
        "--use-llm-layout",
        action="store_true",
        help="Use output/layout.json from the project if it exists; otherwise fall back to static MVP.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    layout_path: Path | None = None
    if args.layout_json:
        layout_path = Path(args.layout_json)
    elif args.use_llm_layout:
        candidate = script_dir / "output" / "layout.json"
        if candidate.exists():
            layout_path = candidate

    if layout_path is not None:
        scene = scene_from_json_dict(json.loads(layout_path.read_text(encoding="utf-8")))
        if not args.map_name:
            args.map_name = scene.map_name
    else:
        scene = generate_mvp_arena()
    map_name = args.map_name or scene.map_name
    writer = scene_to_vmf(scene)

    errors = validate_writer(writer)
    if errors:
        for e in errors:
            print("Validation error:", e)
        return 1

    vmf_text = writer.write()
    errors = validate_vmf_text(vmf_text)
    if errors:
        for e in errors:
            print("VMF validation error:", e)
        return 1

    out_path = Path(os.getcwd()) / f"{map_name}.vmf"
    out_path.write_text(vmf_text, encoding="utf-8")
    print(f"Wrote {out_path}")

    if args.compile:
        return compile_map(out_path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
