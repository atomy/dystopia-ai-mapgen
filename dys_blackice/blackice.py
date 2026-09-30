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
TUNNEL_W, TUNNEL_E = -7680, -2944       # far ends of the metro tunnels (x)
STEP = 8                                # stair risers: 8u on 16u treads (1:2) everywhere

PUNKS, CORPS = 2, 3

# ----------------------------------------------------------------------------- map


class BlackIce:
    TUNNEL_W, TUNNEL_E = TUNNEL_W, TUNNEL_E

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
        # recessed niches for the roller shutters (shutter panel sits at the back)
        for (cx, fy, fac, w, mat) in dress.SHUTTERS:
            back = fy + (dress.NICHE if fac == "-y" else -dress.NICHE)   # into the building
            A(cx - w // 2 - 8, min(fy, back), 0, cx + w // 2 + 8, max(fy, back), 160, "niche")
        S(-3968, 1216, 0, -1664, 1792, 1280, "bld_grid")     # beyond north alley
        S(-3968, -1792, 0, -1664, -1216, 1280, "bld_cement") # beyond south alley
        S(-1664, 1216, 0, 448, 1792, 1280, "bld_grid")       # plaza north office block
        S(-1664, -1792, 0, 448, -1216, 1280, "bld_cement")   # plaza south block
        S(448, -1792, 0, 5376, 1792, 1280, "tower")          # Kuroda tower + annex

        # ---------------- Zone A: metro station (Punk HQ), platform z=-384
        A(-6016, -256, -384, -4480, 512, -64, "metro")          # platform hall
        A(-6016, -640, -448, -4480, -256, -64, "metro_tracks")  # track bed (64 lower)
        # the line runs on into long dark tunnels both ways (forcefields keep players out)
        S(TUNNEL_W - 256, -896, -704, -6400, 0, 0, "rock")      # rock around the west tunnel, beyond the city block
        A(TUNNEL_W, -640, -448, -6016, -256, -192, "metro_tunnel")
        A(-4480, -640, -448, TUNNEL_E, -256, -192, "metro_tunnel")
        # main stairwell up to street level (short landing, then rises +x into the kiosk), 384 wide
        A(-4480, -192, -384, -3680, 192, 224, "metro_stair")
        # metro entrance kiosk at street level, opens onto the street
        A(-3904, -288, 0, -3456, 288, 320, "metro_stair")
        # maintenance tunnel: platform -> north -> up to the back alley
        A(-5120, 512, -384, -4992, 1152, -224, "maint")
        A(-5120, 1024, -384, -4736, 1152, -224, "maint")
        A(-4736, 1024, -384, -3968, 1152, 128, "maint")         # stair hall rising +x into the alley

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
        # two-storey annexes narrow the middle of the plaza (fewer long sight lines)
        S(-1216, 928, 0, -320, 1216, 448, "bld_grid")
        S(-1216, -1216, 0, -320, -928, 448, "bld_cement")
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
        A(1920, -1152, -128, 2688, -1024, 320, "maint")         # corridor stairs down (descending +x)
        A(2560, -1152, -128, 2688, -768, 320, "maint")          # shaft bottom -> maintenance door

        # north service route (obj 2 alternative): a service door in the tower's north facade, off the plaza's
        # north-east corner, leads up a stair hall to a west door into the security hub
        A(448, 1024, 0, 576, 1152, 128, "service")              # service door through the facade
        A(576, 1024, 0, 704, 1152, 144, "service")              # passage
        A(704, 1024, 0, 1152, 1152, 320, "service")             # stair hall rising +x to the hub floor (192)
        # cooling route (obj 3 alternative): hub north door -> duct -> stairs down -> cooling plant -> vault
        A(1536, 1152, 192, 2304, 1280, 320, "maint")            # duct east from the hub's north wall
        A(2304, 1152, -128, 2944, 1280, 320, "maint")           # stair shaft down to the server-hall level
        A(2944, 768, -128, 3712, 1280, 256, "server")           # cooling plant hall
        A(3200, 640, -128, 3328, 768, 0, "server")              # door into the server hall
        A(3712, 768, -128, 4512, 896, 32, "maint")              # corridor east, north of the vault
        A(4384, 512, -128, 4512, 768, 0, "maint")               # into the vault's north-east walkway corner

        # ---------------- Zone E: server hall (floor z=-128)
        A(2304, -192, -128, 2560, 192, 160, "service")          # stairwell from service lobby down to hall
        A(2560, -640, -128, 3712, 640, 192, "server")
        A(2560, -768, -128, 2688, -640, 32, "maint")            # maintenance door into hall (south wall)

        # ---------------- Zone F: core vault
        A(3744, -512, -384, 4512, 512, 320, "vault")
        A(3712, -448, -128, 3744, -320, 0, "vault")             # door S from server hall
        A(3712, 320, -128, 3744, 448, 0, "vault")               # door N from server hall
        # walkways at z=-128 on the west and east sides; long stairs run down along the south and north walls
        S(3744, -512, -144, 3872, -224, -128, "slab")      # SW corner (top of the south stair)
        S(4384, -512, -144, 4512, -224, -128, "slab")      # SE corner
        S(3744, 224, -144, 3872, 512, -128, "slab")        # NW corner
        S(4384, 224, -144, 4512, 512, -128, "slab")        # NE corner (top of the north stair)
        S(3744, -224, -144, 3904, 224, -128, "slab")       # west walkway
        S(4352, -224, -144, 4512, 224, -128, "slab")       # east walkway

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
        # every flight uses 8u risers on 16u treads (1:2, ~27 degrees)
        # metro main stairs: landing inside the arch, then 384 rise over 768 run up into the kiosk
        kit.stairs(m, -4448, -192, -384, -3680, 192, 0, "+x", step=STEP, mat="termireal1/t_trashfloor",
                   riser="dys_nameless/concrete_004_blue")
        for y in (-194, 194):                                   # kiosk railings along the stair opening
            kit.rail(m, -3904, y, -3680, y, 0, h=40, mat="metal/metalwall003a")
        # maintenance: 384 over 768 from the tunnel up into the north alley
        kit.stairs(m, -4736, 1024, -384, -3968, 1152, 0, "+x", step=STEP, mat="metal/metalfloor_001e",
                   riser="dys_fortress/tunnel_wall")
        # fire escape: west of the arcade back door, alley (0) -> landing (320) beside the roof walkway
        kit.stairs(m, -2944, 1024, 0, -2304, 1120, 320, "+x", step=STEP, mat="metal/metalgrate011a",
                   riser="metal/metalwall003a")
        m.detail(box(-2304, 1024, 304, -2176, 1120, 320, {"all": "metal/metalwall003a", "top": "metal/metalgrate011a"}))
        kit.stringer(m, -2944, 1122, -2304, 1122, 0, 0, 320)                       # outer side of the flight
        kit.rail(m, -2304, 1122, -2176, 1122, 320, h=40, mat="metal/metalwall003a")    # landing rails
        kit.rail(m, -2178, 1024, -2178, 1120, 320, h=40, mat="metal/metalwall003a")
        # sunken court steps (plaza level 0 -> -64): 64 over 128 at both ends
        kit.stairs(m, -896, -448, -64, -768, 448, 0, "-x", step=STEP, mat="stone/stonefloor011a",
                   riser="concrete/concretewall060c")
        kit.stairs(m, -256, -448, -64, -128, 448, 0, "+x", step=STEP, mat="stone/stonefloor011a",
                   riser="concrete/concretewall060c")
        # lobby stairs to the mezzanines: 192 over 384
        kit.stairs(m, 1152, 96, 0, 1280, 480, 192, "+y", step=STEP, mat="vaccinert/dys_vaccorpfloor3",
                   riser="vaccinert/dys_vactrim2")
        kit.stairs(m, 1152, -480, 0, 1280, -96, 192, "-y", step=STEP, mat="vaccinert/dys_vaccorpfloor3",
                   riser="vaccinert/dys_vactrim2")
        # service stairwell: 128 over 256, from the service lobby down into the server hall
        kit.stairs(m, 2304, -192, -128, 2560, 192, 0, "-x", step=STEP, mat="metal/metalfloor003a")
        for y in (-194, 194):
            kit.rail(m, 2304, y, 2432, y, 0, h=40, mat="metal/metalwall003a")
        # maintenance corridor: 320 over 640 descending east, then flat through the shaft to the door
        kit.stairs(m, 1920, -1152, -128, 2560, -1024, 192, "-x", step=STEP, mat="metal/metalfloor003a")
        # north service route: 192 over 384 up to the hub's west door, short landing at the top
        kit.stairs(m, 704, 1024, 0, 1088, 1152, 192, "+x", step=STEP, mat="metal/metalfloor003a")
        m.detail(box(1088, 1024, 0, 1152, 1152, 192, {"all": "metal/metalwall003a", "top": "metal/metalfloor003a"}))
        # cooling route: 320 over 640 from the duct down into the cooling plant
        kit.stairs(m, 2304, 1152, -128, 2944, 1280, 192, "-x", step=STEP, mat="metal/metalfloor003a")
        # vault: 256 over 512 along the south and north walls, sloped balustrades on the pit side
        kit.stairs(m, 3872, -512, -384, 4384, -224, -128, "-x", step=STEP, mat="metal/metalfloor003a")
        kit.stairs(m, 3872, 224, -384, 4384, 512, -128, "+x", step=STEP, mat="metal/metalfloor003a")
        kit.stringer(m, 3904, -226, 4384, -226, -384, -144, -384)
        kit.stringer(m, 3872, 226, 4352, 226, -384, -384, -144)

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
        dress_in.routes(self)
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
            if op.kind != "air" or op.style in ("skyroom",) or op.style.startswith("cy_"):
                continue            # cyberspace places its own
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
    import monument
    if assets.model_exists(monument.MODEL):
        pairs += monument.pack_pairs()
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
