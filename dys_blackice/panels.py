"""VGUI screen panels for dys_screen / dys_cyberscreen.

Each panel: name, type ('dys_screen' | 'dys_cyberscreen'), title, buttons [(label, command)].
Labels may be localisation tokens (#dystopia_R_...) or literal text.
Writes maps/<map>_screens.txt and scripts/screens/<panel>.res into a staging dir
that gets packed into the BSP.
"""
from __future__ import annotations

from pathlib import Path

BUTTON_IMAGES = """
		"enabledImage"
		{{
			"material"	"vgui/screens/{b}_enabled"
			"color" "255 255 255 255"
		}}
		"mouseOverImage"
		{{
			"material"	"vgui/screens/{b}_hover"
			"color" "255 255 255 255"
		}}
		"pressedImage"
		{{
			"material"	"vgui/screens/{b}_pushed"
			"color" "255 255 255 255"
		}}
		"disabledImage"
		{{
			"material"	"vgui/screens/{b}_disabled"
			"color" "255 255 255 255"
		}}"""


def _control(kind, name, x, y, w, h, extra=""):
    return (f'\t"{name}"\n\t{{\n\t\t"ControlName"\t\t"{kind}"\n\t\t"fieldName"\t\t"{name}"\n'
            f'\t\t"xpos"\t\t"{x}"\n\t\t"ypos"\t\t"{y}"\n\t\t"wide"\t\t"{w}"\n\t\t"tall"\t\t"{h}"\n'
            f'\t\t"autoResize"\t\t"0"\n\t\t"pinCorner"\t\t"0"\n\t\t"visible"\t\t"1"\n\t\t"enabled"\t\t"1"\n'
            f'{extra}\t}}\n')


def panel_res(name, title, buttons, background="vgui/screens/vgui_bg", cyber=False):
    out = [f'"{name}.res"\n{{\n']
    out.append(_control("MaterialImage", "Background", 0, 0, 256, 256,
                        f'\t\t"zpos"\t\t"-2"\n\t\t"material"\t\t"{background}"\n'))
    out.append(_control("Label", "TitleLabel", 16, 12, 224, 24,
                        f'\t\t"labelText"\t\t"{title}"\n\t\t"textAlignment"\t\t"center"\n\t\t"font"\t\t"SpaceOneSmall"\n'
                        f'\t\t"wrap"\t\t"0"\n\t\t"dulltext"\t\t"0"\n\t\t"brighttext"\t\t"1"\n'))
    n = len(buttons)
    top, bottom = 48, 244
    gap = 8
    bh = min(64, (bottom - top - gap * (n - 1)) // max(1, n))
    total = bh * n + gap * (n - 1)
    y = top + ((bottom - top) - total) // 2
    img = "vgui_button2" if cyber else "vgui_button"
    for i, (label, command) in enumerate(buttons):
        extra = (f'\t\t"tabPosition"\t\t"{i + 1}"\n\t\t"labelText"\t\t"{label}"\n\t\t"textAlignment"\t\t"center"\n'
                 f'\t\t"command"\t\t"{command}"\n\t\t"paintborder"\t\t"0"\n\t\t"font"\t\t"SpaceOneSmall"\n'
                 f'\t\t"Default"\t\t"0"\n' + BUTTON_IMAGES.format(b=img) + "\n")
        out.append(_control("MaterialButton", f"Button{i + 1}", 24, y, 208, bh, extra))
        y += bh + gap
    out.append("}\n")
    return "".join(out)


def write_panels(map_name, panels, stage: Path):
    """panels: list of dicts {name, type, title, buttons, background?}."""
    (stage / "maps").mkdir(parents=True, exist_ok=True)
    (stage / "scripts" / "screens").mkdir(parents=True, exist_ok=True)
    reg = ['"VGUI_Screens"\n{\n']
    files = []
    for p in panels:
        reg.append(f'\t"{p["name"]}"\n\t{{\n\t\t"type"\t\t"{p["type"]}"\n\t}}\n')
        res = panel_res(p["name"], p["title"], p["buttons"], p.get("background", "vgui/screens/vgui_bg"),
                        cyber=p["type"] == "dys_cyberscreen")
        f = stage / "scripts" / "screens" / f"{p['name']}.res"
        f.write_text(res, encoding="utf-8")
        files.append(f)
    reg.append("}\n")
    f = stage / "maps" / f"{map_name}_screens.txt"
    f.write_text("".join(reg), encoding="utf-8")
    files.append(f)
    return files
