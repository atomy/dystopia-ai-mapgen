"""Phase-1 smoke test: sealed room + spawns -> compile -> in-game screenshot."""
import json
import sys

from vmflib import VMF, box, NODRAW
import tools

NAME = "dys_bi_smoke"


def build():
    m = VMF(skyname="dys_cloudysky", detailvbsp="detail.vbsp", detailmaterial="detail/detailsprites")
    x0, y0, z0, x1, y1, z1, t = -512, -512, 0, 512, 512, 384, 16
    floor, wall, ceil = "concrete/concretefloor008a", "metal/metalwall003a", "metal/metalceiling005a"
    m.add(box(x0 - t, y0 - t, z0 - t, x1 + t, y1 + t, z0, {"top": floor}))
    m.add(box(x0 - t, y0 - t, z1, x1 + t, y1 + t, z1 + t, {"bottom": ceil}))
    m.add(box(x0 - t, y0, z0, x0, y1, z1, {"east": wall}))
    m.add(box(x1, y0, z0, x1 + t, y1, z1, {"west": wall}))
    m.add(box(x0, y0 - t, z0, x1, y0, z1, {"north": wall}))
    m.add(box(x0, y1, z0, x1, y1 + t, z1, {"south": wall}))
    m.detail(box(-64, -64, 0, 64, 64, 48, "metal/metalwall003a"))
    m.ent("light", (0, 0, 300), _light="255 240 220 400", _lightHDR="-1 -1 -1 1", _lightscaleHDR="1")
    m.ent("light", (-300, 300, 200), _light="80 160 255 200")
    m.ent("light", (300, -300, 200), _light="255 80 160 200")
    m.ent("dys_spawn", (-400, 0, 16), team="2", spawnid="1", spawnname="Punk Test", spawnflags="1", targetname="sp_punk")
    m.ent("dys_spawn", (400, 0, 16), team="3", spawnid="2", spawnname="Corp Test", spawnflags="1", targetname="sp_corp")
    for i in range(4):
        m.ent("dys_spawn_point", (-400, -150 + i * 100, 8), spawnid="1", angles="0 0 0")
        m.ent("dys_spawn_point", (400, -150 + i * 100, 8), spawnid="2", angles="0 180 0")
    m.ent("info_player_start", (0, -300, 100), angles="0 90 0")
    m.ent("info_camera_start", (-480, -480, 300), angles="25 45 0")
    (tools.MAPS / f"{NAME}.vmf").write_text(m.text(), encoding="utf-8")


if __name__ == "__main__":
    build()
    r = tools.compile_map(NAME, vis="fast", rad="fast")
    print(json.dumps({k: v for k, v in r.items() if k != "log"}, indent=1))
    if not r["ok"]:
        print(r.get("log", ""))
        sys.exit(1)
