"""Cyberspace for dys_blackice: one big open hall north of the city (y 3584..6144), the Black ICE grid.

            north wall: BLACK ICE warning
   [H2 gate turrets]    [red core terrace + H5 core shield]    [H4 vault turrets]
   [H1 lobby turrets]
   punk entry ->           open data plain, pillars, cover           <- corp entry
                                     mid entry                    [H3 maintenance]

Every terminal sits in a small house whose doorway is filled by its ICE: Punk deckers hack (wedge)
the ICE to get in, Corps deckers pass their own ICE. Only the flat hall floor is cyber_floor, because
touching a cyber_floor face re-orients the decker's gravity to it.

Deckers jack in to a small pod outside the hall and float through a glowing blue tube that sweeps down a long,
gentle S-curve through a dark void and enters the hall at floor level (zero gravity between two
cyber_gravity_volumes, whose angles point at the room with gravity); they step out through their team's static
ICE, which the other team cannot pass. The jack-in terminals show their entry camera's view upside down, so the
camera sits at the pod's vertical centre looking into the tube mouth: the view reads either way.
"""
from __future__ import annotations

import math

import kit
from dress import FACE_KEY, FACING, fit_tex, panel
from gameplay import screen, relay, PUNKS, CORPS
from vmflib import VMF, Tex, box, ngon, wedge, NODRAW, TRIGGER

ICE_MAT = "cyberspace/scroller_gibberish"
FLOOR_MAT = "termitex/cysp_floor04_blue"
CORE_FLOOR = "termitex/cysp_floor04_red"
PAD_MAT = "termitex/cysp_floor01"
TRIM = "twincannon/twin_cyberwhite"
DARK = "cyberspace/t_cyspwall1_black"

HALL = (-1792, 3584, 0, 1792, 6144, 1024)
FLOOR = 16                                  # top of the hall's cyber_floor slab
TERRACE = (-448, 5120, 448, 5952, 176)      # core terrace x0, y0, x1, y1, top z
ENTRIES = [  # camera name, pod wall point (x, y), direction into the hall, team of the exit ICE (None = open)
    ("cy_entry_punk", (-1792, 4864), (1, 0), PUNKS),
    ("cy_entry_mid", (0, 3584), (0, 1), None),
    ("cy_entry_corp", (1792, 4864), (-1, 0), CORPS),
]
POD_D, POD_W, POD_Z, POD_H = 256, 256, 640, 160     # spawn pod outside the hall: depth, width, floor z, height
LEAD, TAIL, EXIT = 64, 96, 32                      # level run after the pod, level run before the wall, stub inside
TUBE_H = 64                                        # tube inner half-size (128 x 128), walls 8 thick
TUBE_MAT = "twincannon/twin_cyberblue_trans_additive_nocull"   # glowing blue glass, seen from both sides
EDGE_MAT = "twincannon/twin_cyberwhite"            # light strips along the tube's four edges
FRAME_MAT = "cyberspace/t_cyspwall1_black"
PILLARS = [(-640, 4480), (640, 4480), (-640, 5888), (640, 5888)]
COVER = [(-1280, 4864, 64, 64), (1280, 4864, 64, 64), (-384, 4352, 64, 64), (384, 4352, 64, 64),
         (0, 4864, 128, 48)]           # centre x, y, half-size x, y (blocks 80 high)

# door facing -> world face key for local +v (toward the door), -v, +u, -u
_FACES = {"+y": ("north", "south", "east", "west"), "-y": ("south", "north", "west", "east"),
          "+x": ("east", "west", "south", "north"), "-x": ("west", "east", "north", "south")}


