"""Monument concept "THE FOUNDER" -- a contour-slice portrait bust of Kuroda Corporation's founder.

A head-and-shoulders bust cut into 27 horizontal plates of black glass/metal (a CT scan cast in stone), with thin
light glowing out of the gaps between the plates: faint warm white in the body (the man), turning cyan up the neck
and brightest at the crown (the mind, living on in the BLACK ICE). Serene, eyes closed, head bowed a little toward
the players coming from the west (-X). Stepped squircle slab plinth (echoes the slices, a warm shadow-gap light under
its black cap) with a lit plaque on the west face: the Kuroda emblem (pointy-top hex ring + vertical diamond) in red
neon over a warm-white KURODA inscription.

The head is a signed distance field (smooth-unioned ellipsoids / capsules, numpy); every plate is the SDF section at
its mid height, sampled on dense polar rays and resampled to a few dozen points (half spent on length, half on
curvature, so the nose and lips keep their points), then extruded with small chamfers.

Run: blender --background --factory-startup --python concept_founder.py   (-> build/concepts/founder_*.png)
"""
import sys
from math import cos, pi, radians, sin
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import stage  # noqa: E402

import bmesh  # noqa: E402
import bpy  # noqa: E402
import numpy as np  # noqa: E402
from mathutils import Matrix  # noqa: E402

# ----------------------------------------------------------------------------- layout (Source units)
Z0 = 128.0                        # plinth top = bust base
PITCH, GAP = 10.0, 2.6            # plate pitch / light gap -> 7.4 u plates
CORE_INSET = 2.0                  # the glowing core sits this far inside the plate edges
CHAMFER = 1.0
TILT = radians(7.0)               # head bowed toward the players
HEAD_SCALE = 1.06                 # monument licence: head a touch large for the shoulders
PIVOT = np.array([6.0, 0.0, 290.0])
RAY_C = (6.0, 0.0)                # polar sampling centre (inside every section)
WARM = (1.0, 0.8, 0.6)            # body light (the man) ...
# ... turning into cyan data light (the mind) up the neck: (z, strength, tint 0 warm .. 1 cyan)
GLOW_Z = (128, 236, 262, 300, 405)
GLOW_S = (0.25, 0.8, 2.2, 3.2, 6.0)
GLOW_T = (0.0, 0.08, 0.85, 1.0, 1.0)

# ----------------------------------------------------------------------------- SDF primitives (numpy, p: (n, 3))


def _v(a):
    return np.asarray(a, dtype=float)


def sd_ellipsoid(p, c, r):
    q, r = p - _v(c), _v(r)
    k0 = np.linalg.norm(q / r, axis=-1)
    k1 = np.linalg.norm(q / (r * r), axis=-1)
    return k0 * (k0 - 1.0) / np.maximum(k1, 1e-9)


def sd_capsule(p, a, b, ra, rb=None):
    a, b = _v(a), _v(b)
    rb = ra if rb is None else rb
    pa, ba = p - a, b - a
    h = np.clip((pa @ ba) / (ba @ ba), 0.0, 1.0)
    return np.linalg.norm(pa - h[:, None] * ba, axis=-1) - (ra + (rb - ra) * h)


def smin(a, b, k):
    h = np.clip(0.5 + 0.5 * (b - a) / k, 0.0, 1.0)
    return b + (a - b) * h - k * h * (1.0 - h)


def smax(a, b, k):
    return -smin(-a, -b, k)


# ----------------------------------------------------------------------------- the founder


