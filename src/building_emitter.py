"""
Emit VMF geometry for layout buildings: solid block (legacy) or enterable archetypes.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from layout_rules import Building
from dystopia_entities import DEFAULT_DOOR_MATERIAL, add_func_breakable_window, add_func_door
from vmf_primitives import (
    add_box,
    add_floor_slab,
    add_stair_core,
    add_wall_full,
    add_wall_with_door,
    add_wall_with_window,
    DEFAULT_FLOOR_MATERIAL,
    DEFAULT_GLASS_MATERIAL,
    DEFAULT_ROOF_MATERIAL,
    DEFAULT_WALL_MATERIAL,
)

if TYPE_CHECKING:
    from vmf_writer import VmfWriter

FLOOR_SLAB_THICKNESS = 16
ROOF_SLAB_THICKNESS = 32
DOOR_WIDTH = 128
DOOR_HEIGHT = 128
DOOR_THICKNESS = 8  # thin panel; full wall thickness caused bulky doors sliding into wall
DOOR_Z_OFFSET = 4   # raise door bottom above floor to avoid z-fighting
WINDOW_WIDTH = 96
WINDOW_HEIGHT = 64
GLASS_THICKNESS = 4
STAIR_CORE_SIZE = 64
# Used for window-band extent so solids are clipped in the direction of the window exterior
MAP_EXTENT = 32768


def _default_entrance_sides(archetype: str, base: tuple[int, int], size: tuple[int, int]) -> list[str]:
    if archetype == "spawn_block":
        return ["x_min", "x_max"]
    if archetype == "small_shop":
        return ["y_max"]
    if archetype == "office_midrise":
        return ["x_min"]
    if archetype == "warehouse":
        return ["y_min", "y_max"]
    return ["x_min"]


def _emit_entrance_doors(
    writer: VmfWriter,
    b: Building,
    side: str,
    x0: float,
    y0: float,
    z0: float,
    x1: float,
    y1: float,
    wt: float,
    door_center_x: float,
    door_center_y: float,
    door_material: str,
) -> None:
    """Emit paired sliding func_door leaves: thin panel centered in wall depth to avoid z-fight with frame."""
    half = DOOR_WIDTH / 2
    z_bottom = z0 + DOOR_Z_OFFSET
    z_top = z0 + DOOR_HEIGHT  # align with opening top; door is slightly shorter to avoid z-fight at sill
    dt = float(DOOR_THICKNESS)
    # Center door in wall thickness so it doesn't sit flush with frame (which caused z-fighting)
    wall_center_offset = wt / 2
    x_min_door_lo = x0 + wall_center_offset - dt / 2
    x_min_door_hi = x0 + wall_center_offset + dt / 2
    x_max_door_lo = x1 - wall_center_offset - dt / 2
    x_max_door_hi = x1 - wall_center_offset + dt / 2
    y_min_door_lo = y0 + wall_center_offset - dt / 2
    y_min_door_hi = y0 + wall_center_offset + dt / 2
    y_max_door_lo = y1 - wall_center_offset - dt / 2
    y_max_door_hi = y1 - wall_center_offset + dt / 2
    base_name = f"{b.id}_{side}_door"
    # movedir: doors slide along the wall plane. x_min/x_max -> Y; y_min/y_max -> X.
    if side == "x_min":
        add_func_door(
            writer, x_min_door_lo, door_center_y - half, z_bottom, x_min_door_hi, door_center_y, z_top,
            movedir="0 270 0", targetname=f"{base_name}_l", material=door_material,
        )
        add_func_door(
            writer, x_min_door_lo, door_center_y, z_bottom, x_min_door_hi, door_center_y + half, z_top,
            movedir="0 90 0", targetname=f"{base_name}_r", material=door_material,
        )
    elif side == "x_max":
        add_func_door(
            writer, x_max_door_lo, door_center_y - half, z_bottom, x_max_door_hi, door_center_y, z_top,
            movedir="0 270 0", targetname=f"{base_name}_l", material=door_material,
        )
        add_func_door(
            writer, x_max_door_lo, door_center_y, z_bottom, x_max_door_hi, door_center_y + half, z_top,
            movedir="0 90 0", targetname=f"{base_name}_r", material=door_material,
        )
    elif side == "y_min":
        add_func_door(
            writer, door_center_x - half, y_min_door_lo, z_bottom, door_center_x, y_min_door_hi, z_top,
            movedir="0 180 0", targetname=f"{base_name}_l", material=door_material,
        )
        add_func_door(
            writer, door_center_x, y_min_door_lo, z_bottom, door_center_x + half, y_min_door_hi, z_top,
            movedir="0 0 0", targetname=f"{base_name}_r", material=door_material,
        )
    else:  # y_max
        add_func_door(
            writer, door_center_x - half, y_max_door_lo, z_bottom, door_center_x, y_max_door_hi, z_top,
            movedir="0 180 0", targetname=f"{base_name}_l", material=door_material,
        )
        add_func_door(
            writer, door_center_x, y_max_door_lo, z_bottom, door_center_x + half, y_max_door_hi, z_top,
            movedir="0 0 0", targetname=f"{base_name}_r", material=door_material,
        )


def get_enterable_window_bands(b: Building, base_z: float) -> list[tuple[float, float, float, float, float, float]]:
    """Return AABBs (x_min, y_min, z_min, x_max, y_max, z_max) for each window of an enterable building.
    A solid that overlaps one of these bands would block that window; used to clip solid buildings."""
    if not b.is_enterable() or not b.glass:
        return []
    wt = float(b.wall_thickness)
    x0, y0 = float(b.base[0]), float(b.base[1])
    x1 = x0 + b.size[0]
    y1 = y0 + b.size[1]
    z0 = base_z
    z1 = z0 + b.height
    floor_thick = FLOOR_SLAB_THICKNESS
    roof_thick = ROOF_SLAB_THICKNESS
    storey_height = (z1 - z0 - floor_thick - roof_thick) / max(1, b.floors)
    if b.floor_height is not None:
        storey_height = float(b.floor_height)
    if storey_height < WINDOW_HEIGHT + 32:
        return []
    win_z = z0 + floor_thick + storey_height / 2 - WINDOW_HEIGHT / 2
    win_z_max = win_z + WINDOW_HEIGHT
    door_center_y = (y0 + y1) / 2
    door_center_x = (x0 + x1) / 2
    wy_lo = door_center_y - WINDOW_WIDTH / 2
    wy_hi = door_center_y + WINDOW_WIDTH / 2
    wx_lo = door_center_x - WINDOW_WIDTH / 2
    wx_hi = door_center_x + WINDOW_WIDTH / 2
    entrance_sides = b.entrance_sides if b.entrance_sides else _default_entrance_sides(b.archetype, b.base, b.size)
    bands: list[tuple[float, float, float, float, float, float]] = []
    # x_min wall: exterior is x <= x0; blocking band is solid volume in front of the window
    if "x_min" not in entrance_sides:
        bands.append((-MAP_EXTENT, wy_lo, win_z, x0, wy_hi, win_z_max))
    if "x_max" not in entrance_sides:
        bands.append((x1, wy_lo, win_z, MAP_EXTENT, wy_hi, win_z_max))
    if "y_min" not in entrance_sides:
        bands.append((wx_lo, -MAP_EXTENT, win_z, wx_hi, y0, win_z_max))
    if "y_max" not in entrance_sides:
        bands.append((wx_lo, y1, win_z, wx_hi, MAP_EXTENT, win_z_max))
    return bands


def _box_intersection(
    a: tuple[float, float, float, float, float, float],
    b: tuple[float, float, float, float, float, float],
) -> tuple[float, float, float, float, float, float] | None:
    """Return intersection AABB or None if empty."""
    x0 = max(a[0], b[0])
    y0 = max(a[1], b[1])
    z0 = max(a[2], b[2])
    x1 = min(a[3], b[3])
    y1 = min(a[4], b[4])
    z1 = min(a[5], b[5])
    if x0 >= x1 or y0 >= y1 or z0 >= z1:
        return None
    return (x0, y0, z0, x1, y1, z1)


def _box_subtract(
    solid: tuple[float, float, float, float, float, float],
    hole: tuple[float, float, float, float, float, float],
) -> list[tuple[float, float, float, float, float, float]]:
    """Return list of boxes that cover solid minus hole (hole must be inside solid)."""
    sx0, sy0, sz0, sx1, sy1, sz1 = solid
    hx0, hy0, hz0, hx1, hy1, hz1 = hole
    out: list[tuple[float, float, float, float, float, float]] = []
    # 6 pieces: left/right of hole in x, below/above in y (for middle x band), below/above in z (for middle band)
    if sx0 < hx0:
        out.append((sx0, sy0, sz0, hx0, sy1, sz1))
    if hx1 < sx1:
        out.append((hx1, sy0, sz0, sx1, sy1, sz1))
    if sy0 < hy0:
        out.append((hx0, sy0, sz0, hx1, hy0, sz1))
    if hy1 < sy1:
        out.append((hx0, hy1, sz0, hx1, sy1, sz1))
    if sz0 < hz0:
        out.append((hx0, hy0, sz0, hx1, hy1, hz0))
    if hz1 < sz1:
        out.append((hx0, hy0, hz1, hx1, hy1, sz1))
    return out


def _emit_solid_building(
    writer: VmfWriter,
    b: Building,
    x0: float,
    y0: float,
    z0: float,
    x1: float,
    y1: float,
    wall_material: str,
    roof_material: str,
    floor_material: str,
) -> None:
    w, d, h = x1 - x0, y1 - y0, b.height
    add_box(
        writer,
        x0,
        y0,
        z0,
        w,
        d,
        h,
        wall_material,
        face_materials=[
            roof_material,
            floor_material,
            wall_material,
            wall_material,
            wall_material,
            wall_material,
        ],
    )


def _emit_solid_boxes(
    writer: VmfWriter,
    boxes: list[tuple[float, float, float, float, float, float]],
    wall_material: str,
    roof_material: str,
    floor_material: str,
) -> None:
    """Emit multiple boxes with same materials (top, bottom, then four wall faces)."""
    for (x0, y0, z0, x1, y1, z1) in boxes:
        w, d, h = x1 - x0, y1 - y0, z1 - z0
        add_box(
            writer,
            x0, y0, z0,
            w, d, h,
            wall_material,
            face_materials=[
                roof_material,
                floor_material,
                wall_material,
                wall_material,
                wall_material,
                wall_material,
            ],
        )


def _emit_enterable_building(
    writer: VmfWriter,
    b: Building,
    x0: float,
    y0: float,
    z0: float,
    x1: float,
    y1: float,
    wall_material: str,
    roof_material: str,
    floor_material: str,
    glass_material: str,
) -> None:
    wt = float(b.wall_thickness)
    z1 = z0 + b.height
    floor_thick = FLOOR_SLAB_THICKNESS
    roof_thick = ROOF_SLAB_THICKNESS
    storey_height = (z1 - z0 - floor_thick - roof_thick) / max(1, b.floors)
    if b.floor_height is not None:
        storey_height = float(b.floor_height)

    # Interior bounds (for floor slabs and stair core)
    xi0, yi0 = x0 + wt, y0 + wt
    xi1, yi1 = x1 - wt, y1 - wt

    # Base floor
    add_floor_slab(writer, x0, y0, z0, x1, y1, floor_thick, floor_material)
    # Roof
    add_floor_slab(writer, x0, y0, z1 - roof_thick, x1, y1, roof_thick, roof_material)

    entrance_sides = b.entrance_sides if b.entrance_sides else _default_entrance_sides(b.archetype, b.base, b.size)
    door_center_y = (y0 + y1) / 2
    door_center_x = (x0 + x1) / 2

    door_material = b.materials.get("door", DEFAULT_DOOR_MATERIAL)

    def emit_wall(side: str) -> None:
        has_door = side in entrance_sides
        if has_door:
            if side in ("x_min", "x_max"):
                add_wall_with_door(
                    writer, side, x0, y0, z0, x1, y1, z1, wt,
                    door_center_y, DOOR_WIDTH, DOOR_HEIGHT, wall_material
                )
            else:
                add_wall_with_door(
                    writer, side, x0, y0, z0, x1, y1, z1, wt,
                    door_center_x, DOOR_WIDTH, DOOR_HEIGHT, wall_material
                )
            _emit_entrance_doors(
                writer, b, side, x0, y0, z0, x1, y1, wt,
                door_center_x, door_center_y, door_material,
            )
        elif b.glass and storey_height >= WINDOW_HEIGHT + 32:
            win_z = z0 + floor_thick + storey_height / 2 - WINDOW_HEIGHT / 2
            if side in ("x_min", "x_max"):
                add_wall_with_window(
                    writer, side, x0, y0, z0, x1, y1, z1, wt,
                    door_center_y, WINDOW_WIDTH, win_z, WINDOW_HEIGHT, wall_material
                )
                if side == "x_min":
                    add_func_breakable_window(writer, x0, door_center_y - WINDOW_WIDTH/2, win_z,
                                             x0 + GLASS_THICKNESS, door_center_y + WINDOW_WIDTH/2, win_z + WINDOW_HEIGHT, glass_material)
                else:
                    add_func_breakable_window(writer, x1 - GLASS_THICKNESS, door_center_y - WINDOW_WIDTH/2, win_z,
                                             x1, door_center_y + WINDOW_WIDTH/2, win_z + WINDOW_HEIGHT, glass_material)
            else:
                add_wall_with_window(
                    writer, side, x0, y0, z0, x1, y1, z1, wt,
                    door_center_x, WINDOW_WIDTH, win_z, WINDOW_HEIGHT, wall_material
                )
                if side == "y_min":
                    add_func_breakable_window(writer, door_center_x - WINDOW_WIDTH/2, y0, win_z,
                                              door_center_x + WINDOW_WIDTH/2, y0 + GLASS_THICKNESS, win_z + WINDOW_HEIGHT, glass_material)
                else:
                    add_func_breakable_window(writer, door_center_x - WINDOW_WIDTH/2, y1 - GLASS_THICKNESS, win_z,
                                              door_center_x + WINDOW_WIDTH/2, y1, win_z + WINDOW_HEIGHT, glass_material)
        else:
            add_wall_full(writer, side, x0, y0, z0, x1, y1, z1, wt, wall_material)

    emit_wall("x_min")
    emit_wall("x_max")
    emit_wall("y_min")
    emit_wall("y_max")

    # Interior floor slabs per storey (skip 0 = ground already has base floor)
    for i in range(1, b.floors):
        z_floor = z0 + floor_thick + i * storey_height
        add_floor_slab(writer, xi0, yi0, z_floor, xi1, yi1, floor_thick, floor_material)

    if b.roof_access and b.floors >= 2:
        # Place stair core in a corner that does not have windows, so it doesn't block them.
        def _side_has_window(side: str) -> bool:
            if side in entrance_sides:
                return False
            return bool(b.glass and storey_height >= WINDOW_HEIGHT + 32)

        corners = [
            ("x_min", "y_min", xi0, yi0, xi0 + STAIR_CORE_SIZE, yi0 + STAIR_CORE_SIZE),
            ("x_min", "y_max", xi0, yi1 - STAIR_CORE_SIZE, xi0 + STAIR_CORE_SIZE, yi1),
            ("x_max", "y_min", xi1 - STAIR_CORE_SIZE, yi0, xi1, yi0 + STAIR_CORE_SIZE),
            ("x_max", "y_max", xi1 - STAIR_CORE_SIZE, yi1 - STAIR_CORE_SIZE, xi1, yi1),
        ]
        # Prefer corner with fewest window sides (0 best, then 1, then 2).
        best = min(
            corners,
            key=lambda c: (int(_side_has_window(c[0])) + int(_side_has_window(c[1])), c[0], c[1]),
        )
        _, _, sx0, sy0, sx1, sy1 = best
        add_stair_core(
            writer,
            sx0, sy0, z0 + floor_thick,
            sx1, sy1, z1 - roof_thick,
            wall_material,
        )


def emit_building(
    writer: VmfWriter,
    b: Building,
    base_z: float,
    window_bands: list[tuple[float, float, float, float, float, float]] | None = None,
) -> None:
    """Emit all geometry for one building (solid or enterable).
    window_bands: optional list of AABBs to subtract from solid buildings so they don't block other buildings' windows."""
    if b.height <= 0:
        return
    x0, y0 = float(b.base[0]), float(b.base[1])
    x1 = x0 + b.size[0]
    y1 = y0 + b.size[1]
    z0 = base_z
    wall_material = b.materials.get("wall", DEFAULT_WALL_MATERIAL)
    roof_material = b.materials.get("roof", wall_material or DEFAULT_ROOF_MATERIAL)
    floor_material = b.materials.get("floor", DEFAULT_FLOOR_MATERIAL)
    glass_material = b.materials.get("glass", DEFAULT_GLASS_MATERIAL)

    if not b.is_enterable():
        solid_box = (x0, y0, z0, x1, y1, z0 + b.height)
        if window_bands:
            pieces: list[tuple[float, float, float, float, float, float]] = [solid_box]
            for band in window_bands:
                hole = _box_intersection(solid_box, band)
                if hole is None:
                    continue
                new_pieces: list[tuple[float, float, float, float, float, float]] = []
                for piece in pieces:
                    piece_hole = _box_intersection(piece, hole)
                    if piece_hole is None:
                        new_pieces.append(piece)
                    else:
                        new_pieces.extend(_box_subtract(piece, piece_hole))
                pieces = new_pieces
            if pieces:
                _emit_solid_boxes(writer, pieces, wall_material, roof_material, floor_material)
        else:
            _emit_solid_building(writer, b, x0, y0, z0, x1, y1, wall_material, roof_material, floor_material)
        return
    _emit_enterable_building(
        writer, b, x0, y0, z0, x1, y1,
        wall_material, roof_material, floor_material, glass_material,
    )