def _geom(wall, d):
    """Pod room and void boxes (world, for the CSG) + the tube centre line [(a, z)] for one entry;
    a = distance from the hall wall along d (negative = outside the hall). The whole descent happens outside."""
    sx, sy = -d[1], d[0]
    cz = POD_Z + 16 + (POD_H - 16) // 2               # pod interior centre = tube centre = camera height
    low = FLOOR + TUBE_H                               # tube centre at walking height

    def wbox(a0, a1, s0, s1, z0, z1):
        xa, ya = wall[0] + d[0] * a0 + sx * s0, wall[1] + d[1] * a0 + sy * s0
        xb, yb = wall[0] + d[0] * a1 + sx * s1, wall[1] + d[1] * a1 + sy * s1
        return (int(min(xa, xb)), int(min(ya, yb)), z0, int(max(xa, xb)), int(max(ya, yb)), z1)
    drop = cz - low
    run = 2 * drop                                     # twice the old S-bend's run: a gentle, smooth S
    a1 = -TAIL                                         # the slope ends here, outside the wall
    a0 = a1 - run                                      # and starts here
    a_pod = a0 - LEAD                                  # pod front
    w, g = POD_W // 2, TUBE_H + 8 + 32
    pod = wbox(a_pod - POD_D, a_pod, -w, w, POD_Z, POD_Z + POD_H)
    void = wbox(a_pod, -TAIL + 32, -g, g, 0, cz + g)   # dark space the tube floats through
    throat = wbox(-TAIL, 0, -g, g, 0, low + g)         # low opening through the hall wall
    line = [(a_pod, cz)]
    for k in range(13):                                # cosine S: level at both ends, at most ~38 degrees
        u = k / 12
        line.append((a0 + run * u, cz - drop * (1 - math.cos(math.pi * u)) / 2))
    line.append((EXIT, low))
    return pod, (void, throat), cz, line, EXIT


def shell(b):
    x0, y0, z0, x1, y1, z1 = HALL
    pod, voids, cz, line, a_end = _geom(*ENTRIES[0][1:3])
    m = -line[0][0] + POD_D + 256                      # rock around the hall holds the pods and the voids
    b.solid(x0 - m, y0 - m, z0 - 256, x1 + m, y1 + 512, z1 + 256, "cyrock")
    b.air(*HALL, "cy_hall")
    for name, wall, d, team in ENTRIES:
        pod, voids, cz, line, a_end = _geom(wall, d)
        b.air(*pod, "cy_pod")
        for v in voids:
            b.air(*v, "cy_duct")


def _yaw(d):
    return {(1, 0): 0, (0, 1): 90, (-1, 0): 180, (0, -1): 270}[d]


def _v(a, b, k=1.0):
    return tuple(a[i] + b[i] * k for i in range(3))


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def _norm(a):
    ln = math.sqrt(sum(c * c for c in a))
    return tuple(c / ln for c in a)


def tube(m: VMF, pts, side, h=TUBE_H, t=8, mat=TUBE_MAT, edge=EDGE_MAT, e=5):
    """Square glass tube along a polyline (in a vertical plane), mitred at every joint, with a light strip along
    each of its four edges inside the glass. Walls and strips are func_detail hulls."""
    from vmflib import hull
    tex = Tex(mat, scale=0.25, align="face")
    etex = Tex(edge, scale=0.25, align="face")
    dirs = [_norm(_v(pts[i + 1], pts[i], -1)) for i in range(len(pts) - 1)]
    ups = [_cross(dd, side) for dd in dirs]
    mit = [ups[0]]                  # mitre vectors: offset planes of neighbouring segments meet on them
    for i in range(1, len(ups)):
        dp = 1 + sum(ups[i - 1][j] * ups[i][j] for j in range(3))
        mit.append(tuple((ups[i - 1][k] + ups[i][k]) / dp for k in range(3)))
    mit.append(ups[-1])
    walls, strips = [], []
    for i in range(len(dirs)):
        ends = [(pts[i], mit[i]), (pts[i + 1], mit[i + 1])]
        for sgn in (1, -1):         # top / bottom walls span the full width
            walls.append(hull([_v(_v(p, u, sgn * r), side, w) for p, u in ends for r in (h, h + t)
                               for w in (-(h + t), h + t)], tex))
            walls.append(hull([_v(_v(p, side, sgn * r), u, w) for p, u in ends for r in (h, h + t)
                               for w in (-h, h)], tex))
        for su in (1, -1):          # corner strips embedded in the glass: the inside stays smooth to fly through
            for ss in (1, -1):
                strips.append(hull([_v(_v(p, u, su * r), side, ss * q) for p, u in ends for r in (h + 1, h + 1 + e)
                                    for q in (h + 1, h + 1 + e)], etex))
    m.detail(walls)
    m.detail(strips)


