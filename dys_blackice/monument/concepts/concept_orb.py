"""Monument concept "DATA ORB" -- a globe of light levitating over a black hex monolith.

Hex plinth + tapered hex drum (the solid cover mass) crowned by a projector ring -> a cone of light lifts a hollow
globe of cyan light rings (3 great-circle meridians = 6 half-meridians on the hex axes, equator + 4 parallels,
warm-white network nodes on the equator) -> the Kuroda emblem (red hex ring + vertical diamond) floats as a
hologram at the globe's centre, facing west/east -> one tilted orbit band (black metal, red neon line, two
warm-white data packets) circles it.

Run: blender --background --factory-startup --python concept_orb.py
"""
import sys
from math import atan2, cos, pi, radians, sin
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import stage  # noqa: E402

import bmesh  # noqa: E402
import bpy  # noqa: E402
from mathutils import Matrix, Vector  # noqa: E402

# ----------------------------------------------------------------------------- dimensions (Source units)
ZC, R = 276, 112                 # globe centre height, globe radius (diameter 224) -> globe spans z 164..388
TUBE, TUBE_EQ = 2.0, 3.0         # light tube radii (meridians/parallels, equator)
LATS = (30, 60)                  # parallels at +-these latitudes (+ equator)
MERID_AZ = (30, 90, 150)         # great-circle planes (90 = YZ plane: the globe's outline seen from the west)
DRUM_Z0, DRUM_Z1, DRUM_R0, DRUM_R1 = 34, 112, 104, 90   # hex drum (cover mass) under the floating globe
TOP = DRUM_Z1 + 6                # projector deck (lip top); the gap to the globe (z 164) holds the light cone
ORBIT_R, ORBIT_TILT, ORBIT_AZ = 142, 26, 135   # orbit band radius, tilt from horizontal, tilt direction
EMB_O, EMB_I, EMB_D = 60, 49, 4  # emblem hex ring outer/inner corner radius, half depth (x)
DIA_H, DIA_W, DIA_D = 34, 19, 9  # diamond half height / half width (y) / half depth (x)


# ----------------------------------------------------------------------------- helpers
def finish(name, bm, material, sharp=35.0):
    """Smooth shading with edges sharper than `sharp` degrees split (Blender's 'smooth by angle')."""
    bm.normal_update()
    for e in bm.edges:
        if len(e.link_faces) == 2 and e.calc_face_angle(0.0) > radians(sharp):
            e.smooth = False
    for f in bm.faces:
        f.smooth = True
    return stage.obj_from_bmesh(name, bm, material, smooth=True)


def lathe(name, prof, material, sides=32, cap_bottom=True, cap_top=True, sharp=35.0):
    """Surface of revolution through (r, z) profile points (bottom to top)."""
    bm = bmesh.new()
    rings = [[bm.verts.new((r * cos(2 * pi * i / sides), r * sin(2 * pi * i / sides), z)) for i in range(sides)]
             for r, z in prof]
    for lo, hi in zip(rings, rings[1:]):
        for i in range(sides):
            j = (i + 1) % sides
            bm.faces.new((lo[i], lo[j], hi[j], hi[i]))
    if cap_bottom:
        bm.faces.new(list(reversed(rings[0])))
    if cap_top:
        bm.faces.new(rings[-1])
    return finish(name, bm, material, sharp)


def sweep_ring(name, rad, section, material, c=(0, 0, 0), u=(1, 0, 0), v=(0, 1, 0), seg=48, a0=0.0, a1=360.0, sharp=35.0):
    """Sweep a closed cross-section [(radial, axial), ...] (CCW) around the circle c + rad*(cos a u + sin a v)."""
    c, u, v = Vector(c), Vector(u).normalized(), Vector(v).normalized()
    n = u.cross(v)
    full = abs(a1 - a0) >= 359.999
    steps = seg if full else max(2, round(seg * abs(a1 - a0) / 360))
    count = steps if full else steps + 1
    bm = bmesh.new()
    rows = []
    for i in range(count):
        a = radians(a0 + (a1 - a0) * i / steps)
        er = cos(a) * u + sin(a) * v
        rows.append([bm.verts.new(c + rad * er + dr * er + dz * n) for dr, dz in section])
    k = len(section)
    for i in range(count if full else count - 1):
        A, B = rows[i], rows[(i + 1) % count]
        for j in range(k):
            m = (j + 1) % k
            bm.faces.new((A[j], B[j], B[m], A[m]))
    if not full:
        bm.faces.new(list(reversed(rows[0])))
        bm.faces.new(rows[-1])
    return finish(name, bm, material, sharp)


