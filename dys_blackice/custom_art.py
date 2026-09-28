"""Custom textures for dys_blackice, drawn with Pillow and compiled with vtex.

Outputs go to dystopia/materials/blackice/ (so vbsp/vrad can see them during the
compile) and are packed into the BSP for release.
"""
from __future__ import annotations

import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

import tools

MATSRC = tools.GAME / "materialsrc" / "blackice"
MATDIR = tools.GAME / "materials" / "blackice"
RES = tools.GAME / "resource"
FONT_SPACE = str(RES / "spaceone.ttf")
FONT_DYS = str(RES / "dystopia.ttf")
FONT_JP = r"C:\Windows\Fonts\YuGothB.ttc"
FONT_BAHN = r"C:\Windows\Fonts\bahnschrift.ttf"

GENERATED: list[Path] = []


def _font(path, size):
    return ImageFont.truetype(path, size)


def glow(img: Image.Image, radius=10, strength=1.6) -> Image.Image:
    """Additive bloom: blurred copy added under the sharp image."""
    blur = img.filter(ImageFilter.GaussianBlur(radius))
    from PIL import ImageChops
    boosted = blur.point(lambda v: min(255, int(v * strength)))
    return ImageChops.add(boosted, img)


def compile_tex(name, img: Image.Image, options=("nomip 0",), vmt=None):
    MATSRC.mkdir(parents=True, exist_ok=True)
    MATDIR.mkdir(parents=True, exist_ok=True)
    tga = MATSRC / f"{name}.tga"
    img.save(tga)
    (MATSRC / f"{name}.txt").write_text("\n".join(options) + "\n", encoding="utf-8")
    p = subprocess.run([str(tools.BIN / "vtex.exe"), "-nopause", "-mkdir", "-game", str(tools.GAME), str(MATSRC / f"{name}.txt")],
                       capture_output=True, text=True, timeout=180)
    vtf = MATDIR / f"{name}.vtf"
    if not vtf.exists():
        raise RuntimeError(f"vtex failed for {name}:\n{p.stdout[-2000:]}\n{p.stderr[-1000:]}")
    if vmt:
        (MATDIR / f"{name}.vmt").write_text(vmt, encoding="utf-8")
        GENERATED.append(MATDIR / f"{name}.vmt")
    GENERATED.append(vtf)
    return vtf


def vmt_unlit(name, additive=True, extra=""):
    return ('"UnlitGeneric"\n{\n'
            f'\t"$basetexture" "blackice/{name}"\n'
            + ('\t"$additive" "1"\n' if additive else "")
            + '\t"$nocull" "1"\n\t"$surfaceprop" "glass"\n' + extra + "}\n")


def vmt_selfillum(name, base_is_lit=False):
    return ('"LightmappedGeneric"\n{\n'
            f'\t"$basetexture" "blackice/{name}"\n'
            '\t"$selfillum" "1"\n'
            '\t"$surfaceprop" "metal"\n}\n')


# ----------------------------------------------------------------------------- textures

def kuroda_banner():
    """Tall vertical tower banner: emblem + 黒田 + KURODA."""
    W, H = 256, 1024
    img = Image.new("RGB", (W, H), (0, 0, 0))
    d = ImageDraw.Draw(img)
    red, white = (255, 40, 50), (235, 245, 255)
    # emblem: hexagon ring with an ICE shard
    cx, cy, r = W // 2, 150, 92
    pts = [(cx + r * math.cos(math.radians(60 * i + 30)), cy + r * math.sin(math.radians(60 * i + 30))) for i in range(6)]
    d.polygon(pts, outline=red, width=12)
    shard = [(cx, cy - 58), (cx + 30, cy), (cx, cy + 58), (cx - 30, cy)]
    d.polygon(shard, fill=white)
    d.line([(cx, cy - 58), (cx, cy + 58)], fill=(0, 0, 0), width=4)
    # kanji
    fj = _font(FONT_JP, 150)
    for i, ch in enumerate("黒田"):
        bb = d.textbbox((0, 0), ch, font=fj)
        d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], 290 + i * 170), ch, font=fj, fill=white)
    # latin, vertical stack
    fl = _font(FONT_SPACE, 64)
    for i, ch in enumerate("KURODA"):
        bb = d.textbbox((0, 0), ch, font=fl)
        d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], 640 + i * 62), ch, font=fl, fill=red)
    img = glow(img, radius=8, strength=1.4)
    compile_tex("kuroda_banner", img, ("nomip 0", "nocompress 0"), vmt_unlit("kuroda_banner"))


