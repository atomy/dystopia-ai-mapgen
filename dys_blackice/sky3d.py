"""3D skybox for dys_blackice: a megacity skyline at 1/16 scale.

The skybox room is a sealed box far below the city (y -8192..-6656). sky_camera sits
at SKY_ORIGIN, which maps to world (0, 0, 0).
"""
from __future__ import annotations

import random

import kit
from vmflib import VMF, Tex, box, SKYBOX, NODRAW

SCALE = 16
SKY_ORIGIN = (0, -7424, -384)          # world (0,0,0) in skybox space
ROOM = (-1024, -8192, -512, 1024, -6656, 640)


def w2s(x, y, z):
    """world -> skybox coordinates."""
    return (SKY_ORIGIN[0] + x / SCALE, SKY_ORIGIN[1] + y / SCALE, SKY_ORIGIN[2] + z / SCALE)


def shell(b):
    x0, y0, z0, x1, y1, z1 = ROOM
    b.solid(x0 - 64, y0 - 64, z0 - 64, x1 + 64, y1 + 64, z1 + 64, "skyshell")
    b.air(x0, y0, z0, x1, y1, z1, "skyroom")


def tower(m: VMF, cx, cy, w, d, h, base_z, mat, tex_scale, crown=True, rng=None):
    """Tower in skybox units centred on (cx, cy)."""
    t = Tex(mat, scale=tex_scale, lightmap=64)
    m.add(box(cx - w / 2, cy - d / 2, base_z, cx + w / 2, cy + d / 2, base_z + h,
              {"all": t, "top": Tex("metal/metalwall003a", scale=0.0625, lightmap=64), "bottom": NODRAW}))
    if crown:
        m.add(box(cx - w / 3, cy - d / 3, base_z + h, cx + w / 3, cy + d / 3, base_z + h + 6,
                  {"all": Tex("vaccinert/dys_vacextwall4", scale=0.0625, lightmap=64), "bottom": NODRAW}))
        kit.sprite(m, cx, cy, base_z + h + 7, color=(255, 30, 30), scale=0.12, alpha=220)   # on the crown


def add(b):
    m: VMF = b.m
    rng = random.Random(1337)
    sx, sy, sz = SKY_ORIGIN
    ground = sz                       # street level
    m.ent("sky_camera", SKY_ORIGIN, scale=str(SCALE), angles="0 0 0", fogenable="1", fogblend="0",
          use_angles="0", fogcolor="14 17 30", fogcolor2="24 20 38", fogdir="1 0 0", fogstart="2500", fogend="22000")
    # dark ground plane under everything (never really seen)
    m.add(box(ROOM[0], ROOM[1], ROOM[2], ROOM[3], ROOM[4], ground - 2,
              {"all": NODRAW, "top": Tex("concrete/concretewall008a", scale=0.0625, lightmap=64)}))

    # Kuroda tower continues far above the real facade (world x 576..2560, y -1216..1216, z 1280+)
    kx0, ky0, kz0 = w2s(576, -1216, 1280)
    kx1, ky1, kz1 = w2s(2560, 1216, 7200)
    m.add(box(kx0, ky0, kz0 - 2, kx1, ky1, kz1, {"all": Tex("blackice/lit_windows", scale=1.0 / SCALE, lightmap=64),
                                                   "bottom": NODRAW, "top": Tex("metal/metalwall003a", scale=0.0625)}))
    # banner + spire on top
    from dress import fit_tex
    bx = kx0 - 0.25
    btex = fit_tex("blackice/kuroda_banner", "-x", (bx, sy + 21), kz0 + 228, 42, 168)
    m.brush_ent("func_brush", box(bx - 0.5, sy - 21, kz0 + 60, bx, sy + 21, kz0 + 228, {"all": NODRAW, "west": btex}),
                Solidity="1", solidbsp="0", StartDisabled="0", disableshadows="1", spawnflags="2", InputFilter="0")
    m.add(box((kx0 + kx1) / 2 - 3, sy - 3, kz1, (kx0 + kx1) / 2 + 3, sy + 3, kz1 + 60,
              {"all": Tex("metal/metalwall003a", scale=0.0625), "bottom": NODRAW}))
    kit.sprite(m, (kx0 + kx1) / 2, sy, kz1 + 62, color=(255, 30, 30), scale=0.25, alpha=255)

    # ring of towers outside the playable footprint
    foot = (w2s(-6600, -2000, 0), w2s(5600, 2000, 0))
    fx0, fy0 = foot[0][0], foot[0][1]
    fx1, fy1 = foot[1][0], foot[1][1]
    mats = [("blackice/lit_windows", 1.0 / SCALE), ("buildings/gen18", 0.5 / SCALE), ("buildings/gen16", 0.5 / SCALE),
            ("building_template/building_trainstation_template001d", 0.5 / SCALE), ("blackice/lit_windows", 1.0 / SCALE)]
    placed = []
    for i in range(140):
        cx = rng.uniform(ROOM[0] + 60, ROOM[3] - 60)
        cy = rng.uniform(ROOM[1] + 60, ROOM[4] - 60)
        w, d = rng.uniform(22, 70), rng.uniform(22, 70)
        margin = 18
        if fx0 - margin < cx < fx1 + margin and fy0 - margin < cy < fy1 + margin:
            continue
        if any(abs(cx - px) < (w + pw) / 2 + 6 and abs(cy - py) < (d + pd) / 2 + 6 for px, py, pw, pd in placed):
            continue
        dist = min(abs(cx - (fx0 + fx1) / 2) / 600, 1.0)
        h = rng.uniform(90, 260) + (1 - dist) * 120
        mat, sc = rng.choice(mats)
        tower(m, cx, cy, w, d, h, ground, mat, sc, crown=rng.random() < 0.6, rng=rng)
        placed.append((cx, cy, w, d))
    # a few giant animated billboards facing the city
    for (x, y, fac, mat) in [(fx0 - 60, sy - 40, "+x", "adverts/adverts_cyberfight_001"),
                             (fx1 + 70, sy + 30, "-x", "adverts/adverts_laora_001")]:
        face = "east" if fac == "+x" else "west"
        m.brush_ent("func_brush", box(x - 0.5, y - 40, ground + 110, x + 0.5, y + 40, ground + 150,
                                      {"all": NODRAW, face: Tex(mat, scale=80 / 256)}),
                    Solidity="1", solidbsp="0", StartDisabled="0", disableshadows="1", spawnflags="2", InputFilter="0")
        # on a steel mast with a frame, not hanging in the sky
        m.detail([box(x - 1.5, y - 1.5, ground, x + 1.5, y + 1.5, ground + 110, "metal/metalwall003a"),
                  box(x - 1, y - 41, ground + 108, x + 1, y + 41, ground + 110, "metal/metalwall003a"),
                  box(x - 1, y - 41, ground + 150, x + 1, y + 41, ground + 152, "metal/metalwall003a")])
    return len(placed)