def tube_section(r, sides=6):
    return [(r * cos(2 * pi * j / sides), r * sin(2 * pi * j / sides)) for j in range(sides)]


def rect_section(t, w):
    return [(t, -w), (t, w), (-t, w), (-t, -w)]


def closed_mesh(name, verts, faces, material, sharp=35.0):
    bm = bmesh.new()
    vs = [bm.verts.new(p) for p in verts]
    for f in faces:
        bm.faces.new([vs[i] for i in f])
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    return finish(name, bm, material, sharp)


def hex_ring_yz(name, r_out, r_in, d, zc, material):
    """Pointy-top hexagon outline in the YZ plane (faces west / east), depth 2d along x."""
    def P(r, k, x):
        return (x, r * cos(radians(90 + 60 * k)), zc + r * sin(radians(90 + 60 * k)))
    verts, faces = [], []
    for x in (-d, d):                     # side s (0 west, 1 east): outer = 12s + k, inner = 12s + 6 + k
        verts += [P(r_out, k, x) for k in range(6)] + [P(r_in, k, x) for k in range(6)]
    for k in range(6):
        l = (k + 1) % 6
        for s in (0, 1):
            faces.append((12 * s + k, 12 * s + l, 12 * s + 6 + l, 12 * s + 6 + k))
        faces.append((k, 12 + k, 12 + l, l))
        faces.append((6 + k, 6 + l, 18 + l, 18 + k))
    return closed_mesh(name, verts, faces, material, sharp=20)


def diamond(name, c, h, w, d, material):
    c = Vector(c)
    v = [c + Vector(o) for o in ((0, 0, h), (0, 0, -h), (-d, 0, 0), (0, w, 0), (d, 0, 0), (0, -w, 0))]
    faces = [(0, 2 + i, 2 + (i + 1) % 4) for i in range(4)] + [(1, 2 + (i + 1) % 4, 2 + i) for i in range(4)]
    return closed_mesh(name, v, faces, material, sharp=10)


def hexagon_face_yz(name, r, zc, material, x=0.0):
    bm = bmesh.new()
    bm.faces.new([bm.verts.new((x, r * cos(radians(90 + 60 * k)), zc + r * sin(radians(90 + 60 * k)))) for k in range(6)])
    return stage.obj_from_bmesh(name, bm, material)


def lin(c):
    """Palette values are display sRGB (e.g. Kuroda red 255,60,70); Blender colour inputs are scene-linear."""
    return tuple(((x + 0.055) / 1.055) ** 2.4 if x > 0.04045 else x / 12.92 for x in c)


def holo_fresnel(name, color, strength=3.0, power=2.5, cull=True):
    """Additive glow that brightens toward the silhouette (energy-shell look); transparent face-on."""
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    lw = nt.nodes.new("ShaderNodeLayerWeight")
    lw.inputs["Blend"].default_value = 0.5
    pw = nt.nodes.new("ShaderNodeMath")
    pw.operation = "POWER"
    pw.inputs[1].default_value = power
    mu = nt.nodes.new("ShaderNodeMath")
    mu.operation = "MULTIPLY"
    mu.inputs[1].default_value = strength
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = (*color, 1)
    tr = nt.nodes.new("ShaderNodeBsdfTransparent")
    add = nt.nodes.new("ShaderNodeAddShader")
    nt.links.new(lw.outputs["Facing"], pw.inputs[0])
    nt.links.new(pw.outputs[0], mu.inputs[0])
    nt.links.new(mu.outputs[0], em.inputs["Strength"])
    nt.links.new(tr.outputs[0], add.inputs[0])
    nt.links.new(em.outputs[0], add.inputs[1])
    nt.links.new(add.outputs[0], out.inputs[0])
    if hasattr(m, "surface_render_method"):
        m.surface_render_method = "BLENDED"
    if hasattr(m, "use_backface_culling"):
        m.use_backface_culling = cull
    return m


def drum_r(z):
    return DRUM_R0 + (DRUM_R1 - DRUM_R0) * (z - DRUM_Z0) / (DRUM_Z1 - DRUM_Z0)


