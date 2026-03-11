"""
Rectangular brush helpers: box, corridor, stairwell, rooftop platform, street trench, sky shell.
All emit known-good convex brushes (6 sides). Coordinates: X, Y horizontal; Z up.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vmf_writer import VmfWriter


DEFAULT_FLOOR_MATERIAL = "urban/conc_clean2"
DEFAULT_WALL_MATERIAL = "vaccinecore/metal_panelwall_001"
DEFAULT_ROOF_MATERIAL = "vaccine/dys_metalroof"


def add_box(
    writer: VmfWriter,
    x: float,
    y: float,
    z: float,
    width: float,
    depth: float,
    height: float,
    material: str = DEFAULT_WALL_MATERIAL,
    face_materials: Sequence[str] | None = None,
) -> None:
    """
    Add a 6-sided convex brush (axis-aligned box).
    Origin (x,y,z) = min corner; width (X+), depth (Y+), height (Z+).
    Face order and winding match Hammer/working VMF: same order as dys_cybercybercyber.vmf.
    `face_materials`, when set, overrides per-face materials in this order:
    top, bottom, x-, x+, y+, y-.
    """
    x0, y0, z0 = x, y, z
    x1, y1, z1 = x + width, y + depth, z + height

    # Exact face order and winding from reference VMF (outward normals)
    # 1. Top (z1)  2. Bottom (z0)  3. X-  4. X+  5. Y+  6. Y-
    planes = [
        ((x0, y1, z1), (x1, y1, z1), (x1, y0, z1)),   # top
        ((x0, y0, z0), (x1, y0, z0), (x1, y1, z0)),   # bottom
        ((x0, y1, z1), (x0, y0, z1), (x0, y0, z0)),   # x-
        ((x1, y1, z0), (x1, y0, z0), (x1, y0, z1)),   # x+
        ((x1, y1, z1), (x0, y1, z1), (x0, y1, z0)),   # y+
        ((x1, y0, z0), (x0, y0, z0), (x0, y0, z1)),   # y-
    ]
    writer.add_brush(planes, face_materials if face_materials is not None else material)


def add_room(
    writer: VmfWriter,
    x: float,
    y: float,
    z: float,
    width: float,
    depth: float,
    height: float,
    floor_material: str = DEFAULT_FLOOR_MATERIAL,
    wall_material: str | None = None,
    ceiling_material: str | None = None,
) -> None:
    """Single box room; if materials differ, still one brush for MVP (single material)."""
    mat = wall_material or floor_material
    add_box(writer, x, y, z, width, depth, height, mat)


def add_corridor(
    writer: VmfWriter,
    x: float,
    y: float,
    z: float,
    length: float,
    width: float,
    height: float,
    material: str = DEFAULT_WALL_MATERIAL,
) -> None:
    """Corridor along X (length = X extent)."""
    add_box(writer, x, y, z, length, width, height, material)


def add_street_trench(
    writer: VmfWriter,
    x: float,
    y: float,
    z: float,
    length: float,
    width: float,
    depth: float = 0,
    material: str = DEFAULT_FLOOR_MATERIAL,
) -> None:
    """Street as a flat box (floor). depth=0 means no vertical extent; use small thickness for valid brush."""
    h = 16 if depth == 0 else depth
    add_box(writer, x, y, z, length, width, h, material)


def add_rooftop_platform(
    writer: VmfWriter,
    x: float,
    y: float,
    z: float,
    width: float,
    depth: float,
    thickness: float = 32,
    material: str = DEFAULT_ROOF_MATERIAL,
) -> None:
    """Rooftop as a thin box."""
    add_box(writer, x, y, z, width, depth, thickness, material)


def add_sky_shell(
    writer: VmfWriter,
    x_min: float,
    y_min: float,
    z_min: float,
    x_max: float,
    y_max: float,
    z_max: float,
    thickness: float = 64,
    material: str = "TOOLS/TOOLSSKYBOX",
) -> None:
    """
    Emit a hollow sky room from five axis-aligned brushes.

    The play space remains empty inside the shell; the floor is expected to be
    provided separately by the caller.
    """
    total_width = x_max - x_min
    total_depth = y_max - y_min
    wall_height = z_max - z_min

    # West and east walls.
    add_box(writer, x_min - thickness, y_min, z_min, thickness, total_depth, wall_height, material)
    add_box(writer, x_max, y_min, z_min, thickness, total_depth, wall_height, material)

    # South and north walls.
    add_box(writer, x_min, y_min - thickness, z_min, total_width, thickness, wall_height, material)
    add_box(writer, x_min, y_max, z_min, total_width, thickness, wall_height, material)

    # Ceiling.
    add_box(writer, x_min - thickness, y_min - thickness, z_max, total_width + (thickness * 2), total_depth + (thickness * 2), thickness, material)


# --- Enterable building primitives (hollow shells, openings, glass) ---

DEFAULT_GLASS_MATERIAL = "glass/glasswindow007a"


def add_hollow_shell(
    writer: VmfWriter,
    x0: float,
    y0: float,
    z0: float,
    x1: float,
    y1: float,
    z1: float,
    wall_thickness: float,
    floor_material: str = DEFAULT_FLOOR_MATERIAL,
    wall_material: str = DEFAULT_WALL_MATERIAL,
    roof_material: str = DEFAULT_ROOF_MATERIAL,
    floor_thickness: float = 16,
    roof_thickness: float = 32,
) -> None:
    """
    Emit a hollow rectangular shell: floor slab, four walls, roof slab.
    Interior space is (x0+wall_thickness, y0+wall_thickness, z0+floor_thickness)
    to (x1-wall_thickness, y1-wall_thickness, z1-roof_thickness).
    """
    # Floor
    add_box(writer, x0, y0, z0, x1 - x0, y1 - y0, floor_thickness, floor_material)
    # West wall (x_min)
    add_box(writer, x0, y0, z0, wall_thickness, y1 - y0, z1 - z0, wall_material)
    # East wall (x_max)
    add_box(writer, x1 - wall_thickness, y0, z0, wall_thickness, y1 - y0, z1 - z0, wall_material)
    # South wall (y_min)
    add_box(writer, x0 + wall_thickness, y0, z0, x1 - x0 - 2 * wall_thickness, wall_thickness, z1 - z0, wall_material)
    # North wall (y_max)
    add_box(writer, x0 + wall_thickness, y1 - wall_thickness, z0, x1 - x0 - 2 * wall_thickness, wall_thickness, z1 - z0, wall_material)
    # Roof
    add_box(writer, x0, y0, z1 - roof_thickness, x1 - x0, y1 - y0, roof_thickness, roof_material)


def add_floor_slab(
    writer: VmfWriter,
    x0: float,
    y0: float,
    z: float,
    x1: float,
    y1: float,
    thickness: float,
    material: str = DEFAULT_FLOOR_MATERIAL,
) -> None:
    """Interior floor or ceiling slab (axis-aligned box)."""
    add_box(writer, x0, y0, z, x1 - x0, y1 - y0, thickness, material)


def add_wall_full(
    writer: VmfWriter,
    side: str,
    x0: float,
    y0: float,
    z0: float,
    x1: float,
    y1: float,
    z1: float,
    thickness: float,
    material: str = DEFAULT_WALL_MATERIAL,
) -> None:
    """Emit one full wall (no openings). side: x_min | x_max | y_min | y_max."""
    if side == "x_min":
        _wall_box_x_min(writer, x0, y0, z0, y1, z1, thickness, material)
    elif side == "x_max":
        _wall_box_x_max(writer, x1, y0, z0, y1, z1, thickness, material)
    elif side == "y_min":
        _wall_box_y_min(writer, x0, y0, z0, x1, z1, thickness, material)
    else:
        _wall_box_y_max(writer, x0, y1, z0, x1, z1, thickness, material)


def _wall_box_x_min(
    writer: VmfWriter,
    x0: float,
    y0: float,
    z0: float,
    y1: float,
    z1: float,
    thickness: float,
    material: str,
) -> None:
    add_box(writer, x0, y0, z0, thickness, y1 - y0, z1 - z0, material)


def _wall_box_x_max(
    writer: VmfWriter,
    x1: float,
    y0: float,
    z0: float,
    y1: float,
    z1: float,
    thickness: float,
    material: str,
) -> None:
    add_box(writer, x1 - thickness, y0, z0, thickness, y1 - y0, z1 - z0, material)


def _wall_box_y_min(
    writer: VmfWriter,
    x0: float,
    y0: float,
    z0: float,
    x1: float,
    z1: float,
    thickness: float,
    material: str,
) -> None:
    add_box(writer, x0, y0, z0, x1 - x0, thickness, z1 - z0, material)


def _wall_box_y_max(
    writer: VmfWriter,
    x0: float,
    y1: float,
    z0: float,
    x1: float,
    z1: float,
    thickness: float,
    material: str,
) -> None:
    add_box(writer, x0, y1 - thickness, z0, x1 - x0, thickness, z1 - z0, material)


def add_wall_with_door(
    writer: VmfWriter,
    side: str,
    x0: float,
    y0: float,
    z0: float,
    x1: float,
    y1: float,
    z1: float,
    thickness: float,
    door_center: float,
    door_width: float,
    door_height: float,
    material: str = DEFAULT_WALL_MATERIAL,
) -> None:
    """
    Emit wall segments that leave a rectangular door opening.
    side: "x_min" | "x_max" | "y_min" | "y_max".
    For x_min/x_max: door_center is Y, door_width is along Y, door_height is Z.
    For y_min/y_max: door_center is X, door_width is along X, door_height is Z.
    """
    half = door_width / 2
    d_lo = door_center - half
    d_hi = door_center + half
    z_door_top = z0 + door_height

    if side == "x_min":
        # Left segment: (x0, y0, z0) to (x0+t, d_lo, z1)
        if d_lo > y0:
            _wall_box_x_min(writer, x0, y0, z0, d_lo, z1, thickness, material)
        # Right segment: (x0, d_hi, z0) to (x0+t, y1, z1)
        if d_hi < y1:
            _wall_box_x_min(writer, x0, d_hi, z0, y1, z1, thickness, material)
        # Lintel: (x0, d_lo, z_door_top) to (x0+t, d_hi, z1)
        _wall_box_x_min(writer, x0, d_lo, z_door_top, d_hi, z1, thickness, material)
    elif side == "x_max":
        if d_lo > y0:
            _wall_box_x_max(writer, x1, y0, z0, d_lo, z1, thickness, material)
        if d_hi < y1:
            _wall_box_x_max(writer, x1, d_hi, z0, y1, z1, thickness, material)
        _wall_box_x_max(writer, x1, d_lo, z_door_top, d_hi, z1, thickness, material)
    elif side == "y_min":
        if d_lo > x0:
            _wall_box_y_min(writer, x0, y0, z0, d_lo, z1, thickness, material)
        if d_hi < x1:
            _wall_box_y_min(writer, d_hi, y0, z0, x1, z1, thickness, material)
        _wall_box_y_min(writer, d_lo, y0, z_door_top, d_hi, z1, thickness, material)
    else:  # y_max
        if d_lo > x0:
            _wall_box_y_max(writer, x0, y1, z0, d_lo, z1, thickness, material)
        if d_hi < x1:
            _wall_box_y_max(writer, d_hi, y1, z0, x1, z1, thickness, material)
        _wall_box_y_max(writer, d_lo, y1, z_door_top, d_hi, z1, thickness, material)


def add_wall_with_window(
    writer: VmfWriter,
    side: str,
    x0: float,
    y0: float,
    z0: float,
    x1: float,
    y1: float,
    z1: float,
    thickness: float,
    win_center_axis: float,
    win_axis_size: float,
    win_z_bottom: float,
    win_z_size: float,
    material: str = DEFAULT_WALL_MATERIAL,
) -> None:
    """
    Emit wall segments that leave a rectangular window opening.
    Same axis convention as add_wall_with_door.
    """
    half = win_axis_size / 2
    a_lo = win_center_axis - half
    a_hi = win_center_axis + half
    z_top = win_z_bottom + win_z_size

    if side == "x_min":
        # Below window
        if win_z_bottom > z0:
            _wall_box_x_min(writer, x0, y0, z0, y1, win_z_bottom, thickness, material)
        # Above window
        if z_top < z1:
            _wall_box_x_min(writer, x0, y0, z_top, y1, z1, thickness, material)
        # Left of window
        if a_lo > y0:
            _wall_box_x_min(writer, x0, y0, win_z_bottom, a_lo, z_top, thickness, material)
        # Right of window
        if a_hi < y1:
            _wall_box_x_min(writer, x0, a_hi, win_z_bottom, y1, z_top, thickness, material)
    elif side == "x_max":
        if win_z_bottom > z0:
            _wall_box_x_max(writer, x1, y0, z0, y1, win_z_bottom, thickness, material)
        if z_top < z1:
            _wall_box_x_max(writer, x1, y0, z_top, y1, z1, thickness, material)
        if a_lo > y0:
            _wall_box_x_max(writer, x1, y0, win_z_bottom, a_lo, z_top, thickness, material)
        if a_hi < y1:
            _wall_box_x_max(writer, x1, a_hi, win_z_bottom, y1, z_top, thickness, material)
    elif side == "y_min":
        if win_z_bottom > z0:
            _wall_box_y_min(writer, x0, y0, z0, x1, win_z_bottom, thickness, material)
        if z_top < z1:
            _wall_box_y_min(writer, x0, y0, z_top, x1, z1, thickness, material)
        if a_lo > x0:
            _wall_box_y_min(writer, x0, y0, win_z_bottom, a_lo, z_top, thickness, material)
        if a_hi < x1:
            _wall_box_y_min(writer, a_hi, y0, win_z_bottom, x1, z_top, thickness, material)
    else:
        if win_z_bottom > z0:
            _wall_box_y_max(writer, x0, y1, z0, x1, win_z_bottom, thickness, material)
        if z_top < z1:
            _wall_box_y_max(writer, x0, y1, z_top, x1, z1, thickness, material)
        if a_lo > x0:
            _wall_box_y_max(writer, x0, y1, win_z_bottom, a_lo, z_top, thickness, material)
        if a_hi < x1:
            _wall_box_y_max(writer, a_hi, y1, win_z_bottom, x1, z_top, thickness, material)


def add_glass_panel(
    writer: VmfWriter,
    x0: float,
    y0: float,
    z0: float,
    x1: float,
    y1: float,
    z1: float,
    material: str = DEFAULT_GLASS_MATERIAL,
) -> None:
    """
    Add a thin axis-aligned glass brush filling the given AABB (e.g. in a window opening).
    Caller passes the exact glass bounds; one dimension should be small (wall thickness).
    """
    add_box(writer, x0, y0, z0, x1 - x0, y1 - y0, z1 - z0, material)


def add_stair_core(
    writer: VmfWriter,
    x0: float,
    y0: float,
    z0: float,
    x1: float,
    y1: float,
    z1: float,
    material: str = DEFAULT_WALL_MATERIAL,
) -> None:
    """
    Stairwell core: one vertical shaft box from (x0,y0,z0) to (x1,y1,z1).
    Used for roof access; actual steps can be added by the building emitter.
    """
    add_box(writer, x0, y0, z0, x1 - x0, y1 - y0, z1 - z0, material)
