"""Asset lookup for Dystopia content: materials (VMT/VTF) and models (MDL).

Search order mirrors gameinfo.txt: dystopia/ then core/.
"""
from __future__ import annotations

import functools
import re
import struct
from pathlib import Path

ROOT = Path(r"M:\SteamLibrary\steamapps\common\Dystopia")
SEARCH = [ROOT / "dystopia", ROOT / "core"]

# ------------------------------------------------------------------ files


def find_file(rel: str) -> Path | None:
    rel = rel.replace("\\", "/").lstrip("/")
    for base in SEARCH:
        p = base / rel
        if p.exists():
            return p
    # case-insensitive fallback (Windows is case-insensitive, but be safe)
    return None


# ------------------------------------------------------------------ VMT

_KV = re.compile(r'"?(\$?[A-Za-z0-9_%]+)"?\s+"([^"]*)"|"?(\$?[A-Za-z0-9_%]+)"?[ \t]+([^\s"{}]+)')


def parse_vmt(text: str) -> dict:
    text = re.sub(r"//[^\n]*", "", text)
    m = re.match(r'\s*"?([A-Za-z0-9_]+)"?\s*\{', text)
    shader = m.group(1) if m else ""
    kv = {"__shader": shader.lower()}
    for mm in _KV.finditer(text):
        k = (mm.group(1) or mm.group(3) or "").lower()
        v = mm.group(2) if mm.group(1) else mm.group(4)
        if k and k not in kv:
            kv[k] = v
    return kv


@functools.lru_cache(maxsize=None)
def vmt(material: str) -> dict | None:
    mat = material.lower().replace("\\", "/")
    p = find_file(f"materials/{mat}.vmt")
    if p is None:
        return None
    kv = parse_vmt(p.read_text(encoding="latin-1", errors="replace"))
    if kv.get("__shader") == "patch" and "include" in kv:
        inc = kv["include"].replace("\\", "/")
        inc = re.sub(r"^materials/", "", inc, flags=re.I)
        inc = re.sub(r"\.vmt$", "", inc, flags=re.I)
        base = vmt(inc) or {}
        merged = dict(base)
        merged.update({k: v for k, v in kv.items() if k not in ("__shader", "include")})
        kv = merged
    return kv


def material_exists(material: str) -> bool:
    return vmt(material) is not None


# ------------------------------------------------------------------ VTF

FMT_BPP = {0: 4, 1: 4, 2: 3, 3: 3, 4: 2, 5: 1, 6: 2, 7: 1, 8: 1, 9: 3, 10: 3, 11: 4, 12: 4, 16: 4, 17: 2,
           18: 2, 19: 2, 21: 2, 22: 2, 23: 4, 24: 8, 25: 8, 26: 4}
DXT = {13: (8, 1), 14: (16, 2), 15: (16, 3), 20: (8, 1)}


