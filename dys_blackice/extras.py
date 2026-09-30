"""Release extras for dys_blackice: radar overview, mappaths, music, soundscapes, loading screen."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import custom_art
import look
import tools
from vmflib import VMF

NAME = "dys_blackice"
STAGE = tools.BUILD / "pak"

# ----------------------------------------------------------------------------- overview (radar)
OV_X0, OV_Y1, OV_SCALE = -6400, 2944, 11.5         # upper-left world corner, units per pixel (1024 wide)
LAYERS = [  # name, pos_z (layer active when player z >= pos_z), floor z band [lo, hi)
    ("b1", -1000, (-1000, -100)),
    ("g", -100, (-100, 176)),
    ("l2", 176, (176, 400)),
]
LABELS = [("METRO", -5250, 100, "b1"), ("MARKET", -2600, 0, "g"), ("PLAZA", -620, 0, "g"), ("LOBBY", 1200, 0, "g"),
          ("SERVERS", 3130, 0, "b1"), ("VAULT", 4130, 0, "b1"), ("HUB", 1408, 980, "l2"), ("SECURITY", 2160, 0, "l2"),
          ("DATAVAULT", 4800, -520, "b1"), ("ROOFS", -2000, 860, "l2")]


def _px(x, y):
    return (x - OV_X0) / OV_SCALE, (OV_Y1 - y) / OV_SCALE


def overview(level):
    font = ImageFont.truetype(custom_art.FONT_SPACE, 14)
    pairs = []
    for lname, posz, (zlo, zhi) in LAYERS:
        img = Image.new("RGBA", (1024, 512), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        boxes = []
        for op in level.ops:
            if op.style.startswith("cy_") or op.style in ("skyroom",):
                continue
            blocker = op.kind == "solid" and op.style.startswith("bld_")    # buildings standing in outdoor air
            if op.kind == "solid" and not blocker and not (op.style == "slab" and lname == "l2"):
                continue
            if op.kind == "air" and op.style in ("roof", "plaza") and op.box.z0 > 400:
                continue
            b = op.box
            if b.y0 > 2400 or b.y1 < -2400:        # cyberspace / skybox regions
                continue
            z = b.z0 if (op.kind == "air" or blocker) else b.z1      # slabs: their walkable top
            if not (zlo <= z < zhi):
                continue
            boxes.append((op, b))
        for op, b in boxes:     # fills, in paint order (later ops cover earlier ones, as in the CSG)
            outdoor = look.AIR.get(op.style, {}).get("outdoor", False)
            fill = (0, 0, 0, 0) if op.style.startswith("bld_") else (40, 70, 86, 170) if outdoor else (58, 66, 84, 200)
            x0, y0 = _px(b.x0, b.y1)
            x1, y1 = _px(b.x1, b.y0)
            d.rectangle([x0, y0, x1, y1], fill=fill)
        boxes = [(op, b) for op, b in boxes if not op.style.startswith("bld_")]
        for op, b in boxes:     # edges
            x0, y0 = _px(b.x0, b.y1)
            x1, y1 = _px(b.x1, b.y0)
            d.rectangle([x0, y0, x1, y1], outline=(120, 190, 220, 230))
        for text, x, y, lay in LABELS:
            if lay == lname:
                px, py = _px(x, y)
                bb = d.textbbox((0, 0), text, font=font)
                d.text((px - (bb[2] - bb[0]) / 2, py - 7), text, font=font, fill=(230, 240, 255, 235))
        name = f"{NAME}_{lname}"
        custom_art.MATSRC.mkdir(parents=True, exist_ok=True)
        tga = tools.GAME / "materialsrc" / "overviews" / f"{name}.tga"
        tga.parent.mkdir(parents=True, exist_ok=True)
        img.save(tga)
        (tga.with_suffix(".txt")).write_text("nomip 1\nnolod 1\nclamps 1\nclampt 1\n", encoding="utf-8")
        import subprocess
        subprocess.run([str(tools.BIN / "vtex.exe"), "-nopause", "-mkdir", "-game", str(tools.GAME), str(tga.with_suffix(".txt"))],
                       capture_output=True, timeout=180)
        vtf = tools.GAME / "materials" / "overviews" / f"{name}.vtf"
        vmt = vtf.with_suffix(".vmt")
        vmt.write_text('"UnlitGeneric"\n{\n\t"$basetexture" "overviews/' + name + '"\n\t"$ignorez" "1"\n'
                       '\t"$vertexalpha" "1"\n\t"$translucent" "1"\n}\n', encoding="utf-8")
        pairs += [(f"materials/overviews/{name}.vtf", vtf), (f"materials/overviews/{name}.vmt", vmt)]
        img.save(tools.BUILD / f"overview_{lname}.png")
    txt = [f'// overview description file for {NAME}.bsp\n\n"{NAME}"\n{{\n']
    for lname, posz, _ in LAYERS:
        txt.append(f'\t"{lname}"\n\t{{\n\t\t"material"\t"overviews/{NAME}_{lname}"\n\t\t"pos_x"\t\t"{OV_X0}"\n'
                   f'\t\t"pos_y"\t\t"{OV_Y1}"\n\t\t"pos_z"\t\t"{posz}"\n\t\t"scale"\t\t"{OV_SCALE}"\n\t\t"rotate"\t"0"\n\t}}\n')
    txt.append("}\n")
    f = STAGE / "resource" / "overviews" / f"{NAME}.txt"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text("".join(txt), encoding="utf-8")
    pairs.append((f"resource/overviews/{NAME}.txt", f))
    return pairs


# ----------------------------------------------------------------------------- map paths (objective guides)
Z = 16
ROUTES = {
    # (team, objective): waypoints (x, y, z_floor)
    (2, 1): [(-5200, 150, -384), (-4600, 0, -384), (-4464, 0, -384), (-3680, 0, 0), (-3500, 0, 0), (-2900, 0, 0),
             (-1900, 0, 0), (-1560, -260, 0), (-1150, -350, 0), (-600, -560, 0), (-300, -620, 0), (0, 300, 0),
             (110, 576, 0), (288, 640, 0)],
    (2, 2): [(-2048, 640, 0), (-2048, 280, 0), (-1800, 0, 0), (-1560, -260, 0), (-1150, -350, 0), (-600, -560, 0),
             (-300, -620, 0), (200, 0, 0), (800, 0, 0), (1216, 60, 0), (1216, 540, 192), (1280, 700, 192),
             (1280, 800, 192), (1408, 1000, 192)],
    (2, 3): [(2160, 0, 192), (1872, -192, 192), (1700, -300, 192), (1216, -540, 192), (1216, -60, 0), (1700, 0, 0),
             (2200, 0, 0), (2432, 0, -64), (2700, -290, -128), (3400, -290, -128), (3728, -384, -128),
             (3840, -370, -128), (4400, -370, -384), (4128, -160, -384)],
    (3, 1): [(2160, 0, 192), (1872, 192, 192), (1500, 620, 192), (1216, 540, 192), (1216, 60, 0), (800, 450, 0),
             (500, 608, 0), (288, 600, 0), (140, 576, 0), (-200, 400, 0)],
    (3, 2): [(2160, 0, 192), (1984, 480, 192), (1984, 960, 192), (1700, 960, 192), (1408, 1000, 192)],
    (3, 3): [(4800, 0, -128), (4528, 256, -128), (4450, 370, -128), (4400, 370, -128), (3860, 370, -384),
             (4000, 200, -384), (4128, 160, -384)],
}


def mappaths():
    nodes = []
    for (team, obj), pts in ROUTES.items():
        base = len(nodes) + 1
        for i, (x, y, z) in enumerate(pts):
            nid = base + i
            child = nid + 1 if i < len(pts) - 1 else 0
            nodes.append((nid, x, y, z + Z, child, team, obj if i == 0 else 0))
    out = ['"mappaths"\n{\n']
    for (nid, x, y, z, child, team, obj) in nodes:
        out.append(f'\t"{nid}"\n\t{{\n\t\t"x"\t\t"{x:.6f}"\n\t\t"Y"\t\t"{y:.6f}"\n\t\t"z"\t\t"{z:.6f}"\n'
                   f'\t\t"child"\t\t"{child}"\n\t\t"child2"\t\t"0"\n\t\t"team"\t\t"{team}"\n\t\t"obj"\t\t"{obj}"\n'
                   f'\t\t"subobj"\t\t"0"\n\t\t"hide"\t\t"0"\n\t}}\n')
    out.append("}\n")
    f = STAGE / "resource" / "mappaths" / f"{NAME}.txt"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text("".join(out), encoding="utf-8")
    return [(f"resource/mappaths/{NAME}.txt", f)]


# ----------------------------------------------------------------------------- music + soundscapes
def music():
    f = STAGE / "maps" / f"{NAME}_music.txt"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text('// Paths are relative to the "sound\\music" folder.\n\n"map_music_settings"\n{\n'
                 '\t"intro"\t\t"random/bioxeed - blue rain.mp3"\n}\n', encoding="utf-8")
    return [(f"maps/{NAME}_music.txt", f)]


def _loop(wave, vol, pitch=100, level=None):
    s = f'\t"playlooping"\n\t{{\n\t\t"volume"\t"{vol}"\n\t\t"wave"\t\t"{wave}"\n\t\t"pitch"\t\t"{pitch}"\n'
    if level:
        s += f'\t\t"soundlevel"\t"{level}"\n'
    return s + "\t}\n"


def _random(waves, time, vol, level="SNDLVL_140dB"):
    s = (f'\t"playrandom"\n\t{{\n\t\t"time"\t\t"{time}"\n\t\t"volume"\t"{vol}"\n\t\t"pitch"\t\t"90,110"\n'
         f'\t\t"soundlevel"\t"{level}"\n\t\t"position"\t"random"\n\t\t"rndwave"\n\t\t{{\n')
    for w in waves:
        s += f'\t\t\t"wave"\t"{w}"\n'
    return s + "\t\t}\n\t}\n"


THUNDER = ["ambient/atmosphere/thunder1.wav", "ambient/atmosphere/thunder2.wav", "ambient/atmosphere/thunder3.wav",
           "ambient/atmosphere/thunder4.wav", "silo/thunder1.mp3"]
SOUNDSCAPES = {
    "blackice.street": [_loop("broadcast/street.wav", 0.45), _loop("fedio/outside_windyambient.wav", 0.35),
                        _loop("ambient/atmosphere/city_rumble_loop1.wav", 0.25),
                        _random(THUNDER, "18,40", "0.35,0.6"),
                        _random(["ambient/atmosphere/city_skypass1.wav", "ambient/atmosphere/city_truckpass1.wav"], "20,45", "0.2,0.4")],
    "blackice.plaza": [_loop("fedio/outside_windyambient.wav", 0.45), _loop("vaccine/vaccine_city2.wav", 0.35),
                       _random(THUNDER, "15,35", "0.4,0.7"),
                       _random(["ambient/atmosphere/city_skypass1.wav", "ambient/atmosphere/city_beacon_loop1.wav"], "25,50", "0.2,0.35")],
    "blackice.metro": [_loop("ambient/atmosphere/undercity_loop1.wav", 0.4), _loop("injection/deepambience2.wav", 0.3),
                       _random(["injection/drips/drips02.mp3", "injection/drips/drips05.mp3", "injection/drips/drips13.mp3",
                                "injection/drips/drips19.mp3", "injection/drips/drips24.mp3"], "3,8", "0.2,0.4", "SNDLVL_75dB"),
                       _random(["ambient/machines/razor_train_wheels_loop1.wav", "ambient/alarms/train_horn_distant1.wav"],
                               "30,60", "0.15,0.3")],
    "blackice.tower": [_loop("vaccine/inside_hum1.wav", 0.35), _loop("fedio/hallway_ambient.wav", 0.3),
                       _random(THUNDER, "25,50", "0.12,0.22")],
    "blackice.servers": [_loop("broadcast/server_rotation_loop.wav", 0.4), _loop("fedio/secroom_computer.wav", 0.35),
                         _loop("injection/machinehumloop3.wav", 0.25)],
    "blackice.vault": [_loop("fedio/reactor_core.wav", 0.45), _loop("injection/electrichum.wav", 0.3),
                       _loop("fedio/reactor_ambient.wav", 0.3)],
    "blackice.cyber": [_loop("fedio/cyber_ambient.wav", 0.45), _loop("cybernetic/ambience01.wav", 0.3)],
}


def soundscapes():
    out = []
    for name, parts in SOUNDSCAPES.items():
        out.append(f'"{name}"\n{{\n\t"dsp"\t"1"\n' + "".join(parts) + "}\n\n")
    f = STAGE / "scripts" / f"soundscapes_{NAME}.txt"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text("".join(out), encoding="utf-8")
    return [(f"scripts/soundscapes_{NAME}.txt", f)]


def place_soundscapes(m: VMF):
    spots = [  # soundscape, origin, radius
        ("blackice.metro", (-5200, 100, -300), 1200), ("blackice.metro", (-4200, 0, -150), 500),
        ("blackice.metro", (-4500, 1088, -300), 800), ("blackice.street", (-3000, 0, 80), 1100),
        ("blackice.street", (-2200, 0, 80), 900), ("blackice.street", (-2800, 1120, 80), 1000),
        ("blackice.street", (-2800, -1120, 80), 1000), ("blackice.street", (-2000, 640, 60), 500),
        ("blackice.plaza", (-600, 0, 100), 1500), ("blackice.plaza", (-600, 900, 100), 900),
        ("blackice.plaza", (-600, -900, 100), 900), ("blackice.tower", (288, 576, 60), 300),
        ("blackice.tower", (288, -576, 60), 300), ("blackice.tower", (1200, 0, 120), 900),
        ("blackice.tower", (1408, 980, 260), 450), ("blackice.tower", (2160, 0, 260), 600),
        ("blackice.tower", (2160, 0, 60), 600), ("blackice.tower", (1900, -1088, 260), 800),
        ("blackice.servers", (3130, 0, -60), 900), ("blackice.vault", (4128, -330, -60), 800),
        ("blackice.vault", (4800, 0, -60), 450),
    ]
    for ss, org, rad in spots:
        m.ent("env_soundscape", org, soundscape=ss, radius=str(rad), StartDisabled="0")


# ----------------------------------------------------------------------------- loading screen
def loading_screen(src_image: Path | None):
    """1024x1024 DXT1 at materials/loading/<map>.vtf, built from a beauty screenshot."""
    W = 1024
    if src_image and Path(src_image).exists():
        im = Image.open(src_image).convert("RGB")
        h = W * im.height // im.width
        im = im.resize((W, h))
        canvas = Image.new("RGB", (W, W), (6, 8, 14))
        canvas.paste(im, (0, (W - h) // 2 - 60))
    else:
        canvas = Image.new("RGB", (W, W), (6, 8, 14))
    d = ImageDraw.Draw(canvas)
    d.rectangle([0, 780, W, W], fill=(6, 8, 14))
    d.text((56, 800), "BLACK ICE", font=ImageFont.truetype(custom_art.FONT_SPACE, 96), fill=(235, 245, 255))
    d.text((60, 918), "KURODA SYSTEMS  //  ARCOLOGY BLOCK 7  //  黒田", font=ImageFont.truetype(custom_art.FONT_JP, 30), fill=(255, 60, 70))
    d.text((60, 960), "Punks: crash the BLACK ICE core.   Corps: protect the datavault.",
           font=ImageFont.truetype(custom_art.FONT_BAHN, 24), fill=(170, 190, 210))
    src = tools.GAME / "materialsrc" / "loading" / f"{NAME}.tga"
    src.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(src)
    canvas.save(tools.BUILD / "loading_preview.jpg", quality=90)
    src.with_suffix(".txt").write_text("nomip 1\nnolod 1\n", encoding="utf-8")
    import subprocess
    subprocess.run([str(tools.BIN / "vtex.exe"), "-nopause", "-mkdir", "-game", str(tools.GAME), str(src.with_suffix(".txt"))],
                   capture_output=True, timeout=180)
    vtf = tools.GAME / "materials" / "loading" / f"{NAME}.vtf"
    return [(f"materials/loading/{NAME}.vtf", vtf)] if vtf.exists() else []


def all_pairs(level, loading_src=None):
    pairs = []
    pairs += overview(level)
    pairs += mappaths()
    pairs += music()
    pairs += soundscapes()
    pairs += loading_screen(loading_src)
    return pairs
