from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from spawn_layout import resolve_spawn_positions


def _axis_deltas(values: list[int]) -> list[int]:
    return [current - previous for previous, current in zip(values, values[1:])]


def test_evenly_spaces_aligned_vertical_spawns_without_blockers() -> None:
    resolved = resolve_spawn_positions(
        [
            (-768, 0, -64),
            (-768, 256, -64),
            (-768, 640, -64),
            (-768, 896, -64),
        ],
        team_side=1,
        arena_bounds=(-1024, -1024, 1024, 1024),
        building_boxes=[],
    )

    xs = {x for x, _y, _yaw in resolved}
    ys = [y for _x, y, _yaw in resolved]

    assert xs == {-768}
    assert _axis_deltas(ys) == [256, 256, 256]


def test_keeps_irregular_spacing_when_a_building_blocks_the_line() -> None:
    resolved = resolve_spawn_positions(
        [
            (-768, 0, -64),
            (-768, 256, -64),
            (-768, 512, -64),
            (-768, 768, -64),
        ],
        team_side=1,
        arena_bounds=(-1024, -1024, 1024, 1024),
        building_boxes=[((-832, 320), (128, 128))],
    )

    ys = [y for _x, y, _yaw in resolved]

    assert _axis_deltas(ys) == [192, 384, 192]