def _level_size(fmt, w, h):
    if fmt in DXT:
        bs, _ = DXT[fmt]
        return max(1, (w + 3) // 4) * max(1, (h + 3) // 4) * bs
    return w * h * FMT_BPP.get(fmt, 4)


@functools.lru_cache(maxsize=4096)
def vtf_header(path: str):
    with open(path, "rb") as f:
        data = f.read(128)
    if data[:4] != b"VTF\0":
        return None
    vmaj, vmin, hsize = struct.unpack_from("<III", data, 4)
    w, h, flags, frames, first = struct.unpack_from("<HHIHH", data, 16)
    fmt, = struct.unpack_from("<i", data, 52)
    mips = data[56]
    lfmt, = struct.unpack_from("<i", data, 57)
    lw, lh = data[61], data[62]
    depth = struct.unpack_from("<H", data, 63)[0] if vmin >= 2 else 1
    return {"ver": (vmaj, vmin), "hsize": hsize, "w": w, "h": h, "flags": flags, "frames": frames,
            "fmt": fmt, "mips": mips, "lfmt": lfmt, "lw": lw, "lh": lh, "depth": max(1, depth)}


def texture_path(material: str) -> Path | None:
    kv = vmt(material)
    if not kv:
        return None
    base = kv.get("$basetexture") or kv.get("$envmap") or kv.get("$bumpmap")
    if not base:
        return None
    base = base.replace("\\", "/")
    base = re.sub(r"\.vtf$", "", base, flags=re.I)
    return find_file(f"materials/{base}.vtf")


def texture_size(material: str) -> tuple[int, int] | None:
    p = texture_path(material)
    if not p:
        return None
    hd = vtf_header(str(p))
    return (hd["w"], hd["h"]) if hd else None


def decode_vtf(path: Path, max_dim=128):
    """Decode one mip level (largest <= max_dim) of frame 0 to a PIL image."""
    from PIL import Image
    hd = vtf_header(str(path))
    if not hd:
        return None
    raw = Path(path).read_bytes()
    fmt, w, h, mips = hd["fmt"], hd["w"], hd["h"], hd["mips"]
    frames = max(1, hd["frames"])
    faces = 6 if hd["flags"] & 0x4000 else 1  # ENVMAP
    # offset of high-res data
    if hd["ver"][1] >= 3:
        nres, = struct.unpack_from("<I", raw, 68)
        off = None
        for i in range(nres):
            tag = raw[80 + i * 8: 83 + i * 8]
            val, = struct.unpack_from("<I", raw, 84 + i * 8)
            if tag == b"\x30\x00\x00":
                off = val
        if off is None:
            return None
    else:
        off = hd["hsize"]
        if hd["lfmt"] != -1 and hd["lw"] and hd["lh"]:
            off += _level_size(hd["lfmt"], hd["lw"], hd["lh"])
    # mips stored smallest -> largest
    levels = []
    for m in range(mips):
        lw, lh = max(1, w >> m), max(1, h >> m)
        levels.append((m, lw, lh))
    pick = next((lv for lv in levels if max(lv[1], lv[2]) <= max_dim), levels[-1])
    pos = off
    for m in range(mips - 1, -1, -1):
        lw, lh = max(1, w >> m), max(1, h >> m)
        size = _level_size(fmt, lw, lh) * frames * faces * hd["depth"]
        if m == pick[0]:
            data = raw[pos: pos + _level_size(fmt, lw, lh)]
            break
        pos += size
    lw, lh = pick[1], pick[2]
    try:
        if fmt in DXT:
            bw, bh = max(4, (lw + 3) // 4 * 4), max(4, (lh + 3) // 4 * 4)
            img = Image.frombytes("RGBA", (bw, bh), data, "bcn", DXT[fmt][1])
            if (bw, bh) != (lw, lh):
                img = img.crop((0, 0, lw, lh))
            return img
        modes = {0: ("RGBA", "RGBA"), 1: ("RGBA", "ABGR"), 2: ("RGB", "RGB"), 3: ("RGB", "BGR"),
                 12: ("RGBA", "BGRA"), 11: ("RGBA", "ARGB"), 16: ("RGB", "BGRX"), 5: ("L", "L"),
                 6: ("LA", "LA"), 8: ("L", "L"), 9: ("RGB", "RGB"), 10: ("RGB", "BGR"), 4: ("RGB", "RGB;16"),
                 17: ("RGB", "BGR;16"), 23: ("RGBA", "RGBA"), 22: ("LA", "LA")}
        if fmt in modes:
            mode, rawmode = modes[fmt]
            return Image.frombytes(mode, (lw, lh), data, "raw", rawmode)
    except Exception:
        return None
    return None


# ------------------------------------------------------------------ MDL


@functools.lru_cache(maxsize=None)
def mdl_info(model: str) -> dict | None:
    """Read hull/view bbox from an MDL header (studiohdr_t v44-49)."""
    p = find_file(model if model.lower().startswith("models/") else f"models/{model}")
    if p is None:
        return None
    full = p.read_bytes()
    data = full[:408]
    if data[:4] != b"IDST":
        return None
    ver, = struct.unpack_from("<i", data, 4)
    f = struct.unpack_from("<18f", data, 80)
    eye, illum = f[0:3], f[3:6]
    hull_min, hull_max = f[6:9], f[9:12]
    view_min, view_max = f[12:15], f[15:18]
    flags, = struct.unpack_from("<i", data, 152)
    kvi, kvs = struct.unpack_from("<ii", data, 312)
    kv = full[kvi:kvi + kvs].decode("latin-1", errors="replace").lower() if 0 < kvi < len(full) and kvs > 0 else ""
    has_propdata = "prop_data" in kv
    allow_static = re.search(r'"allowstatic"\s*"1"', kv) is not None
    static_ok = bool(flags & 0x10) and (not has_propdata or allow_static)
    return {"ver": ver, "hull_min": hull_min, "hull_max": hull_max, "view_min": view_min,
            "view_max": view_max, "flags": flags, "path": str(p), "static_ok": static_ok, "keyvalues": kv}


def model_exists(model: str) -> bool:
    return mdl_info(model) is not None


# ------------------------------------------------------------------ contact sheets


def list_materials(folder: str, bases=None) -> list[str]:
    out = set()
    for base in (bases or SEARCH):
        d = base / "materials" / folder
        if not d.exists():
            continue
        for p in d.rglob("*.vmt"):
            rel = p.relative_to(base / "materials").as_posix()[:-4].lower()
            out.add(rel)
    return sorted(out)


def contact_sheet(materials, out_path, cols=8, thumb=128, title=""):
    from PIL import Image, ImageDraw, ImageFont
    font = ImageFont.load_default()
    rows = (len(materials) + cols - 1) // cols
    lab = 26
    sheet = Image.new("RGB", (cols * thumb, rows * (thumb + lab) + 20), (24, 24, 28))
    d = ImageDraw.Draw(sheet)
    d.text((4, 4), title, fill=(255, 255, 0), font=font)
    for i, mat in enumerate(materials):
        x, y = (i % cols) * thumb, 20 + (i // cols) * (thumb + lab)
        p = texture_path(mat)
        img = decode_vtf(p, max_dim=thumb) if p else None
        if img is not None:
            has_alpha = False
            if img.mode in ("RGBA", "LA"):
                lo, hi = img.getchannel("A").getextrema()
                has_alpha = lo < 250
            img = img.convert("RGB").resize((thumb - 4, thumb - 4))
            sheet.paste(img, (x + 2, y + 2))
            if has_alpha:
                d.polygon([(x + thumb - 18, y + 2), (x + thumb - 2, y + 2), (x + thumb - 2, y + 18)], fill=(255, 0, 255))
        else:
            d.rectangle([x + 2, y + 2, x + thumb - 2, y + thumb - 2], outline=(120, 0, 0))
        sz = texture_size(mat)
        name = mat.split("/", 1)[-1] if "/" in mat else mat
        d.text((x + 2, y + thumb), name[:21], fill=(230, 230, 230), font=font)
        d.text((x + 2, y + thumb + 12), f"{name[21:33]} {sz[0]}x{sz[1]}" if sz else name[21:33], fill=(150, 200, 255), font=font)
    sheet.save(out_path, quality=88)
    return out_path