def entry(m: VMF, name, wall, d, team):
    """Spawn pod outside the hall -> zero-g tube through a dark duct and the hall wall, sweeping down to the floor
    -> (team ICE) -> hall."""
    sx, sy = -d[1], d[0]

    def P(a, sd, z):
        return (wall[0] + d[0] * a + sx * sd, wall[1] + d[1] * a + sy * sd, z)

    def lbox(a0, a1, s0, s1, z0, z1, mats):
        (xa, ya, _), (xb, yb, _) = P(a0, s0, 0), P(a1, s1, 0)
        return box(min(xa, xb), min(ya, yb), z0, max(xa, xb), max(ya, yb), z1, mats)

    pod, voids, cz, line, a_end = _geom(wall, d)
    w, g, h = POD_W / 2, TUBE_H + 8 + 32, TUBE_H
    a_pod, low = line[0][0], FLOOR + TUBE_H
    # pod: cyber floor, camera at the pod centre looking into the tube mouth, soft light
    m.brush_ent("cyber_floor", lbox(a_pod - POD_D, a_pod, -w, w, POD_Z, POD_Z + 16,
                                    {"all": NODRAW, "top": "cyberspace/wall_squaresolid"}))
    m.ent("point_camera", P(a_pod - POD_D / 2, 0, cz), targetname=name, angles=f"0 {_yaw(d)} 0", FOV="90",
          renderTarget="camera1", UseScreenAspectRatio="0", fogEnable="0", fogColor="0 0 0", fogStart="2048",
          fogEnd="4096", spawnflags="0")
    kit.light(m, *P(a_pod - POD_D / 2, 0, 0)[:2], POD_Z + POD_H - 24, color=(90, 160, 255), bright=110, fifty=120,
              hundred=320)
    # frames close the gaps around the tube where it leaves the pod and where it passes the hall wall
    fr = Tex(FRAME_MAT)
    for a0_, a1_, zc, z0_, z1_ in ((a_pod, a_pod + 8, cz, POD_Z, POD_Z + POD_H), (0, 8, low, FLOOR, low + g)):
        m.detail([lbox(a0_, a1_, -g, -h - 8, z0_, z1_, fr), lbox(a0_, a1_, h + 8, g, z0_, z1_, fr),
                  lbox(a0_, a1_, -h - 8, h + 8, z0_, zc - h - 8, fr) if zc - h - 8 > z0_ else None,
                  lbox(a0_, a1_, -h - 8, h + 8, zc + h + 8, z1_, fr) if z1_ > zc + h + 8 else None])
    tube(m, [P(a, 0, z) for a, z in line], (sx, sy, 0))
    # gravity off entering the tube (angles point back at the pod), on again at the exit (point into the hall)
    m.brush_ent("cyber_gravity_volume", lbox(a_pod - 8, a_pod + 8, -h, h, cz - h, cz + h, TRIGGER),
                angles=f"0 {_yaw((-d[0], -d[1]))} 0")       # straddles the pod/tube boundary (verified)
    m.brush_ent("cyber_gravity_volume", lbox(a_end - 24, a_end - 8, -h, h, FLOOR, FLOOR + 2 * h, TRIGGER),
                angles=f"0 {_yaw(d)} 0")
    if team is not None:
        # static, unhackable team ICE across the exit: only this team's deckers get out
        face = {(1, 0): ("east", "west"), (-1, 0): ("east", "west"), (0, 1): ("north", "south")}[d]
        m.brush_ent("cyber_ice", lbox(a_end - 32, a_end, -h, h, FLOOR, FLOOR + 2 * h,
                                      {"all": NODRAW, face[0]: ICE_MAT, face[1]: ICE_MAT}),
                    targetname=f"ice_{name[9:]}_tube", team=str(team), spawnflags="1", WedgeDelay="5")
    # landing pad with two plasma beams just past the exit
    px, py, _ = P(a_end + 112, 0, 0)
    m.detail(ngon(px, py, 112, 8, FLOOR, FLOOR + 4, {"all": TRIM, "top": disc_tex(PAD_MAT, px, py, 112)}, rot=22.5))
    beam = "dys_nameless/redplasma2" if team == PUNKS else "dys_nameless/plasma2"
    for side in (-1, 1):
        bx, by, _ = P(a_end + 112, side * 96, 0)
        m.brush_ent("func_illusionary", box(bx - 8, by - 8, FLOOR + 4, bx + 8, by + 8, FLOOR + 324, beam),
                    rendermode="0", disableshadows="1")
    kit.light(m, px, py, FLOOR + 200, color=(255, 90, 60) if team == PUNKS else (90, 150, 255), bright=160,
              fifty=200, hundred=520)


