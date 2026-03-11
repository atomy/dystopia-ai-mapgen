# Dystopia citygen

Generate Dystopia map layouts (JSON) and export them to VMF, then optionally compile to BSP.

![In-game screenshot of a completely AI-generated Dystopia map](doc/benchmark/dys_gpt_5_4_xhigh.png)

*Benchmark runs and more screenshots: [doc/benchmark/README.md](doc/benchmark/README.md).*

## How to use the tool chain

You can either use an **LLM-generated layout** (JSON from a model) or the **static MVP** (hardcoded arena). The generator writes the VMF into the **maps** folder (parent of `dystopia_citygen`).

### Option A: LLM-generated layout (full chain)

1. **Prepare the LLM request** (run from `dystopia_citygen`):
   ```bat
   cd dystopia_citygen
   prepare_llm_request.bat
   ```
   This writes `output/llm_layout_request.md` with the system prompt, schema, and catalog paths.

2. **Get JSON from the LLM** (e.g. in Cursor):
   - Open `dystopia_citygen/output/llm_layout_request.md`.
   - Attach the catalog files so the model can use only allowed materials/entities:
     - `output/texture_catalog_mapsrc_enriched.json`
     - `output/used_entities_models_mapsrc.json`
   - Ask the model to produce a city layout; it should respond with **only** JSON matching `city_layout_schema.json`.
   - Save the model’s response as `dystopia_citygen/output/layout.json` (no markdown fences or commentary).

3. **Generate the VMF** (run from the **maps** folder):
   ```bat
   run_generator.bat --use-llm-layout
   ```
   This uses `dystopia_citygen/output/layout.json` and writes e.g. `dys_ai.vmf` in the maps folder.

4. **Optional – compile to BSP:**
   ```bat
   run_generator.bat --use-llm-layout --compile
   ```

If you prefer to pass the layout file explicitly (e.g. from another path or name):
```bat
run_generator.bat --layout-json dystopia_citygen/output/layout.json
```

### Option B: Static map (fallback)

Without any layout file, the generator uses the hardcoded MVP arena. From the **maps** folder:

```bat
run_generator.bat
```

You get the same result if you use `--use-llm-layout` but `output/layout.json` does not exist.

### Generator options (run_generator.bat)

| Option | Description |
|--------|-------------|
| (none) | Use static MVP arena. |
| `--use-llm-layout` | Use `output/layout.json` if it exists; otherwise static MVP. |
| `--layout-json <path>` | Use this JSON file as the layout (path relative to current dir, e.g. from maps: `dystopia_citygen/output/layout.json`). |
| `--map-name <name>` | Output VMF name without extension (default: from layout or `dys_ai`). |
| `--compile` | Run vbsp, vvis, vrad after writing the VMF to produce a .bsp. |

**Where to run:** Run `run_generator.bat` from the **maps** folder so the VMF (and BSP) are written there. Run `prepare_llm_request.bat` from **dystopia_citygen**.

### Other scripts (use the .bat variants)

| Task | Command (from dystopia_citygen) |
|------|--------------------------------|
| Prepare LLM request | `prepare_llm_request.bat` |
| Catalog textures (base) | `catalog_textures.bat` |
| Catalog used textures (VMF scan) | `catalog_used_textures.bat` [--vmf-dir ...] [--output-dir ...] |
| Generate static layout JSON | `generate_layout.bat` |
| Compile existing VMF | `compile_map.bat` [vmf_path] |

Use the **.bat** files so execution can be allowed in Cursor; do not invoke `.py` scripts directly.