def head_sdf(p):
    """Stylised bald head, face toward -X, in the un-tilted head frame (chin ~262, crown ~398)."""
    d = sd_ellipsoid(p, (6, 0, 344), (54, 44, 54))                         # cranium
    d = smin(d, sd_ellipsoid(p, (-20, 0, 350), (29, 39, 31)), 8)           # forehead
    d = smin(d, sd_capsule(p, (-47, -20, 336), (-47, 20, 336), 7), 7)      # brow (strong, shades the eyes)
    d = smin(d, sd_ellipsoid(p, (-17, 0, 306), (32, 36, 32)), 10)          # midface
    d = smin(d, sd_ellipsoid(p, (-6, 0, 292), (36, 35, 22)), 10)           # jaw mass
    for s in (-1, 1):
        d = smin(d, sd_ellipsoid(p, (-28, 34 * s, 318), (16, 10, 11)), 8)            # cheekbones
        d = smin(d, sd_capsule(p, (10, 35 * s, 298), (-35, 13 * s, 268), 8), 9)       # jaw line
    d = smin(d, sd_ellipsoid(p, (-43, 0, 269), (13, 17, 11)), 7)           # chin
    d = smin(d, sd_capsule(p, (-47, 0, 336), (-70, 0, 303), 5, 8), 4)      # nose bridge -> tip
    d = smin(d, sd_ellipsoid(p, (-57, 0, 301), (9, 14, 6)), 5)             # nostril wings
    d = smin(d, sd_ellipsoid(p, (-50, 0, 290), (9, 17, 5)), 4)             # upper lip
    d = smin(d, sd_ellipsoid(p, (-48, 0, 281), (8, 15, 5)), 4)             # lower lip
    for s in (-1, 1):
        d = smax(d, -sd_ellipsoid(p, (-53, 17 * s, 325), (6, 12, 5)), 5)   # shallow eye sockets
        d = smin(d, sd_ellipsoid(p, (-47, 17 * s, 323), (6, 11, 5)), 4)    # full, closed lids
        d = smin(d, sd_ellipsoid(p, (14, 43 * s, 318), (12, 6, 18)), 4)    # ears
    return d


def sd_superprism(p, cx, W, D, n=3.0):
    """Vertical prism with a superellipse section, half extents W (y) / D (x) per point (approximate SDF)."""
    rho = (np.abs((p[:, 0] - cx) / D) ** n + np.abs(p[:, 1] / W) ** n) ** (1.0 / n)
    return (rho - 1.0) * np.minimum(W, D)


def body_sdf(p):
    """Neck, shoulders; a classic bust cut, narrowing to its base on the plinth (world frame)."""
    z = p[:, 2]
    t = np.clip((z - Z0) / (198.0 - Z0), 0.0, 1.0)
    W = 76.0 + 26.0 * np.sin(t * pi / 2)                    # the arm cut curves in toward the base
    D = 45.0 + 5.0 * t
    torso = np.maximum(sd_superprism(p, 12.0, W, D, 3.0),
                       sd_ellipsoid(p, (12, 0, 150), (90, 130, 95)))                    # shoulder line dome
    d = smin(sd_capsule(p, (10, 0, 215), (3, 0, 300), 31), torso, 14)                  # neck
    for s in (-1, 1):
        d = smin(d, sd_ellipsoid(p, (12, 100 * s, 196), (30, 22, 30)), 10)            # deltoids
        d = smin(d, sd_capsule(p, (14, 20 * s, 246), (12, 88 * s, 222), 15), 14)      # trapezius slope
    return d


def sdf(p):
    q = p - PIVOT
    c, s = cos(TILT), sin(TILT)
    local = np.stack([q[:, 0] * c + q[:, 2] * s, q[:, 1], -q[:, 0] * s + q[:, 2] * c], axis=-1) / HEAD_SCALE + PIVOT
    d = smin(head_sdf(local) * HEAD_SCALE, body_sdf(p), 6.0)
    return np.maximum(d, Z0 - p[:, 2])


# ----------------------------------------------------------------------------- slicing

ANG = np.linspace(0.0, 2 * pi, 540, endpoint=False)
RAD = np.arange(160.0, 0.0, -1.0)          # marched from outside in -> outer envelope of the section


def section_radius(z, level=0.0):
    """Outer radius of the section {sdf < level} at height z along each polar ray from RAY_C."""
    cx, cy = RAY_C
    ca, sa = np.cos(ANG), np.sin(ANG)
    X = cx + RAD[None, :] * ca[:, None]
    Y = cy + RAD[None, :] * sa[:, None]
    P = np.stack([X.ravel(), Y.ravel(), np.full(X.size, z)], axis=-1)
    inside = (sdf(P) < level).reshape(X.shape)
    has = inside.any(axis=1)
    first = np.argmax(inside, axis=1)
    r_in = RAD[first]
    r_out = RAD[np.maximum(first - 1, 0)]
    for _ in range(14):
        rm = 0.5 * (r_in + r_out)
        dm = sdf(np.stack([cx + rm * ca, cy + rm * sa, np.full(rm.size, z)], axis=-1)) < level
        r_in, r_out = np.where(dm, rm, r_in), np.where(dm, r_out, rm)
    return np.where(has, 0.5 * (r_in + r_out), 0.0)


