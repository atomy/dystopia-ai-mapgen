"""Release QA + packaging for dys_blackice.

python release.py qa       -> clean-client test (loose custom files hidden, pak only)
python release.py shots    -> beauty screenshots (1920x1080, no HUD)
python release.py loading  -> rebuild loading screen from the best beauty shot and repack
python release.py zip      -> build/release/dys_blackice_v<VERSION>.zip (+ source zip)
"""
from __future__ import annotations

import re
import shutil
import sys
import time
import zipfile
from pathlib import Path

import extras
import tools

NAME = "dys_blackice"
VERSION = "1.2"
LOOSE = [tools.GAME / "materials" / "blackice", *(tools.GAME / "materials" / "overviews").glob(f"{NAME}_*"),
         tools.GAME / "materials" / "loading" / f"{NAME}.vtf", tools.GAME / "models" / "blackice",
         tools.GAME / "materials" / "models" / "blackice"]
HIDE = tools.BUILD / "hidden_loose"


def hide_loose():
    HIDE.mkdir(parents=True, exist_ok=True)
    moved = []
    for p in LOOSE:
        if p.exists():
            dst = HIDE / p.relative_to(tools.GAME).as_posix().replace("/", "__")    # unique: several are "blackice"
            if dst.exists():
                shutil.rmtree(dst) if dst.is_dir() else dst.unlink()
            shutil.move(str(p), str(dst))
            moved.append((dst, p))
    return moved


def restore_loose(moved):
    for dst, orig in moved:
        if dst.exists() and not orig.exists():
            shutil.move(str(dst), str(orig))


def qa():
    moved = hide_loose()
    try:
        shots = []
        with tools.GameSession(NAME, width=1600, height=900) as g:
            g.cmd("sv_cheats 1", "developer 1", "mp_instantspawn 1", "jointeam 2", "setclass 1", "joinimplant 2", sleep=6.0)
            g.cmd("kill", sleep=4.0)
            g.cmd("r_drawvgui 1", "cl_drawhud 1", sleep=1.0)
            # custom textures from the pak: tower banner + logos
            g.cmd("setpos -1500 0 200", "setang -15 0 0", sleep=2.5)
            shots.append(g.shot("qa_tower"))
            # meatspace gate screen (north guard post, north wall)
            g.cmd("setpos 288 560 57", "setang 5 90 0", sleep=2.5)
            shots.append(g.shot("qa_gate_screen"))
            # jack in at the metro: lands on the Punk entry pad in the cyberspace hall
            g.cmd("setpos -5376 474 -327", "setang 5 90 0", sleep=1.5)
            g.cmd("+use", sleep=2.5)
            g.cmd("-use", sleep=4.0)
            shots.append(g.shot("qa_cyber_entry"))
            log = g.log()
    finally:
        restore_loose(moved)
    bad = [l for l in log.splitlines() if re.search(r"(?i)missing|not found|couldn't|can't find|error|unknown entity|failed", l)
           and not re.search(r"(?i)shader|metamod|textwindow|DiscordRP|combo", l)]
    return shots, bad, log


def logic():
    """Replay the objective chain with I/O logging; check the maintenance-door gating."""
    with tools.GameSession(NAME, width=1280, height=720) as g:
        g.cmd("sv_cheats 1", "developer 2", "mp_instantspawn 1", "jointeam 2", sleep=5.0)
        g.cmd("echo QA_MAINT_EARLY", "ent_fire maint_open Trigger", sleep=2.0)
        g.cmd("echo QA_GATE", "ent_fire gate_fp TestActivator", sleep=64.0)     # 60 s override
        g.cmd("echo QA_HUB", "ent_fire hub_done Trigger", sleep=3.0)
        g.cmd("echo QA_MAINT_LATE", "ent_fire maint_open Trigger", sleep=2.0)
        g.cmd("echo QA_SHIELD", "ent_fire shield_down Trigger", sleep=2.0)
        g.cmd("echo QA_CORE", "ent_fire core RemoveHealth 99999", sleep=5.0)
        log = g.log()
    early = log.split("QA_MAINT_EARLY")[1].split("QA_GATE")[0]
    late = log.split("QA_MAINT_LATE")[1].split("QA_SHIELD")[0]
    checks = {
        "maint door stays shut before hub": "maint_door.Open" not in early,
        "maint door opens after hub": "maint_door.Open" in late,
        "obj1 captured": "Objective 1 captured" in log,
        "obj2 captured": "Objective 2 captured" in log,
        "punks win on core": "Final objective 3 completed by team 2" in log,
        "vault spawn enabled by hub": "spawn_corp_vault.Enable" in log,
    }
    return checks, log


