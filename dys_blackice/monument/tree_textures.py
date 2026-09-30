"""Textures for the Kuroda fibre tree, drawn with Pillow and compiled with vtex.

kuroda_tree_cable     512 trim sheet, VertexLitGeneric with phong, envmap and selfillum. Base alpha is the selfillum
                      mask and normal alpha is the phong/envmap mask. Bands (image rows):
                        A   0-255  cable insulation (U along the cable, V around it; tiles in U)
                        B 256-383  fibre ramp (U 0 = base .. 1 = tip: dark strand -> cyan glow -> white tip)
                        C 384-447  brushed black metal (rim cap, floor ports)
                        D 448-511  black mirror (the pool)
kuroda_tree_concrete  512 dark wet board-formed concrete (planter), 128u per tile.
kuroda_tree_neon      256 unlit neon palette. Rows:
                        0-63     red tube (emblems, rim band)
                        64-127   cyan tube (ripples, port rings, cyan tips)
                        128-191  cool white-hot (tips, nodes)
                        192-255  cyan tube ramping dim -> bright along U (trunk strands)
kuroda_tree_leaf      512 additive atlas ($nocull). Cells:
                        data leaves: cyan A, cyan B, white, red
                        glow dots: cyan, red, white
                      The UV layout is mirrored in build_tree.LEAF_CELLS.
"""
from __future__ import annotations

import math
import random
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

GAME = Path(r"M:\SteamLibrary\steamapps\common\Dystopia\dystopia")
VTEX = GAME.parent / "bin" / "win32" / "vtex.exe"
SRC = GAME / "materialsrc" / "models" / "blackice"
DST = GAME / "materials" / "models" / "blackice"
FONT_SPACE = str(GAME / "resource" / "spaceone.ttf")

RED, CYAN, WHITE = (255, 60, 70), (90, 220, 255), (225, 240, 255)
CABLE_BANDS = {"A": (0, 256), "B": (256, 384), "C": (384, 448), "D": (448, 512)}
LEAF_CELLS = {  # name: (x0, y0, size) in image pixels of the 512 atlas
    "cyan_a": (0, 0, 256), "cyan_b": (256, 0, 256), "white": (0, 256, 256), "red": (256, 256, 128),
    "glow_cyan": (384, 256, 128), "glow_red": (256, 384, 128), "glow_white": (384, 384, 128),
}


# ----------------------------------------------------------------------------- helpers

def _pixels(img):
    return getattr(img, "get_flattened_data", img.getdata)()


def _noise(w, h, seed, lo, hi, blur=0):
    rng = random.Random(seed)
    img = Image.new("L", (w, h))
    img.putdata([rng.randint(lo, hi) for _ in range(w * h)])
    return img.filter(ImageFilter.GaussianBlur(blur)) if blur else img


def _scale(img: Image.Image, k: float) -> Image.Image:
    return img.point(lambda v: min(255, int(v * k)))


def normal_map(height: Image.Image, strength=2.0, spec: Image.Image | None = None) -> Image.Image:
    """Height (L) -> DirectX-style tangent normal map (green = image down), wraps in x, clamps in y.
    spec (L) goes into alpha (phong / envmap mask)."""
    w, h = height.size
    hd = list(_pixels(height))
    out = bytearray(w * h * 4)
    sd = list(_pixels(spec)) if spec else [255] * (w * h)
    k = strength / 255.0
    for y in range(h):
        row = y * w
        up = max(0, y - 1) * w
        dn = min(h - 1, y + 1) * w
        for x in range(w):
            xl = x - 1 if x else w - 1
            xr = x + 1 if x < w - 1 else 0
            dx = (hd[row + xr] - hd[row + xl]) * k
            dy = (hd[dn + x] - hd[up + x]) * k
            inv = 1.0 / math.sqrt(dx * dx + dy * dy + 1.0)
            i = (row + x) * 4
            out[i] = int(128 - 127 * dx * inv)
            out[i + 1] = int(128 - 127 * dy * inv)
            out[i + 2] = int(128 + 127 * inv)
            out[i + 3] = sd[row + x]
    return Image.frombytes("RGBA", (w, h), bytes(out))


