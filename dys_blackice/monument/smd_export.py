"""Minimal Source SMD exporter for Blender: reference mesh, convex collision pieces, 1-frame idle.

Conventions (verified against SDK 2013 studiomdl + stock Dystopia props):
- studiomdl rotates SMD geometry +90 deg about Z, so everything is pre-rotated by -90 deg here:
  Blender +X = model +X = world east for a prop at yaw 0.
- Blender's counter-clockwise front faces are written in loop order (same winding as stock props).
- Single bone "root"; Blender units = Source units.
- Collision: studiomdl splits $concave pieces by vertex connectivity and only welds vertices whose
  position, normal AND uv match. Each piece is written with shared radial normals and uv 0,0 so it
  stays one closed convex element. One mesh object = one convex piece.
"""
from __future__ import annotations

import math

import bpy
from mathutils import Matrix, Vector

HEADER = 'version 1\nnodes\n0 "root" -1\nend\nskeleton\ntime 0\n0 0 0 0 0 0 0\nend\n'
FIX = Matrix.Rotation(math.radians(-90.0), 4, "Z")


def _f(v):
    s = f"{v:.5f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def _line(co, n, uv):
    return (f"0 {_f(co.x)} {_f(co.y)} {_f(co.z)} {_f(n.x)} {_f(n.y)} {_f(n.z)} "
            f"{_f(uv[0])} {_f(uv[1])} 1 0 1\n")


def triangles(obj):
    """Yield (material, [(co, normal, uv)] * 3) in model space for one mesh object."""
    deps = bpy.context.evaluated_depsgraph_get()
    ev = obj.evaluated_get(deps)
    me = ev.to_mesh()
    try:
        me.calc_loop_triangles()
        mw = FIX @ obj.matrix_world
        nm = mw.to_3x3().inverted_safe().transposed()
        cn = me.corner_normals
        uvl = me.uv_layers.active.data if me.uv_layers.active else None
        for lt in me.loop_triangles:
            slot = obj.material_slots[lt.material_index] if obj.material_slots else None
            mat = slot.material.name if slot and slot.material else "default"
            tri = []
            for li in lt.loops:
                co = mw @ me.vertices[me.loops[li].vertex_index].co
                n = (nm @ cn[li].vector).normalized()
                tri.append((co, n, tuple(uvl[li].uv) if uvl else (0.0, 0.0)))
            yield mat, tri
    finally:
        ev.to_mesh_clear()


def export_ref(path, objects) -> dict:
    """Reference (render) mesh. Returns {'tris': n, 'materials': sorted names}."""
    n, mats = 0, set()
    with open(path, "w", encoding="ascii", newline="\n") as f:
        f.write(HEADER + "triangles\n")
        for obj in objects:
            for mat, tri in triangles(obj):
                f.write(mat + "\n")
                for co, nrm, uv in tri:
                    f.write(_line(co, nrm, uv))
                n += 1
                mats.add(mat)
        f.write("end\n")
    return {"tris": n, "materials": sorted(mats)}


def export_phys(path, objects, material="phys") -> int:
    """Collision mesh: one convex piece per object. Returns the piece count."""
    with open(path, "w", encoding="ascii", newline="\n") as f:
        f.write(HEADER + "triangles\n")
        for obj in objects:
            tris = [t for _, t in triangles(obj)]
            pts = [v[0] for t in tris for v in t]
            c = sum(pts, Vector()) / len(pts)
            for t in tris:
                f.write(material + "\n")
                for co, _, _ in t:
                    f.write(_line(co, (co - c).normalized(), (0.0, 0.0)))
        f.write("end\n")
    return len(objects)


def export_idle(path):
    with open(path, "w", encoding="ascii", newline="\n") as f:
        f.write(HEADER)
