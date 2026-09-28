import json
import sys
import time

import tools
from csg import Level
from vmflib import VMF, Tex, SKYBOX

NAME = "dys_bi_csgtest"

STYLE = {
    "room_a": {"floor": "vaccinert/dys_vaccorpfloor3", "wall": "vaccinert/dys_cleanwall2", "ceil": "vaccinert/dys_vaccorpfloor1"},
    "room_b": {"floor": "concrete/concretefloor008a", "wall": "metal/metalwall003a", "ceil": "metal/metalceiling005a"},
    "yard": {"floor": "concrete/concretefloor011a", "wall": "vaccinert/dys_vacextwall1", "ceil": SKYBOX},
}


def resolver(solid, air, d, box):
    st = STYLE.get(air.style)
    if not st:
        return None
    if solid.style == "sky":
        return SKYBOX
    if d == "top":
        return st["floor"]
    if d == "bottom":
        return st["ceil"]
    return st["wall"]


def build():
    L = Level()
    # hull / ground mass
    L.solid(-1024, -1024, -64, 1024, 1024, 640, "rock")
    L.solid(-1024, -1024, 512, 1024, 1024, 640, "sky")
    # rooms
    L.air(-768, -512, 0, -64, 512, 256, "room_a")
    L.air(64, -512, 0, 768, 0, 192, "room_b")
    # doorway a->b through the wall x -64..64
    L.air(-64, -256, 0, 64, -128, 128, "room_b")
    # courtyard open to the sky, reached from room_a through a door
    L.air(64, 64, 0, 768, 768, 512, "yard")
    L.air(-64, 256, 0, 64, 384, 128, "room_a")
    # window from room_b to yard
    L.air(256, 0, 64, 512, 64, 160, "room_b")
    leaks = L.check_leaks()
    print("leaks:", [(o.style, d, r) for o, d, r in leaks][:5])
    t = time.time()
    solids, faces = L.build(resolver)
    print(f"built {len(solids)} brushes, {len(faces)} faces in {time.time()-t:.2f}s")
    m = VMF(skyname="dys_cloudysky")
    m.add(solids)
    m.ent("light", (-400, 0, 200), _light="255 230 200 300")
    m.ent("light", (400, -256, 150), _light="120 180 255 250")
    m.ent("light_environment", (400, 400, 300), angles="-50 30 0", pitch="-50", _light="120 140 190 180", _ambient="40 45 70 60")
    m.ent("info_player_start", (-400, 0, 16), angles="0 0 0")
    m.ent("dys_spawn", (-400, 0, 16), team="2", spawnid="1", spawnflags="1", spawnname="A")
    m.ent("dys_spawn_point", (-400, 0, 8), spawnid="1")
    m.ent("dys_spawn", (400, -300, 16), team="3", spawnid="2", spawnflags="1", spawnname="B")
    m.ent("dys_spawn_point", (400, -300, 8), spawnid="2")
    (tools.MAPS / f"{NAME}.vmf").write_text(m.text(), encoding="utf-8")


if __name__ == "__main__":
    build()
    r = tools.compile_map(NAME, vis="fast", rad="fast")
    print(json.dumps({k: v for k, v in r.items() if k != "log"}, indent=1))
    if not r["ok"]:
        print(r.get("log", ""))
        sys.exit(1)
