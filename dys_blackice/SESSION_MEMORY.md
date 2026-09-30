# Session memory: dys_blackice (2026-09-28, playtest rounds 2026-09-29 and 2026-09-30)

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
- `maps/dys_blackice.bsp` v1.3, about 28 MB, with everything packed inside. It is a rainy neon-city objective map:
  metro, street market, plaza, tower lobby, server hall and core vault, plus one open cyberspace hall.
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
8. **Playtest round 1 (2026-09-29, v1.1).** The user played the map and asked for five changes, all done:
   - Remove the energy crystals and the rotating ceiling rings from cyberspace.
   - Put each terminal in a small house whose door is the ICE.
   - Replace the node-and-tunnel cyberspace with one big open room.
   - Make the turrets destroyable with about 10 bolts each.
   - Move the gate turrets away from the gate, because they shot anyone trying to breach it.
9. **Playtest round 2 (2026-09-30, v1.2).** A longer play session with screenshots, all addressed:
   - Lamps, pipes, monitors and signs that hung in mid-air or faced the wrong way. The validator now flags props
     and thin panels with nothing behind them and glow sprites with nothing near them.
   - All stairs were too steep (16u risers). Every flight is now 8u risers on 16u treads.
   - The plaza was a sniper lane. Two annex buildings narrow it, and an ad tower, containers, columns,
     balustrades, barricades and wrecks break the sight lines.
   - Canopy turrets restored at the gate (cyberspace can only disable them). The lobby turrets could still hit
     attackers through the gate lattice, so the closed gate got an invisible solid layer. Gate override 60 s.
   - Cyberspace spawns: deckers now start in a pod high on the wall and float down a zero-gravity tube, like the
     official maps. The tube exits carry static team ICE.
   - Shop shutters recessed into the facades; a spawn exit freed from a staircase; metro tunnels that continue
     behind forcefields; a readable station sign; forcefields set into their openings.
   - A custom Kuroda monument model (Blender, scripted, compiled with studiomdl) replaces the brush obelisk.
10. **Playtest round 3 (2026-09-30, v1.3).**
   - The monument felt too aggressive (crystal spikes). Five parallel sub-agents sketched five calmer concepts
     in Blender on one shared stage (`monument/concepts/stage.py`, the same plaza stand-in and cameras). The
     user picked the Fibre Tree, which the same agent then built as the real prop.
   - The security gate can now only be breached in meatspace (the cyberspace gate lock was removed).
   - Decker spawn pods moved outside the hall; the tubes run through a dark duct and the hall wall.
   - Fire-escape balconies hung in mid-air above the roof walkway, and ten neon signs floated 4u off their
     facades. The validator now groups touching detail brushes into clusters and requires every cluster to
     touch the shell, a world brush or a prop.
   - Alternative routes: a north service door (plaza side, opens with the gate) up to a west door into the
     hub, and a cooling route from the hub's north door through a new cooling plant to the vault (opens with
     the hub). A lobby turret terminal in cyberspace; turret terminals lock when their objective falls.
   - The gate alarm kept sounding after capture (looping WAV, see below); override cut to 30 s.
   - Spawn pads blocked movement; the arcade's spawn points crowded its jack-in terminal.

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
- **Turrets spawn invulnerable.**
  - A freshly spawned `npc_turret_ceiling` ignores all damage, even while deployed and firing, until it receives
    `Enable`. `SetVincible` does not help. The map sends `Enable` from a `logic_auto` `OnMapSpawn`.
  - After that, one boltgun bolt does 82 damage, so 800 hp takes 10 bolts. The bolt's zap adds nothing.
  - A disabled or retracted turret takes no damage.
  - A destroyed turret rebuilds after about 60 s (`respawntime` 0) and stays damageable.
- **cyber_floor re-orients gravity.**
  - Touching any face of a `cyber_floor` brush turns the decker's gravity toward that face (wall-walking). Bumping
    the side of a raised `cyber_floor` block flipped a test decker onto a wall.
  - Keep raised geometry as plain `func_detail`, which deckers walk on normally, unless wall-walking is intended.
  - Deckers stop about 32u from walls, wider than the meatspace hull.
- **Turrets and gates.** `npc_turret_ceiling` ignores `tools/toolsblock_los`: a lattice gate
  (`metal/metalgate001a`, `%compilepassbullets`) lets turrets shoot straight through. Only a solid brush in the door
  stops them, and it blocks bullets both ways.
- **Spawn pads.** `dys_spawn_point` shows `models/props/prop_spawner.mdl`, which is solid and blocks movement.
  Spawnflag 1 ("Disable Model") removes it; the map places the same pad as a non-solid prop for the look.
- **Locking a terminal after capture.** Route the screen's button outputs through `logic_relay`s and send the
  relays `Disable` on capture: pressing the buttons then does nothing.