def _tube_row(img: Image.Image, r0, r1, stops, ramp=None):
    """Fill image rows r0..r1 with a neon tube profile (bright centre, dark edges); ramp(x) scales along U."""
    d = ImageDraw.Draw(img)
    n, w = r1 - r0, img.size[0]
    for i in range(n):
        t = abs((i + 0.5) / n * 2 - 1)
        for k in range(len(stops) - 1):
            (t0, c0), (t1, c1) = stops[k], stops[k + 1]
            if t0 <= t <= t1:
                f = (t - t0) / (t1 - t0)
                c = tuple(int(c0[j] + (c1[j] - c0[j]) * f) for j in range(3))
                break
        if ramp is None:
            d.line([(0, r0 + i), (w, r0 + i)], fill=c)
        else:
            for x in range(w):
                s = ramp(x / (w - 1))
                img.putpixel((x, r0 + i), tuple(int(v * s) for v in c))


# ----------------------------------------------------------------------------- kuroda_tree_cable

def cable():
    W = H = 512
    rng = random.Random(3)
    base = Image.new("RGB", (W, H), (0, 0, 0))
    mask = Image.new("L", (W, H), 0)                      # selfillum
    hgt = Image.new("L", (W, H), 128)
    spec = Image.new("L", (W, H), 0)
    bd, md, hd, sd = (ImageDraw.Draw(i) for i in (base, mask, hgt, spec))

    # ---- A: insulation. Black with a faint blue cast, fine longitudinal ridges, jacket print every 64u.
    a0, a1 = CABLE_BANDS["A"]
    noise = _noise(W, a1 - a0, 11, 0, 255, 0.8)
    jacket = Image.composite(Image.new("RGB", (W, a1 - a0), (15, 16, 21)), Image.new("RGB", (W, a1 - a0), (9, 10, 13)),
                             noise.point(lambda v: int(v * 0.5)))
    base.paste(jacket, (0, a0))
    for y in range(a0 + 8, a1, 16):                       # ridges run along the cable (along U)
        bd.line([(0, y), (W, y)], fill=(6, 7, 9), width=2)
        hd.line([(0, y), (W, y)], fill=96, width=2)
    sd.rectangle([0, a0, W, a1 - 1], fill=175)
    font = ImageFont.truetype(FONT_SPACE, 15)
    for x in range(0, W, 256):                             # KURODA jacket print, barely visible
        for y in (a0 + 52, a0 + 180):
            bd.text((x + 18, y), "KURODA  DATALINE  7  //  0.9 PB/S", font=font, fill=(34, 37, 45))
    for x in range(120, W, 256):                           # thin clamp band (brushed steel) every 64u
        bd.rectangle([x, a0, x + 5, a1 - 1], fill=(44, 48, 57))
        hd.rectangle([x, a0, x + 5, a1 - 1], fill=168)
        sd.rectangle([x, a0, x + 5, a1 - 1], fill=235)

    # ---- B: fibre ramp along U (0 = base, 1 = tip)
    b0, b1 = CABLE_BANDS["B"]
    for x in range(W):
        t = x / (W - 1)
        g = max(0.0, (t - 0.42) / 0.58) ** 1.7                 # glow only in the outer part (the AgX lesson)
        hot = max(0.0, (t - 0.9) / 0.1) ** 2
        c = tuple(int(10 + (CYAN[j] - 10) * g + (WHITE[j] - CYAN[j]) * hot * g) for j in range(3))
        bd.line([(x, b0), (x, b1 - 1)], fill=c)
        md.line([(x, b0), (x, b1 - 1)], fill=int(255 * g))
    sd.rectangle([0, b0, W, b1 - 1], fill=150)

    # ---- C: brushed black metal with bevel highlights at both edges
    c0, c1 = CABLE_BANDS["C"]
    bd.rectangle([0, c0, W, c1 - 1], fill=(27, 30, 36))
    for _ in range(420):
        y = rng.randrange(c0 + 3, c1 - 3)
        x0 = rng.randrange(W)
        ln = rng.randint(40, 300)
        col = rng.choice([(34, 37, 45), (20, 22, 27), (40, 44, 53)])
        bd.line([(x0, y), (x0 + ln, y)], fill=col)
        if x0 + ln > W:
            bd.line([(x0 - W, y), (x0 + ln - W, y)], fill=col)
    for y in (c0, c0 + 1, c1 - 2, c1 - 1):
        bd.line([(0, y), (W, y)], fill=(70, 76, 88))
    sd.rectangle([0, c0, W, c1 - 1], fill=225)

    # ---- D: black mirror
    d0, d1 = CABLE_BANDS["D"]
    bd.rectangle([0, d0, W, d1 - 1], fill=(3, 4, 6))
    sd.rectangle([0, d0, W, d1 - 1], fill=255)

    for r0, r1 in CABLE_BANDS.values():                    # keep bands from bleeding in the normal map
        hd.line([(0, r0), (W, r0)], fill=128)
        hd.line([(0, r1 - 1), (W, r1 - 1)], fill=128)
    out = base.convert("RGBA")
    out.putalpha(mask)
    return out, normal_map(hgt.filter(ImageFilter.GaussianBlur(0.8)), 2.2, spec)


