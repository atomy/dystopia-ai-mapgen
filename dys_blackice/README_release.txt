==============================================================================
 dys_blackice  --  "Black ICE"                                    version 1.3
 Objective map for Dystopia (Punks attack / Corps defend)
==============================================================================

 Night. Rain. Neon.
 Kuroda Systems runs Arcology Block 7 from a tower that disappears into the
 storm clouds. Under it sits a datavault guarded by BLACK ICE, the corp's
 lethal AI firewall. The Punks are coming up out of the old monorail tunnels
 to crash it.

------------------------------------------------------------------------------
 INSTALL
------------------------------------------------------------------------------
 Copy  maps/dys_blackice.bsp  into  <Steam>/steamapps/common/Dystopia/dystopia/maps/
 Everything else (screens, custom textures, radar overview, objective guide
 paths, soundscapes, music, loading screen, cubemaps) is packed in the BSP.
 Servers: add  dys_blackice  to mapcycle.txt. Clients download it like any map.

------------------------------------------------------------------------------
 FLOW
------------------------------------------------------------------------------
 Punks spawn in an abandoned monorail station (Metro Hideout) and fight up
 through the Three Happy Dragon street market into Kuroda Plaza.

 1. BREACH THE SECURITY GATE (Kuroda Plaza)
    Use the Gate Control screen inside the NORTH guard post (meatspace
    only). The override takes 30 seconds and sounds an alarm (it stops when
    the gate falls); a Corp can
    abort it from the same screen.
    On success the NetExcess Arcade becomes a forward Punk spawn and the
    guard-post passages into the lobby open.

 2. CRACK THE SECURITY HUB (tower mezzanine, north side)
    A decker cracks the hub console (8 seconds, cyberdeck required). Two ways
    up: the lobby stairs to the mezzanine, or the north service door in the
    plaza's north-east corner (opens with the gate) and its stair hall, which
    leads straight into the hub from the west.
    On success the Kuroda Security spawn flips to the Punks, the blast doors
    to the service lobby open, and the Corps fall back to Datavault Control.

 3. CRASH THE BLACK ICE CORE (core vault, final objective)
    Three ways into the vault: the main route through the service lobby and
    the server hall, the maintenance shaft (cyber door), and the cooling
    route from the hub's north door through the cooling plant to the vault's
    north-east walkway (opens with the hub).
    The core can't be damaged while its shield is up. Two ways to drop it:
    - Cyberspace: the BLACK ICE SHIELD terminal in the black core house on the
      red terrace (encrypted ICE) drops it for 40 seconds. Corp deckers can
      raise it again early.
    - Meatspace: destroy BOTH shield emitters on the vault walkway to take
      the shield down for good.
    Destroying the core wins the round for the Punks. Corps win if they hold
    until time runs out.

 SIDE SYSTEMS
    - Turrets: two under the canopy in front of the security gate, two in the
      lobby, two in the core vault. Each takes about 10 boltgun bolts to
      destroy and rebuilds after about a minute. The closed gate blocks the
      lobby turrets' line of fire (and all bullets). From the red
      TurretControls houses in cyberspace deckers can disable or enable the
      gate and lobby turrets, and capture, enable or disable the vault
      turrets. The gate turrets shut down when the gate falls, the lobby
      turrets when the hub falls, and their terminals go dead with them.
    - Maintenance access: a cyberspace terminal opens the service shaft that
      flanks into the server hall. It closes again after 25 seconds.
    - Jack-in points: Metro Hideout (x2), NetExcess Arcade, Security Hub
      (neutral), Kuroda Security (x2), Datavault Control.

 CYBERSPACE
    One open hall. Deckers jack in to a small pod outside the hall and float
    down a long glowing zero-gravity tube through a dark void; it enters the
    hall at floor level: Punks from the west, Corps from the east, the
    Security Hub jack-in from the south.
    The Punk and Corp tube exits are sealed with static team ICE, so the
    other team can't get in. Every terminal sits in a small house whose door
    is its ICE: wedge or break the ICE to get in. Corp deckers pass through
    their own ICE.

 ROUTES
    Metro -> main stair -> market street                     (main lane)
    Metro -> maintenance tunnel -> north alley -> fire escape -> rooftops
    Market -> south alley -> plaza south side                (flank)
    Plaza NE corner -> north service door -> stair hall -> hub   (after obj 1)
    Lobby -> blast doors -> server hall -> vault             (main, after obj 2)
    Lobby mezzanine -> maintenance corridor -> service shaft (flank, cyber door)
    Hub north door -> duct -> cooling plant -> vault NE door (flank, after obj 2)
    Server hall <-> cooling plant                            (link)

------------------------------------------------------------------------------
 TECHNICAL
------------------------------------------------------------------------------
 - Compiled with Dystopia's own vbsp/vvis/vrad (full vis, -both -final:
   HDR + LDR lighting), cubemaps built for LDR and HDR.
 - Custom content packed in the BSP:
     materials/blackice/*          Kuroda banner and logo, BLACK ICE warning,
                                   night-office window facade
     materials/overviews/*         3-layer radar overview
     materials/loading/*           loading screen
     resource/overviews, resource/mappaths, maps/*_screens.txt,
     scripts/screens/*.res, scripts/soundscapes_dys_blackice.txt,
     maps/dys_blackice_music.txt
 - Everything else is stock Dystopia and Half-Life 2 content.
 - 3D skybox: a megacity skyline at 1/16 scale.

------------------------------------------------------------------------------
 CHANGES
------------------------------------------------------------------------------
 1.3  Fibre-optic Kuroda tree replaces the monument. The security gate can
      only be breached in meatspace, with a 30 s override whose alarm stops
      when the gate falls. New routes: north service door to the hub, and
      the cooling route from the hub to the vault. Lobby turret terminal in
      cyberspace; turret terminals go dead when their objective falls.
      Decker pods outside the hall with long glowing tubes you can see from
      inside. Spawn pads no longer block movement; the arcade jack-in is
      clear. Floating balconies and signs fixed, smaller roof billboard.
 1.2  Kuroda monument in the plaza. Plaza reworked against long sniper
      lines (annexes, ad tower, containers, columns, balustrades). Gate
      override 60 s, canopy turrets back (disable only from cyberspace),
      closed gate blocks the lobby turrets. All stairs 1:2. Zero-g cyber
      tubes with team ICE. Shop shutters recessed, lamps and pipes mounted
      on walls, metro tunnels continue behind forcefields.
 1.1  Cyberspace rebuilt as one open hall with ICE-door terminal houses.
      Turrets can now be destroyed (10 bolts). The gate turrets moved
      behind the gate.
 1.0  First release.

------------------------------------------------------------------------------
 CREDITS
------------------------------------------------------------------------------
 Map: atomy
 Built with a custom procedural toolchain (Python + Dystopia SDK tools)
 authored with Claude (Anthropic).
 Music: "blue rain" by bioxeed (ships with Dystopia).
 Textures, models and sounds: Team Dystopia and Valve.