def lettering(body, size, z, material, faces_az):
    """Flat neon lettering on the tapered drum faces (a texture in the real model; geometry here)."""
    cu = bpy.data.curves.new("kuroda_txt", type="FONT")
    cu.body, cu.size, cu.align_x, cu.align_y, cu.resolution_u = body, size, "CENTER", "CENTER", 2
    tmp = bpy.data.objects.new("txt_tmp", cu)
    stage.collection().objects.link(tmp)
    me = bpy.data.meshes.new_from_object(tmp.evaluated_get(bpy.context.evaluated_depsgraph_get()))
    bpy.data.objects.remove(tmp)
    me.materials.append(material)
    c30 = cos(radians(30))
    tilt = atan2((DRUM_R0 - DRUM_R1) * c30, DRUM_Z1 - DRUM_Z0)      # the drum faces lean back by this much
    for az in faces_az:
        a = radians(az)
        d = Vector((cos(a), sin(a), 0))
        x = Vector((-sin(a), cos(a), 0))
        y = -sin(tilt) * d + cos(tilt) * Vector((0, 0, 1))
        m = Matrix((x, y, x.cross(y))).transposed().to_4x4()
        m.translation = d * (drum_r(z) * c30 + 0.4) + Vector((0, 0, z))
        ob = bpy.data.objects.new(f"lettering{az}", me)
        ob.matrix_world = m
        stage.collection().objects.link(ob)


# ============================================================================= build
sc = stage.reset()
CYAN, RED, WHITE = lin(stage.CYAN), lin(stage.RED), lin(stage.WHITE)
metal = stage.mat("kuroda_metal", (0.014, 0.015, 0.02), rough=0.2, metal=0.8)
cyan = stage.neon("neon_cyan", CYAN, 2.2)
cyan_hot = stage.neon("neon_cyan_hot", CYAN, 4.0)
cyan_dim = stage.neon("neon_cyan_dim", CYAN, 1.6)
red = stage.neon("neon_red", RED, 6.0)
red_hot = stage.neon("neon_red_hot", lin((1.0, 0.45, 0.45)), 7.0)
white = stage.neon("neon_white", WHITE, 8.0)
holo_red = stage.hologram("holo_red", RED, 1.5, 0.10)
haze = holo_fresnel("holo_haze", CYAN, strength=0.7, power=4.0, cull=True)

# --- base: hex plinth (flat face to the west, phase 30) + tapered hex drum = the solid cover mass
stage.prism("ped_tier1", 146, 0, 10, metal, phase=30)
stage.prism("ped_seam", 138, 10, 12, cyan, phase=30)                    # cyan light gap between the tiers
stage.prism("ped_tier2", 128, 12, DRUM_Z0, metal, phase=30)
stage.prism("drum", DRUM_R0, DRUM_Z0, DRUM_Z1, metal, phase=30, r_top=DRUM_R1)
stage.prism("drum_redline", drum_r(96) + 0.8, 96, 99, red, phase=30, r_top=drum_r(99) + 0.8)   # Kuroda red line
stage.prism("drum_lip", DRUM_R1 + 6, DRUM_Z1, TOP, metal, phase=30)       # overhanging crown -> crisp shadow line
stage.prism("drum_footline", drum_r(DRUM_Z0 + 4) + 0.8, DRUM_Z0 + 4, DRUM_Z0 + 5.5, cyan_dim, phase=30,
            r_top=drum_r(DRUM_Z0 + 5.5) + 0.8)
lettering("KURODA", 15, 66, red, [60 * k for k in range(6)])
# projector deck: two concentric light rings and a hot lens
sweep_ring("emitter_outer", 72, tube_section(2.0), cyan_hot, c=(0, 0, TOP + 0.5), seg=64)
sweep_ring("emitter_inner", 44, tube_section(1.5), cyan, c=(0, 0, TOP + 0.5), seg=48)
stage.prism("lens", 16, TOP, TOP + 1.5, cyan_hot, sides=24)

# a slim shaft of light from the lens up to the globe's south pole, fading as it rises (stacked bands of falling
# strength = the gradient texture of the real additive material). A wide cone read as a solid glass stand, so the
# gap stays open and the globe visibly floats.
BEAM = [(17, TOP + 1), (14, TOP + 12), (11.5, TOP + 24), (10, TOP + 36), (9, ZC - R - 3)]
for i, (lo, hi) in enumerate(zip(BEAM, BEAM[1:])):
    bmat = holo_fresnel(f"holo_beam{i}", CYAN, strength=3.2 * (1 - i / 5.5) ** 1.5, power=1.2, cull=False)
    lathe(f"beam{i}", [lo, hi], bmat, sides=24, cap_bottom=False, cap_top=False)