BEAUTY = [
    ("hero_street", -3380, -60, 150, -14, 2),
    ("hero_plaza", -800, -260, 30, -18, 30),
    ("hero_monument", -760, -120, 10, -20, 18),
    ("hero_tower_low", -300, -520, 40, -35, 12),
    ("hero_metro", -5980, 430, -300, 2, -18),
    ("hero_lobby", 640, -700, 250, 12, 40),
    ("hero_servers", 2600, -300, 40, 3, 10),
    ("hero_vault", 4480, -470, 40, 22, 145),
    ("hero_cyber", 1500, 3700, 520, 16, 150),
    ("hero_alley", -1760, 1150, 330, 14, 185),
    ("hero_arcade", -2270, 470, 160, 12, 30),
]


def shots():
    paths, log = tools.tour(NAME, BEAUTY, width=1920, height=1080, prefix=f"{NAME}_beauty", settle=2.0)
    return paths


def loading(src=None):
    src = src or tools.BUILD / "release" / "screenshots" / f"{NAME}_beauty_hero_street.jpg"
    if not src.exists():
        src = tools.SHOTS / f"{NAME}_beauty_hero_street.jpg"
    pairs = extras.loading_screen(src)
    return tools.pack(NAME, pairs)


def make_zip():
    out = tools.BUILD / "release"
    out.mkdir(parents=True, exist_ok=True)
    z = out / f"{NAME}_v{VERSION}.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(tools.MAPS / f"{NAME}.bsp", f"maps/{NAME}.bsp")
        zf.write(tools.SRC / "README_release.txt", f"{NAME}_readme.txt")
    zs = out / f"{NAME}_v{VERSION}_source.zip"
    with zipfile.ZipFile(zs, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(tools.MAPS / f"{NAME}.vmf", f"mapsrc/{NAME}.vmf")
        for p in sorted(tools.SRC.glob("*.py")) + [tools.SRC / "PLAN.md", tools.SRC / "README_release.txt"]:
            zf.write(p, f"generator/{p.name}")
        for p in sorted((tools.SRC / "monument").glob("*.*")):
            if p.suffix in (".py", ".qc", ".md"):
                zf.write(p, f"generator/monument/{p.name}")
        for sub in ("blackice", "models/blackice"):
            for p in sorted((tools.GAME / "materialsrc" / sub).glob("*")):
                zf.write(p, f"materialsrc/{sub}/{p.name}")
    return z, zs


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "qa"
    if cmd == "qa":
        s, bad, log = qa()
        (tools.BUILD / "qa_console.log").write_text(log, encoding="utf-8")
        print("shots:", [str(p) for p in s])
        print("suspicious console lines:", len(bad))
        for l in bad[:40]:
            print("  |", l[:200])
    elif cmd == "logic":
        checks, log = logic()
        (tools.BUILD / "qa_logic.log").write_text(log, encoding="utf-8")
        for k, v in checks.items():
            print(f"{'PASS' if v else 'FAIL'}  {k}")
    elif cmd == "shots":
        print(shots())
    elif cmd == "loading":
        print(loading())
    elif cmd == "zip":
        print(make_zip())
