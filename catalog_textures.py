#!/usr/bin/env python3
"""
Scan Dystopia materials and write a JSON + Markdown catalog for mapping.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

src = Path(__file__).resolve().parent / "src"
sys.path.insert(0, str(src))

from catalog_textures import write_catalog_outputs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Catalog Dystopia materials for map editing.")
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).resolve().parent / "output"),
        help="Directory where texture_catalog.json and texture_catalog.md will be written.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    json_path, md_path = write_catalog_outputs(output_dir=Path(args.output_dir))
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
