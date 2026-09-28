# Session memory: dys_blackice (2026-09-28)

Notes from the Claude Code session that built **dys_blackice**. They are written for future sessions and
contributors, so they cover what was verified, what went wrong, and why things are the way they are.
Paths are relative to the Dystopia install (`<Dystopia>/dystopia/...`).

## Brief
- **Prompt:** "I want you to build a ready to release dystopia game map, make a plan for yourself how you would
  conquer this challenge."
- **Model:** Claude Opus 5.5 in Claude Code.
- **Direction from the user during the session:** take a fresh approach and don't rely on dystopia_citygen,
  whose output was too basic to be playable.

## Outcome
- `maps/dys_blackice.bsp` v1.0, about 23 MB, with everything packed inside. It is a rainy neon-city objective map:
  metro, street market, plaza, tower lobby, server hall and core vault, plus a 5-node cyberspace.
- Three objectives: breach the gate, crack the security hub, crash the BLACK ICE core.
- The generator in this folder is the single source of truth. See [README.md](README.md) to build it and
  [PLAN.md](PLAN.md) for the design and status.

## How the session went
1. **Survey.** Read the FGD, the official map sources (`examples/*.vmf`) and the texture and entity catalogs.
   The FGD is partly stale; see the facts below.
2. **Toolchain.** Built a VMF writer, a box-CSG shell builder, compile and pack steps, and in-game automation.
   A smoke-test map was compiled and screenshotted in-game.
3. **Palette.** 98 texture contact sheets were rendered from VTFs. Three parallel agents catalogued them into
   notes (kept under `build/`, which is not tracked).
4. **Grey-box and gameplay.** The objective chain was verified end to end in-game before any art work began.
5. **Art passes.** Street and plaza, tower facade and 3D skyline, then interiors, cyberspace, lighting and weather.
6. **QA.**
   - Automated walk tests on every stair and route.
   - An objective-logic regression.
   - A clean-client test with loose files hidden, so content loads only from the pak.
   - Visual checks in both HDR and LDR.
7. **Release.** Radar overview, mappaths, soundscapes, music, loading screen, LDR and HDR cubemaps, and a zip.

## Verified Dystopia facts
- **Brush-entity origin.** Brush entities need an `origin` keyvalue set to the bounds centre, as Hammer writes
  it. Without it, `dys_jackpoint` reports "too far away" because range is measured from (0,0,0).
- **Stale FGD entries.** `dys_location` and `dys_steam` are listed in `dystopia.fgd` but do not exist in the
  current game. Use `env_steam`; there is no location entity.
- **Forcefields start enabled.** `dys_forcefield` has no working start-disabled key. Disable it from a
  `logic_auto` `OnMapSpawn`.
- **Jack-in points.**
  - Layout: a wall-mounted `prop_jackin_*` model with a 30x30x1 `dys_jackpoint` brush 5.5u in front of it.
    The front face uses `dys_monitor1a`. The jackpoint's `target` is a `point_camera` placed in cyberspace.
  - The player has to stand right at the terminal to use it.
- **Sealing.** Translucent or `$additive` materials on world brushes do not seal and cause leaks. Only
  `cyberspace/wall_squaresolid` works as a cyber floor that seals (opaque, surfaceprop `cybergravity`).
- **Final objective.** `dys_objective` with spawnflags 8 is the final objective. `SetPunks` on it ends the round.
  `dys_spawn` ownership flips with `SetPunks` and `SetCorps`, and spawn IDs increase from the Punk side.
- **Packing.** Custom maps ship these inside the BSP pak: `maps/<map>_screens.txt`, `scripts/screens/*.res`,
  `resource/overviews`, `resource/mappaths`, `resource/helpers`, `maps/<map>_music.txt` and
  `scripts/soundscapes_<map>.txt`. The soundscape file loads automatically from the pak (verified).
- **Static props.**
  - vbsp deletes a `prop_static` whose model lacks the static-prop flag.
  - It also deletes one whose model has a `prop_data` block without `allowstatic`. `kit.prop` falls back to
    `prop_dynamic_override` for these.
- **Lighting.** Interiors look right with quadratic lights (brightness in the hundreds). Short
  `_fifty/_zero_percent_distance` falloffs left rooms dark. Tile materials with `$envmap` look washed out until
  cubemaps are built, so judge the lighting only after `buildcubemaps`.

## In-game automation notes (tools.py)
- **Launch.** Start `dystopia.exe` with an absolute `-game` path. Its video settings then live in a separate
  profile from normal Steam launches.
- **Sending commands.**
  - Send commands into the running game with `dystopia.exe -hijack +exec <cfg>`.
  - The hijack command line swallows negative numbers, so always write commands to a cfg and exec it.
  - `wait` does nothing for hijacked commands, so pace them from Python.
- **Spectator and player setup.**
  - A free-roaming spectator needs `spec_mode 6` sent again before each `setpos`.
  - `getpos` and `setpos` use eye position, about 57u above the feet.
  - Test recipe: `mp_instantspawn 1` (needs cheats), `jointeam 2`, `setclass 1`, `joinimplant 2` (cyberdeck),
    `kill`, then stand at the terminal and `+use`. Success shows as `execing cyberspace.cfg` in the console log.
- **Cubemaps.** `buildcubemaps` is finished when the engine rewrites the BSP; watch its modification time.
  Build LDR and HDR by switching `mat_hdr_level`, then restore it.
- **Never change archived cvars in automated runs.** In Dystopia `r_drawviewmodel` is archived, unlike stock
  Source. The game saves `config.cfg` on quit and syncs it to Steam Cloud, so restoring the local file is not
  enough; the tester lost their gun viewmodel this way. `GameSession.close()` now sets the viewmodel back on.

## Design decisions
- **Box-CSG shell.** The world is painted as ordered solid and air boxes, so sealing is guaranteed by
  construction and a leak check runs before vbsp. All detail is `func_detail` or brush entities.
- **No objective skipping.** The cyberspace-controlled maintenance door only works after the hub has fallen.
  Without that, Punks could skip objective 2. The Datavault spawn starts disabled for the same reason.
- **Two ways through each objective.**
  - Gate: a meatspace override or a cyberspace hack.
  - Core shield: a temporary drop from cyberspace or a permanent drop by destroying the emitters.
- **Custom art is generated.** The Kuroda logos, window facade, BLACK ICE warning, overview and loading screen
  are all made by scripts (Pillow and vtex), so they can be rebuilt from the repo alone.

## Known limitations / next steps
- **Playtesting.** The map has not been played by real players yet. Timings and health values are first-pass:
  10 s override, 8 s crack, 40 s shield drop, core 2600 hp, emitters 900 hp, turrets 800 hp.
- **Round time** comes from the server default.
- **Loading screen.** It is packed in the BSP, but the engine may read it before the pak is mounted. Official
  maps ship it loose.
- **Possible polish.** Areaportals for extra performance, more cyberspace variety, more interior detail.
