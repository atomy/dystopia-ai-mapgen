"""
Rectangular brush helpers: box, corridor, stairwell, rooftop platform, street trench, sky shell.
All emit known-good convex brushes (6 sides). Coordinates: X, Y horizontal; Z up.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vmf_writer import VmfWriter


def add_box(
    writer: VmfWriter,
    x: float,
    y: float,
    z: float,
    width: float,
    depth: float,
    height: float,
    material: str = "DEV/DEV_MEASUREGENERIC01",
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
    floor_material: str = "DEV/DEV_MEASUREGENERIC01",
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
    material: str = "DEV/DEV_MEASUREGENERIC01",
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
    material: str = "DEV/DEV_MEASUREGENERIC01",
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
    material: str = "DEV/DEV_MEASUREGENERIC01",
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
