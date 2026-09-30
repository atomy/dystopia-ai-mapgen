"""Shared preview stage for monument concept sketches (Blender, headless).

    import stage
    stage.reset()
    ...build the concept at the origin: Source units, base centre on z=0, +X east (toward the Kuroda tower),
       -X west (the players' approach)...
    stage.environment()
    stage.render("orb")        # -> dys_blackice/build/concepts/orb_{eye,approach,wide}.png

Run:  blender --background --factory-startup --python concept_orb.py
The stage is the same rough plaza stand-in the real monument previews use (sunken court, plaza deck, lit tower
facade, night sky, bloom), so the concepts can be compared side by side.
"""
from __future__ import annotations

from math import cos, radians, sin
from pathlib import Path

import bmesh
import bpy
from mathutils import Vector

HERE = Path(__file__).resolve().parent
OUT = HERE.parents[1] / "build" / "concepts"
GAME = Path(r"M:\SteamLibrary\steamapps\common\Dystopia\dystopia")
RED, CYAN, WHITE, AMBER = (1.0, 0.235, 0.275), (0.35, 0.86, 1.0), (1.0, 0.95, 0.9), (1.0, 0.6, 0.2)

VIEWS = {  # name: (camera position, look-at, horizontal fov) -- same as the real monument previews
    "eye": ((-370, -230, 64), (0, 0, 184), 90),          # player standing in the sunken court
    "approach": ((-1152, -40, 128), (0, 0, 200), 90),    # entering the plaza from the market street
    "wide": ((-780, -600, 430), (0, 0, 175), 50),        # elevated three-quarter view
}


def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    return bpy.context.scene


def collection(name="concept"):
    sc = bpy.context.scene
    c = bpy.data.collections.get(name)
    if c is None:
        c = bpy.data.collections.new(name)
        sc.collection.children.link(c)
    return c


# ----------------------------------------------------------------------------- materials

def mat(name, color, rough=0.35, metal=0.6, emit=0.0, emit_color=None, alpha=1.0):
    """Principled material. emit > 0 makes it glow (emit_color defaults to color); alpha < 1 = see-through."""
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if emit:
        b.inputs["Emission Color"].default_value = (*(emit_color or color), 1)
        b.inputs["Emission Strength"].default_value = emit
    if alpha < 1:
        b.inputs["Alpha"].default_value = alpha
        if hasattr(m, "surface_render_method"):
            m.surface_render_method = "BLENDED"
        if hasattr(m, "use_backface_culling"):
            m.use_backface_culling = False
    return m


def neon(name, color, strength=8.0):
    """Pure emission (neon tubes, light strips, holograms)."""
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = (*color, 1)
    em.inputs["Strength"].default_value = strength
    nt.links.new(em.outputs[0], out.inputs[0])
    return m


def hologram(name, color, strength=3.0, alpha=0.35):
    """See-through glowing surface (hologram membranes, glass with light)."""
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    em = nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value = (*color, 1)
    em.inputs["Strength"].default_value = strength
    tr = nt.nodes.new("ShaderNodeBsdfTransparent")
    mix = nt.nodes.new("ShaderNodeMixShader")
    mix.inputs[0].default_value = alpha
    nt.links.new(tr.outputs[0], mix.inputs[1])
    nt.links.new(em.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], out.inputs[0])
    if hasattr(m, "surface_render_method"):
        m.surface_render_method = "BLENDED"
    if hasattr(m, "use_backface_culling"):
        m.use_backface_culling = False
    return m


# ----------------------------------------------------------------------------- geometry helpers

def obj_from_bmesh(name, bm, material, coll=None, smooth=False):
    me = bpy.data.meshes.new(name)
    bm.to_mesh(me)
    bm.free()
    if smooth:
        for p in me.polygons:
            p.use_smooth = True
    me.materials.append(material)
    ob = bpy.data.objects.new(name, me)
    (coll or collection()).objects.link(ob)
    return ob


def box(name, x0, y0, z0, x1, y1, z1, material, coll=None):
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co = Vector(((x0 + x1) / 2 + v.co.x * (x1 - x0), (y0 + y1) / 2 + v.co.y * (y1 - y0),
                       (z0 + z1) / 2 + v.co.z * (z1 - z0)))
    return obj_from_bmesh(name, bm, material, coll)


