"""dys_blackice — map definition.

Punks attack west->east:  Metro (HQ) -> Market street -> Kuroda Plaza [obj1 gate]
-> Tower lobby [obj2 security hub] -> Server hall -> Core vault [obj3 core, final].
Cyberspace lives in a separate sealed region north of the city (y > 3000).
"""
from __future__ import annotations

import json
import math
import sys
import time

import assets
import custom_art
import cyberspace
import dress
import dress_in
import dress_polish
import extras
import gameplay
import look
import kit
import panels
import sky3d
import tools
import validate
from csg import Level
from vmflib import VMF, Tex, box, SKYBOX, NODRAW, BLACK, PLAYERCLIP

NAME = "dys_blackice"
TEST_BUILD = "--test" in sys.argv

PUNKS, CORPS = 2, 3

# ----------------------------------------------------------------------------- map


class BlackIce:
    def __init__(self):
        self.L = Level(cell=512)
        self.m = VMF(skyname="exosky_01", detailvbsp="detail.vbsp", detailmaterial="detail/detailsprites",
                     message="Black ICE", maxpropscreenwidth="-1")

    # -- shorthands
    def air(self, x0, y0, z0, x1, y1, z1, style, **tags):
        return self.L.air(x0, y0, z0, x1, y1, z1, style, **tags)

    def solid(self, x0, y0, z0, x1, y1, z1, style, **tags):
        return self.L.solid(x0, y0, z0, x1, y1, z1, style, **tags)

    # ------------------------------------------------------------------ shell
    def shell(self):
        S, A = self.solid, self.air
        # world mass + sky lid for the city
        S(-6400, -1792, -768, 5376, 1792, 1408, "rock")
        S(-6400, -1792, 1280, 5376, 1792, 1408, "sky")
        # building masses that face outdoor areas get facade textures (one style per block)
        for (x0, x1, st) in [(-3968, -3456, "bld_dark"), (-3456, -2944, "bld_brick"), (-2944, -2432, "bld_cement"),
                             (-2432, -1664, "bld_rust")]:
            S(x0, 320, 0, x1, 960, 1280, st)                 # market north blocks
        for (x0, x1, st) in [(-3968, -3456, "bld_dark"), (-3456, -3072, "bld_grid"), (-3072, -2560, "bld_brick"),
                             (-2560, -2048, "bld_cement"), (-2048, -1664, "bld_rust")]:
            S(x0, -960, 0, x1, -320, 1280, st)               # market south blocks
        S(-3968, 1216, 0, -1664, 1792, 1280, "bld_grid")     # beyond north alley
        S(-3968, -1792, 0, -1664, -1216, 1280, "bld_cement") # beyond south alley
        S(-1664, 1216, 0, 448, 1792, 1280, "bld_grid")       # plaza north office block
        S(-1664, -1792, 0, 448, -1216, 1280, "bld_cement")   # plaza south block
        S(448, -1792, 0, 5376, 1792, 1280, "tower")          # Kuroda tower + annex

        # ---------------- Zone A: metro station (Punk HQ), platform z=-384
        A(-6016, -256, -384, -4480, 512, -64, "metro")          # platform hall
        A(-6016, -640, -448, -4480, -256, -64, "metro_tracks")  # track bed (64 lower)
        A(-6272, -640, -448, -6016, -256, -192, "metro_tracks") # west tunnel mouth
        A(-4480, -640, -448, -4224, -256, -192, "metro_tracks") # east tunnel mouth
        # main stairwell up to street level (rises +x), 384 wide
        A(-4480, -192, -384, -3904, 192, 224, "metro_stair")
        # metro entrance kiosk at street level, opens onto the street
        A(-3904, -288, 0, -3456, 288, 320, "metro_stair")
        # maintenance tunnel: platform -> north -> up to the back alley
        A(-5120, 512, -384, -4992, 1152, -224, "maint")
        A(-5120, 1024, -384, -4544, 1152, -224, "maint")
        A(-4544, 1024, -384, -3968, 1152, 128, "maint")         # stair hall rising +x into the alley

        # ---------------- Zone B: market street (outdoor) z=0
        A(-3456, -320, 0, -1664, 320, 1280, "street")
        # skyline breaks: lower rooftops seen from the street
        A(-3456, 384, 640, -2560, 960, 1280, "roof")
        A(-2432, -960, 768, -1664, -384, 1280, "roof")
        # north alley + south alley
        A(-3968, 1024, 0, -1664, 1216, 1280, "alley")
        A(-3968, -1216, 0, -1664, -1024, 1280, "alley")
        # shops (north side)
        A(-3328, 320, 0, -2944, 704, 224, "shop")               # noodle bar
        A(-3136, 704, 0, -3008, 1024, 160, "shop")              # back passage to alley
        A(-2304, 384, 0, -1792, 896, 288, "arcade")             # Neon Arcade (punk fwd spawn)
        A(-2176, 320, 0, -1920, 384, 160, "arcade")             # arcade front door
        A(-1920, 896, 0, -1792, 1024, 160, "arcade")            # arcade back door to alley
        # shops (south side)
        A(-3072, -704, 0, -2560, -320, 224, "shop")             # electronics
        A(-2688, -1024, 0, -2560, -704, 160, "shop")            # back door to south alley
        # fire escape: alley -> rooftop walkway (z=320) at the alley's east end
        A(-2304, 960, 320, -1664, 1024, 1280, "roof")           # walkway strip on top of the north block edge
        A(-2304, 704, 320, -1664, 960, 1280, "roof")

        # ---------------- Zone C: Kuroda Plaza (outdoor)
        A(-1664, -1216, 0, 448, 1216, 1280, "plaza")
        A(-896, -448, -64, -128, 448, 0, "court")               # sunken court
        # guard posts (interiors) against the tower facade
        S(128, 384, 0, 448, 768, 256, "guardpost")
        S(128, -768, 0, 448, -384, 256, "guardpost")
        A(160, 416, 0, 416, 736, 192, "guard")                  # GP north interior
        A(128, 512, 0, 160, 640, 128, "guard")                  # GP north plaza door
        A(160, -736, 0, 416, -416, 192, "guard")                # GP south interior
        A(128, -640, 0, 160, -512, 128, "guard")                # GP south plaza door
        # corridors from guard posts through the tower wall into the lobby
        A(416, 560, 0, 576, 656, 128, "guard")
        A(416, -656, 0, 576, -560, 128, "guard")
        # tower setback: upper facade steps back to x=576 above the entrance storey
        A(448, -1216, 480, 576, 1216, 1280, "plaza")
        # guard post window slits (glass added in dressing)
        A(128, 432, 72, 160, 496, 144, "guard")
        A(128, 656, 72, 160, 720, 144, "guard")
        A(192, 384, 72, 384, 416, 144, "guard")
        A(128, -496, 72, 160, -432, 144, "guard")
        A(128, -720, 72, 160, -656, 144, "guard")
        A(192, -416, 72, 384, -384, 144, "guard")
        # the security gate opening (roller gate = obj1)
        A(448, -192, 0, 576, 192, 256, "lobby")

        # ---------------- Zone D: tower lobby (atrium) + upper floor
        A(576, -768, 0, 1856, 768, 448, "lobby")
        # mezzanine slabs (z 176..192), painted solid after the atrium air
        S(576, 480, 176, 1856, 768, 192, "slab")
        S(576, -768, 176, 1856, -480, 192, "slab")
        S(1600, -480, 176, 1856, 480, 192, "slab")
        # security hub (obj2), north of the upper floor
        A(1152, 800, 192, 1664, 1152, 400, "hub")
        A(1216, 768, 192, 1344, 800, 320, "hub")                # door 1
        A(1472, 768, 192, 1600, 800, 320, "hub")                # door 2
        # corps spawn (upper floor east of lobby)
        A(1888, -512, 192, 2432, 512, 448, "corpspawn")
        A(1856, -256, 192, 1888, -128, 320, "corpspawn")        # exit 1 to east mezz
        A(1856, 128, 192, 1888, 256, 320, "corpspawn")          # exit 2 to east mezz
        A(1920, 512, 192, 2048, 1024, 320, "corpspawn")         # corps corridor north
        A(1664, 896, 192, 2048, 1024, 320, "corpspawn")         # -> hub back door
        # ground floor service lobby behind blast doors
        A(1888, -512, 0, 2432, 512, 160, "service")
        A(1856, -128, 0, 1888, 128, 144, "service")             # blast door opening
        # maintenance flank: south mezz -> corridor -> down to server hall south side
        A(1216, -1024, 192, 1344, -768, 320, "maint")           # door off south mezz
        A(1216, -1152, 192, 2688, -1024, 320, "maint")          # corridor east
        A(2560, -1152, -128, 2688, -768, 320, "maint")          # shaft with stairs down (rises -y)

        # ---------------- Zone E: server hall (floor z=-128)
        A(2432, -192, -128, 2560, 192, 160, "service")          # stair from service lobby down to hall
        A(2560, -640, -128, 3712, 640, 192, "server")
        A(2560, -768, -128, 2688, -640, 32, "maint")            # maintenance door into hall (south wall)

        # ---------------- Zone F: core vault
        A(3744, -512, -384, 4512, 512, 320, "vault")
        A(3712, -448, -128, 3744, -320, 0, "vault")             # door S from server hall
        A(3712, 320, -128, 3744, 448, 0, "vault")               # door N from server hall
        # ring walkway at z=-128 around a central pit
        S(3744, -512, -144, 3904, -224, -128, "slab")      # south walkway (gap over the stairs)
        S(4064, -512, -144, 4512, -224, -128, "slab")
        S(3744, 224, -144, 4192, 512, -128, "slab")        # north walkway (gap over the stairs)
        S(4352, 224, -144, 4512, 512, -128, "slab")
        S(3744, -224, -144, 3904, 224, -128, "slab")
        S(4352, -224, -144, 4512, 224, -128, "slab")

        # ---------------- Zone G: corps final spawn
        A(4544, -384, -128, 5056, 384, 128, "corpspawn")
        A(4512, -320, -128, 4544, -192, 0, "corpspawn")
        A(4512, 192, -128, 4544, 320, 0, "corpspawn")

        # ---------------- cyberspace (separate sealed region)
        cyberspace.shell(self)
        # ---------------- 3D skybox room
        sky3d.shell(self)

    # ------------------------------------------------------------------ geometry details needed for grey-box play
    def details(self):
        m = self.m
        # metro main stairs: 384 rise over 576 run
        kit.stairs(m, -4480, -192, -384, -3904, 192, 0, "+x", step=16, mat="termireal1/t_trashfloor", riser="dys_nameless/concrete_004_blue")
        # maintenance: straight flight from the tunnel (-384) up into the north alley (0)
        kit.stairs(m, -4544, 1024, -384, -3968, 1152, 0, "+x", mat="metal/metalfloor_001e", riser="dys_fortress/tunnel_wall")
        # fire escape: alley (0) -> walkway (320) along the north block's back wall, rising -x
        kit.stairs(m, -2240, 1024, 0, -1728, 1120, 320, "-x", mat="metal/metalgrate011a", riser="metal/metalwall003a")
        m.detail(box(-2304, 1024, 304, -2240, 1120, 320, {"all": "metal/metalwall003a", "top": "metal/metalgrate011a"}))
        kit.rail(m, -2304, 1122, -1728, 1122, 0, h=40, mat="metal/metalwall003a")      # outer rail along the flight
        kit.rail(m, -2306, 1024, -2306, 1120, 304, h=40, mat="metal/metalwall003a")    # landing end rail
        kit.clip_box(m, -2310, 1120, 0, -1728, 1126, 400)
        # sunken court steps (plaza level 0 -> -64)
        kit.stairs(m, -896, -448, -64, -832, 448, 0, "-x", mat="stone/stonefloor011a", riser="concrete/concretewall060c")
        kit.stairs(m, -192, -448, -64, -128, 448, 0, "+x", mat="stone/stonefloor011a", riser="concrete/concretewall060c")
        # lobby stairs to mezzanines (0 -> 192)
        kit.stairs(m, 1152, 192, 0, 1280, 480, 192, "+y", mat="vaccinert/dys_vaccorpfloor3", riser="vaccinert/dys_vactrim2")
        kit.stairs(m, 1152, -480, 0, 1280, -192, 192, "-y", mat="vaccinert/dys_vaccorpfloor3", riser="vaccinert/dys_vactrim2")
        # service stair down into server hall (0 -> -128), descending +x
        kit.stairs(m, 2432, -192, -128, 2560, 192, 0, "-x", mat="metal/metalfloor003a")
        # maintenance shaft down to server hall level (192 -> -128), descending +y (rises -y)
        kit.stairs(m, 2560, -1152, -128, 2688, -768, 192, "-y", mat="metal/metalfloor003a")
        # vault: stairs from walkway (-128) down to floor (-384)
        kit.stairs(m, 3904, -512, -384, 4064, -224, -128, "-x", mat="metal/metalfloor003a")
        kit.stairs(m, 4192, 224, -384, 4352, 512, -128, "+x", mat="metal/metalfloor003a")

    # ------------------------------------------------------------------ build
    def build(self):
        self.shell()
        leaks = self.L.check_leaks()
        if leaks:
            for op, d, r in leaks[:20]:
                print("LEAK:", op.style, op.box, d, r)
            raise SystemExit("air touches the void")
        t = time.time()
        solids, faces = self.L.build(look.resolver, zcuts=look.zcuts)
        self.faces = faces
        print(f"shell: {len(solids)} brushes, {len(faces)} visible faces ({time.time() - t:.1f}s)")
        self.m.add(solids)
        self.details()
        dress.street(self)
        dress.plaza(self)
        self.gameplay_stub()
        gameplay.add_gameplay(self)
        cyberspace.add(self)
        dress_in.metro(self)
        dress_in.lobby(self)
        dress_in.server_vault(self)
        dress_polish.shops(self)
        dress_polish.alleys(self)
        dress_polish.tower_extras(self)
        print("skyline towers:", sky3d.add(self))
        print("cubemaps:", self.place_cubemaps())
        extras.place_soundscapes(self.m)
        if TEST_BUILD:
            # test-only helpers (never in release): force a decker loadout on the activator
            self.m.ent("dys_forceloadout", (-5200, 0, -300), targetname="test_deck", spawnflags="2", Class="1", Weapon="1")
            self.m.ent("dys_forceloadout", (-5200, 0, -280), targetname="test_deck_enh", spawnflags="1", Class="1", Weapon="1")
        return self

    def place_cubemaps(self):
        """One env_cubemap per room-sized air volume (+ a grid over big outdoor spaces)."""
        m, n = self.m, 0
        seen = []
        for op in self.L.ops:
            if op.kind != "air" or op.style in ("skyroom",):
                continue
            bx = op.box
            dx, dy, dz = bx.x1 - bx.x0, bx.y1 - bx.y0, bx.z1 - bx.z0
            if min(dx, dy) < 160 or dz < 96:
                continue
            outdoor = look.AIR.get(op.style, {}).get("outdoor", False)
            step = 768 if outdoor else 640
            nx, ny = max(1, round(dx / step)), max(1, round(dy / step))
            for i in range(nx):
                for j in range(ny):
                    x = bx.x0 + dx * (i + 0.5) / nx
                    y = bx.y0 + dy * (j + 0.5) / ny
                    z = bx.z0 + min(72, dz / 2)
                    if any(abs(x - px) < 200 and abs(y - py) < 200 and abs(z - pz) < 120 for px, py, pz in seen):
                        continue
                    lab = self.L.label_at(int(x), int(y), int(z))
                    if lab is None or lab.kind != "air":
                        continue
                    m.ent("env_cubemap", (round(x), round(y), round(z)), cubemapsize="0")
                    seen.append((x, y, z))
                    n += 1
        return n

    def gameplay_stub(self):
        m = self.m
        m.ent("light_environment", (-600, 0, 800), angles="-62 35 0", pitch="-62", SunSpreadAngle="10",
              _light="60 74 118 42", _ambient="20 24 44 34", _lightHDR="-1 -1 -1 1", _ambientHDR="-1 -1 -1 1",
              _lightscaleHDR="1", _AmbientScaleHDR="1")
        m.ent("env_fog_controller", (-600, 0, 900), targetname="fog_city", fogenable="1", fogblend="0",
              fogcolor="12 15 26", fogcolor2="24 20 38", fogdir="1 0 0", fogstart="700", fogend="5200",
              fogmaxdensity="0.72", foglerptime="0", farz="-1", spawnflags="1", use_angles="0", angles="0 0 0")

    def write(self):
        path = tools.MAPS / f"{NAME}.vmf"
        path.write_text(self.m.text(), encoding="utf-8")
        return path