# ----------------------------------------------------------------------------- kuroda_tree_concrete

def concrete():
    W = H = 512                                            # 128u per tile: 4 px per unit
    rng = random.Random(9)
    mott = _noise(32, 32, 4, 0, 255).resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(10))
    base = Image.composite(Image.new("RGB", (W, H), (46, 48, 54)), Image.new("RGB", (W, H), (28, 29, 34)), mott)
    grain = _noise(W, H, 5, 0, 255, 0.6)
    base = Image.composite(Image.new("RGB", (W, H), (52, 54, 60)), base, grain.point(lambda v: 60 if v > 214 else 0))
    hgt = Image.composite(Image.new("L", (W, H), 150), Image.new("L", (W, H), 118), grain.point(lambda v: 90 if v > 200 else 0))
    spec = _scale(mott, 0.35).point(lambda v: 70 + v)      # damp; streaks below are wetter
    bd, hd, sd = ImageDraw.Draw(base), ImageDraw.Draw(hgt), ImageDraw.Draw(spec)
    for y in range(0, H, 16):                              # board-formed texture: faint horizontal planks every 4u
        bd.line([(0, y), (W, y)], fill=(24, 25, 29))
        hd.line([(0, y), (W, y)], fill=104)
    for y in (0, 256):                                     # formwork joints every 64u
        bd.rectangle([0, y, W, y + 2], fill=(16, 17, 20))
        hd.rectangle([0, y, W, y + 2], fill=60)
    for x in (0, 256):
        bd.rectangle([x, 0, x + 2, H], fill=(18, 19, 22))
        hd.rectangle([x, 0, x + 2, H], fill=66)
        for y in (0, 256):                                 # form-tie holes near the joints
            for dx, dy in ((40, 40), (216, 40), (40, 216), (216, 216)):
                cx, cy = x + dx, y + dy
                bd.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(12, 12, 15))
                hd.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=40)
    for _ in range(26):                                    # rain streaks
        x = rng.randrange(W)
        y0 = rng.randrange(H)
        ln = rng.randint(60, 260)
        w = rng.randint(2, 7)
        bd.rectangle([x, y0, x + w, y0 + ln], fill=(22, 23, 27))
        sd.rectangle([x, y0, x + w, y0 + ln], fill=190)
    base = base.filter(ImageFilter.GaussianBlur(0.4))
    return base, normal_map(hgt.filter(ImageFilter.GaussianBlur(1.0)), 2.0, spec.filter(ImageFilter.GaussianBlur(2)))


# ----------------------------------------------------------------------------- kuroda_tree_neon

