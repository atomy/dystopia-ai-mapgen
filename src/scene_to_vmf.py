"""
Convert Scene to VMF: build world solids and Dystopia entities from layout.
"""

from __future__ import annotations

from layout_rules import EntityHint, PropPlacement, Scene
from vmf_writer import VmfWriter
from vmf_primitives import add_box, add_sky_shell
from dystopia_entities import (
    add_dys_spawn,
    add_dys_spawn_point,
    add_dys_jackpoint,
    add_point_camera,
    TEAM_CORP,
    TEAM_PUNK,
)


FLOOR_Z = -64
FLOOR_THICKNESS = 32
MAT_FLOOR = "DEV/DEV_MEASUREGENERIC01"
MAT_WALL = "DEV/DEV_MEASUREGENERIC01"
MAT_ROOF = "DEV/DEV_MEASUREGENERIC01"
SKY_MATERIAL = "TOOLS/TOOLSSKYBOX"
SKY_WALL_HEIGHT = 1152
SKY_THICKNESS = 64
ARENA_PADDING = 256
SPAWN_CLEARANCE = 128


def _vec3(values: tuple[int, int, int]) -> str:
    return f"{int(values[0])} {int(values[1])} {int(values[2])}"


def _angles(values: tuple[int, int, int] | None) -> str:
    if values is None:
        return "0 0 0"
    return _vec3(values)


def _add_prop(writer: VmfWriter, prop: PropPlacement) -> None:
    writer.add_entity(
        "prop_static",
        model=prop.model,
        origin=_vec3(prop.origin),
        angles=_angles(prop.angles),
        solid="6",
    )


def _add_entity_hint(writer: VmfWriter, entity: EntityHint) -> None:
    payload = {
        "origin": _vec3(entity.origin),
        "angles": _angles(entity.angles),
    }
    payload.update({str(key): str(value) for key, value in entity.properties.items()})
    writer.add_entity(entity.classname, **payload)


def _scene_bounds(scene: Scene) -> tuple[int, int, int, int]:
    """Return x_min, y_min, x_max, y_max that cover the full generated scene."""
    xs: list[int] = []
    ys: list[int] = []

    for district in scene.districts:
        xs.extend([district.bounds.x_min, district.bounds.x_max])
        ys.extend([district.bounds.y_min, district.bounds.y_max])

    for street in scene.streets:
        half_width = street.width // 2
        for x, y in street.path:
            xs.extend([x - half_width, x + half_width])
            ys.extend([y - half_width, y + half_width])

    for building in scene.buildings:
        xs.extend([building.base[0], building.base[0] + building.size[0]])
        ys.extend([building.base[1], building.base[1] + building.size[1]])

    for x, y, _z in scene.spawns.corp + scene.spawns.punk:
        xs.append(x)
        ys.append(y)

    for objective in scene.objectives:
        xs.append(objective.position[0])
        ys.append(objective.position[1])

    for prop in scene.props:
        xs.append(prop.origin[0])
        ys.append(prop.origin[1])

    for entity in scene.entities:
        xs.append(entity.origin[0])
        ys.append(entity.origin[1])

    if not xs or not ys:
        return (-1024, -1024, 1024, 1024)

    return (
        min(xs) - ARENA_PADDING,
        min(ys) - ARENA_PADDING,
        max(xs) + ARENA_PADDING,
        max(ys) + ARENA_PADDING,
    )


def _clamp_to_arena(
    x: int, y: int, x_min: int, y_min: int, x_max: int, y_max: int, margin: int = 64
) -> tuple[int, int]:
    """Clamp x,y to inside the playable area (inside sky shell / floor)."""
    return (
        max(x_min + margin, min(x_max - margin, x)),
        max(y_min + margin, min(y_max - margin, y)),
    )


def _move_spawn_out_of_buildings(
    x: int,
    y: int,
    buildings: list[tuple[tuple[int, int], tuple[int, int]]],
    clearance: int = SPAWN_CLEARANCE,
) -> tuple[int, int, str]:
    """Keep spawn points out of building solids and away from walls, facing outward."""
    yaw = "0"
    for (bx, by), (bw, bd) in buildings:
        x0, y0 = bx, by
        x1, y1 = bx + bw, by + bd
        # Keep a clearance ring around each building so pads are not pressed against walls.
        if (x0 - clearance) <= x <= (x1 + clearance) and (y0 - clearance) <= y <= (y1 + clearance):
            best = (x, y, yaw)
            best_dist = float("inf")
            # Source yaw: 0=east, 90=north, 180=west, 270=south.
            # Face away from the wall that forced the spawn pad outward.
            candidates = [
                (x0 - clearance, y, "180"),
                (x1 + clearance, y, "0"),
                (x, y0 - clearance, "270"),
                (x, y1 + clearance, "90"),
            ]
            for nx, ny, candidate_yaw in candidates:
                dist = abs(nx - x) + abs(ny - y)
                if dist < best_dist:
                    best_dist = dist
                    best = (nx, ny, candidate_yaw)
            return best
    return (x, y, yaw)