def prism(name, r, z0, z1, material, sides=6, phase=0.0, r_top=None, coll=None, cx=0.0, cy=0.0):
    """Vertical n-gon prism / frustum centred on (cx, cy); phase in degrees."""
    bm = bmesh.new()
    rt = r if r_top is None else r_top
    lo = [bm.verts.new((cx + r * cos(radians(phase + 360 * i / sides)), cy + r * sin(radians(phase + 360 * i / sides)), z0))
          for i in range(sides)]
    hi = [bm.verts.new((cx + rt * cos(radians(phase + 360 * i / sides)), cy + rt * sin(radians(phase + 360 * i / sides)), z1))
          for i in range(sides)]
    bm.faces.new(list(reversed(lo)))
    bm.faces.new(hi)
    for i in range(sides):
        j = (i + 1) % sides
        bm.faces.new((lo[i], lo[j], hi[j], hi[i]))
    return obj_from_bmesh(name, bm, material, coll)


def torus(name, major, minor, material, loc=(0, 0, 0), rot=(0, 0, 0), major_seg=48, minor_seg=12, coll=None):
    bm = bmesh.new()
    for i in range(major_seg):
        a = 2 * 3.141592653589793 * i / major_seg
        for j in range(minor_seg):
            b = 2 * 3.141592653589793 * j / minor_seg
            bm.verts.new(((major + minor * cos(b)) * cos(a), (major + minor * cos(b)) * sin(a), minor * sin(b)))
    bm.verts.ensure_lookup_table()
    for i in range(major_seg):
        for j in range(minor_seg):
            a, b = i * minor_seg + j, i * minor_seg + (j + 1) % minor_seg
            c, d = ((i + 1) % major_seg) * minor_seg + (j + 1) % minor_seg, ((i + 1) % major_seg) * minor_seg + j
            bm.faces.new((bm.verts[a], bm.verts[d], bm.verts[c], bm.verts[b]))
    ob = obj_from_bmesh(name, bm, material, coll, smooth=True)
    ob.location, ob.rotation_euler = loc, rot
    return ob


def sphere(name, radius, material, loc=(0, 0, 0), segments=32, rings=16, coll=None):
    bm = bmesh.new()
    bmesh.ops.create_uvsphere(bm, u_segments=segments, v_segments=rings, radius=radius)
    ob = obj_from_bmesh(name, bm, material, coll, smooth=True)
    ob.location = loc
    return ob


def light(kind, name, loc, color, power, target=None, size=50, blend=0.3, coll=None):
    """kind: POINT / SPOT / AREA. power in Blender watts at this 1-unit-per-Source-unit scale (points: 1e5..3e6)."""
    ld = bpy.data.lights.new(name, kind)
    ld.color = color
    ld.energy = power
    if kind == "SPOT":
        ld.spot_size = radians(size)
        ld.spot_blend = blend
    ob = bpy.data.objects.new(name, ld)
    ob.location = loc
    (coll or collection("lights")).objects.link(ob)
    if target is not None:
        aim(ob, target)
    return ob


def aim(ob, target):
    ob.rotation_euler = (Vector(target) - Vector(ob.location)).to_track_quat("-Z", "Y").to_euler()


# ----------------------------------------------------------------------------- stage + render

