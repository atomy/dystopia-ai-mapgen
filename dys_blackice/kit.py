"""Detail kit: stairs, doors, glass, rails, pillars, lights, props, triggers.

Everything here emits func_detail / brush entities / point entities into a VMF,
never world brushes, so none of it affects sealing or vis.
"""
from __future__ import annotations

import math

import assets
from vmflib import (VMF, Tex, box, hull, ngon, wedge, NODRAW, PLAYERCLIP, CLIP, TRIGGER, INVISIBLE, num)

UP = {"+x": (1, 0), "-x": (-1, 0), "+y": (0, 1), "-y": (0, -1)}


def stairs(m: VMF, x0, y0, z0, x1, y1, z1, rise: str, step=16, mat="concrete/concretefloor008a",
           riser=None, clip=True):
    """Solid staircase filling the box, rising toward `rise`. Returns step count."""
    x0, x1 = min(x0, x1), max(x0, x1)
    y0, y1 = min(y0, y1), max(y0, y1)
    h = z1 - z0
    n = max(1, round(h / step))
    sh = h / n
    along_x = rise in ("+x", "-x")
    length = (x1 - x0) if along_x else (y1 - y0)
    run = length / n
    solids = []
    for i in range(n):
        top = z0 + sh * (i + 1)
        if rise == "+x":
            bx = (x0 + run * i, y0, x1, y1)
        elif rise == "-x":
            bx = (x0, y0, x1 - run * i, y1)
        elif rise == "+y":
            bx = (x0, y0 + run * i, x1, y1)
        else:
            bx = (x0, y0, x1, y1 - run * i)
        mats = {"top": mat, "all": riser or mat}
        solids.append(box(round(bx[0]), round(bx[1]), z0 if i == 0 else round(z0 + sh * i), round(bx[2]), round(bx[3]), round(top), mats))
    m.detail(solids)
    if clip:
        # smooth ramp over the step noses so movement doesn't judder
        m.add(wedge(x0, y0, z0, x1, y1, z1, rise=rise, mats=PLAYERCLIP))
    return n


def stringer(m: VMF, x0, y0, x1, y1, zb, z0, z1, h=40, t=4, mat="metal/metalwall003a", clip=64):
    """Solid side wall of a flight along an axis-aligned line (x0,y0)->(x1,y1): from the floor zb up to the
    stair line (z0 at the start, z1 at the end) plus h, with a sloped player clip on top."""
    if y0 == y1:
        a, b = (x0, y0 - t / 2), (x0, y0 + t / 2)
        c, d = (x1, y0 - t / 2), (x1, y0 + t / 2)
    else:
        a, b = (x0 - t / 2, y0), (x0 + t / 2, y0)
        c, d = (x0 - t / 2, y1), (x0 + t / 2, y1)
    pts = [(*a, zb), (*b, zb), (*c, zb), (*d, zb), (*a, z0 + h), (*b, z0 + h), (*c, z1 + h), (*d, z1 + h)]
    m.detail(hull(pts, mat))
    if clip:
        m.add(hull([(*a, z0 + h), (*b, z0 + h), (*c, z1 + h), (*d, z1 + h),
                    (*a, z0 + h + clip), (*b, z0 + h + clip), (*c, z1 + h + clip), (*d, z1 + h + clip)], PLAYERCLIP))


def filter_team(m: VMF, name, team):
    return m.ent("filter_activator_team", (0, 0, 0), targetname=name, filterteam=str(team), Negated="0")