class Local:
    """House frame: u runs along the door wall, v from the back wall (0) to the door wall (depth)."""

    def __init__(self, cx, cy, depth, facing):
        self.cx, self.cy, self.d, self.f = cx, cy, depth, facing

    def xy(self, u, v):
        cx, cy, d = self.cx, self.cy, self.d
        return {"+y": (cx + u, cy - d / 2 + v), "-y": (cx - u, cy + d / 2 - v),
                "+x": (cx - d / 2 + v, cy - u), "-x": (cx + d / 2 - v, cy + u)}[self.f]

    def box(self, u0, v0, z0, u1, v1, z1, mats):
        (x0, y0), (x1, y1) = self.xy(u0, v0), self.xy(u1, v1)
        if isinstance(mats, dict):
            keys = dict(zip(("vpos", "vneg", "upos", "uneg"), _FACES[self.f]))
            mats = {keys.get(k, k): t for k, t in mats.items()}
        return box(x0, y0, z0, x1, y1, z1, mats)


def disc_tex(mat, cx, cy, r, tw=512):
    """Top/bottom texture fitted to the square (cx +- r, cy +- r) so round textures sit centred."""
    sc = 2 * r / tw
    return Tex(mat, scale=sc, uoff=-(cx - r) / sc, voff=(cy + r) / sc)


def icon_cube(m: VMF, cx, cy, z0, icon, s=48):
    """Floating holographic cube with the node icon on its four sides."""
    mats = {"top": NODRAW, "bottom": NODRAW}
    for f, (fx, fy, _) in FACING.items():
        r = (-fy, fx)                                   # viewer's right when facing this side
        left = (cx + fx * s - r[0] * s, cy + fy * s - r[1] * s)
        mats[FACE_KEY[f]] = fit_tex(icon, f, left, z0 + 2 * s, 2 * s, 2 * s)
    return m.brush_ent("func_illusionary", box(cx - s, cy - s, z0, cx + s, cy + s, z0 + 2 * s, mats),
                       rendermode="0", disableshadows="1")


def house(m: VMF, cx, cy, z, facing, ext, icon, ice_name, scr_name, panel_name, protection="1",
          w=256, d=320, h=192, side_sign=None, light=(120, 150, 255)):
    """Terminal house: the ICE fills the doorway, the screen hangs on the back wall facing the door."""
    L = Local(cx, cy, d, facing)
    t, tf, dw, dh = 16, 32, 128, 160
    W = w / 2
    e, inner, trim = Tex(ext), Tex(DARK), Tex(TRIM)
    m.detail([
        L.box(-W, 0, z, W, t, z + h, {"all": e, "vpos": inner}),                           # back wall
        L.box(-W, t, z, -W + t, d - tf, z + h, {"all": e, "upos": inner}),                  # side walls
        L.box(W - t, t, z, W, d - tf, z + h, {"all": e, "uneg": inner}),
        L.box(-W, d - tf, z, -dw / 2, d, z + h, {"all": e, "vneg": inner, "upos": trim}),  # door wall
        L.box(dw / 2, d - tf, z, W, d, z + h, {"all": e, "vneg": inner, "uneg": trim}),
        L.box(-dw / 2, d - tf, z + dh, dw / 2, d, z + h, {"all": e, "vneg": inner, "bottom": trim}),
        L.box(-W, 0, z + h, W, d, z + h + 16, {"all": e, "bottom": inner}),                # roof
        # white door frame proud of the facade
        L.box(-dw / 2 - 8, d, z, -dw / 2, d + 2, z + dh + 8, trim),
        L.box(dw / 2, d, z, dw / 2 + 8, d + 2, z + dh + 8, trim),
        L.box(-dw / 2, d, z + dh, dw / 2, d + 2, z + dh + 8, trim),
    ])
    # the ICE is the door
    m.brush_ent("cyber_ice", L.box(-dw / 2, d - tf, z, dw / 2, d, z + dh,
                                   {"all": NODRAW, "vpos": ICE_MAT, "vneg": ICE_MAT}),
                targetname=ice_name, team=str(CORPS), spawnflags="9", WedgeDelay="5")
    # screen on the back wall, recessed in a frame
    sx, sy = L.xy(0, t)
    zc = z + 80
    s = screen(m, "dys_cyberscreen", scr_name, panel_name, sx, sy, zc, facing, w=64, h=64,
               team=str(CORPS), protection=protection, icename=ice_name)
    fm = {"all": DARK, "vpos": "termitex/cysp_scroller02"}
    m.detail([L.box(-42, t, zc - 42, 42, t + 5, zc - 32, fm), L.box(-42, t, zc + 32, 42, t + 5, zc + 42, fm),
              L.box(-42, t, zc - 32, -32, t + 5, zc + 32, fm), L.box(32, t, zc - 32, 42, t + 5, zc + 32, fm)])
    kit.light(m, *L.xy(0, d / 2), z + h - 32, color=light, bright=140, fifty=160, hundred=420)
    if icon:
        icon_cube(m, *L.xy(0, d / 2), z + h + 80, icon)
    if side_sign:
        for u, fac in ((-W, "uneg"), (W, "upos")):
            px, py = L.xy(u, d / 2)
            f = _FACES[facing][("vpos", "vneg", "upos", "uneg").index(fac)]
            face = {"east": "+x", "west": "-x", "north": "+y", "south": "-y"}[f]
            panel(m, px, py, z + 24, z + 24 + 144, face, 144, side_sign, depth=1)
    return s


