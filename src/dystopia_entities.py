"""
Dystopia entity presets: dys_spawn, dys_spawn_point, dys_jackpoint, point_camera.
Emit via VmfWriter.add_entity (and add_brush for jackpoint).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vmf_writer import VmfWriter


# Dystopia spawn teams used by shipped maps:
# 2 = punk, 3 = corp
TEAM_CORP = "3"
TEAM_PUNK = "2"


def add_dys_spawn(
    writer: VmfWriter,
    spawnid: str,
    team: str,
    origin: tuple[float, float, float],
    spawnflags: str = "1",
) -> None:
    """Add dys_spawn container. spawnid links to dys_spawn_point(s)."""
    x, y, z = origin
    writer.add_entity(
        classname="dys_spawn",
        spawnflags=spawnflags,
        spawnid=spawnid,
        team=team,
        origin=f"{int(x)} {int(y)} {int(z)}",
    )


def add_dys_spawn_point(
    writer: VmfWriter,
    spawnid: str,
    origin: tuple[float, float, float],
    angles: str = "0 0 0",
    spawnflags: str = "0",
) -> None:
    """Add single spawn point linked to dys_spawn by spawnid."""
    x, y, z = origin
    writer.add_entity(
        classname="dys_spawn_point",
        angles=angles,
        spawnflags=spawnflags,
        spawnid=spawnid,
        origin=f"{int(x)} {int(y)} {int(z)}",
    )


def add_dys_jackpoint(
    writer: VmfWriter,
    origin: tuple[float, float, float],
    target: str,
    size: tuple[float, float, float] = (32, 32, 32),
) -> None:
    """Add dys_jackpoint brush entity; target must match a point_camera targetname."""
    x, y, z = origin
    wx, wy, wz = size[0] / 2, size[1] / 2, size[2] / 2
    x0, y0, z0 = x - wx, y - wy, z - wz
    x1, y1, z1 = x + wx, y + wy, z + wz
    # Same face order and winding as vmf_primitives.add_box (reference VMF)
    planes = [
        ((x0, y1, z1), (x1, y1, z1), (x1, y0, z1)),   # top
        ((x0, y0, z0), (x1, y0, z0), (x1, y1, z0)),   # bottom
        ((x0, y1, z1), (x0, y0, z1), (x0, y0, z0)),   # x-
        ((x1, y1, z0), (x1, y0, z0), (x1, y0, z1)),   # x+
        ((x1, y1, z1), (x0, y1, z1), (x0, y1, z0)),   # y+
        ((x1, y0, z0), (x0, y0, z0), (x0, y0, z1)),   # y-
    ]
    solid_id = writer.alloc_id()
    sides = []
    axis_order = ["z+", "z-", "x-", "x+", "y+", "y-"]
    from vmf_writer import _plane_string, _uaxis_vaxis_for_plane
    for i, (p1, p2, p3) in enumerate(planes):
        side_id = writer.alloc_id()
        axis = axis_order[i]
        uaxis, vaxis = _uaxis_vaxis_for_plane(axis)
        sides.append({
            "id": side_id,
            "plane": _plane_string(p1, p2, p3),
            "material": "TOOLS/TOOLSNODRAW" if i != 3 else "DEV/DEV_MEASUREGENERIC01",
            "uaxis": uaxis,
            "vaxis": vaxis,
            "rotation": "0",
            "lightmapscale": "16",
            "smoothing_groups": "0",
        })
    writer.add_entity(
        classname="dys_jackpoint",
        spawnflags="0",
        target=target,
        origin=f"{int(x)} {int(y)} {int(z)}",
        solid={"id": solid_id, "sides": sides},
    )


def add_point_camera(
    writer: VmfWriter,
    targetname: str,
    origin: tuple[float, float, float],
    render_target: str | None = None,
    angles: str = "0 0 0",
    fov: str = "90",
) -> None:
    """Add point_camera for jack-in. targetname is referenced by dys_jackpoint target."""
    x, y, z = origin
    rt = render_target or targetname
    writer.add_entity(
        classname="point_camera",
        angles=angles,
        targetname=targetname,
        renderTarget=rt,
        FOV=fov,
        fogEnable="0",
        fogColor="0 0 0",
        fogStart="2048",
        fogEnd="4096",
        spawnflags="0",
        origin=f"{int(x)} {int(y)} {int(z)}",
    )
