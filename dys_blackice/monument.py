"""Kuroda monument: the custom static prop in the centre of the Kuroda Plaza court, plus its lights.

build()        textures (Pillow -> vtex), Blender headless (geometry, SMDs, QC), studiomdl. Raises on failure.
pack_pairs()   (internal path, disk path) for every file the BSP must carry.
place(m, ...)  prop_static + red emblem glow, cool uplights on the shaft, cyan spill from the crystals.
Sources and rebuild notes: monument/README.md.
"""
from __future__ import annotations

import importlib.util
import json
import math
import re
import subprocess
import sys
from pathlib import Path

import assets
import kit
from vmflib import VMF

SRC = Path(__file__).resolve().parent
DIR = SRC / "monument"
BUILD = SRC / "build" / "monument"
GAME = assets.ROOT / "dystopia"
BLENDER = Path(r"C:\Program Files\Blender Foundation\Blender 5.2\blender.exe")
STUDIOMDL = Path(r"M:\SteamLibrary\steamapps\common\Source SDK Base 2013 Multiplayer\bin\studiomdl.exe")

MODEL = "models/blackice/kuroda_monument.mdl"
MODEL_EXT = (".mdl", ".vvd", ".dx80.vtx", ".dx90.vtx", ".sw.vtx", ".phy")
MATERIALS = ("kuroda_metal.vmt", "kuroda_metal.vtf", "kuroda_metal_n.vtf", "kuroda_ice.vmt", "kuroda_ice.vtf",
             "kuroda_ice_n.vtf", "kuroda_neon.vmt", "kuroda_neon.vtf")
RED, CYAN, COOL = (255, 60, 70), (90, 220, 255), (150, 210, 255)
EMBLEM_Z = 326                                  # emblem centre above the base (model units)
PUCKS, PUCK_R = (30, 90, 150, 210, 270, 330), 86  # uplight pucks on the pedestal corners
CRYSTALS = (30, 150, 210, 330)                  # crystal clusters at the plinth corners


def _textures():
    spec = importlib.util.spec_from_file_location("monument_textures", DIR / "textures.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _run(cmd, log: Path, **kw):
    p = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)
    log.write_text(p.stdout + p.stderr, encoding="utf-8")
    return p.returncode, p.stdout + p.stderr


def build(previews=False) -> list[Path]:
    """Regenerate everything and compile the model. previews=True also renders build/monument_preview_*.png."""
    _textures().build()
    BUILD.mkdir(parents=True, exist_ok=True)
    qc = DIR / "kuroda_monument.qc"
    code, out = _run([BLENDER, "--background", "--factory-startup", "--python", DIR / "build_monument.py", "--",
                      "--out", BUILD, "--qc", qc] + (["--preview", SRC / "build"] if previews else []),
                     BUILD / "blender.log", timeout=900)
    info = next((json.loads(l[14:]) for l in out.splitlines() if l.startswith("MONUMENT_INFO ")), None)
    if code or info is None:
        raise RuntimeError(f"Blender build failed, see {BUILD / 'blender.log'}\n{out[-1500:]}")
    for ext in MODEL_EXT:                       # never let stale output pass the checks below
        (GAME / (MODEL[:-4] + ext)).unlink(missing_ok=True)
    code, log = _run([STUDIOMDL, "-game", GAME, "-nop4", qc], BUILD / "studiomdl.log", timeout=600, cwd=DIR)
    bad = [l for l in log.splitlines() if re.search(r"(?i)error|warning", l)]
    if code or "Completed" not in log or bad:
        raise RuntimeError(f"studiomdl failed, see {BUILD / 'studiomdl.log'}\n" + "\n".join(bad[:20] or [log[-1500:]]))
    assets.mdl_info.cache_clear()
    mi = assets.mdl_info(MODEL)
    if not mi or not mi["static_ok"]:
        raise RuntimeError(f"{MODEL}: bad header or not a static prop: {mi}")
    files = [d for _, d in pack_pairs()]
    missing = [f for f in files if not f.exists()]
    if missing:
        raise RuntimeError(f"missing outputs: {missing}")
    print(f"monument: {info['tris']} tris, {info['pieces']} collision pieces, materials {info['materials']}, "
          f"hull {mi['hull_min']} .. {mi['hull_max']}")
    return files + [Path(f) for f in info.get("previews", [])]


def pack_pairs() -> list[tuple[str, Path]]:
    """Model + material files the BSP pak must carry."""
    stem = MODEL[:-4]
    pairs = [(stem + ext, GAME / (stem + ext)) for ext in MODEL_EXT]
    return pairs + [(f"materials/models/blackice/{n}", GAME / "materials" / "models" / "blackice" / n) for n in MATERIALS]


def place(m: VMF, x, y, z, yaw=0):
    """Monument with its base centre at (x, y, z) on the floor; at yaw 0 the emblem faces west and east."""
    kit.prop(m, MODEL, x, y, z, yaw=yaw, solid=6, on_floor=False)

    def at(r, az, dz):
        a = math.radians(az + yaw)
        return x + r * math.cos(a), y + r * math.sin(a), z + dz

    for side in (180, 0):                       # red glow in front of / behind the ring (the diamond blocks a centred light)
        kit.light(m, *at(40, side, EMBLEM_Z), color=RED, bright=140, fifty=200, hundred=800)
        kit.sprite(m, *at(18, side, EMBLEM_Z), color=RED, scale=0.5, alpha=60)
    for az in PUCKS:                            # uplights from the pucks, each washing one shaft face (pitch > 0 = up)
        kit.spot(m, *at(PUCK_R, az, 72), pitch=78, yaw=(az + yaw + 180) % 360, color=COOL, bright=160, inner=22, outer=40)
    for az in CRYSTALS:                         # cyan spill from the black-ice crystals onto the court floor
        kit.light(m, *at(150, az, 28), color=CYAN, bright=40, fifty=64, hundred=240)


if __name__ == "__main__":
    for f in build(previews="--previews" in sys.argv):
        print(f)