def environment():
    """Plaza stand-in: sunken court (768 x 896, floor z 0, plaza deck +64), lit tower facade, side blocks, night."""
    coll = collection("stage")
    wet = mat("stage_wet_concrete", (0.035, 0.036, 0.042), 0.22, metal=0.0)
    deck = mat("stage_plaza", (0.05, 0.05, 0.058), 0.35, metal=0.0)
    wins = GAME / "materialsrc" / "blackice" / "lit_windows.tga"
    facade = mat("stage_facade", (0.02, 0.02, 0.03), 0.4, metal=0.0)
    if wins.exists():
        nt = facade.node_tree
        b = nt.nodes["Principled BSDF"]
        tex = nt.nodes.new("ShaderNodeTexImage")
        tex.image = bpy.data.images.load(str(wins), check_existing=True)
        tex.projection = "BOX"
        mp = nt.nodes.new("ShaderNodeMapping")
        mp.inputs["Scale"].default_value = (1 / 256, 1 / 256, 1 / 256)
        tc = nt.nodes.new("ShaderNodeTexCoord")
        nt.links.new(tc.outputs["Object"], mp.inputs[0])
        nt.links.new(mp.outputs[0], tex.inputs[0])
        nt.links.new(tex.outputs["Color"], b.inputs["Base Color"])
        nt.links.new(tex.outputs["Color"], b.inputs["Emission Color"])
        b.inputs["Emission Strength"].default_value = 1.2
    box("court_floor", -384, -448, -8, 384, 448, 0, wet, coll)
    for (x0, y0, x1, y1) in ((-2200, -1300, -384, 1300), (384, -1300, 1100, 1300), (-384, 448, 384, 1300),
                             (-384, -1300, 384, -448)):
        box("plaza", x0, y0, 0, x1, y1, 64, deck, coll)
    box("tower", 960, -1216, 0, 1088, 1216, 3200, facade, coll)
    for y in (-1500, 1500):
        box("block", -2200, y - 200, 0, 1100, y + 200, 1800, facade, coll)
    world = bpy.data.worlds.new("night")
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs["Color"].default_value = (0.006, 0.008, 0.016, 1)
    bg.inputs["Strength"].default_value = 1.0
    bpy.context.scene.world = world
    sun = light("SUN", "moon", (0, 0, 2000), (0.5, 0.6, 1.0), 0.03, coll=coll)
    sun.rotation_euler = (radians(50), 0, radians(-120))


def _bloom(sc):
    try:
        tree = bpy.data.node_groups.new("comp", "CompositorNodeTree")
        sc.compositing_node_group = tree
        rl = tree.nodes.new("CompositorNodeRLayers")
        gl = tree.nodes.new("CompositorNodeGlare")
        out = tree.nodes.new("NodeGroupOutput")
        tree.interface.new_socket("Image", in_out="OUTPUT", socket_type="NodeSocketColor")
        if "Type" in gl.inputs:
            gl.inputs["Type"].default_value = "Bloom"
        else:
            gl.glare_type = "BLOOM"
        for key, val in (("Threshold", 0.6), ("Strength", 0.6), ("Size", 0.7)):
            if key in gl.inputs:
                gl.inputs[key].default_value = val
        tree.links.new(rl.outputs["Image"], gl.inputs["Image"])
        tree.links.new(gl.outputs["Image"], out.inputs[0])
        return True
    except Exception as e:  # compositor API differs between Blender versions; renders still work
        print("bloom disabled:", e)
        return False


def render(tag, views=("eye", "approach", "wide"), res=(1280, 720), samples=48, save_blend=True):
    """Render the standard views to build/concepts/<tag>_<view>.png; returns the paths."""
    sc = bpy.context.scene
    OUT.mkdir(parents=True, exist_ok=True)
    sc.render.engine = "BLENDER_EEVEE"
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.image_settings.file_format = "PNG"
    for attr, val in (("taa_render_samples", samples), ("use_raytracing", True), ("use_shadows", True)):
        if hasattr(sc.eevee, attr):
            setattr(sc.eevee, attr, val)
    sc.view_settings.view_transform = "AgX"
    _bloom(sc)
    if save_blend:
        bpy.context.preferences.filepaths.save_version = 0
        bpy.ops.wm.save_as_mainfile(filepath=str(OUT / f"{tag}.blend"))
    done = []
    for name in views:
        loc, target, fov = VIEWS[name]
        cd = bpy.data.cameras.new(name)
        cd.angle = radians(fov)
        cd.clip_start, cd.clip_end = 4, 20000
        ob = bpy.data.objects.new(f"cam_{name}", cd)
        sc.collection.objects.link(ob)
        ob.location = loc
        aim(ob, target)
        sc.camera = ob
        sc.render.filepath = str(OUT / f"{tag}_{name}.png")
        bpy.ops.render.render(write_still=True)
        done.append(sc.render.filepath)
    print("CONCEPT_RENDERS " + ";".join(done))
    return done
