#!/usr/bin/env python3
"""
Compile an existing VMF with the local Source SDK tools.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

src = Path(__file__).resolve().parent / "src"
sys.path.insert(0, str(src))

from compile_tools import compile_map


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compile a Dystopia VMF map.")
    parser.add_argument(
        "vmf_path",
        nargs="?",
        default="dys_ai.vmf",
        help="Path to the VMF file to compile. Defaults to dys_ai.vmf in the current directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return compile_map(args.vmf_path)


if __name__ == "__main__":
    sys.exit(main())