def pack_list(b):
    """(internal path, disk path) pairs for everything the BSP must carry."""
    stage = tools.BUILD / "pak"
    hero = tools.BUILD / "release" / "screenshots" / "dys_blackice_beauty_hero_street.jpg"
    pairs = extras.all_pairs(b.L, hero)
    for f in panels.write_panels(NAME, gameplay.PANELS, stage):
        pairs.append((f.resolve().relative_to(stage.resolve()).as_posix(), f))
    for f in sorted(custom_art.MATDIR.glob("*.v[mt][tf]")):
        pairs.append((f"materials/blackice/{f.name}", f))
    return pairs


if __name__ == "__main__":
    t0 = time.time()
    b = BlackIce().build()
    b.write()
    print(f"generated in {time.time() - t0:.1f}s")
    if "--art" in sys.argv or not (custom_art.MATDIR / "kuroda_banner.vtf").exists():
        custom_art.build_all()
    pairs = pack_list(b)
    problems = validate.check(b.m, gameplay.PANELS, b.L)
    for p in problems:
        print("VALIDATE:", p)
    if "--compile" in sys.argv:
        final = "--final" in sys.argv
        r = tools.compile_map(NAME, vis="full" if final else "fast", rad="final" if final else "fast")
        print(json.dumps({k: v for k, v in r.items() if k != "log"}, indent=1))
        if not r["ok"]:
            print(r.get("log", ""))
            sys.exit(1)
        print("pack:", tools.pack(NAME, pairs))