- **Looping sounds.** An `ambient_generic` flagged "Is NOT Looped" (spawnflags 32) ignores `StopSound`. If its
  WAV loops anyway (a `cue ` chunk, e.g. `ambient/alarms/alarm1.wav`), it sounds forever. Flag looping WAVs as
  looped (spawnflags 16 = start silent only).
- **Zero-g tubes.** Two `cyber_gravity_volume` brushes, one at each end of a tube, switch gravity off inside it.
  Their `angles` must point at the room that has gravity (verified: a decker hovers in the tube and lands on the
  hall floor after the exit volume). A static `cyber_ice` (spawnflags 1) with a team lets only that team through.
- **Entry cameras.** The jack-in terminal's screen shows the target `point_camera` upside down. Rolling the camera
  180 degrees also rolls the arriving decker's view, so keep roll 0 and make the camera's view symmetric instead.
- **Tube look.** Official maps build tubes from translucent brushes (dys_cybernetic: `twincannon/twin_cyberblue_trans`).
  From inside, a plain translucent wall almost vanishes against a blue room. The additive, `$nocull`
  `twincannon/twin_cyberblue_trans_additive_nocull` plus light strips embedded in the glass along the four edges
  reads from inside and outside. Keep the inside smooth: strips that stick into the tube snag the decker.
- **Tube paths.** A decker flying a tube stops dead on any other brush inside it: a cover block in the path of
  the tube's lower bend trapped the test decker. Zero-g also has no friction, so an idle decker keeps drifting.
- **Circlet rings.** `cyspfinal/circlet*` are additive. On a small disc, world-aligned texture coordinates split
  the ring into loose white arcs; fit the texture to the disc. Official maps stack them as static halos.
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
- **Weapon tests in multiplayer.**
  - `god`, `buddha` and `notarget` do nothing in multiplayer.
  - To survive, give the test player health with `ent_fire player addoutput "health 90000"`.
  - Turret bullets knock the player away. `sv_friction 1000` holds the player in place.
  - A damage filter on the player makes turrets stop engaging, which also stops them taking damage.
  - Send `setpos`/`setang` and `+attack` in separate cfgs. In one cfg the shot can fire before the teleport.
  - `setweapon 3` picks the boltgun for the light class (1 shotgun, 2 laser rifle). `givecurrentammo` refills.
  - `ent_dump <name>` prints each entity's health to the console log.
- **Hiding loose files for the clean-client test.** Give every hidden folder a unique name. Several custom
  folders are called `blackice`; hiding them by folder name alone overwrote one with the next and lost the
  files. They were restored byte-exact from the BSP pak. `release.hide_loose` now keys by relative path.
- **Never change archived cvars in automated runs.** In Dystopia `r_drawviewmodel` is archived, unlike stock
  Source. The game saves `config.cfg` on quit and syncs it to Steam Cloud, so restoring the local file is not
  enough; the tester lost their gun viewmodel this way. `GameSession.close()` now sets the viewmodel back on.

## Design decisions
- **Box-CSG shell.** The world is painted as ordered solid and air boxes, so sealing is guaranteed by
  construction and a leak check runs before vbsp. All detail is `func_detail` or brush entities.
- **No objective skipping.** The cyberspace-controlled maintenance door only works after the hub has fallen.
  Without that, Punks could skip objective 2. The Datavault spawn starts disabled for the same reason.
- **How each objective opens.**
  - Gate: meatspace only, a 30 s override at the north guard post (the cyberspace hack was removed on request).
  - Core shield: two ways, a temporary drop from cyberspace or a permanent drop by destroying the emitters.
- **Cyberspace is one open hall.** A red core terrace with ramps, cover blocks, black pillars, three wall pods
  with zero-g tubes down to landing pads, and five terminal houses. Each house's doorway is its ICE, and the screen hangs on the back
  wall facing the door. Floating node icons (`vaccinert/dys_*node`) label the houses.
- **Gate turrets on the canopy.** Two turrets hang under the canopy in front of the gate; cyberspace can only
  disable or enable them (no capture). A solid, invisible layer in the closed gate keeps the lobby turrets from
  shooting through it; it lifts with the gate.
- **Stairs are 1:2.** 8u risers on 16u treads (about 27 degrees) with a player-clip ramp over the steps.
- **Custom art is generated.** The Kuroda logos, window facade, BLACK ICE warning, overview and loading screen
  are all made by scripts (Pillow and vtex), so they can be rebuilt from the repo alone.

## Known limitations / next steps
- **Playtesting.** One solo playtest so far, no full match. Timings and health values are first-pass:
  30 s override, 8 s crack, 40 s shield drop, core 2600 hp, emitters 900 hp, turrets 800 hp (10 bolts).
- **Gate objective marker.** The IFF box is drawn around the gate itself, which invites shooting it. The breach
  actually happens at the override screen in the north guard post or in cyberspace.
- **Round time** comes from the server default.
- **Loading screen.** It is packed in the BSP, but the engine may read it before the pak is mounted. Official
  maps ship it loose.
- **Possible polish.** Areaportals for extra performance, more cyberspace variety, more interior detail.