def polar_xy(r):
    return np.stack([RAY_C[0] + r * np.cos(ANG), RAY_C[1] + r * np.sin(ANG)], axis=-1)


def resample(xy, n):
    """Closed dense polyline -> n points; half the points follow arc length, half follow curvature."""
    seg = np.roll(xy, -1, axis=0) - xy
    L = np.linalg.norm(seg, axis=1)
    ang = np.arctan2(seg[:, 1], seg[:, 0])
    turn = np.abs((np.roll(ang, -1) - ang + pi) % (2 * pi) - pi)
    w = L / L.sum() + 0.5 * (turn + np.roll(turn, 1)) / max(turn.sum(), 1e-9)
    cum = np.concatenate([[0.0], np.cumsum(w)])
    t = np.linspace(0.0, cum[-1], n, endpoint=False)
    i = np.clip(np.searchsorted(cum, t, side="right") - 1, 0, len(xy) - 1)
    f = (t - cum[i]) / np.maximum(cum[i + 1] - cum[i], 1e-12)
    return xy[i] + f[:, None] * seg[i]


def npts(xy):
    per = np.linalg.norm(np.roll(xy, -1, axis=0) - xy, axis=1).sum()
    return int(np.clip(20 + per / 18.0, 28, 50))


def offset(pts, d):
    """Offset a closed CCW polygon inward by d (mitred, clamped)."""
    prev, nxt = np.roll(pts, 1, axis=0), np.roll(pts, -1, axis=0)
    e1, e2 = pts - prev, nxt - pts
    n1 = np.stack([e1[:, 1], -e1[:, 0]], axis=-1) / np.maximum(np.linalg.norm(e1, axis=1), 1e-9)[:, None]
    n2 = np.stack([e2[:, 1], -e2[:, 0]], axis=-1) / np.maximum(np.linalg.norm(e2, axis=1), 1e-9)[:, None]
    nv = n1 + n2
    nv /= np.maximum(np.linalg.norm(nv, axis=1), 1e-9)[:, None]
    cosh = np.maximum((nv * n1).sum(axis=1), 0.5)
    return pts - nv * (d / cosh)[:, None]


def add_prism(bm, pts, z0, z1, cb=0.0, ct=0.0, glow=None):
    """Closed prism from a CCW polygon with optional bottom/top edge chamfers; returns (flat faces, smooth faces).
    glow = (strength, (r, g, b)) writes the 'glow' / 'tint' vertex attributes read by glow_mat()."""
    pts = np.asarray(pts, dtype=float)
    loops = [(offset(pts, cb), z0), (pts, z0 + cb)] if cb > 0 else [(pts, z0)]
    loops += [(pts, z1 - ct), (offset(pts, ct), z1)] if ct > 0 else [(pts, z1)]
    if glow is not None:
        ls = bm.verts.layers.float.get("glow") or bm.verts.layers.float.new("glow")
        lc = bm.verts.layers.color.get("tint") or bm.verts.layers.color.new("tint")
    vl = []
    for lp, z in loops:
        row = [bm.verts.new((float(x), float(y), z)) for x, y in lp]
        if glow is not None:
            for v in row:
                v[ls] = glow[0]
                v[lc] = (*glow[1], 1.0)
        vl.append(row)
    n = len(pts)
    flat = [bm.faces.new(list(reversed(vl[0]))), bm.faces.new(vl[-1])]
    smooth = []
    for li, (a, b) in enumerate(zip(vl[:-1], vl[1:])):
        wall = (cb > 0 and li == 1) or (cb <= 0 and li == 0)
        for i in range(n):
            j = (i + 1) % n
            f = bm.faces.new((a[i], a[j], b[j], b[i]))
            (smooth if wall else flat).append(f)
    return flat, smooth


def shade(bm, flat, smooth):
    for f in flat:
        f.smooth = False
    for f in smooth:
        f.smooth = True


# ----------------------------------------------------------------------------- materials