def kuroda_wide():
    W, H = 1024, 256
    img = Image.new("RGB", (W, H), (0, 0, 0))
    d = ImageDraw.Draw(img)
    red, white = (255, 40, 50), (235, 245, 255)
    cx, cy, r = 140, 128, 88
    pts = [(cx + r * math.cos(math.radians(60 * i + 30)), cy + r * math.sin(math.radians(60 * i + 30))) for i in range(6)]
    d.polygon(pts, outline=red, width=11)
    d.polygon([(cx, cy - 56), (cx + 28, cy), (cx, cy + 56), (cx - 28, cy)], fill=white)
    d.text((270, 38), "KURODA", font=_font(FONT_SPACE, 132), fill=white)
    d.text((276, 178), "SYSTEMS  //  黒田  //  DATAVAULT 7", font=_font(FONT_JP, 38), fill=red)
    img = glow(img, radius=7, strength=1.3)
    compile_tex("kuroda_wide", img, ("nomip 0",), vmt_unlit("kuroda_wide"))


def ice_warning():
    W, H = 512, 256
    img = Image.new("RGB", (W, H), (0, 0, 0))
    d = ImageDraw.Draw(img)
    red = (255, 40, 40)
    d.rectangle([6, 6, W - 7, H - 7], outline=red, width=6)
    for i in range(0, W, 40):
        d.polygon([(i, 20), (i + 20, 20), (i + 8, 44), (i - 12, 44)], fill=(255, 190, 0))
    d.text((24, 60), "WARNING", font=_font(FONT_SPACE, 64), fill=red)
    d.text((24, 136), "BLACK ICE ACTIVE", font=_font(FONT_SPACE, 40), fill=(255, 235, 235))
    d.text((24, 190), "LETHAL INTRUSION COUNTERMEASURES", font=_font(FONT_SPACE, 20), fill=(255, 120, 120))
    img = glow(img, radius=5, strength=1.3)
    compile_tex("ice_warning", img, ("nomip 0",), vmt_unlit("ice_warning"))


def lit_windows():
    """Night office facade: 4 storeys x 8 bays per 512px tile, slab bands, ~30% lit (selfillum mask in alpha)."""
    import random
    rng = random.Random(3)
    W, H = 512, 512
    img = Image.new("RGBA", (W, H), (10, 12, 18, 0))
    d = ImageDraw.Draw(img)
    floors, bays = 4, 8
    fh, bw = H // floors, W // bays
    for f in range(floors):
        y0 = f * fh
        # slab band + spandrel
        d.rectangle([0, y0, W, y0 + 22], fill=(34, 38, 48, 0))
        d.line([(0, y0 + 22), (W, y0 + 22)], fill=(70, 80, 96, 0), width=2)
        for b in range(bays):
            x0 = b * bw + 4
            x1 = (b + 1) * bw - 4
            wy0, wy1 = y0 + 30, y0 + fh - 6
            if rng.random() < 0.32:
                col = rng.choice([(255, 210, 150), (210, 228, 255), (255, 236, 200), (160, 205, 255)])
                k = rng.uniform(0.45, 0.9)
                col = tuple(int(v * k) for v in col)
                d.rectangle([x0, wy0, x1, wy1], fill=col + (255,))
                if rng.random() < 0.35:
                    for yy in range(wy0 + 3, wy1, 6):
                        d.line([(x0, yy), (x1, yy)], fill=tuple(int(v * 0.55) for v in col) + (255,))
                if rng.random() < 0.25:     # silhouette of a desk/partition
                    d.rectangle([x0, wy1 - 18, x1, wy1], fill=(20, 22, 30, 255))
            else:
                g = rng.randint(22, 34)
                d.rectangle([x0, wy0, x1, wy1], fill=(g, g + 6, g + 16, 30))
                d.line([(x0, wy0), (x1, wy1)], fill=(g + 14, g + 18, g + 30, 30), width=1)
            d.line([(x1 + 4, y0 + 22), (x1 + 4, y0 + fh)], fill=(48, 54, 66, 0), width=6)   # mullion
    compile_tex("lit_windows", img, ("nomip 0",),
                '"LightmappedGeneric"\n{\n\t"$basetexture" "blackice/lit_windows"\n\t"$selfillum" "1"\n'
                '\t"$surfaceprop" "glass"\n}\n')


def build_all():
    GENERATED.clear()
    kuroda_banner()
    kuroda_wide()
    ice_warning()
    lit_windows()
    return list(GENERATED)


if __name__ == "__main__":
    for f in build_all():
        print(f)
