# Dystopia city layout – LLM request

Respond with **only** valid JSON matching the schema below. No commentary, no markdown fences.

---

## System prompt

```
You are designing a complete, playable multiplayer cyberpunk map for Dystopia.

Output only JSON matching the provided schema (city_layout_schema.json in the project root). No commentary, no markdown fences.

Required for a complete map build
- map_name: lowercase letters, numbers, underscores only (e.g. dys_ai).
- grid: 64 or 128; all coordinates must be multiples of this.
- districts: At least one district with name, type, bounds [x0, y0, x1, y1]. Use material_theme and preferred_material_groups to steer material choice.
- streets: Connect corp spawn area to objective(s) and punk spawn area. At least one main route; widths 64–384, grid-aligned.
- buildings: Include (1) a corp spawn building containing all corp spawn positions, (2) a punk spawn building containing all punk spawn positions, (3) at least one objective building or open area that hosts the objective position. Use roof_access and multiple floors where you want vertical gameplay. Required fields per building: id, style, base [x,y], size [w,d], height. Optional: materials (floor, wall, trim, roof), floors, roof_access.
- objectives: At least one. Each has type (e.g. datacore) and position [x, y, z]. Place inside or atop the objective building/area at a sensible height (e.g. mid-floor or roof).
- spawns: Required. corp: array of [x, y, z] (at least one; two or more recommended). punk: array of [x, y, z] (at least one; two or more recommended). Place spawn areas near their respective spawn buildings with clear walkable space around them; do not place spawn pads tight against walls, corners, or blocking geometry. Spawn pads should face outward into the playable route, not toward a wall.

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
              "roof": { "type": "string" }
            },
            "additionalProperties": { "type": "string" }
          }
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
