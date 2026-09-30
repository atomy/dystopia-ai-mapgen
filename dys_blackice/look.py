"""Surface look for dys_blackice: per-zone material recipes + the CSG resolver.

Air styles describe the room seen from inside (floor/ceiling/wall bands, bands are
relative to the room's floor). Solid styles with facades describe how a building
looks from outdoor air (bands in absolute z).
"""
from __future__ import annotations

import functools

import assets
from vmflib import Tex, SKYBOX, NODRAW

SCALE = 0.25


@functools.lru_cache(maxsize=None)
def _texh(mat):
    sz = assets.texture_size(mat)
    return sz if sz else (512, 512)


def T(mat, scale=SCALE, lm=16, rot=0):
    return Tex(mat, scale=scale, lightmap=lm, rotation=rot)


def band(mat, scale=SCALE, lm=16):
    """Wall texture whose bottom edge is aligned to the band's bottom z."""
    def make(zb):
        w, h = _texh(mat)
        return Tex(mat, scale=scale, lightmap=lm, voff=(zb / scale) % h)
    return make


def flat(mat, scale=SCALE, lm=16):
    def make(zb):
        return Tex(mat, scale=scale, lightmap=lm)
    return make


# ----------------------------------------------------------------------------- interiors
# walls: list of (z_rel_lo, z_rel_hi or None, maker)
AIR = {
    # --- metro (Punk HQ)
    "metro": dict(floor=T("tile/tilefloor009a"), ceil=T("concrete/concreteceiling004a"),
                  walls=[(0, 128, band("tile/tilewall009d")), (128, 256, band("tile/tilewall006b")),
                         (256, None, band("concrete/concretewall008a"))]),
    "metro_tracks": dict(floor=T("nature/gravelfloor002b", rot=90), ceil=T("concrete/concreteceiling004a"),
                         walls=[(0, 192, band("dys_fortress/tunnel_wall", scale=0.25)),
                                (192, None, band("concrete/concretewall008a"))]),
    "metro_stair": dict(floor=T("termireal1/t_trashfloor"), ceil=T("concrete/concreteceiling004a"),
                        walls=[(0, None, band("dys_nameless/concrete_004_blue"))]),
    "maint": dict(floor=T("metal/metalfloor_001e"), ceil=T("concrete/concreteceiling004a"),
                  walls=[(0, None, band("dys_fortress/tunnel_wall"))]),
    "metro_tunnel": dict(floor=T("nature/gravelfloor002b", rot=90), ceil=T("concrete/concreteceiling004a"),
                         walls=[(0, None, band("dys_fortress/tunnel_wall", scale=0.25))]),
    # recessed shop-door niches in the market facades
    "niche": dict(floor=T("urban/sidewalk"), ceil=T("metal/metalwall003a"),
                  walls=[(0, None, flat("metal/metalwall003a"))]),
    # --- market interiors
    "shop": dict(floor=T("tile/tilefloor020a"), ceil=T("props/acousticceiling002a"),
                 walls=[(0, 96, band("urban/old_cement4")), (96, None, band("brick/brickwall017b"))]),
    "arcade": dict(floor=T("dys_cybernetic/floor_black_glossy"), ceil=T("metal/metalceiling005a"),
                   walls=[(0, None, band("vaccinert/dys_vaccorpwall3"))]),
    # --- tower
    "guard": dict(floor=T("vaccinert/dys_vaccorpfloor1"), ceil=T("vaccinert/dys_vacclean1"),
                  walls=[(0, 128, band("vaccinert/dys_vacwall1")), (128, None, band("vaccinert/dys_vaccorpwall3"))]),
    "lobby": dict(floor=T("tile/tilefloor020a", lm=16), ceil=T("dys_cybernetic/metal_dark_indoors"),
                  walls=[(0, 128, band("vaccinert/dys_vacwall1")), (128, 192, band("vaccinert/dys_vaccorpwall1")),
                         (192, 320, band("vaccinert/dys_vacwall1")), (320, None, band("vaccinert/dys_vaccorpwall3"))]),
    "hub": dict(floor=T("dys_cybernetic/floor_black_glossy"), ceil=T("dys_cybernetic/metal_dark_indoors"),
                walls=[(0, None, band("coast/panel01", scale=0.25))]),
    "corpspawn": dict(floor=T("vaccinert/dys_vaccorpfloor3"), ceil=T("vaccinert/dys_vacclean1"),
                      walls=[(0, 128, band("vaccinert/dys_vacwall1")), (128, None, band("vaccinert/dys_vaccorpwall3"))]),
    "service": dict(floor=T("metal/metalfloor_001e"), ceil=T("metal/metalceiling005a"),
                    walls=[(0, None, band("dys_cybernetic/wall_interior_008"))]),
    "server": dict(floor=T("metal/metalfloor_001e"), ceil=T("dys_cybernetic/metal_dark_indoors"),
                   walls=[(0, 128, band("metal/metalwall002b")), (128, None, band("metal/metalwall002a"))]),
    "vault": dict(floor=T("metal/metalfloor_001e"), ceil=T("dys_cybernetic/metal_dark_indoors"),
                  walls=[(0, 256, band("metal/metalcombine001")), (256, None, band("metal/metalwall002a"))]),
    # --- outdoor (walls come from the building facades)
    "street": dict(floor=T("twincannon/road_asphalt2", lm=32), outdoor=True),
    "alley": dict(floor=T("urban/dirty_road02", scale=0.25, lm=32), outdoor=True),
    "plaza": dict(floor=T("dys_nameless/concrete_floor_001", lm=32), outdoor=True),
    "court": dict(floor=T("stone/stonefloor011a", lm=32), outdoor=True),
    "roof": dict(floor=T("dys_fortress/gravel", lm=64), outdoor=True),
    # --- cyberspace hall (opaque shell; glowing layers are entities)
    "cy_hall": dict(floor=T("cyberspace/wall_squaresolid"), ceil=T("cyberspace/t_cyspwall1_black", scale=0.5),
                    walls=[(0, None, flat("cyberspace/cube_purple", scale=0.5))]),
}

