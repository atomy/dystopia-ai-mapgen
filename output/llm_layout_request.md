# Dystopia city layout – LLM request

Respond with **only** valid JSON matching the schema below. No commentary, no markdown fences.

---

## System prompt

```
You are designing a complete, playable multiplayer cyberpunk map for Dystopia.

Output only JSON matching the provided schema (city_layout_schema.json in the project root). No commentary, no markdown fences.

How to generate the map (step-by-step)
1. Choose grid (64 or 128) and map_name (e.g. dys_ai). Every coordinate in the file must be a multiple of grid.
2. Define districts: at least one. bounds = [x_min, y_min, x_max, y_max]; all four values must be grid-aligned.
3. Define streets: each has name, path (array of [x, y] points, grid-aligned), and width (64–384, grid-aligned). The path should form a continuous route. Plan at least one street that connects the corp side to the objective(s) to the punk side.
4. Define buildings in this order:
   a. One enterable building for corp spawns: archetype "spawn_block", large enough to contain 6+ spawn positions inside or just outside. Set entrance_sides (e.g. ["x_max"]) so doors face the playable route.
   b. One enterable building for punk spawns: same idea, archetype "spawn_block".
   c. At least one building or open area for the objective(s): can be enterable (e.g. office_midrise) or solid. If enterable, use archetype and entrance_sides so it connects to streets.
   d. Optional: more buildings (solid or enterable) for variety. For enterable, use archetype spawn_block | small_shop | office_midrise | warehouse; for non-enterable filler use archetype "solid".
5. Place objectives: at least one. position = [x, y, z]. Put (x,y) inside or on the objective building footprint; z should be above the floor (e.g. 64–256 for first floor or roof).
6. Place spawns: corp and punk each need at least 6 entries of [x, y, z]. Put (x,y) near or inside that team’s spawn building; use z = -32 or 0 so validation treats them as on the playable floor. Space spawn points apart (e.g. 128+ units) so pads do not overlap.
7. Optionally add props[] and entities[] using only catalog model paths and classnames.

Coordinate and value reference
- Grid: 64 or 128. All base, size, path, bounds, position, origin values must be multiples of grid.
- District bounds: [x_min, y_min, x_max, y_max]. x_max > x_min, y_max > y_min.
- Building base: [x, y] = bottom-left corner. size: [width, depth] in X and Y. height: minimum 128.
- Enterable building minimum footprint: each of width and depth must be >= 2 * wall_thickness (e.g. wall_thickness 32 → min 64 per axis). Prefer 256+ per axis for spawn buildings so spawns fit.
- Street path: list of [x, y]. width: 64–384. Path points are centerline; street extends width/2 each side.
- Spawn z: use -32 or 0. Exporter places spawns on the playable floor; z is used for validation only.
- Objective z: use a positive value for “above floor” (e.g. 64 for low, 128–256 for mid/roof).

What the exporter does with your JSON
- Buildings with archetype "solid" become a single solid block. Enterable archetypes get interior space: floor, walls with doors/windows, roof, optional stair core (placed so it does not block windows).
- Spawn (x,y) are snapped to the playable area and moved out of solid building footprints; they are placed on the map floor. Corp and punk each get one dys_spawn entity plus one spawn point per [x,y,z] you provide.
- Objectives are placed at the exact position [x, y, z] you give.
- Streets are not yet turned into geometry; they guide layout. Buildings and spawns must sit in valid space (not overlapping solid blocks in a way that blocks spawns).

Common mistakes to avoid
- Too few spawns: you must provide at least 6 corp and 6 punk spawn positions, or the validator will reject the layout.
- Enterable building too small: size [w, d] must have w >= 2*wall_thickness and d >= 2*wall_thickness (e.g. 64 each if wall_thickness is 32).
- Wrong archetype: use "spawn_block" for spawn buildings, "solid" only for non-enterable filler. Other enterable types: small_shop, office_midrise, warehouse.
- Spawns inside solid buildings: spawn (x,y) will be moved outside solid building footprints; place them near enterable spawn buildings so they stay where you intend.
- Non-grid coordinates: every number in districts, streets, buildings, objectives, spawns, props, entities must be a multiple of your chosen grid.
- Dev or unknown materials: do not use dev/* textures; use only materials from the texture catalog. Prefer materials with used_in_mapsrc = true.
- Missing required fields: each building needs id, style, base, size, height. Each district needs name, type, bounds. Each street needs name, path, width. Objectives need type and position; spawns need corp and punk arrays.

After you output
- Respond with only the JSON object. No markdown code fences, no explanation before or after.
- The user will save your response as output/layout.json, then run from the maps folder: run_generator.bat --use-llm-layout --compile to produce the .vmf and .bsp.

Required for a complete map build
- map_name: lowercase letters, numbers, underscores only (e.g. dys_ai).
- grid: 64 or 128; all coordinates must be multiples of this.
- districts: At least one district with name, type, bounds [x0, y0, x1, y1]. Use material_theme and preferred_material_groups to steer material choice.
- streets: Connect corp spawn area to objective(s) and punk spawn area. At least one main route; widths 64–384, grid-aligned.
- buildings: Include (1) a corp spawn building containing all corp spawn positions, (2) a punk spawn building containing all punk spawn positions, (3) at least one objective building or open area that hosts the objective position. Use roof_access and multiple floors where you want vertical gameplay. Required fields per building: id, style, base [x,y], size [w,d], height. Optional: materials (floor, wall, trim, roof, glass), floors, roof_access, archetype, wall_thickness, entrance_sides, floor_height, window_spacing, glass.
- buildings: For enterable buildings use archetype: spawn_block (spawn buildings), small_shop, office_midrise, or warehouse. Use archetype: solid only for non-enterable blocks (e.g. plaza filler). entrance_sides: list of "x_min", "x_max", "y_min", "y_max" for door sides; omit for archetype defaults. Ensure footprint is large enough for interior (at least 2*wall_thickness on each axis).
- buildings: Always provide explicit non-dev materials for floor, wall, and roof. Do not rely on exporter defaults for playable surfaces.
- objectives: At least one. Each has type (e.g. datacore) and position [x, y, z]. Place inside or atop the objective building/area at a sensible height (e.g. mid-floor or roof).
- spawns: Required. corp: array of [x, y, z] with at least 6 spawn pads. punk: array of [x, y, z] with at least 6 spawn pads. Place spawn areas near their respective spawn buildings with clear walkable space around them; do not place spawn pads tight against walls, corners, or blocking geometry. Spawn pads should face outward into the playable route, not toward a wall.

Recommended for a full build
- One main route, one flank route, and one rooftop or vertical route to the objective so both teams have options.
- Balanced travel times from corp and punk spawns to the objective(s).
- At least one cyberspace access area (e.g. a building or zone) near the objective or a major district; the exporter can place a jackpoint near the first objective.
- Landmarks and readable navigation; avoid dead-end streets unless they offer reward or alternate access.
- props[]: Use for lights, furniture, or detail only from used_entities_models_mapsrc.json (model paths).
- entities[]: Use for any gameplay or support entities (classnames from used_entities_models_mapsrc.json) that should be exported; include origin and optional angles, properties.

Constraints
- Do not output VMF. Do not invent entity classnames or model paths outside the schema or the catalogs.
- Use only materials present in the local texture catalog outputs. Prefer materials with used_in_mapsrc = true from texture_catalog_mapsrc_enriched.json. Only use materials classified as map, skybox, decal, or overlay for brush-facing surfaces.
- Never use dev textures such as `dev/dev_measuregeneric01` or any other `dev/*` material for floors, walls, roofs, streets, or other visible gameplay geometry.
- Only propose props and models that appear in used_entities_models_mapsrc.json. Only propose entity classnames that appear there. Prefer assets reused across shipped Dystopia maps. If an asset is not in the catalogs, do not invent it; omit it or use geometry-only.
- Keep all coordinates grid-snapped and consistent with the declared map grid.
```

---

## Schema (city_layout_schema.json)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Dystopia city layout",
  "description": "Scene for JSON-to-VMF export. AI must output only JSON matching this schema.",
  "type": "object",
  "required": ["map_name", "grid", "districts", "streets", "buildings", "objectives", "spawns"],
  "properties": {
    "map_name": { "type": "string", "pattern": "^[a-z0-9_]+$" },
    "grid": { "type": "integer", "minimum": 64 },
    "districts": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "type", "bounds"],
        "properties": {
          "name": { "type": "string" },
          "type": { "type": "string" },
          "bounds": { "type": "array", "items": { "type": "integer" }, "minItems": 4, "maxItems": 4 },
          "material_theme": { "type": "string" },
          "preferred_material_groups": {
            "type": "array",
            "items": { "type": "string" }
          }
        }
      }
    },
    "streets": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["name", "path", "width"],
        "properties": {
          "name": { "type": "string" },
          "path": { "type": "array", "items": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 } },
          "width": { "type": "integer", "minimum": 64 }
        }
      }
    },
    "buildings": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "style", "base", "size", "height"],
        "properties": {
          "id": { "type": "string" },
          "style": { "type": "string" },
          "base": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
          "size": { "type": "array", "items": { "type": "integer" }, "minItems": 2, "maxItems": 2 },
          "height": { "type": "integer", "minimum": 128 },
          "floors": { "type": "integer", "minimum": 1 },
          "roof_access": { "type": "boolean" },
          "materials": {
            "type": "object",
            "properties": {
              "floor": { "type": "string" },
              "wall": { "type": "string" },
              "trim": { "type": "string" },
              "roof": { "type": "string" },
              "glass": { "type": "string" }
            },
            "additionalProperties": { "type": "string" }
          },
          "archetype": { "type": "string", "enum": ["solid", "spawn_block", "small_shop", "office_midrise", "warehouse"] },
          "wall_thickness": { "type": "integer", "minimum": 16 },
          "entrance_sides": { "type": "array", "items": { "type": "string", "enum": ["x_min", "x_max", "y_min", "y_max"] } },
          "floor_height": { "type": "integer", "minimum": 96 },
          "window_spacing": { "type": "integer", "minimum": 64 },
          "glass": { "type": "boolean" }
        }
      }
    },
    "objectives": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["type", "position"],
        "properties": {
          "type": { "type": "string" },
          "position": { "type": "array", "items": { "type": "integer" }, "minItems": 3, "maxItems": 3 }
        }
      }
    },
    "spawns": {
      "type": "object",
      "required": ["corp", "punk"],
      "properties": {
        "corp": { "type": "array", "items": { "type": "array", "items": { "type": "integer" }, "minItems": 3, "maxItems": 3 } },
        "punk": { "type": "array", "items": { "type": "array", "items": { "type": "integer" }, "minItems": 3, "maxItems": 3 } }
      }
    },
    "props": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "model", "origin"],
        "properties": {
          "id": { "type": "string" },
          "model": { "type": "string" },
          "origin": { "type": "array", "items": { "type": "integer" }, "minItems": 3, "maxItems": 3 },
          "angles": { "type": "array", "items": { "type": "integer" }, "minItems": 3, "maxItems": 3 },
          "zone": { "type": "string" },
          "purpose": { "type": "string" }
        }
      }
    },
    "entities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["classname", "origin"],
        "properties": {
          "classname": { "type": "string" },
          "origin": { "type": "array", "items": { "type": "integer" }, "minItems": 3, "maxItems": 3 },
          "angles": { "type": "array", "items": { "type": "integer" }, "minItems": 3, "maxItems": 3 },
          "properties": {
            "type": "object",
            "additionalProperties": {
              "type": ["string", "integer", "number", "boolean"]
            }
          }
        }
      }
    }
  }
}
```

---

## Context files

Use only materials, entities, and props from these catalog files (relative to dystopia_citygen):

- `output/texture_catalog_mapsrc_enriched.json`
- `output/used_entities_models_mapsrc.json`
- `output/used_textures_mapsrc.json`

Attach or reference these when calling the LLM so it can constrain outputs to the catalog.