def glow_mat(name):
    """Emission driven by the per-vertex 'glow' (strength) and 'tint' (colour) attributes."""
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    s = nt.nodes.new("ShaderNodeAttribute")
    s.attribute_type, s.attribute_name = "GEOMETRY", "glow"
    c = nt.nodes.new("ShaderNodeAttribute")
    c.attribute_type, c.attribute_name = "GEOMETRY", "tint"
    nt.links.new(s.outputs["Fac"], em.inputs["Strength"])
    nt.links.new(c.outputs["Color"], em.inputs["Color"])
    nt.links.new(em.outputs[0], out.inputs[0])
    return m


def glossy_black(name, color=(0.012, 0.012, 0.014), rough=0.2, metal=0.0, coat=0.0):
    """Black glass / lacquered metal: dark dielectric so it keeps a 4 % reflection (a black metal would not)."""
    m = stage.mat(name, color, rough, metal=metal)
    b = m.node_tree.nodes["Principled BSDF"]
    if coat and "Coat Weight" in b.inputs:
        b.inputs["Coat Weight"].default_value = coat
        b.inputs["Coat Roughness"].default_value = 0.04
    return m


# ----------------------------------------------------------------------------- build: bust


def glow_at(z):
    """Gap light by height: faint warm body -> cyan, brighter up the face -> brightest at the crown (the mind)."""
    t = float(np.interp(z, GLOW_Z, GLOW_T))
    col = tuple(WARM[i] + (stage.CYAN[i] - WARM[i]) * t for i in range(3))
    return float(np.interp(z, GLOW_Z, GLOW_S)), col


def build_bust(black, glow):
    plates = []
    for k in range(60):
        z0 = Z0 + k * PITCH
        zc = z0 + (PITCH - GAP) / 2
        r = section_radius(zc)
        if np.sqrt(np.mean(r ** 2)) < 22.0:        # equivalent radius: crown reached, no tiny knob plate on top
            break
        plates.append(dict(k=k, z0=z0, z1=z0 + PITCH - GAP, zc=zc, r=r, ri=section_radius(zc, level=-CORE_INSET)))

    game_tris = 0                                  # estimate for the real prop: no chamfers, cores without caps
    bm = bmesh.new()
    flat_all, smooth_all = [], []
    for pl in plates:
        xy = polar_xy(pl["r"])
        pts = resample(xy, npts(xy))
        fl, sm = add_prism(bm, pts, pl["z0"], pl["z1"], CHAMFER, CHAMFER)
        flat_all += fl
        smooth_all += sm
        game_tris += 4 * len(pts) - 4
    shade(bm, flat_all, smooth_all)
    ob_plates = stage.obj_from_bmesh("founder_plates", bm, black)

    bm = bmesh.new()
    for a, b in zip(plates[:-1], plates[1:]):
        ri = np.maximum(np.minimum(a["ri"], b["ri"]), 0.0)
        if ri.max() < 3.0:
            continue
        xy = polar_xy(ri)
        pts = resample(xy, npts(xy))
        add_prism(bm, pts, a["z1"] - 0.6, b["z0"] + 0.6, glow=glow_at(0.5 * (a["z1"] + b["z0"])))
        game_tris += 2 * len(pts)
    ob_core = stage.obj_from_bmesh("founder_core", bm, glow)
    ob_core.visible_shadow = False
    print(f"FOUNDER game-prop bust estimate: {game_tris} tris")
    return ob_plates, ob_core, plates


# ----------------------------------------------------------------------------- build: plinth + plaque


def squircle(a, b, n=4.0, seg=64):
    t = np.linspace(0.0, 2 * pi, seg, endpoint=False)
    c, s = np.cos(t), np.sin(t)
    return np.stack([a * np.sign(c) * np.abs(c) ** (2 / n), b * np.sign(s) * np.abs(s) ** (2 / n)], axis=-1)


