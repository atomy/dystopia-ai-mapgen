==============================================================================
 dys_blackice  --  "Black ICE"                                    version 1.0
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
    - Meatspace: use the Gate Control screen inside the NORTH guard post.
      The override takes 10 seconds and plays an alarm; a Corp can abort it
      from the same screen.
    - Cyberspace: hack the GATE LOCK terminal (password ICE) in the purple
      gate node. That opens the gate instantly.
    On success the NetExcess Arcade becomes a forward Punk spawn and the
    guard-post passages into the lobby open.

 2. CRACK THE SECURITY HUB (tower mezzanine, north side)
    A decker cracks the hub console (8 seconds, cyberdeck required).
    On success the Kuroda Security spawn flips to the Punks, the blast doors
    to the service lobby open, and the Corps fall back to Datavault Control.

 3. CRASH THE BLACK ICE CORE (core vault, final objective)
    The core can't be damaged while its shield is up. Two ways to drop it:
    - Cyberspace: the encrypted BLACK ICE SHIELD terminal in the core node
      drops it for 40 seconds. Corp deckers can raise it again early.
    - Meatspace: destroy BOTH shield emitters on the vault walkway to take
      the shield down for good.
    Destroying the core wins the round for the Punks. Corps win if they hold
    until time runs out.

 SIDE SYSTEMS
    - Plaza and vault turrets: capture, enable or disable them from cyberspace.
    - Maintenance access: a cyberspace terminal opens the service shaft that
      flanks into the server hall. It closes again after 25 seconds.
    - Jack-in points: Metro Hideout (x2), NetExcess Arcade, Security Hub
      (neutral), Kuroda Security (x2), Datavault Control.

 ROUTES
    Metro -> main stair -> market street                     (main lane)
    Metro -> maintenance tunnel -> north alley -> fire escape -> rooftops
    Market -> south alley -> plaza south side                (flank)
    Lobby -> blast doors -> server hall -> vault             (main, after obj 2)
    Lobby mezzanine -> maintenance corridor -> service shaft (flank, cyber door)

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
 CREDITS
------------------------------------------------------------------------------
 Map: atomy
 Built with a custom procedural toolchain (Python + Dystopia SDK tools)
 authored with Claude (Anthropic).
 Music: "blue rain" by bioxeed (ships with Dystopia).
 Textures, models and sounds: Team Dystopia and Valve.