def slide_door(m: VMF, name, x0, y0, z0, x1, y1, z1, mat, frame_mat=None, filtername=None,
               start_disabled=False, speed=220, trigger_pad=72, sound=True, lip=6):
    """Split sliding door filling an opening; leaves slide sideways into the wall.
    The opening's long horizontal axis is the slide axis. Proximity trigger opens it."""
    dx, dy = x1 - x0, y1 - y0
    along_x = dx >= dy
    solids = []
    if along_x:
        mid = (x0 + x1) // 2
        a = m.brush_ent("func_door", box(x0, y0, z0, mid, y1, z1, mat), targetname=name, movedir="0 180 0",
                        speed=str(speed), wait="-1", lip=str(lip), spawnflags="0", forceclosed="1",
                        noise1="doors/doormove2.wav" if sound else None, noise2="doors/door_metal_thin_close2.wav" if sound else None,
                        origin=((x0 + mid) / 2, (y0 + y1) / 2, (z0 + z1) / 2), disablereceiveshadows="1")
        b = m.brush_ent("func_door", box(mid, y0, z0, x1, y1, z1, mat), targetname=name, movedir="0 0 0",
                        speed=str(speed), wait="-1", lip=str(lip), spawnflags="0", forceclosed="1",
                        origin=((mid + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2), disablereceiveshadows="1")
        tbox = box(x0, y0 - trigger_pad, z0, x1, y1 + trigger_pad, z1, TRIGGER)
    else:
        mid = (y0 + y1) // 2
        a = m.brush_ent("func_door", box(x0, y0, z0, x1, mid, z1, mat), targetname=name, movedir="0 270 0",
                        speed=str(speed), wait="-1", lip=str(lip), spawnflags="0", forceclosed="1",
                        noise1="doors/doormove2.wav" if sound else None, noise2="doors/door_metal_thin_close2.wav" if sound else None,
                        origin=((x0 + x1) / 2, (y0 + mid) / 2, (z0 + z1) / 2), disablereceiveshadows="1")
        b = m.brush_ent("func_door", box(x0, mid, z0, x1, y1, z1, mat), targetname=name, movedir="0 90 0",
                        speed=str(speed), wait="-1", lip=str(lip), spawnflags="0", forceclosed="1",
                        origin=((x0 + x1) / 2, (mid + y1) / 2, (z0 + z1) / 2), disablereceiveshadows="1")
        tbox = box(x0 - trigger_pad, y0, z0, x1 + trigger_pad, y1, z1, TRIGGER)
    trig = m.brush_ent("trigger_multiple", tbox, targetname=f"{name}_trig", spawnflags="1", wait="0.2",
                       filtername=filtername, StartDisabled="1" if start_disabled else "0")
    trig.out("OnStartTouch", name, "Open")
    trig.out("OnEndTouchAll", name, "Close")
    return a, b, trig


def gate(m: VMF, name, x0, y0, z0, x1, y1, z1, mat, speed=60, lip=12, sound="doors/garage_move1.wav"):
    """Roller gate that lifts up when told to Open (no trigger)."""
    return m.brush_ent("func_door", box(x0, y0, z0, x1, y1, z1, mat), targetname=name, movedir="-90 0 0",
                       speed=str(speed), wait="-1", lip=str(lip), spawnflags="0", forceclosed="1",
                       noise1=sound, noise2="doors/garage_stop1.wav",
                       origin=((x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2))


def glass(m: VMF, x0, y0, z0, x1, y1, z1, mat="glass/glasswindow007a", breakable=False, name=None, edge=NODRAW):
    """Glass pane; only the two large faces get the glass material."""
    dx, dy, dz = x1 - x0, y1 - y0, z1 - z0
    thin = min((dx, "x"), (dy, "y"), (dz, "z"))[1]
    faces = {"x": ("east", "west"), "y": ("north", "south"), "z": ("top", "bottom")}[thin]
    mats = {k: (mat if k in faces else edge) for k in ("top", "bottom", "north", "south", "east", "west")}
    s = box(x0, y0, z0, x1, y1, z1, mats)
    if breakable:
        return m.brush_ent("func_breakable_surf", s, targetname=name, health="5", fragility="30",
                           surfacetype="0", error="0", spawnflags="0", propdata="0")
    return m.brush_ent("func_brush", s, targetname=name, Solidity="2", solidbsp="0", StartDisabled="0",
                       rendermode="0", renderamt="255", disableshadows="1", spawnflags="2", InputFilter="0",
                       vrad_brush_cast_shadows="0")


def rail(m: VMF, x0, y0, x1, y1, z, h=40, t=4, mat="metal/metalrail001a", post_every=128, cap=None):
    """Simple metal railing along an axis-aligned line (func_detail + clip to stop jumping over? no)."""
    solids = []
    if abs(x1 - x0) >= abs(y1 - y0):
        ya, yb = y0 - t / 2, y0 + t / 2
        solids.append(box(min(x0, x1), round(ya), z + h - 4, max(x0, x1), round(yb), z + h, cap or mat))
        solids.append(box(min(x0, x1), round(ya), z + h / 2 - 2, max(x0, x1), round(yb), z + h / 2 + 2, mat))
        n = max(1, int(abs(x1 - x0) // post_every))
        for i in range(n + 1):
            x = min(x0, x1) + i * abs(x1 - x0) / n
            x = min(max(x, min(x0, x1) + 2), max(x0, x1) - 2)
            solids.append(box(round(x - 2), round(ya), z, round(x + 2), round(yb), z + h - 4, mat))
    else:
        xa, xb = x0 - t / 2, x0 + t / 2
        solids.append(box(round(xa), min(y0, y1), z + h - 4, round(xb), max(y0, y1), z + h, cap or mat))
        solids.append(box(round(xa), min(y0, y1), z + h / 2 - 2, round(xb), max(y0, y1), z + h / 2 + 2, mat))
        n = max(1, int(abs(y1 - y0) // post_every))
        for i in range(n + 1):
            y = min(y0, y1) + i * abs(y1 - y0) / n
            y = min(max(y, min(y0, y1) + 2), max(y0, y1) - 2)
            solids.append(box(round(xa), round(y - 2), z, round(xb), round(y + 2), z + h - 4, mat))
    return m.detail(solids)


def clip_box(m: VMF, x0, y0, z0, x1, y1, z1, kind=PLAYERCLIP):
    return m.add(box(x0, y0, z0, x1, y1, z1, kind))


def pillar(m: VMF, x, y, z0, z1, w=32, mat="concrete/concretewall071a", round_sides=0, cap_mat=None):
    if round_sides:
        s = ngon(x, y, w / 2, round_sides, z0, z1, {"all": mat, "top": cap_mat or mat, "bottom": cap_mat or mat})
    else:
        s = box(x - w / 2, y - w / 2, z0, x + w / 2, y + w / 2, z1, {"all": mat, "top": cap_mat or mat, "bottom": cap_mat or mat})
    return m.detail(s)


def prop(m: VMF, model, x, y, z, yaw=0, pitch=0, roll=0, skin=0, solid=6, fade=None, on_floor=True,
         cls="prop_static", **kv):
    """prop_static by default. If on_floor, lifts the model so its hull rests at z."""
    info = assets.mdl_info(model)
    assert info, f"missing model {model}"
    if cls == "prop_static" and not info["static_ok"]:
        cls = "prop_dynamic_override"      # physics/breakable models can't be static
        kv.setdefault("DisableBoneFollowers", "1")
    zz = z
    if fade is None:     # small clutter fades out; big props stay
        mn, mx = info["hull_min"], info["hull_max"]
        if max(mx[i] - mn[i] for i in range(3)) < 72:
            fade = (1400, 1900)
    if on_floor and pitch == 0 and roll == 0:
        zz = z - info["hull_min"][2]
    d = dict(model=model, angles=f"{num(pitch)} {num(yaw)} {num(roll)}", skin=str(skin), solid=str(solid))
    d["disableshadows"] = kv.pop("disableshadows", "0")
    if cls in ("prop_static", "prop_dynamic_override", "prop_dynamic"):
        d["screenspacefade"] = "0"
        if fade:
            d["fademindist"], d["fademaxdist"] = str(fade[0]), str(fade[1])
    d.update(kv)
    return m.ent(cls, (x, y, zz), **d)


def light(m: VMF, x, y, z, color=(255, 240, 220), bright=200, name=None, style=None, q=None, hdr_scale=1.0,
          fifty=None, hundred=None, **kv):
    d = dict(_light=f"{color[0]} {color[1]} {color[2]} {bright}", _lightHDR="-1 -1 -1 1",
             _lightscaleHDR=str(hdr_scale), targetname=name)
    if style is not None:
        d["style"] = str(style)
    if fifty is not None:
        d["_fifty_percent_distance"] = str(fifty)
        d["_zero_percent_distance"] = str(hundred or fifty * 2.5)
    if q:
        d["_quadratic_attn"], d["_linear_attn"], d["_constant_attn"] = str(q[0]), str(q[1]), str(q[2])
    d.update(kv)
    return m.ent("light", (x, y, z), **d)


def spot(m: VMF, x, y, z, pitch=-90, yaw=0, color=(255, 240, 220), bright=400, inner=30, outer=45, name=None, **kv):
    d = dict(_light=f"{color[0]} {color[1]} {color[2]} {bright}", _lightHDR="-1 -1 -1 1", _lightscaleHDR="1",
             angles=f"{num(pitch)} {num(yaw)} 0", pitch=str(pitch), _inner_cone=str(inner), _cone=str(outer),
             _exponent="1", targetname=name)
    d.update(kv)
    return m.ent("light_spot", (x, y, z), **d)


def sprite(m: VMF, x, y, z, color=(255, 255, 255), scale=0.25, mat="sprites/light_glow03.vmt", alpha=160, name=None):
    return m.ent("env_sprite", (x, y, z), model=mat, rendercolor=f"{color[0]} {color[1]} {color[2]}", renderamt=str(alpha),
                 rendermode="9", scale=str(scale), spawnflags="1", GlowProxySize="4", HDRColorScale="1.0",
                 targetname=name, framerate="10.0")


def trigger(m: VMF, cls, x0, y0, z0, x1, y1, z1, **kv):
    return m.brush_ent(cls, box(x0, y0, z0, x1, y1, z1, TRIGGER), **kv)