def build_plinth(stone, black, gap_glow):
    bm = bmesh.new()
    fl, sm = [], []
    for (a, b, n, z0, z1, cb, ct) in ((114, 134, 4, 0, 10, 0, 1.5),      # base slab
                                      (104, 124, 4, 10, 20, 0, 1.5),     # second step
                                      (92, 112, 5, 20, 110, 0, 1.5)):    # main block
        f, s = add_prism(bm, squircle(a, b, n), z0, z1, cb, ct)
        fl += f
        sm += s
    shade(bm, fl, sm)
    ob = stage.obj_from_bmesh("plinth", bm, stone)

    bm = bmesh.new()
    f, s = add_prism(bm, squircle(98, 118, 5), 114, Z0, 1.5, 1.5)          # cap slab (black, floats on light)
    shade(bm, f, s)
    stage.obj_from_bmesh("plinth_cap", bm, black)

    bm = bmesh.new()
    add_prism(bm, squircle(89, 109, 5), 109.5, 114.5, glow=(1.6, WARM))    # warm shadow-gap light under the cap
    ob = stage.obj_from_bmesh("plinth_gap", bm, gap_glow)
    ob.visible_shadow = False


def yz_prism(bm, pts_yz, x0, x1):
    """Extrude a CCW (seen from -X) polygon given in (y, z) between x0 (front, -X) and x1."""
    front = [bm.verts.new((x0, y, z)) for y, z in pts_yz]
    back = [bm.verts.new((x1, y, z)) for y, z in pts_yz]
    n = len(front)
    bm.faces.new(front)
    bm.faces.new(list(reversed(back)))
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((front[j], front[i], back[i], back[j]))


def yz_ring(bm, outer, inner, x0, x1):
    """Band between two matching polygons (y, z), extruded in x."""
    n = len(outer)
    fo = [bm.verts.new((x0, y, z)) for y, z in outer]
    fi = [bm.verts.new((x0, y, z)) for y, z in inner]
    bo = [bm.verts.new((x1, y, z)) for y, z in outer]
    bi = [bm.verts.new((x1, y, z)) for y, z in inner]
    for i in range(n):
        j = (i + 1) % n
        bm.faces.new((fo[i], fo[j], fi[j], fi[i]))
        bm.faces.new((bo[j], bo[i], bi[i], bi[j]))
        bm.faces.new((fo[j], fo[i], bo[i], bo[j]))
        bm.faces.new((fi[i], fi[j], bi[j], bi[i]))


def build_plaque(black_glass, red, red_hot, warm):
    xf = -92.0                                   # main block west face
    px0, px1 = xf - 1.6, xf + 1.0                # plaque panel, 1.6 u proud
    PY, PZ0, PZ1 = 44.0, 28.0, 104.0
    stage.box("plaque", px0, -PY, PZ0, px1, PY, PZ1, black_glass)
    # warm-white hairline frame around the panel
    bm = bmesh.new()
    o = [(-PY - 1.2, PZ0 - 1.2), (-PY - 1.2, PZ1 + 1.2), (PY + 1.2, PZ1 + 1.2), (PY + 1.2, PZ0 - 1.2)]
    i = [(-PY, PZ0), (-PY, PZ1), (PY, PZ1), (PY, PZ0)]
    # (y, z) seen from -X: +y is to the viewer's left, so this order is CCW for the viewer
    yz_ring(bm, o, i, px0 + 0.4, px1)
    stage.obj_from_bmesh("plaque_frame", bm, warm)

    ec, R, W = 76.0, 24.0, 3.8                     # emblem centre z, hex vertex radius, band width
    Ri = R - W / cos(radians(30))
    hexo = [(R * cos(radians(90 + 60 * i)), ec + R * sin(radians(90 + 60 * i))) for i in range(6)]
    hexi = [(Ri * cos(radians(90 + 60 * i)), ec + Ri * sin(radians(90 + 60 * i))) for i in range(6)]
    bm = bmesh.new()
    yz_ring(bm, hexo, hexi, px0 - 1.4, px0 + 0.2)
    stage.obj_from_bmesh("emblem_ring", bm, red)
    bm = bmesh.new()
    dia = [(0.0, ec - 0.62 * R), (-0.3 * R, ec), (0.0, ec + 0.62 * R), (0.3 * R, ec)]
    yz_prism(bm, dia, px0 - 1.8, px0 + 0.2)
    stage.obj_from_bmesh("emblem_diamond", bm, red_hot)

    # inscription (a texture on the real prop)
    cu = bpy.data.curves.new("inscription", "FONT")
    cu.body = "K U R O D A"
    cu.size = 7.5
    cu.align_x = "CENTER"
    cu.extrude = 0.3
    ob = bpy.data.objects.new("inscription", cu)
    stage.collection().objects.link(ob)
    ob.data.materials.append(warm)
    ob.location = (px0 - 0.4, 0.0, 37.0)
    ob.rotation_euler = Matrix(((0, 0, -1), (-1, 0, 0), (0, 1, 0))).to_euler()
    # thin warm rule between emblem and inscription
    stage.box("plaque_rule", px0 - 0.6, -22, 47.6, px0 + 0.2, 22, 48.4, warm)


