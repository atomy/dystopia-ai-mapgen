"""
Shared spawn placement helpers used by export and layout validation.
"""

from __future__ import annotations

from statistics import median


FLOOR_Z = -64
FLOOR_THICKNESS = 32
SPAWN_FLOOR_Z = FLOOR_Z + FLOOR_THICKNESS
SPAWN_CLEARANCE = 128
ARENA_MARGIN = 64


def clamp_to_arena(
    x: int, y: int, x_min: int, y_min: int, x_max: int, y_max: int, margin: int = ARENA_MARGIN
) -> tuple[int, int]:
    """Clamp x,y to inside the playable area (inside sky shell / floor)."""
    return (
        max(x_min + margin, min(x_max - margin, x)),
        max(y_min + margin, min(y_max - margin, y)),
    )


def move_spawn_out_of_buildings(
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
        if (x0 - clearance) <= x <= (x1 + clearance) and (y0 - clearance) <= y <= (y1 + clearance):
            best = (x, y, yaw)
            best_dist = float("inf")
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


def _resolve_single_spawn_position(
    x: int,
    y: int,
    arena_bounds: tuple[int, int, int, int],
    building_boxes: list[tuple[tuple[int, int], tuple[int, int]]],
) -> tuple[int, int, str]:
    arena_x_min, arena_y_min, arena_x_max, arena_y_max = arena_bounds
    x, y = clamp_to_arena(x, y, arena_x_min, arena_y_min, arena_x_max, arena_y_max)
    x, y, yaw = move_spawn_out_of_buildings(x, y, building_boxes)
    x, y = clamp_to_arena(x, y, arena_x_min, arena_y_min, arena_x_max, arena_y_max)
    return (x, y, yaw)


def _detect_line_orientation(positions: list[tuple[int, int]]) -> str | None:
    if len(positions) < 3:
        return None
    xs = {x for x, _y in positions}
    ys = {y for _x, y in positions}
    if len(xs) == 1 and len(ys) > 1:
        return "vertical"
    if len(ys) == 1 and len(xs) > 1:
        return "horizontal"
    return None


def _dominant_spacing(axis_values: list[int]) -> int:
    deltas = [current - previous for previous, current in zip(axis_values, axis_values[1:]) if current > previous]
    if not deltas:
        return 0
    return max(1, int(round(median(deltas))))


def _clamp_sequence_start(start: int, spacing: int, count: int, axis_min: int, axis_max: int) -> int:
    max_start = axis_max - (spacing * (count - 1))
    return max(axis_min, min(max_start, start))


def _line_has_direct_blocker(
    orientation: str,
    fixed_value: int,
    axis_start: int,
    axis_end: int,
    buildings: list[tuple[tuple[int, int], tuple[int, int]]],
) -> bool:
    span_min = min(axis_start, axis_end)
    span_max = max(axis_start, axis_end)
    for (bx, by), (bw, bd) in buildings:
        x0, y0 = bx, by
        x1, y1 = bx + bw, by + bd
        if orientation == "vertical":
            if x0 <= fixed_value <= x1 and span_min <= y1 and span_max >= y0:
                return True
        else:
            if y0 <= fixed_value <= y1 and span_min <= x1 and span_max >= x0:
                return True
    return False


def _build_evenly_spaced_line(
    authored_xy: list[tuple[int, int]],
    resolved_xy: list[tuple[int, int, str]],
    arena_bounds: tuple[int, int, int, int],
    building_boxes: list[tuple[tuple[int, int], tuple[int, int]]],
) -> list[tuple[int, int, str]] | None:
    orientation = _detect_line_orientation(authored_xy)
    if orientation is None:
        return None

    arena_x_min, arena_y_min, arena_x_max, arena_y_max = arena_bounds
    if orientation == "vertical":
        axis_min = arena_y_min + ARENA_MARGIN
        axis_max = arena_y_max - ARENA_MARGIN
        fixed_min = arena_x_min + ARENA_MARGIN
        fixed_max = arena_x_max - ARENA_MARGIN
        authored_axis = [y for _x, y in authored_xy]
        authored_fixed = [x for x, _y in authored_xy]
        resolved_fixed = [x for x, _y, _yaw in resolved_xy]
    else:
        axis_min = arena_x_min + ARENA_MARGIN
        axis_max = arena_x_max - ARENA_MARGIN
        fixed_min = arena_y_min + ARENA_MARGIN
        fixed_max = arena_y_max - ARENA_MARGIN
        authored_axis = [x for x, _y in authored_xy]
        authored_fixed = [y for _x, y in authored_xy]
        resolved_fixed = [y for _x, y, _yaw in resolved_xy]

    sorted_indices = sorted(range(len(authored_xy)), key=lambda idx: authored_axis[idx])
    sorted_authored_axis = [authored_axis[idx] for idx in sorted_indices]
    spacing = _dominant_spacing(sorted_authored_axis)
    if spacing <= 0 or (spacing * (len(authored_xy) - 1)) > (axis_max - axis_min):
        return None

    start_candidates = {
        _clamp_sequence_start(
            sorted_authored_axis[order] - (order * spacing),
            spacing,
            len(sorted_indices),
            axis_min,
            axis_max,
        )
        for order in range(len(sorted_indices))
    }
    centered_start = int(round((sum(sorted_authored_axis) / len(sorted_authored_axis)) - (spacing * (len(sorted_indices) - 1) / 2)))
    start_candidates.add(
        _clamp_sequence_start(centered_start, spacing, len(sorted_indices), axis_min, axis_max)
    )

    fixed_candidates = {
        value
        for value in {authored_fixed[sorted_indices[0]], *resolved_fixed}
        if fixed_min <= value <= fixed_max
    }

    best_score: int | None = None
    best_positions: list[tuple[int, int, str]] | None = None
    for fixed_value in sorted(fixed_candidates):
        for start in sorted(start_candidates):
            axis_values = [start + (order * spacing) for order in range(len(sorted_indices))]
            if _line_has_direct_blocker(orientation, fixed_value, axis_values[0], axis_values[-1], building_boxes):
                continue

            candidate_positions: list[tuple[int, int, str]] = []
            for axis_value in axis_values:
                x = fixed_value if orientation == "vertical" else axis_value
                y = axis_value if orientation == "vertical" else fixed_value
                resolved = _resolve_single_spawn_position(x, y, arena_bounds, building_boxes)
                if resolved[:2] != (x, y):
                    candidate_positions = []
                    break
                candidate_positions.append(resolved)
            if not candidate_positions:
                continue

            score = 0
            for order, original_idx in enumerate(sorted_indices):
                score += abs(axis_values[order] - authored_axis[original_idx])
                score += abs(fixed_value - authored_fixed[original_idx])
            if best_score is None or score < best_score:
                best_score = score
                best_positions = candidate_positions

    if best_positions is None:
        return None

    out: list[tuple[int, int, str] | None] = [None] * len(sorted_indices)
    for order, original_idx in enumerate(sorted_indices):
        out[original_idx] = best_positions[order]
    return [position for position in out if position is not None]


def resolve_spawn_positions(
    positions: list[tuple[int, int, int]],
    team_side: int,
    arena_bounds: tuple[int, int, int, int],
    building_boxes: list[tuple[tuple[int, int], tuple[int, int]]],
) -> list[tuple[int, int, str]]:
    """Resolve authored spawn coordinates into final exporter x/y placements."""
    authored_xy = [
        _resolve_single_spawn_position(pos[0], pos[1], arena_bounds, [])[0:2]
        for pos in positions
    ]
    out = [
        _resolve_single_spawn_position(pos[0], pos[1], arena_bounds, building_boxes)
        for pos in positions
    ]
    even_line = _build_evenly_spaced_line(authored_xy, out, arena_bounds, building_boxes)
    if even_line is not None:
        return even_line

    if not out:
        arena_x_min, arena_y_min, arena_x_max, arena_y_max = arena_bounds
        fallback = (
            (arena_x_min + 128, (arena_y_min + arena_y_max) // 2)
            if team_side == 1
            else (arena_x_max - 128, (arena_y_min + arena_y_max) // 2)
        )
        out.append(_resolve_single_spawn_position(fallback[0], fallback[1], arena_bounds, building_boxes))
    return out
