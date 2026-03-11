#!/usr/bin/env python3
"""
Prepare LLM request for map layout generation.

Reads prompts/city_layout_system.txt and city_layout_schema.json, then writes
output/llm_layout_request.md with the full system prompt, schema, and catalog
paths. You run the LLM yourself (e.g. in Cursor with this file and the catalogs
attached), then save the model output as output/layout.json and run the
generator with --layout-json or --use-llm-layout.

Build chain (LLM layout):
  1. Run: python prepare_llm_request.py
  2. Open output/llm_layout_request.md (and attach output/*.json catalogs in Cursor)
  3. Run the LLM; save response as output/layout.json
  4. From maps folder: run_generator.bat --use-llm-layout [--compile]

Fallback (static map): run run_generator.bat without --layout-json and without
--use-llm-layout (or with --use-llm-layout when output/layout.json is missing)
to build the hardcoded MVP arena.
"""
from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    prompt_path = root / "prompts" / "city_layout_system.txt"
    schema_path = root / "city_layout_schema.json"
    out_dir = root / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "llm_layout_request.md"

    system_prompt = prompt_path.read_text(encoding="utf-8")
    schema_text = schema_path.read_text(encoding="utf-8")

    catalog_paths = [
        "output/texture_catalog_mapsrc_enriched.json",
        "output/used_entities_models_mapsrc.json",
        "output/used_textures_mapsrc.json",
    ]

    sections = [
        "# Dystopia city layout – LLM request",
        "",
        "Respond with **only** valid JSON matching the schema below. No commentary, no markdown fences.",
        "",
        "---",
        "",
        "## System prompt",
        "",
        "```",
        system_prompt.strip(),
        "```",
        "",
        "---",
        "",
        "## Schema (city_layout_schema.json)",
        "",
        "```json",
        schema_text.strip(),
        "```",
        "",
        "---",
        "",
        "## Context files",
        "",
        "Use only materials, entities, and props from these catalog files (relative to dystopia_citygen):",
        "",
    ]
    for p in catalog_paths:
        sections.append(f"- `{p}`")
    sections.extend([
        "",
        "Attach or reference these when calling the LLM so it can constrain outputs to the catalog.",
        "",
    ])

    out_path.write_text("\n".join(sections), encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
