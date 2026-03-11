"""
Convert Scene to VMF: build world solids and Dystopia entities from layout.
"""

from __future__ import annotations

from layout_rules import Building, EntityHint, PropPlacement, Scene
from model_placement_rules import get_model_placement_rule, resolve_prop_origin
from vmf_writer import VmfWriter
from vmf_primitives import add_box, add_sky_shell, DEFAULT_FLOOR_MATERIAL
from building_emitter import get_enterable_window_bands, emit_building, ROOF_SLAB_THICKNESS
from dystopia_entities import (
    add_dys_spawn,
    add_dys_spawn_point,
    TEAM_CORP,
    TEAM_PUNK,
)
from spawn_layout import FLOOR_THICKNESS, FLOOR_Z, SPAWN_FLOOR_Z, Z_FIGHT_OFFSET, resolve_spawn_positions


SKY_MATERIAL = "TOOLS/TOOLSSKYBOX"
SKY_WALL_HEIGHT = 1152
SKY_THICKNESS = 64
ARENA_PADDING = 256


def _vec3(values: tuple[int, int, int]) -> str:
    return f"{int(values[0])} {int(values[1])} {int(values[2])}"


def _angles(values: tuple[int, int, int] | None) -> str:
    if values is None:
        return "0 0 0"
    return _vec3(values)


def _add_prop(writer: VmfWriter, prop: PropPlacement) -> None:
    origin = resolve_prop_origin(prop.model, prop.origin)
    writer.add_entity(
        "prop_static",
        model=prop.model,
        origin=_vec3(origin),
        angles=_angles(prop.angles),
        solid="6",
    )


def has_ceiling_above(
    buildings: list[Building],
    x: int,
    y: int,
    z: int,
    base_z: float,
) -> bool:
    """Return True if (x, y) is under a building ceiling at or above z."""
    for b in buildings:
        if b.height <= 0:
            continue
        x0, y0 = float(b.base[0]), float(b.base[1])
        x1 = x0 + b.size[0]
        y1 = y0 + b.size[1]
        if not (x0 <= x <= x1 and y0 <= y <= y1):
            continue
        z1 = base_z + b.height
        if b.is_enterable():
            ceiling_underside = z1 - ROOF_SLAB_THICKNESS
        else:
            ceiling_underside = z1
        if ceiling_underside >= z:
            return True
    return False


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
    add_box(writer, arena_x_min, arena_y_min, FLOOR_Z, arena_width, arena_depth, FLOOR_THICKNESS, DEFAULT_FLOOR_MATERIAL)

    # Buildings: solid block or enterable archetype (raised by Z_FIGHT_OFFSET to avoid z-fighting with arena floor)
    base_z = FLOOR_Z + FLOOR_THICKNESS + Z_FIGHT_OFFSET
    # Collect window bands from enterable buildings so solid buildings can be clipped and not block windows
    all_window_bands: list[tuple[float, float, float, float, float, float]] = []
    for b in scene.buildings:
        if b.is_enterable():
            all_window_bands.extend(get_enterable_window_bands(b, base_z))
    for b in scene.buildings:
        emit_building(writer, b, base_z, window_bands=all_window_bands if not b.is_enterable() else None)

    # Dystopia entities: one spawn container + points per team.
    # Spawns must be inside the arena (sky shell) and in empty space (not inside solid building brushes).
    spawn_floor = SPAWN_FLOOR_Z
    corp_spawns = scene.spawns.corp if scene.spawns.corp else [(-768, 0, spawn_floor)]
    punk_spawns = scene.spawns.punk if scene.spawns.punk else [(768, 0, spawn_floor)]
    # Only solid buildings block spawn placement; enterable buildings may contain spawns.
    building_boxes = [(b.base, b.size) for b in scene.buildings if b.height > 0 and not b.is_enterable()]
    arena_bounds = (arena_x_min, arena_y_min, arena_x_max, arena_y_max)
    corp_xy = resolve_spawn_positions(corp_spawns, 1, arena_bounds, building_boxes)
    punk_xy = resolve_spawn_positions(punk_spawns, 2, arena_bounds, building_boxes)
    # Corp spawn id 1
    add_dys_spawn(writer, "1", TEAM_CORP, (corp_xy[0][0], corp_xy[0][1], spawn_floor))
    for (x, y, yaw) in corp_xy:
        add_dys_spawn_point(writer, "1", (x, y, spawn_floor), angles=f"0 {yaw} 0")
    # Punk spawn id 2
    add_dys_spawn(writer, "2", TEAM_PUNK, (punk_xy[0][0], punk_xy[0][1], spawn_floor))
    for (x, y, yaw) in punk_xy:
        add_dys_spawn_point(writer, "2", (x, y, spawn_floor), angles=f"0 {yaw} 0")

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
        rule = get_model_placement_rule(prop.model)
        if rule and rule.requires_ceiling:
            origin = resolve_prop_origin(prop.model, prop.origin)
            if not has_ceiling_above(scene.buildings, origin[0], origin[1], origin[2], base_z):
                continue
        _add_prop(writer, prop)

    for entity in scene.entities:
        _add_entity_hint(writer, entity)

    return writer
