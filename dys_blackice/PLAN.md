# dys_blackice — build plan

Goal: a release-ready Dystopia objective map (Punks attack, Corps defend) that ships as one
self-contained BSP, built from a fresh purpose-made generator (not dystopia_citygen).

## Concept
Night, rain, neon. Punks raid Kuroda Corp's Arcology Block 7 to crash BLACK ICE, the
corp's lethal AI firewall, whose physical core sits in a datavault under the tower.

Flow (meatspace):
1. Punk HQ: abandoned metro station (underground). Punk jackpoint lives here.
2. Neon market street: shopfronts, stalls, steam, cables, fire-escape flank.
3. Kuroda Plaza: open approach, cover, skybridge, guard posts, turrets.
   **Obj 1: breach the security gate.** Done either from the guard-post screen (meatspace)
   or from the Gate Control terminal in cyberspace (password ICE). Unlocks a forward spawn.
4. Tower lobby / atrium: two floors, mezzanine, stairs, reception. Corps start spawn is here.
   **Obj 2: seize the security hub** (decker crack, trigger_crackable). Spawns shift.
5. Server hall: cold-blue rack rows, a catwalk, and a maintenance-tunnel flank
   (the flank is opened from cyberspace).
6. Core vault: tall chamber with the BLACK ICE core behind a shield.
   **Obj 3 (final): crash the core.** Drop the shield in cyberspace (encrypted ICE), then shoot
   the core (a func_breakable that feeds the objective's health bar).

Cyberspace: a compact, separate region (entry node, gate node, security node, core node).
It uses tubes with gravity volumes, jump and speed pads, energy crystals, and cyber_ice-guarded
dys_cyberscreens that drive meatspace doors, turrets and objectives.

## Dystopia systems (learned from official VMF sources)
- dys_spawn (team, spawnid, spawnname) + dys_spawn_point; captured with SetPunks/SetCorps.
- dys_objective (Index, team=3 owner, spawnflags 8 = final, objtarget, SetPunks/SetHealth).
- dys_jackpoint (thin brush) -> point_camera in cyberspace = decker entry.
- dys_cyberscreen (panelname, icename, protection 1=password / 2=encryption) + cyber_ice (spawnflags 9).
- dys_screen / dys_cyberscreen panels: maps/<map>_screens.txt + scripts/screens/*.res.
- filter_activator_team gates, dys_forcefield spawn doors, npc_turret_ceiling, dys_ammodisp.
- info_camera_start / punkswin / corpswin, dys_location, dys_helper, dys_onscreeninfo.
- Release extras packed in the BSP: _screens.txt, screen .res files, resource/overviews,
  materials/overviews, resource/mappaths, resource/helpers, _music.txt, soundscapes.

## Toolchain (all local)
- Generator: Python 3.12 + Pillow, in this folder (dystopia_citygen/dys_blackice/).
  vmf.py (writer) · geo.py (brush kit: rooms with openings, stairs, trims, pillars, facades)
  · assets.py (verified materials and models, with sizes read from VTF/MDL headers) · map_*.py (the design)
- Compile: Dystopia's own bin/win32 vbsp / vvis / vrad (-both -final for release).
- Pack: bspzip (SDK 2013 MP). Cubemaps: buildcubemaps run in-game (LDR + HDR).
- QA: static validator (I/O targets, materials and models exist, no dev textures, leak check),
  automated in-game screenshot runs (windowed Dystopia, setpos/setang + jpeg),
  logic tests via ent_fire + developer I/O logging in console.log.

## Status (2026-09-28)
- [x] 1 Toolchain: vmflib, box-CSG shell (leak-proof), compile, bspzip pack, in-game automation
      (GameSession/-hijack via cfg exec, screenshot tours, movement tests, cubemap builds)
- [x] 2 Palette: 98 contact sheets catalogued by 3 agents (build/palette_notes_*.md)
- [x] 3 Grey-box + full objective chain (verified in-game: obj1 -> obj2 -> final, Punks win)
- [x] 4 Art pass: metro, market street, alleys, plaza, tower facade + 3D skyline, lobby, hub,
      spawns, server hall, vault; custom Kuroda/ICE textures; rain, fog, lighting
- [x] 5 Cyberspace: jack-in verified (brush-entity origin fix), nodes, ICE-guarded terminals
- [x] 6 Movement QA: every stair/route walked by an automated player
- [x] 7 Release extras: radar overview (3 layers), mappaths, soundscapes (auto-load verified),
      music, loading screen - all packed in the BSP
- [x] 8 Final: cubemaps LDR+HDR, clean-client test (pak-only), logic regression (6/6 pass),
      beauty shots, loading screen, release zip (build/release/)

## Rebuild
    python blackice.py --compile --final      # generate + validate + compile + pack
    python -c "import tools; tools.build_cubemaps('dys_blackice')"
    python release.py qa | logic | shots | loading | zip

## Phases (each ends with a compile + in-game check)
1. Toolchain + smoke test (tiny sealed room with spawns loads in game, screenshot works).
2. Asset palette: VTF previews and contact sheets, then choose materials, props, sky, sounds.
3. Grey-box of the full layout with all gameplay entities and logic; verify flow and scale.
4. Art pass: texturing, trims, props, lighting, neon, rain, fog, soundscapes, music.
5. Cyberspace build and hookup.
6. Optimisation: func_detail, nodraw, hints/areaportals, clips, perf check.
7. Release polish: overview, loading screen, mappaths, helpers, locations, text.
8. Final compile, cubemaps, pack, QA pass, release zip + README.