def neon():
    W = H = 256
    img = Image.new("RGB", (W, H))
    _tube_row(img, 0, 64, [(0, (255, 205, 205)), (0.3, (255, 90, 100)), (0.7, (240, 45, 58)), (1.0, (120, 12, 22))])
    _tube_row(img, 64, 128, [(0, (225, 250, 255)), (0.3, (120, 230, 255)), (0.7, (60, 190, 240)), (1.0, (10, 60, 90))])
    _tube_row(img, 128, 192, [(0, (255, 255, 255)), (0.4, (235, 248, 255)), (0.8, (160, 225, 255)), (1.0, (70, 150, 200))])
    _tube_row(img, 192, 256, [(0, (205, 245, 255)), (0.3, (110, 225, 255)), (0.7, (50, 175, 225)), (1.0, (8, 50, 75))],
              ramp=lambda u: 0.22 + 0.78 * u ** 1.3)
    return img


# ----------------------------------------------------------------------------- kuroda_tree_leaf

def _leaf(size, color, variant, seed):
    """Additive data leaf: faint body, glowing rim, midrib and circuit-like veins ending in dots.
    The cell's height is the leaf's length (V), its width the leaf's width (U)."""
    S = size * 4
    rng = random.Random(seed)
    layer = Image.new("L", (S, S), 0)                      # intensity; tinted at the end
    d = ImageDraw.Draw(layer)
    m = int(S * 0.05)
    box = [m, m, S - m, S - m]
    d.ellipse(box, fill=40)                                # body: a faint tinted panel
    rim = Image.new("L", (S, S), 0)
    ImageDraw.Draw(rim).ellipse(box, outline=215, width=int(S * 0.03))
    cx = S // 2
    lw = max(2, int(S * 0.012))
    d.line([(cx, int(S * 0.14)), (cx, int(S * 0.86))], fill=120, width=lw)       # midrib
    ys = [0.26, 0.38, 0.5, 0.62, 0.74] if variant == 0 else [0.3, 0.44, 0.58, 0.72]
    for k, fy in enumerate(ys):
        y = int(S * fy)
        half = 0.5 * math.sqrt(max(0.0, 1 - ((fy - 0.5) / 0.46) ** 2)) * (S - 2 * m)
        for sgn in (-1, 1):
            if variant == 0:                               # diagonal veins
                x1 = cx + sgn * half * 0.62
                y1 = y - int(S * 0.07)
                d.line([(cx, y), (x1, y1)], fill=92, width=lw)
            else:                                          # circuit traces: out, then up
                x1 = cx + sgn * half * rng.uniform(0.45, 0.62)
                y1 = y - int(S * 0.05)
                d.line([(cx, y), (x1, y), (x1, y1)], fill=92, width=lw, joint="curve")
            r = int(S * 0.018)
            d.ellipse([x1 - r, y1 - r, x1 + r, y1 + r], fill=170)
    r = int(S * 0.028)
    d.ellipse([cx - r, int(S * 0.86) - r, cx + r, int(S * 0.86) + r], fill=200)   # stem node
    glow = rim.filter(ImageFilter.GaussianBlur(S * 0.03)).point(lambda v: min(255, int(v * 1.6)))
    lum = ImageChops.lighter(ImageChops.lighter(layer, rim), _scale(glow, 0.45))
    lum = lum.resize((size, size), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.5))
    col = Image.merge("RGB", [lum.point(lambda v, c=c: int(v * c / 255)) for c in color])
    hot = lum.point(lambda v: max(0, v - 205) * 2)         # whiten only the very brightest rim pixels
    return ImageChops.add(col, Image.merge("RGB", [hot, hot, hot]))


def _glow_dot(size, color):
    img = Image.new("RGB", (size, size))
    px = img.load()
    c = (size - 1) / 2
    for y in range(size):
        for x in range(size):
            r = math.hypot(x - c, y - c) / (size / 2)
            if r >= 1:
                continue
            k = (1 - r) ** 2.2
            core = max(0.0, 1 - r / 0.18)
            px[x, y] = tuple(min(255, int(color[j] * k + 255 * core * 0.8)) for j in range(3))
    return img