# --- globe of light
ZERO = (0, 0, ZC)
for az in MERID_AZ:
    a = radians(az)
    sweep_ring(f"meridian{az}", R, tube_section(TUBE), cyan, c=ZERO, u=(cos(a), sin(a), 0), v=(0, 0, 1), seg=56)
sweep_ring("equator", R, tube_section(TUBE_EQ), cyan_hot, c=ZERO, seg=64)
for lat in LATS:
    for s in (-1, 1):
        rr, zz = R * cos(radians(lat)), ZC + s * R * sin(radians(lat))
        sweep_ring(f"parallel{s * lat}", rr, tube_section(TUBE), cyan, c=(0, 0, zz), seg=48 if lat < 45 else 32)
for k in range(6):                     # network nodes where the six meridians cross the equator
    az = radians(30 + 60 * k)
    stage.sphere(f"node{k}", 5.0, white, loc=(R * cos(az), R * sin(az), ZC), segments=8, rings=6)
for s in (-1, 1):                      # hex pole caps; the north one carries a red status light
    z0, z1 = sorted((ZC + s * (R - 3), ZC + s * (R + 5)))
    stage.prism(f"pole_cap{s}", 10, z0, z1, metal, phase=30)
stage.prism("pole_light", 6.5, ZC + R + 5, ZC + R + 6, red, phase=30)
stage.sphere("globe_haze", R + 1, haze, loc=ZERO, segments=32, rings=16)

# --- Kuroda emblem hologram at the centre (faces west / east)
hex_ring_yz("emblem_ring", EMB_O, EMB_I, EMB_D, ZC, red)
hexagon_face_yz("emblem_membrane", EMB_I, ZC, holo_red)
diamond("emblem_diamond", ZERO, DIA_H, DIA_W, DIA_D, red_hot)

# --- tilted orbit band: black metal ribbon, red neon line on its outer face, two warm-white data packets
t, ph = radians(ORBIT_TILT), radians(ORBIT_AZ)
n = Vector((sin(t) * cos(ph), sin(t) * sin(ph), cos(t)))
u = Vector((0, 0, 1)).cross(n).normalized()
v = n.cross(u)
sweep_ring("orbit_band", ORBIT_R, rect_section(1.8, 6.0), metal, c=ZERO, u=u, v=v, seg=72)
sweep_ring("orbit_line", ORBIT_R + 2.0, rect_section(0.6, 1.6), red, c=ZERO, u=u, v=v, seg=72)
for i, a in enumerate((45, 225)):
    sweep_ring(f"packet{i}", ORBIT_R + 2.5, tube_section(3.2, 8), white, c=ZERO, u=u, v=v, seg=120, a0=a - 4, a1=a + 4)

# ----------------------------------------------------------------------------- lights
for x in (-24, 24):
    stage.light("POINT", f"emblem_red{x}", (x, 0, ZC), RED, 6e5)
stage.light("POINT", "projector_glow", (0, 0, TOP + 24), CYAN, 2.0e5)
for k in range(6):                     # cool floor uplights in the court (light_spot entities in the map)
    az = radians(30 + 60 * k)
    d = Vector((cos(az), sin(az), 0))
    stage.light("SPOT", f"uplight{k}", tuple(d * 250 + Vector((0, 0, 4))), lin((0.55, 0.82, 1.0)), 6.0e5,
                target=(0, 0, 150), size=34, blend=0.6)

# ----------------------------------------------------------------------------- report + render
objs = [ob for ob in stage.collection().objects if ob.type == "MESH"]
tris = sum(len(p.vertices) - 2 for ob in objs for p in ob.data.polygons)
mats = sorted({s.material.name for ob in objs for s in ob.material_slots})
pts = [ob.matrix_world @ vx.co for ob in objs for vx in ob.data.vertices]
print(f"ORB_STATS tris={tris} objects={len(objs)} materials={mats}")
print(f"ORB_STATS top={max(p.z for p in pts):.1f} max_radius={max(Vector((p.x, p.y)).length for p in pts):.1f}")

stage.environment()
stage.render("orb")
