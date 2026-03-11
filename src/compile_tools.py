"""
Helpers for compiling Source/Dystopia maps from the generator tooling.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path


def _resolve_game_dir(vmf_path: Path) -> Path:
    env_value = os.environ.get("DYSTOPIA_GAME_DIR")
    if env_value:
        return Path(env_value)

    # Default to the workspace's sibling Dystopia game directory.
    return vmf_path.parent.parent


def _resolve_sdk_bin_dir(game_dir: Path) -> Path:
    env_value = os.environ.get("SOURCE_SDK_BIN_DIR")
    if env_value:
        return Path(env_value)

    default_bin = game_dir.parent.parent / "Source SDK Base 2013 Multiplayer" / "bin"
    return default_bin


def _run_stage(exe_path: Path, game_dir: Path, map_target: str) -> int:
    command = [str(exe_path), "-game", str(game_dir), map_target]
    print(f"Running: {' '.join(command)}", flush=True)
    completed = subprocess.run(command, check=False)
    return completed.returncode


def compile_map(vmf_path: str | Path) -> int:
    """
    Compile a VMF with vbsp, vvis, and vrad.

    Environment overrides:
    - DYSTOPIA_GAME_DIR
    - SOURCE_SDK_BIN_DIR
    """
    vmf_path = Path(vmf_path).resolve()
    game_dir = _resolve_game_dir(vmf_path)
    sdk_bin_dir = _resolve_sdk_bin_dir(game_dir)
    map_stem_path = vmf_path.with_suffix("")

    vbsp = sdk_bin_dir / "vbsp.exe"
    vvis = sdk_bin_dir / "vvis.exe"
    vrad = sdk_bin_dir / "vrad.exe"

    required_tools = [vbsp, vvis, vrad]
    missing = [str(tool) for tool in required_tools if not tool.exists()]
    if missing:
        for tool in missing:
            print(f"Missing compile tool: {tool}")
        print("Set SOURCE_SDK_BIN_DIR if your SDK bin path differs.")
        return 1

    if not game_dir.exists():
        print(f"Game directory does not exist: {game_dir}")
        print("Set DYSTOPIA_GAME_DIR if your game path differs.")
        return 1

    exit_code = _run_stage(vbsp, game_dir, str(vmf_path))
    if exit_code != 0:
        return exit_code

    exit_code = _run_stage(vvis, game_dir, str(map_stem_path))
    if exit_code != 0:
        return exit_code

    exit_code = _run_stage(vrad, game_dir, str(map_stem_path))
    return exit_code