def add(b):
    m: VMF = b.m
    x0, y0, z0, x1, y1, z1 = HALL

    # ---- walkable surfaces. Only the flat hall floor is cyber_floor: touching any cyber_floor face
    # re-orients the decker's gravity to it (verified in-game), so raised parts are plain func_detail.
    m.brush_ent("cyber_floor", box(x0, y0, 0, x1, y1, FLOOR, {"all": NODRAW, "top": FLOOR_MAT}))
    tx0, ty0, tx1, ty1, tz = TERRACE
    red = Tex("cyberspace/cube_red", scale=0.5)
    m.detail([
        box(tx0, ty0, FLOOR, tx1, ty1, tz, {"all": red, "top": CORE_FLOOR}),
        wedge(tx0 - 416, ty0 + 32, FLOOR, tx0, ty0 + 224, tz, "+x", {"all": red, "top": CORE_FLOOR}),
        wedge(tx1, ty0 + 32, FLOOR, tx1 + 416, ty0 + 224, tz, "-x", {"all": red, "top": CORE_FLOOR}),
    ])
    for name, wall, d, team in ENTRIES:
        entry(m, name, wall, d, team)
    blue = Tex("cyberspace/cube_blue")
    for (cx, cy, hx, hy) in COVER:
        m.detail(box(cx - hx, cy - hy, FLOOR, cx + hx, cy + hy, FLOOR + 80, {"all": blue, "top": FLOOR_MAT}))

    # ---- terminal houses (the ICE is the door)
    # (no gate lock in cyberspace: the security gate can only be breached in meatspace)
    # Objective turret terminals: disable/enable only (no capture). Their buttons go through relays that the
    # objective's capture disables (gameplay.py), so the terminals go dead once their objective has fallen.
    for x, y, fac, key, tur, panel_name in ((-960, 5760, "-y", "gate", "tur_plaza", "bi_cyber_gateturrets"),
                                           (-960, 3968, "+y", "lobby", "tur_lobby", "bi_cyber_lobbyturrets")):
        s = house(m, x, y, FLOOR, fac, "cyberspace/cube_red", "vaccinert/dys_turretnode",
                  f"ice_{key}turrets", f"cy_{key}turret_screen", panel_name, light=(255, 90, 80))
        s.out("Button1", f"cy_{key}turrets_off", "Trigger")
        s.out("Button2", f"cy_{key}turrets_on", "Trigger")
        relay(m, f"cy_{key}turrets_off", x, y, FLOOR + 40).out("OnTrigger", tur, "Disable")
        relay(m, f"cy_{key}turrets_on", x, y, FLOOR + 60).out("OnTrigger", tur, "Enable")
    s = house(m, 960, 3968, FLOOR, "+y", "cyberspace/cube_green", "termitex/icon_door",
              "ice_maint", "cy_maint_screen", "bi_cyber_maint", light=(90, 255, 140))
    s.out("Button1", "maint_open", "Trigger")
    s.out("Button2", "maint_door", "Close")
    s = house(m, 960, 5760, FLOOR, "-y", "cyberspace/cube_red", "vaccinert/dys_turretnode",
              "ice_vault", "cy_vault_screen", "bi_cyber_vault", side_sign="cyberspace/infocoredefense",
              light=(255, 90, 80))
    s.out("Button1", "tur_vault", "Enable")
    s.out("Button2", "tur_vault", "Disable")
    s.out("Button3", "tur_vault", "SetTeamTouched")
    # the core house: black monolith on the red terrace, encrypted ICE (the BLACK ICE warning is its icon)
    s = house(m, 0, 5536, tz, "-y", DARK, None, "ice_core", "cy_core_screen", "bi_cyber_core",
              protection="2", w=320, d=384, h=224, side_sign="cyberspace/infocoreshield", light=(255, 70, 70))
    s.out("Button1", "cy_core_fp", "TestActivator")
    s.out("Button2", "cy_core_fc", "TestActivator")
    f = kit.filter_team(m, "cy_core_fp", 2)
    f.kv["origin"] = "0 5000 600"
    f.out("OnPass", "shield_down", "Trigger")
    f = kit.filter_team(m, "cy_core_fc", CORPS)
    f.kv["origin"] = "0 5000 640"
    f.out("OnPass", "shield_up", "Trigger")
    for px in (-320, 320):                    # red plasma pylons flanking the core approach (wide decker gaps)
        m.detail(box(px - 24, 5240, tz, px + 24, 5288, tz + 448, "dys_nameless/redplasma2"))
    kit.light(m, 0, 5200, tz + 220, color=(255, 60, 60), bright=220, fifty=320, hundred=900)
    panel(m, 0, y1 - 1, 620, 876, "-y", 512, "blackice/ice_warning", depth=1, cls="func_illusionary")


    # ---- data pillars: black columns with glowing blue edges
    edge = Tex("twincannon/twin_cyberblue")
    for (px, py) in PILLARS:
        m.detail(box(px - 32, py - 32, FLOOR, px + 32, py + 32, z1, DARK))
        m.detail([box(px + sx * 32 - 4, py + sy * 32 - 4, FLOOR, px + sx * 32 + 4, py + sy * 32 + 4, z1, edge)
                  for sx in (-1, 1) for sy in (-1, 1)])

    # ---- bitstream columns on the hall walls
    for x in (-1536, -768, 768, 1536):
        panel(m, x, y0 + 1, 64, 704, "+y", 96, "cyspfinal/bitstream1a", depth=1, cls="func_illusionary")
    for x in (-1536, -1024, 1024, 1536):
        panel(m, x, y1 - 1, 64, 704, "-y", 96, "cyspfinal/bitstream1a", depth=1, cls="func_illusionary")
    for y in (4224, 5504):
        panel(m, x0 + 1, y, 64, 704, "+x", 96, "cyspfinal/bitstream1a", depth=1, cls="func_illusionary")
        panel(m, x1 - 1, y, 64, 704, "-x", 96, "cyspfinal/bitstream1a", depth=1, cls="func_illusionary")

    # ---- light, cubemaps, soundscapes
    for lx in (-1152, 0, 1152):
        for ly in (4224, 5504):
            kit.light(m, lx, ly, 560, color=(150, 130, 255), bright=240, fifty=900, hundred=2200)
    for (cx, cy) in ((-1024, 4864), (0, 4480), (1024, 4864), (0, 5100)):
        m.ent("env_cubemap", (cx, cy, 480), cubemapsize="0")
    for (sx, sy, sz), ss, rad in [((-1150, 4864, 200), "CyberSpace.Node1", 900), ((0, 4400, 200), "CyberSpace.Node2", 900),
                                  ((1150, 4864, 200), "CyberSpace.Node1", 900), ((0, 5536, 400), "CyberSpace.Node3", 800),
                                  ((-960, 5760, 200), "CyberSpace.Node2", 600), ((960, 5760, 200), "CyberSpace.Node2", 600)]:
        m.ent("env_soundscape", (sx, sy, sz), radius=str(rad), soundscape=ss, StartDisabled="0")