def scene_to_vmf(scene: Scene) -> VmfWriter:
    writer = VmfWriter()

    arena_x_min, arena_y_min, arena_x_max, arena_y_max = _scene_bounds(scene)
    arena_width = arena_x_max - arena_x_min
    arena_depth = arena_y_max - arena_y_min
    shell_top_z = FLOOR_Z + SKY_WALL_HEIGHT

    # Seal the playable space so VBSP/VVIS can generate portals.
    add_sky_shell(
        writer,
        arena_x_min,
        arena_y_min,
        FLOOR_Z,
        arena_x_max,
        arena_y_max,
        shell_top_z,
        thickness=SKY_THICKNESS,
        material=SKY_MATERIAL,
    )

    # Arena floor.
    add_box(writer, arena_x_min, arena_y_min, FLOOR_Z, arena_width, arena_depth, FLOOR_THICKNESS, MAT_FLOOR)

    # Buildings as boxes (skip plaza with height 0)
    for b in scene.buildings:
        if b.height <= 0:
            continue
        x, y = b.base
        w, d = b.size
        wall_material = b.materials.get("wall", MAT_WALL)
        roof_material = b.materials.get("roof", wall_material or MAT_ROOF)
        floor_material = b.materials.get("floor", MAT_FLOOR)

        add_box(writer, x, y, FLOOR_Z + FLOOR_THICKNESS, w, d, b.height, wall_material)

        # Add thin roof and floor caps so JSON material hints affect visible surfaces.
        add_box(writer, x, y, FLOOR_Z + FLOOR_THICKNESS, w, d, 16, floor_material)
        add_box(writer, x, y, FLOOR_Z + FLOOR_THICKNESS + b.height - 16, w, d, 16, roof_material)

    # Dystopia entities: one spawn container + points per team, one jackpoint + camera
    # Spawns must be inside the arena (sky shell) and in empty space (not inside solid building brushes).
    spawn_floor = FLOOR_Z + FLOOR_THICKNESS
    corp_spawns = scene.spawns.corp if scene.spawns.corp else [(-768, 0, spawn_floor)]
    punk_spawns = scene.spawns.punk if scene.spawns.punk else [(768, 0, spawn_floor)]
    building_boxes = [(b.base, b.size) for b in scene.buildings if b.height > 0]

    def place_spawns(positions: list[tuple[int, int, int]], team_side: int) -> list[tuple[int, int, str]]:
        """Clamp to arena, keep spawn pads clear of walls, and return x/y plus facing yaw."""
        out: list[tuple[int, int, str]] = []
        for pos in positions:
            x, y = _clamp_to_arena(pos[0], pos[1], arena_x_min, arena_y_min, arena_x_max, arena_y_max)
            x, y, yaw = _move_spawn_out_of_buildings(x, y, building_boxes)
            x, y = _clamp_to_arena(x, y, arena_x_min, arena_y_min, arena_x_max, arena_y_max)
            out.append((x, y, yaw))
        if not out:
            fallback = (
                (arena_x_min + 128, (arena_y_min + arena_y_max) // 2)
                if team_side == 1
                else (arena_x_max - 128, (arena_y_min + arena_y_max) // 2)
            )
            x, y, yaw = _move_spawn_out_of_buildings(fallback[0], fallback[1], building_boxes)
            x, y = _clamp_to_arena(x, y, arena_x_min, arena_y_min, arena_x_max, arena_y_max)
            out.append((x, y, yaw))
        return out

    corp_xy = place_spawns(corp_spawns, 1)
    punk_xy = place_spawns(punk_spawns, 2)
    # Corp spawn id 1
    add_dys_spawn(writer, "1", TEAM_CORP, (corp_xy[0][0], corp_xy[0][1], spawn_floor))
    for (x, y, yaw) in corp_xy:
        add_dys_spawn_point(writer, "1", (x, y, spawn_floor), angles=f"0 {yaw} 0")
    # Punk spawn id 2
    add_dys_spawn(writer, "2", TEAM_PUNK, (punk_xy[0][0], punk_xy[0][1], spawn_floor))
    for (x, y, yaw) in punk_xy:
        add_dys_spawn_point(writer, "2", (x, y, spawn_floor), angles=f"0 {yaw} 0")
    # Jackpoint + camera near objective
    obj_pos = scene.objectives[0].position
    jp_x, jp_y, jp_z = obj_pos[0], obj_pos[1], obj_pos[2]
    add_dys_jackpoint(writer, (jp_x, jp_y, jp_z), "cam1", (24, 24, 24))
    add_point_camera(writer, "cam1", (jp_x + 64, jp_y, jp_z + 400))

    # Basic lighting so the map does not compile black.
    writer.add_entity(
        "light_environment",
        angles="0 45 0",
        pitch="-45",
        _light="255 255 255 300",
        _ambient="96 96 128 40",
        origin=f"0 0 {shell_top_z - 64}",
    )
    writer.add_entity("light", origin="-768 0 128", _light="255 220 200 250")
    writer.add_entity("light", origin="768 0 128", _light="200 220 255 250")
    writer.add_entity("light", origin="0 0 384", _light="255 255 255 350")

    for prop in scene.props:
        _add_prop(writer, prop)

    for entity in scene.entities:
        _add_entity_hint(writer, entity)

    return writer
