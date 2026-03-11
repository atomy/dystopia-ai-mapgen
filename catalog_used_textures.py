#!/usr/bin/env python3
"""
Scan a VMF source directory and enrich the material catalog with real usage data.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

src = Path(__file__).resolve().parent / "src"
sys.path.insert(0, str(src))

from catalog_textures import (
    entity_scan_to_markdown,
    normalize_entity_scan,
    scan_vmf_entities_and_models,
    scan_vmf_material_usage,
    usage_scan_to_markdown,
    write_catalog_outputs,
)


DEFAULT_VMF_DIR = Path("mapsrc")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Enrich the Dystopia material catalog with VMF usage.")
    parser.add_argument(
        "--vmf-dir",
        default=str(DEFAULT_VMF_DIR),
        help="Directory to recursively scan for .vmf files.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).resolve().parent / "output"),
        help="Directory where the enriched catalog outputs will be written.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    vmf_dir = Path(args.vmf_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    usage_scan = scan_vmf_material_usage(vmf_dir)
    entity_scan = normalize_entity_scan(scan_vmf_entities_and_models(vmf_dir))
    used_json_path = output_dir / "used_textures_mapsrc.json"
    used_md_path = output_dir / "used_textures_mapsrc.md"
    entity_json_path = output_dir / "used_entities_models_mapsrc.json"
    entity_md_path = output_dir / "used_entities_models_mapsrc.md"
    used_json_path.write_text(json.dumps(usage_scan, indent=2), encoding="utf-8")
    used_md_path.write_text(usage_scan_to_markdown(usage_scan), encoding="utf-8")
    entity_json_path.write_text(json.dumps(entity_scan, indent=2), encoding="utf-8")
    entity_md_path.write_text(entity_scan_to_markdown(entity_scan), encoding="utf-8")

    json_path, md_path = write_catalog_outputs(
        output_dir=output_dir,
        vmf_dir=vmf_dir,
        file_prefix="texture_catalog_mapsrc_enriched",
    )

    print(f"Scanned {usage_scan['vmf_count']} VMF files from {vmf_dir}")
    print(f"Found {usage_scan['unique_material_count']} unique referenced materials")
    print(f"Found {entity_scan['unique_entity_classes']} unique entity classes")
    print(f"Found {entity_scan['unique_external_models']} unique external models")
    print(f"Wrote {used_json_path}")
    print(f"Wrote {used_md_path}")
    print(f"Wrote {entity_json_path}")
    print(f"Wrote {entity_md_path}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
