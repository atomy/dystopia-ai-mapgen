"""Textures for the Kuroda monument, drawn with Pillow and compiled with vtex.

kuroda_metal  1024 trim sheet, black glossy metal. Base alpha = selfillum mask, normal alpha = phong/envmap mask.
              Bands (image rows): A 0-383 shaft panels, B 384-639 pedestal text, C 640-767 step risers,
              D 768-895 treads, E 896-1023 brushed trim. Each band tiles horizontally.
kuroda_ice    512 "black ice" crystal glass: cyan edge glow along both long edges, faint circuit veins.
kuroda_neon   256 unlit neon palette: rows 0-63 red tube, 64-127 white-hot gem, 128-191 cyan tube, 192-255 dim red.
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
FONT_JP = r"C:\Windows\Fonts\YuGothB.ttc"

RED, CYAN, WHITE = (255, 60, 70), (90, 220, 255), (235, 245, 255)
BANDS = {"A": (0, 384), "B": (384, 640), "C": (640, 768), "D": (768, 896), "E": (896, 1024)}


# ----------------------------------------------------------------------------- helpers

def _glow(layer: Image.Image, radius, strength=1.0) -> Image.Image:
    """Add a blurred halo under a glow layer (RGB or L)."""
    blur = layer.filter(ImageFilter.GaussianBlur(radius)).point(lambda v: min(255, int(v * strength)))
    return ImageChops.lighter(layer, blur)


def _noise(w, h, seed, lo, hi, blur=0):
    rng = random.Random(seed)
    img = Image.new("L", (w, h))
    img.putdata([rng.randint(lo, hi) for _ in range(w * h)])
    return img.filter(ImageFilter.GaussianBlur(blur)) if blur else img


def _pixels(img):
    return getattr(img, "get_flattened_data", img.getdata)()


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
            nx, ny, nz = -dx, -dy, 1.0
            inv = 1.0 / math.sqrt(nx * nx + ny * ny + 1.0)
            i = (row + x) * 4
            out[i] = int(128 + 127 * nx * inv)
            out[i + 1] = int(128 + 127 * ny * inv)
            out[i + 2] = int(128 + 127 * nz * inv)
            out[i + 3] = sd[row + x]
    return Image.frombytes("RGBA", (w, h), bytes(out))


def _hex(cx, cy, r, phase=90):
    return [(cx + r * math.cos(math.radians(phase + 60 * i)), cy + r * math.sin(math.radians(phase + 60 * i))) for i in range(6)]


def _emblem(d: ImageDraw.ImageDraw, cx, cy, r, color, width, diamond=WHITE):
    """Kuroda logo: pointy-top hexagon outline + vertical diamond."""
    d.polygon(_hex(cx, cy, r), outline=color, width=width)
    d.polygon([(cx, cy - r * 0.62), (cx + r * 0.3, cy), (cx, cy + r * 0.62), (cx - r * 0.3, cy)], fill=diamond)


# ----------------------------------------------------------------------------- kuroda_metal

def metal():
    W = H = 1024
    rng = random.Random(7)
    base = Image.new("RGB", (W, H), (16, 18, 24))
    glow = Image.new("RGB", (W, H), (0, 0, 0))          # selfillum colour layer
    hgt = Image.new("L", (W, H), 128)                     # height for the normal map
    spec = Image.new("L", (W, H), 190)
    bd, gd, hd, sd = (ImageDraw.Draw(i) for i in (base, glow, hgt, spec))

    # subtle large-scale mottling + brushed streaks everywhere
    mott = _noise(64, 64, 1, 0, 255, 0).resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(24))
    base = Image.composite(Image.new("RGB", (W, H), (21, 24, 31)), base, mott.point(lambda v: int(v * 0.55)))
    bd = ImageDraw.Draw(base)
    for _ in range(900):
        y = rng.randrange(H)
        x0 = rng.randrange(W)
        ln = rng.randint(40, 400)
        c = rng.choice([(24, 27, 34), (12, 13, 18), (28, 31, 39)])
        bd.line([(x0, y), (x0 + ln, y)], fill=c)
        if x0 + ln > W:
            bd.line([(x0 - W, y), (x0 + ln - W, y)], fill=c)

    # ---- A: shaft panels (x = up the shaft, 1024 px = 256u; y = across the face, 384 px = 80u)
    a0, a1 = BANDS["A"]
    cy = (a0 + a1) // 2
    px = 384 / 80.0                                        # px per unit across
    for x in range(0, W, 256):                             # horizontal panel joints every 64u
        for dx in (0,):
            bd.rectangle([x - 2 + dx, a0, x + 1 + dx, a1 - 1], fill=(7, 8, 11))
            hd.rectangle([x - 2, a0, x + 1, a1 - 1], fill=70)
            sd.rectangle([x - 2, a0, x + 1, a1 - 1], fill=60)
            bd.line([(x + 2, a0), (x + 2, a1 - 1)], fill=(44, 48, 58))
    for s in (-22, 22):                                    # vertical seams dividing each face
        y = int(cy + s * px)
        bd.rectangle([0, y - 1, W, y + 1], fill=(8, 9, 12))
        hd.rectangle([0, y - 1, W, y + 1], fill=80)
        sd.rectangle([0, y - 1, W, y + 1], fill=70)
    lip = int(3.2 * px)                                    # bright lip beside the neon groove (groove = +-2u)
    for sgn in (-1, 1):
        y0 = cy + sgn * int(2.0 * px)
        y1 = cy + sgn * lip
        bd.rectangle([0, min(y0, y1), W, max(y0, y1)], fill=(58, 63, 74))
        hd.rectangle([0, min(y0, y1), W, max(y0, y1)], fill=150)
        sd.rectangle([0, min(y0, y1), W, max(y0, y1)], fill=255)
    for x in range(64, W, 128):                            # cyan status LEDs along the groove, every 32u
        for sgn in (-1, 1):
            y = cy + sgn * int(6.0 * px)
            gd.rectangle([x - 5, y - 3, x + 5, y + 3], fill=CYAN if (x // 128) % 4 else RED)
            hd.rectangle([x - 6, y - 4, x + 6, y + 4], fill=112)
    for x in range(0, W, 256):                             # bolts at panel corners
        for s in (-30, -14, 14, 30):
            for xx in (x + 12, x + 244):
                y = int(cy + s * px)
                bd.ellipse([xx - 4, y - 4, xx + 4, y + 4], fill=(40, 44, 52))
                hd.ellipse([xx - 4, y - 4, xx + 4, y + 4], fill=175)
    for x in (128, 640):                                   # small engraved serial plates
        y = int(cy - 30 * px)
        bd.rectangle([x, y, x + 90, y + 22], fill=(30, 33, 41))
        bd.text((x + 6, y + 3), "KRD-7", font=ImageFont.truetype(FONT_SPACE, 16), fill=(90, 96, 110))
        hd.rectangle([x, y, x + 90, y + 22], fill=118)

    # ---- B: pedestal riser, one 96x32u face per 1024x256 px; KURODA lettering in red neon
    b0, b1 = BANDS["B"]
    bd.rectangle([0, b0, W, b1], fill=(15, 17, 22))
    bd.rectangle([0, b0, W, b0 + 14], fill=(66, 71, 82))          # top rim bevel
    bd.line([(0, b0 + 15), (W, b0 + 15)], fill=(110, 118, 132), width=2)
    hd.rectangle([0, b0, W, b0 + 14], fill=165)
    sd.rectangle([0, b0, W, b0 + 16], fill=255)
    bd.rectangle([0, b1 - 22, W, b1], fill=(9, 10, 13))            # kick plate
    hd.rectangle([0, b1 - 22, W, b1], fill=110)
    gd.rectangle([0, b1 - 34, W, b1 - 29], fill=CYAN)              # floor light line
    hd.rectangle([0, b1 - 36, W, b1 - 27], fill=100)
    for x in range(0, W, 256):
        bd.line([(x, b0 + 16), (x, b1 - 23)], fill=(9, 10, 13), width=3)
    tl = Image.new("RGB", (W, b1 - b0), (0, 0, 0))
    td = ImageDraw.Draw(tl)
    fk, fl, fs = ImageFont.truetype(FONT_JP, 92), ImageFont.truetype(FONT_SPACE, 104), ImageFont.truetype(FONT_SPACE, 26)
    wk = td.textbbox((0, 0), "黒田", font=fk)
    wl = td.textbbox((0, 0), "KURODA", font=fl)
    gap = 46
    total = 118 + gap + (wk[2] - wk[0]) + gap + (wl[2] - wl[0]) + gap + 118
    x = (W - total) // 2
    ty = 112
    _emblem(td, x + 59, ty, 56, RED, 9)
    x += 118 + gap
    td.text((x - wk[0], ty - (wk[1] + wk[3]) // 2), "黒田", font=fk, fill=WHITE)
    x += wk[2] - wk[0] + gap
    td.text((x - wl[0], ty - (wl[1] + wl[3]) // 2), "KURODA", font=fl, fill=RED)
    x += wl[2] - wl[0] + gap
    _emblem(td, x + 59, ty, 56, RED, 9)
    sub = "KURODA SYSTEMS  //  DATAVAULT 7  //  BLACK ICE"
    ws = td.textbbox((0, 0), sub, font=fs)
    td.text(((W - (ws[2] - ws[0])) // 2, 176), sub, font=fs, fill=(200, 45, 55))
    tmask = tl.convert("L").point(lambda v: 255 if v > 40 else 0)
    hgt.paste(96, (0, b0), tmask.filter(ImageFilter.MaxFilter(3)))  # engraved lettering
    glow.paste(_glow(tl, 6, 1.2), (0, b0))

    # ---- C: step riser, 16u tall (128 px), cyan light line under the nosing
    c0, c1 = BANDS["C"]
    bd.rectangle([0, c0, W, c1], fill=(17, 19, 25))
    bd.rectangle([0, c0, W, c0 + 6], fill=(80, 86, 98))
    hd.rectangle([0, c0, W, c0 + 6], fill=170)
    sd.rectangle([0, c0, W, c0 + 7], fill=255)
    gd.rectangle([0, c0 + 13, W, c0 + 19], fill=CYAN)
    hd.rectangle([0, c0 + 11, W, c0 + 21], fill=104)
    bd.rectangle([0, c1 - 10, W, c1], fill=(10, 11, 14))
    for x in range(0, W, 256):
        bd.line([(x, c0 + 24), (x, c1 - 11)], fill=(8, 9, 12), width=3)
        hd.line([(x, c0 + 24), (x, c1 - 11)], fill=90, width=3)

    # ---- D: treads / tops, 32u across (128 px); nosing at the top edge, anti-slip ribs along U
    d0, d1 = BANDS["D"]
    bd.rectangle([0, d0, W, d1], fill=(20, 22, 28))
    for y in range(d0 + 20, d1 - 4, 9):
        bd.line([(0, y), (W, y)], fill=(12, 13, 17), width=2)
        hd.line([(0, y), (W, y)], fill=100, width=2)
    for x in range(0, W, 128):
        bd.line([(x, d0 + 16), (x, d1)], fill=(10, 11, 14), width=2)
        hd.line([(x, d0 + 16), (x, d1)], fill=96, width=2)
    bd.rectangle([0, d0, W, d0 + 12], fill=(74, 80, 93))
    hd.rectangle([0, d0, W, d0 + 12], fill=160)
    sd.rectangle([d0 * 0, d0, W, d0 + 13], fill=250)
    sd.rectangle([0, d0 + 14, W, d1], fill=215)                     # wet

    # ---- E: brushed trim (chamfers, frame, collar, neck, finial)
    e0, e1 = BANDS["E"]
    bd.rectangle([0, e0, W, e1], fill=(38, 42, 50))
    for _ in range(700):
        y = rng.randrange(e0 + 2, e1 - 2)
        x0 = rng.randrange(W)
        ln = rng.randint(60, 500)
        c = rng.choice([(46, 50, 60), (30, 33, 40), (55, 60, 71)])
        bd.line([(x0, y), (x0 + ln, y)], fill=c)
        if x0 + ln > W:
            bd.line([(x0 - W, y), (x0 + ln - W, y)], fill=c)
    bd.rectangle([0, e0, W, e0 + 3], fill=(20, 22, 27))
    bd.rectangle([0, e1 - 4, W, e1], fill=(20, 22, 27))
    sd.rectangle([0, e0, W, e1], fill=245)

    # soften band borders in the height map so normals don't bleed across bands
    for (r0, r1) in BANDS.values():
        hd.line([(0, r0), (W, r0)], fill=128)
        hd.line([(0, r1 - 1), (W, r1 - 1)], fill=128)

    mask = glow.convert("L").point(lambda v: min(255, v * 3))
    rgb = Image.composite(glow, base, mask)
    out = rgb.convert("RGBA")
    out.putalpha(mask)
    hgt = hgt.filter(ImageFilter.GaussianBlur(1.2))
    return out, normal_map(hgt, 3.0, spec)


# ----------------------------------------------------------------------------- kuroda_ice

def ice():
    W = H = 512
    rng = random.Random(21)
    base = Image.new("RGB", (W, H), (6, 10, 18))
    grad = Image.linear_gradient("L").resize((W, H)).point(lambda v: int(60 * math.sin(math.pi * v / 255)))
    base = Image.composite(Image.new("RGB", (W, H), (14, 26, 44)), base, grad)
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    hgt = Image.new("L", (W, H), 128)
    bd, gd, hd = ImageDraw.Draw(base), ImageDraw.Draw(glow), ImageDraw.Draw(hgt)
    for _ in range(14):                                   # fracture planes
        x0, y0 = rng.randrange(W), rng.randrange(40, H - 40)
        ang = rng.uniform(-0.5, 0.5)
        ln = rng.randint(120, 380)
        x1, y1 = x0 + ln * math.cos(ang), y0 + ln * math.sin(ang)
        bd.line([(x0, y0), (x1, y1)], fill=(24, 40, 60), width=2)
        hd.line([(x0, y0), (x1, y1)], fill=160, width=3)
        bd.line([(x0 - W, y0), (x1 - W, y1)], fill=(24, 40, 60), width=2)
        hd.line([(x0 - W, y0), (x1 - W, y1)], fill=160, width=3)
    vein = (22, 92, 118)
    for i in range(5):                                    # circuit veins along the crystal axis
        y = rng.randrange(80, H - 80)
        x = rng.randrange(W)
        pts = [(x, y)]
        for _ in range(rng.randint(3, 6)):
            x += rng.randint(40, 140)
            pts.append((x, y))
            if rng.random() < 0.6:
                y = max(60, min(H - 60, y + rng.choice((-1, 1)) * rng.randint(16, 60)))
                pts.append((x, y))
        for k in range(len(pts) - 1):
            for off in (0, -W):
                a, b = (pts[k][0] + off, pts[k][1]), (pts[k + 1][0] + off, pts[k + 1][1])
                gd.line([a, b], fill=vein, width=3)
        for off in (0, -W):
            ex, ey = pts[-1][0] + off, pts[-1][1]
            gd.ellipse([ex - 5, ey - 5, ex + 5, ey + 5], fill=(70, 190, 230))
    glow = _glow(glow, 5, 0.7)
    for y in range(0, 30):                                # glowing crystal edges (both long edges)
        k = (1 - y / 30) ** 1.6
        c = tuple(int(v * k) for v in CYAN) if y > 3 else (200, 245, 255)
        gd = ImageDraw.Draw(glow)
        gd.line([(0, y), (W, y)], fill=c)
        gd.line([(0, H - 1 - y), (W, H - 1 - y)], fill=c)
    mask = glow.convert("L").point(lambda v: min(255, v * 3))
    out = Image.composite(glow, base, mask).convert("RGBA")
    out.putalpha(mask)
    return out, normal_map(hgt.filter(ImageFilter.GaussianBlur(1.5)).resize((256, 256), Image.LANCZOS), 2.0,
                           Image.new("L", (256, 256), 255))


# ----------------------------------------------------------------------------- kuroda_neon

def neon():
    W = H = 256
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)

    def band(r0, r1, stops):
        n = r1 - r0
        for i in range(n):
            t = abs((i + 0.5) / n * 2 - 1)            # 0 at the band centre, 1 at the edges
            for k in range(len(stops) - 1):
                (t0, c0), (t1, c1) = stops[k], stops[k + 1]
                if t0 <= t <= t1:
                    f = (t - t0) / (t1 - t0)
                    c = tuple(int(c0[j] + (c1[j] - c0[j]) * f) for j in range(3))
                    break
            d.line([(0, r0 + i), (W, r0 + i)], fill=c)
    band(0, 64, [(0, (255, 205, 205)), (0.3, (255, 90, 100)), (0.7, (240, 45, 58)), (1.0, (120, 12, 22))])
    band(64, 128, [(0, (255, 255, 255)), (0.35, (255, 225, 228)), (0.75, (255, 120, 130)), (1.0, (230, 50, 62))])
    band(128, 192, [(0, (225, 250, 255)), (0.3, (120, 230, 255)), (0.7, (60, 190, 240)), (1.0, (10, 60, 90))])
    band(192, 256, [(0, (230, 55, 66)), (1.0, (150, 22, 32))])
    return img


# ----------------------------------------------------------------------------- compile

VMT_LIT = """"VertexLitGeneric"
{{
	"$basetexture" "models/blackice/{name}"
	"$bumpmap" "models/blackice/{name}_n"
	"$selfillum" "1"
	"$phong" "1"
	"$phongexponent" "{exp}"
	"$phongboost" "{boost}"
	"$phongfresnelranges" "[0.35 0.7 1]"
	"$envmap" "env_cubemap"
	"$normalmapalphaenvmapmask" "1"
	"$envmaptint" "{tint}"
	"$surfaceprop" "{prop}"
}}
"""
VMT_NEON = """"UnlitGeneric"
{
	"$basetexture" "models/blackice/kuroda_neon"
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
    base, nrm = metal()
    out += [_vtex("kuroda_metal", base), _vtex("kuroda_metal_n", nrm, ("normal 1",))]
    base, nrm = ice()
    out += [_vtex("kuroda_ice", base), _vtex("kuroda_ice_n", nrm, ("normal 1",))]
    out.append(_vtex("kuroda_neon", neon(), ("nocompress 1",)))
    vmts = {"kuroda_metal": VMT_LIT.format(name="kuroda_metal", exp=28, boost=2.5, tint="[0.32 0.35 0.42]", prop="metal"),
            "kuroda_ice": VMT_LIT.format(name="kuroda_ice", exp=60, boost=4, tint="[0.55 0.7 0.85]", prop="glass"),
            "kuroda_neon": VMT_NEON}
    for name, text in vmts.items():
        p = DST / f"{name}.vmt"
        p.write_text(text, encoding="utf-8")
        out.append(p)
    return out


if __name__ == "__main__":
    for f in build():
        print(f)
    sys.exit(0)
