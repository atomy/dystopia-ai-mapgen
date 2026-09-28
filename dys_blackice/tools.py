"""Compile + in-game automation for Dystopia maps.

compile_map(): Dystopia's own vbsp/vvis/vrad (bin/win32), leak detection, log capture.
run_game():    launches Dystopia windowed on a map, runs a console script, waits for
               it to quit, returns the new console.log text and any new screenshots.
               The user's cfg/config.cfg is backed up and restored around each run.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import time
from pathlib import Path

ROOT = Path(r"M:\SteamLibrary\steamapps\common\Dystopia")
GAME = ROOT / "dystopia"
BIN = ROOT / "bin" / "win32"
MAPS = GAME / "maps"
SDK_BIN = Path(r"M:\SteamLibrary\steamapps\common\Source SDK Base 2013 Multiplayer\bin")
SRC = Path(__file__).resolve().parent
BUILD = SRC / "build"
SHOTS = GAME / "screenshots"


def _run(cmd, log_path: Path, timeout=None, cwd=None, env=None):
    t0 = time.time()
    with open(log_path, "w", encoding="utf-8", errors="replace") as log:
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout, cwd=cwd, env=env)
        out = p.stdout.decode("utf-8", errors="replace")
        log.write(out)
    return p.returncode, out, time.time() - t0


def compile_map(name: str, vis: str | None = "fast", rad: str | None = "fast", rad_extra=(), threads=None) -> dict:
    """vis: None|'fast'|'full'; rad: None|'fast'|'normal'|'final'."""
    BUILD.mkdir(exist_ok=True)
    vmf = MAPS / f"{name}.vmf"
    stem = MAPS / name
    lin = MAPS / f"{name}.lin"
    if lin.exists():
        lin.unlink()
    res = {"name": name, "ok": False}
    code, out, dt = _run([str(BIN / "vbsp.exe"), "-game", str(GAME), str(vmf)], BUILD / f"{name}_vbsp.log")
    res["vbsp"] = (code, round(dt, 1))
    res["leak"] = lin.exists() or "LEAKED" in out
    res["vbsp_warnings"] = [l for l in out.splitlines() if re.search(r"(?i)error|warning|leak|overlapping|degenerate|can't|could not|missing", l)]
    if code != 0 or res["leak"]:
        res["log"] = out[-3000:]
        return res
    if vis:
        args = [str(BIN / "vvis.exe")] + (["-fast"] if vis == "fast" else []) + ["-game", str(GAME), str(stem)]
        code, out, dt = _run(args, BUILD / f"{name}_vvis.log")
        res["vvis"] = (code, round(dt, 1))
        if code != 0:
            res["log"] = out[-3000:]
            return res
    if rad:
        args = [str(BIN / "vrad.exe")]
        if rad == "fast":
            args += ["-fast", "-bounce", "2", "-noextra"]
        elif rad == "final":
            args += ["-both", "-final", "-StaticPropLighting", "-StaticPropPolys"]
        args += list(rad_extra) + ["-game", str(GAME), str(stem)]
        code, out, dt = _run(args, BUILD / f"{name}_vrad.log")
        res["vrad"] = (code, round(dt, 1))
        res["rad_warnings"] = [l for l in out.splitlines() if re.search(r"(?i)error|warning|too many|overflow|exceed", l)][:30]
        if code != 0:
            res["log"] = out[-3000:]
            return res
    res["ok"] = True
    res["bsp_size_mb"] = round((MAPS / f"{name}.bsp").stat().st_size / 1e6, 2)
    return res


def pack(name: str, pairs) -> dict:
    """Add files into the BSP pakfile (bspzip -addlist), keeping existing entries.
    pairs: iterable of (internal_path, disk_path)."""
    bsp = MAPS / f"{name}.bsp"
    lst = BUILD / f"{name}_pack.txt"
    lines = []
    pairs = list(pairs)
    for internal, disk in pairs:
        lines += [internal.replace("\\", "/"), str(Path(disk).resolve())]
    lst.write_text("\n".join(lines) + "\n", encoding="utf-8")
    env = dict(os.environ, VPROJECT=str(GAME))
    code, out, dt = _run([str(SDK_BIN / "bspzip.exe"), "-addlist", str(bsp), str(lst), str(bsp)],
                         BUILD / f"{name}_bspzip.log", env=env)
    return {"code": code, "files": len(pairs), "seconds": round(dt, 1), "tail": out[-400:] if code else ""}


def pak_list(name: str) -> list[str]:
    import io
    import struct
    import zipfile
    with open(MAPS / f"{name}.bsp", "rb") as f:
        hdr = f.read(1036)
        off, length, _, _ = struct.unpack("<iiii", hdr[8 + 40 * 16: 8 + 41 * 16])
        f.seek(off)
        data = f.read(length)
    return zipfile.ZipFile(io.BytesIO(data)).namelist()


# --------------------------------------------------------------------------- game

CONFIG_FILES = ["config.cfg"]


def _backup_cfg(tag):
    bdir = BUILD / "cfg_backup"
    bdir.mkdir(parents=True, exist_ok=True)
    for f in CONFIG_FILES:
        src = GAME / "cfg" / f
        if src.exists():
            shutil.copy2(src, bdir / f)
    return bdir


def _restore_cfg(bdir):
    changed = []
    for f in CONFIG_FILES:
        b = bdir / f
        dst = GAME / "cfg" / f
        if b.exists() and (not dst.exists() or dst.read_bytes() != b.read_bytes()):
            changed.append(f)
            shutil.copy2(b, dst)
    return changed


def game_running() -> bool:
    out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq dystopia.exe"], capture_output=True, text=True).stdout
    return "dystopia.exe" in out.lower()


def _log_tail(log_path: Path, start: int) -> str:
    if not log_path.exists():
        return ""
    with open(log_path, "rb") as f:
        f.seek(start)
        return f.read().decode("utf-8", errors="replace")


def hijack(commands: list[str]):
    """Send console commands to the running game (Source -hijack relay)."""
    args = [str(BIN / "dystopia.exe"), "-hijack", "-game", str(GAME)]
    for c in commands:
        parts = c.split(" ", 1)
        args += ["+" + parts[0]] + ([parts[1]] if len(parts) > 1 else [])
    subprocess.run(args, cwd=str(ROOT), timeout=60)


READY_MARKERS = ("Redownloading all lightmaps", "Soundscape:", " connected")


def run_game(mapname: str, script: list[str], timeout=240, width=1600, height=900, extra_args=(),
             ready_timeout=120, settle=4.0) -> dict:
    """Launch the game on `mapname`, wait until the client is in game (console.log),
    then inject `script` via -hijack (console commands, may contain 'wait N').
    The script should end in 'quit'. Returns log text + new screenshots."""
    assert not game_running(), "Dystopia is already running"
    cfg_name = "dbi_auto"
    cfg_path = GAME / "cfg" / f"{cfg_name}.cfg"
    cfg_path.write_text("\n".join(script) + "\n", encoding="utf-8")
    log_path = GAME / "console.log"
    start = log_path.stat().st_size if log_path.exists() else 0
    shots_before = set(os.listdir(SHOTS)) if SHOTS.exists() else set()
    bdir = _backup_cfg(mapname)
    args = [
        str(BIN / "dystopia.exe"), "-game", str(GAME), "-novid", "-windowed", "-noborder",
        "-w", str(width), "-h", str(height), "-condebug", "-insecure", "-nojoy", "-nosteamcontroller",
        *extra_args,
        "+sv_lan", "1", "+sv_cheats", "1", "+map", mapname,
    ]
    t0 = time.time()
    proc = subprocess.Popen(args, cwd=str(ROOT))
    ready = False
    while time.time() - t0 < ready_timeout and proc.poll() is None:
        time.sleep(1.0)
        tail = _log_tail(log_path, start)
        if f"{mapname}" in tail and any(m in tail for m in READY_MARKERS):
            ready = True
            break
    if ready:
        time.sleep(settle)
        hijack([f"exec {cfg_name}"])
    try:
        proc.wait(timeout=max(5, timeout - (time.time() - t0)))
        timed_out = False
    except subprocess.TimeoutExpired:
        proc.kill()
        timed_out = True
    dt = time.time() - t0
    time.sleep(1.0)
    changed = _restore_cfg(bdir)
    try:
        cfg_path.unlink()
    except OSError:
        pass
    text = _log_tail(log_path, start)
    shots_after = set(os.listdir(SHOTS)) if SHOTS.exists() else set()
    new_shots = sorted(SHOTS / s for s in (shots_after - shots_before))
    return {"seconds": round(dt, 1), "timed_out": timed_out, "ready": ready, "log": text,
            "shots": new_shots, "cfg_restored": changed}


class GameSession:
    """Interactive control of a running Dystopia instance via -hijack.

    with GameSession("dys_blackice") as g:
        g.cmd("hidepanel team", "spec_mode 6")
        g.view(0, 0, 128, 10, 90, "lobby")      # -> screenshots/lobby.jpg
    """

    def __init__(self, mapname, width=1600, height=900, extra_args=(), ready_timeout=150, settle=5.0):
        assert not game_running(), "Dystopia is already running"
        self.mapname = mapname
        self.log_path = GAME / "console.log"
        self.start = self.log_path.stat().st_size if self.log_path.exists() else 0
        self.bdir = _backup_cfg(mapname)
        args = [
            str(BIN / "dystopia.exe"), "-game", str(GAME), "-novid", "-windowed", "-noborder",
            "-w", str(width), "-h", str(height), "-condebug", "-insecure", "-nojoy", "-nosteamcontroller",
            *extra_args, "+sv_lan", "1", "+sv_cheats", "1", "+map", mapname,
        ]
        self.t0 = time.time()
        self.proc = subprocess.Popen(args, cwd=str(ROOT))
        self.ready = False
        while time.time() - self.t0 < ready_timeout and self.proc.poll() is None:
            time.sleep(1.0)
            tail = _log_tail(self.log_path, self.start)
            if mapname in tail and any(m in tail for m in READY_MARKERS):
                self.ready = True
                break
        if not self.ready:
            self.close()
            raise RuntimeError("game did not reach the map:\n" + _log_tail(self.log_path, self.start)[-3000:])
        time.sleep(settle)
        self.shots = []

    def cmd(self, *commands, sleep=0.6):
        # write to a cfg and exec it: the -hijack command line eats negative numbers
        self._n = getattr(self, "_n", 0) + 1
        name = f"dbi_c{self._n % 20}"
        (GAME / "cfg" / f"{name}.cfg").write_text("\n".join(commands) + "\n", encoding="utf-8")
        hijack([f"exec {name}"])
        time.sleep(sleep)

    def log(self):
        return _log_tail(self.log_path, self.start)

    def shot(self, name, wait_s=8.0):
        target = SHOTS / f"{name}.jpg"
        if target.exists():
            target.unlink()
        self.cmd(f"jpeg {name} 92", sleep=0.3)
        t = time.time()
        while time.time() - t < wait_s:
            if target.exists() and target.stat().st_size > 0:
                time.sleep(0.3)
                self.shots.append(target)
                return target
            time.sleep(0.2)
        return None

    def view(self, x, y, z, pitch, yaw, name, settle=1.2, spec=True):
        pre = ["spec_mode 6"] if spec else []
        self.cmd(*pre, f"setpos {x} {y} {z}", f"setang {pitch} {yaw} 0", sleep=settle)
        return self.shot(name)

    def close(self):
        if self.proc.poll() is None:
            try:
                self.cmd("r_drawviewmodel 1", "mat_hdr_level 0", "cl_spec_mode 5", sleep=0.5)
                hijack(["quit"])
                self.proc.wait(timeout=30)
            except Exception:
                self.proc.kill()
        time.sleep(1.0)
        self.restored = _restore_cfg(self.bdir)
        for i in range(20):
            try:
                (GAME / "cfg" / f"dbi_c{i}.cfg").unlink()
            except OSError:
                pass
        return self.log()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


def build_cubemaps(mapname, hdr=True, timeout=300):
    """Run buildcubemaps in-game (LDR, then HDR). Completion = the engine rewrites the BSP.
    Restores mat_hdr_level 0 (the user's setting) afterwards."""
    bsp = MAPS / f"{mapname}.bsp"

    def wait_for_write(t_before):
        t0 = time.time()
        while time.time() - t0 < timeout:
            if bsp.stat().st_mtime > t_before:
                size = -1
                while size != bsp.stat().st_size:       # wait until the write settles
                    size = bsp.stat().st_size
                    time.sleep(2.0)
                return True
            time.sleep(1.0)
        return False

    ok = []
    with GameSession(mapname, width=1280, height=720) as g:
        g.cmd("sv_cheats 1", "mat_specular 1", "mat_hdr_level 0", sleep=5.0)
        t_before = bsp.stat().st_mtime
        g.cmd("buildcubemaps", sleep=2.0)
        ok.append(wait_for_write(t_before))
        time.sleep(6.0)
        if hdr:
            g.cmd("mat_hdr_level 2", sleep=10.0)
            t_before = bsp.stat().st_mtime
            g.cmd("buildcubemaps", sleep=2.0)
            ok.append(wait_for_write(t_before))
            time.sleep(6.0)
            g.cmd("mat_hdr_level 0", sleep=5.0)
        log = g.log()
    return ok, log


def tour(mapname, views, width=1600, height=900, pre=(), prefix=None, vgui=False, settle=1.2):
    """views: list of (name, x, y, z, pitch, yaw). Spectator free-roam screenshots."""
    prefix = prefix or mapname
    paths = []
    with GameSession(mapname, width=width, height=height) as g:
        g.cmd("spec_mode 6", f"r_drawvgui {1 if vgui else 0}", "cl_drawhud 0",
              "mat_picmip 0", *pre, sleep=3.0)
        g.cmd("spec_mode 6", sleep=1.0)
        for (name, x, y, z, pitch, yaw) in views:
            p = g.view(x, y, z, pitch, yaw, f"{prefix}_{name}", settle=settle)
            paths.append(p)
        log = g.log()
    return paths, log


def shot_script(views, settle_frames=90, pre=(), hud=False):
    """views: list of (x, y, z, pitch, yaw) spectator/noclip camera poses."""
    lines = [
        "wait 300", "sv_cheats 1", "developer 0", "con_notifytime 0",
        f"cl_drawhud {1 if hud else 0}", "mat_picmip 0",
        *pre,
    ]
    for (x, y, z, pitch, yaw) in views:
        lines += [f"setpos {x} {y} {z}", f"setang {pitch} {yaw} 0", f"wait {settle_frames}", "jpeg", "wait 30"]
    lines += ["wait 60", "quit"]
    return lines


def getpos(g, tag):
    """Ask the game for the player's eye position; returns (x, y, z) or None."""
    g.cmd(f"echo DBI_POS_{tag}", "getpos", sleep=0.6)
    tail = g.log().split(f"DBI_POS_{tag}")[-1]
    m = re.search(r"setpos (-?[\d.]+) (-?[\d.]+) (-?[\d.]+)", tail)
    return tuple(float(v) for v in m.groups()) if m else None


def walk_tests(mapname, tests, team=2, pre=()):
    """tests: list of (name, (x, y, z_eye), yaw, seconds, expect_fn(start, end) -> bool).
    Spawns as a player, then for each test teleports, walks forward, and reports."""
    results = []
    with GameSession(mapname, width=1280, height=720) as g:
        g.cmd("sv_cheats 1", "mp_instantspawn 1", f"jointeam {team}", *pre, sleep=5.0)
        for (name, (x, y, z), yaw, secs, expect) in tests:
            g.cmd("-forward", f"setpos {x} {y} {z}", f"setang 0 {yaw} 0", sleep=1.0)
            p0 = getpos(g, name + "_a")
            g.cmd("+forward", sleep=secs)
            g.cmd("-forward", sleep=0.8)
            p1 = getpos(g, name + "_b")
            ok = bool(p0 and p1 and expect(p0, p1))
            results.append((name, ok, p0, p1))
    return results