def leaf_atlas():
    img = Image.new("RGB", (512, 512))
    img.paste(_leaf(256, CYAN, 0, 1), LEAF_CELLS["cyan_a"][:2])
    img.paste(_leaf(256, CYAN, 1, 2), LEAF_CELLS["cyan_b"][:2])
    img.paste(_leaf(256, WHITE, 0, 3), LEAF_CELLS["white"][:2])
    img.paste(_leaf(128, RED, 1, 4), LEAF_CELLS["red"][:2])
    img.paste(_glow_dot(128, CYAN), LEAF_CELLS["glow_cyan"][:2])
    img.paste(_glow_dot(128, RED), LEAF_CELLS["glow_red"][:2])
    img.paste(_glow_dot(128, WHITE), LEAF_CELLS["glow_white"][:2])
    return img


# ----------------------------------------------------------------------------- compile

VMT_CABLE = """"VertexLitGeneric"
{
	"$basetexture" "models/blackice/kuroda_tree_cable"
	"$bumpmap" "models/blackice/kuroda_tree_cable_n"
	"$selfillum" "1"
	"$phong" "1"
	"$phongexponent" "36"
	"$phongboost" "3"
	"$phongfresnelranges" "[0.3 0.65 1]"
	"$envmap" "env_cubemap"
	"$normalmapalphaenvmapmask" "1"
	"$envmaptint" "[0.26 0.29 0.35]"
	"$surfaceprop" "metal"
}
"""
VMT_CONCRETE = """"VertexLitGeneric"
{
	"$basetexture" "models/blackice/kuroda_tree_concrete"
	"$bumpmap" "models/blackice/kuroda_tree_concrete_n"
	"$phong" "1"
	"$phongexponent" "14"
	"$phongboost" "1.2"
	"$phongfresnelranges" "[0.4 0.75 1]"
	"$surfaceprop" "concrete"
}
"""
VMT_NEON = """"UnlitGeneric"
{
	"$basetexture" "models/blackice/kuroda_tree_neon"
	"$model" "1"
	"$surfaceprop" "glass"
}
"""
VMT_LEAF = """"UnlitGeneric"
{
	"$basetexture" "models/blackice/kuroda_tree_leaf"
	"$additive" "1"
	"$nocull" "1"
	"$model" "1"
	"$surfaceprop" "glass"
}
"""


def _vtex(name, img: Image.Image, options=()):
    SRC.mkdir(parents=True, exist_ok=True)
    DST.mkdir(parents=True, exist_ok=True)
    img.save(SRC / f"{name}.tga")
    txt = SRC / f"{name}.txt"
    txt.write_text("".join(o + "\n" for o in options), encoding="utf-8")
    vtf = DST / f"{name}.vtf"
    if vtf.exists():
        vtf.unlink()
    p = subprocess.run([str(VTEX), "-nopause", "-mkdir", "-game", str(GAME), str(txt)],
                       capture_output=True, text=True, timeout=300)
    if not vtf.exists():
        raise RuntimeError(f"vtex failed for {name}:\n{p.stdout[-2000:]}\n{p.stderr[-1000:]}")
    return vtf


def build() -> list[Path]:
    """Draw all textures, compile them with vtex and write the VMTs. Returns the material files."""
    out = []
    base, nrm = cable()
    out += [_vtex("kuroda_tree_cable", base), _vtex("kuroda_tree_cable_n", nrm, ("normal 1",))]
    base, nrm = concrete()
    out += [_vtex("kuroda_tree_concrete", base), _vtex("kuroda_tree_concrete_n", nrm, ("normal 1",))]
    out.append(_vtex("kuroda_tree_neon", neon(), ("nocompress 1",)))
    out.append(_vtex("kuroda_tree_leaf", leaf_atlas()))
    for name, text in (("kuroda_tree_cable", VMT_CABLE), ("kuroda_tree_concrete", VMT_CONCRETE),
                       ("kuroda_tree_neon", VMT_NEON), ("kuroda_tree_leaf", VMT_LEAF)):
        p = DST / f"{name}.vmt"
        p.write_text(text, encoding="utf-8")
        out.append(p)
    return out


if __name__ == "__main__":
    for f in build():
        print(f)
    sys.exit(0)