# ----------------------------------------------------------------------------- lights


def build_lights():
    def L(*a, radius=None, spec=1.0, **k):
        ob = stage.light(*a, **k)
        if radius is not None:
            ob.data.shadow_soft_size = radius
        ob.data.specular_factor = spec
        return ob
    # red neon spill from the emblem onto the plinth front + wet floor (no specular blob on the plaque glass)
    L("POINT", "emblem_red", (-130, 0, 76), stage.RED, 1.8e5, radius=10, spec=0.0)
    L("POINT", "emblem_red_floor", (-110, 0, 24), stage.RED, 6e4, radius=10, spec=0.0)
    # soft cool uplights in the court floor grazing the shoulders and the plinth (not the face)
    for s in (-1, 1):
        L("SPOT", f"uplight_{s}", (-170, 150 * s, 6), (0.62, 0.86, 1.0), 1.2e6, target=(0, 80 * s, 210),
          size=34, blend=0.7, radius=30)
    # big soft warm key from the plaza masts, high and in front: gives the face its form
    L("SPOT", "key_warm", (-520, -300, 620), (1.0, 0.85, 0.7), 2.6e7, target=(-30, 0, 320), size=24, blend=0.9,
      radius=120)
    # cool fill from the north-west so the far cheek does not drop to black
    L("SPOT", "fill_cool", (-420, 380, 420), (0.55, 0.75, 1.0), 5e6, target=(-20, 0, 300), size=30, blend=0.9,
      radius=160)
    # cyan rim from the tower side to cut the silhouette out of the facade
    for s in (-1, 1):
        L("SPOT", f"rim_{s}", (300, 230 * s, 470), stage.CYAN, 1.2e7, target=(0, 0, 300), size=34, blend=0.7,
          radius=60)


# ----------------------------------------------------------------------------- main


def tris(objs):
    n = 0
    for ob in objs:
        if ob.type == "MESH":
            n += sum(len(p.vertices) - 2 for p in ob.data.polygons)
    return n


def main():
    stage.reset()
    black = glossy_black("founder_black_glass", (0.022, 0.022, 0.026), rough=0.34, coat=0.9)  # satin black + lacquer
    cap_black = glossy_black("plinth_black", (0.012, 0.012, 0.014), rough=0.22)
    stone = stage.mat("plinth_stone", (0.03, 0.031, 0.036), rough=0.28, metal=0.05)
    glass = glossy_black("plaque_glass", (0.004, 0.004, 0.005), rough=0.08, coat=1.0)
    glow = glow_mat("founder_core_glow")
    gap_glow = glow_mat("plinth_gap_glow")
    red = stage.neon("emblem_red", stage.RED, 10.0)
    red_hot = stage.neon("emblem_red_hot", (1.0, 0.42, 0.42), 14.0)
    warm = stage.neon("warm_white", stage.WHITE, 3.0)

    _, _, plates = build_bust(black, glow)
    build_plinth(stone, cap_black, gap_glow)
    build_plaque(glass, red, red_hot, warm)
    build_lights()

    concept = [o for o in stage.collection().objects]
    top = max(pl["z1"] for pl in plates)
    print(f"FOUNDER plates={len(plates)} top_z={top:.1f} tris={tris(concept)} "
          f"(bust={tris([bpy.data.objects['founder_plates'], bpy.data.objects['founder_core']])})")
    stage.environment()
    # extra portrait view for judging the face up close (added at runtime; the three standard views are unchanged)
    stage.VIEWS.setdefault("closeup", ((-230, -340, 290), (-18, 0, 312), 52))
    stage.render("founder", views=("eye", "approach", "wide", "closeup"))


main()