# ----------------------------------------------------------------------------- facades
# solid style -> bands in absolute z (lo, hi, maker); faces toward outdoor air use these.
FACADES = {
    "bld_brick": [(0, 224, band("brick/brickwall017b")), (224, None, band("brick/brickwall045c"))],
    "bld_cement": [(0, 224, band("urban/old_cement4")), (224, None, band("buildings/gen16", scale=0.5))],
    "bld_rust": [(0, 224, band("metal/metaldoor032a")), (224, None, band("buildings/gen01", scale=0.5))],
    "bld_grid": [(0, 224, band("urban/old_cement4")), (224, None, band("buildings/gen18", scale=0.5))],
    "bld_dark": [(0, None, band("concrete/concretewall008a"))],
    "tower": [(0, 32, band("vaccinert/dys_vactrim2")), (32, 480, band("vaccinert/dys_vacextwall4")),
              (480, None, band("blackice/lit_windows", scale=1.0))],
    "guardpost": [(0, None, band("vaccinert/dys_vacextwall3"))],
    "plazawall": [(0, None, band("concrete/concretewall060c"))],
    "rock": [(0, None, band("concrete/concretewall008a"))],
}
ROOFS = {"bld_brick": "dys_fortress/gravel", "bld_cement": "dys_fortress/gravel", "bld_rust": "dys_fortress/gravel",
         "bld_grid": "dys_fortress/gravel", "guardpost": "metal/metalfloor_001e", "tower": "metal/metalfloor_001e"}
SLAB_TOP = {"lobby": T("vaccinert/dys_vaccorpfloor3"), "vault": T("metal/metalfloor_001e")}
SLAB_SIDE = T("vaccinert/dys_vactrim2")
SLAB_UNDER = T("vaccinert/dys_vacclean1")


def _bands_pick(bands, z0, z1, base):
    """bands relative to `base`; choose the band containing the piece mid-height."""
    mid = (z0 + z1) / 2 - base
    for lo, hi, maker in bands:
        if mid >= lo and (hi is None or mid < hi):
            return maker(base + lo)
    lo, hi, maker = bands[-1]
    return maker(base + lo)


def resolver(solid, air, d, bx, zr):
    if air.style == "skyroom":
        return Tex(SKYBOX)
    st = AIR.get(air.style)
    if st is None:
        return None
    outdoor = st.get("outdoor", False)
    if solid.style == "sky":
        return SKYBOX if outdoor else None
    if d == "top":
        if outdoor and solid.style in ROOFS:
            return T(ROOFS[solid.style], lm=64)
        if solid.style == "slab":
            return SLAB_TOP.get(air.style, st["floor"])
        return st["floor"]
    if d == "bottom":
        if solid.style == "slab":
            return SLAB_UNDER
        return st.get("ceil", T(NODRAW))
    # vertical faces
    if solid.style == "slab":
        return SLAB_SIDE
    if outdoor:
        fac = FACADES.get(solid.style) or FACADES["rock"]
        return _bands_pick(fac, zr[0], zr[1], 0)
    return _bands_pick(st["walls"], zr[0], zr[1], air.box.z0)


def zcuts(op):
    """z levels at which vertical faces must be split for texture bands."""
    if op is None:
        return ()
    if op.kind == "air":
        st = AIR.get(op.style)
        if not st or "walls" not in st:
            return ()
        return [op.box.z0 + lo for lo, hi, mk in st["walls"] if lo] + \
               [op.box.z0 + hi for lo, hi, mk in st["walls"] if hi]
    fac = FACADES.get(op.style)
    if fac:
        return [lo for lo, hi, mk in fac if lo] + [hi for lo, hi, mk in fac if hi]
    return ()


def lightmap_scale(op, side):
    return None
