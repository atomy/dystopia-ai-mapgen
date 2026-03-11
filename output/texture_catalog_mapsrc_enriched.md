# Dystopia Texture Catalog

- Game dir: `M:\SteamLibrary\steamapps\common\Dystopia\dystopia`
- Material root: `M:\SteamLibrary\steamapps\common\Dystopia\dystopia\materials`
- Total materials: `3531`
- Map-usable materials: `2338`

## Usage Summary

- `decal`: `84`
- `effect`: `29`
- `map`: `2173`
- `model`: `687`
- `overlay`: `50`
- `particle`: `53`
- `skybox`: `31`
- `sprite`: `34`
- `ui`: `390`

## VMF Usage

- VMF source dir: `mapsrc`
- VMF files scanned: `21`
- Unique materials referenced by VMFs: `1843`
- Catalog materials used by scanned VMFs: `1177`
- Referenced materials missing from this install: `666`

## Notes

- `map` is a default mapping-friendly bucket.
- `skybox` materials are usable for sky brushes.
- `decal` and `overlay` are often useful in detailing passes.
- `ui`, `model`, `particle`, `sprite`, and `effect` entries are cataloged for completeness but are usually not brush-face textures.

## Materials By Group

### `EMP_overlay`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `EMP_overlay` | `Modulate` | `-` | `overlay` | `0` | `EMP_scanline` |

### `SDK`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `SDK/bloom` | `Cyber_Bloom` | `-` | `map` | `0` | `-` |
| `SDK/blurfilterx` | `BlurFilterX` | `-` | `map` | `0` | `_rt_SmallFB0` |
| `SDK/blurfiltery` | `BlurFilterY` | `-` | `map` | `0` | `_rt_SmallFB1` |
| `SDK/cyberbloom` | `Cyber_Bloom` | `-` | `map` | `0` | `-` |
| `SDK/cyberblurfilterx` | `Cyber_BlurFilterX` | `-` | `map` | `0` | `-` |
| `SDK/cyberblurfiltery` | `Cyber_BlurFilterY` | `-` | `map` | `0` | `-` |
| `SDK/cyberdownsample` | `Cyber_Downsample` | `-` | `map` | `0` | `-` |
| `SDK/downsample` | `Downsample_nohdr` | `-` | `map` | `0` | `_rt_FullFrameFB` |
| `SDK/downsample_bloom` | `Cyber_Downsample` | `-` | `map` | `0` | `-` |
| `SDK/sdk_blur` | `SDK_Blur` | `-` | `map` | `0` | `_rt_FullFrameFB` |
| `SDK/sdk_postprocess` | `SDK_PostProcess` | `-` | `map` | `0` | `_rt_FullFrameFB` |

### `Thermal`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `Thermal` | `Patch` | `-` | `map` | `0` | `-` |

### `Thermal_coldsuit_hands`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `Thermal_coldsuit_hands` | `dys_thermal` | `-` | `map` | `0` | `-` |

### `Thermal_dx8`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `Thermal_dx8` | `vertexlitgeneric` | `-` | `map` | `0` | `thermal_yellow` |

### `adverts`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `adverts/adverts_aphrodite` | `unlitgeneric` | `glass` | `map` | `1` | `adverts/adverts_aphrodite` |
| `adverts/adverts_cyberfight_001` | `unlitgeneric` | `-` | `map` | `2` | `adverts/adverts_cyberfight_001` |
| `adverts/adverts_kitty` | `unlitgeneric` | `glass` | `map` | `1` | `adverts/adverts_kitty` |
| `adverts/adverts_laora_001` | `unlitgeneric` | `-` | `map` | `2` | `adverts/adverts_laora_001` |

### `avatars`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `avatars/ai01` | `unlitgeneric` | `-` | `map` | `0` | `avatars/ai01` |
| `avatars/ai02` | `unlitgeneric` | `-` | `map` | `0` | `avatars/ai02` |
| `avatars/ai03` | `unlitgeneric` | `-` | `map` | `0` | `avatars/ai03` |
| `avatars/ai04` | `unlitgeneric` | `-` | `map` | `0` | `avatars/ai04` |
| `avatars/ai05` | `unlitgeneric` | `-` | `map` | `0` | `avatars/ai05` |
| `avatars/ai06` | `unlitgeneric` | `-` | `map` | `0` | `avatars/ai06` |
| `avatars/background_corp01` | `unlitgeneric` | `-` | `map` | `0` | `avatars/background_corp01` |
| `avatars/background_dmt` | `unlitgeneric` | `-` | `map` | `0` | `avatars/background_dmt` |
| `avatars/background_dmt_corp` | `unlitgeneric` | `-` | `map` | `0` | `avatars/background_dmt_corp` |
| `avatars/background_dmt_punk` | `unlitgeneric` | `-` | `map` | `0` | `avatars/background_dmt_punk` |
| `avatars/background_dtrust` | `UnlitGeneric` | `-` | `map` | `0` | `avatars/background_dtrust` |
| `avatars/background_punk01` | `unlitgeneric` | `-` | `map` | `0` | `avatars/background_punk01` |
| `avatars/dmt` | `UnlitTwoTexture` | `-` | `map` | `0` | `avatars/dmt` |
| `avatars/handler001` | `UnlitTwoTexture` | `-` | `map` | `0` | `avatars/handler001` |
| `avatars/player_corp_decker` | `UnlitTwoTexture` | `-` | `map` | `0` | `avatars/player_corp_decker` |
| `avatars/player_corp_heavy` | `UnlitTwoTexture` | `-` | `map` | `0` | `avatars/player_corp_heavy` |
| `avatars/player_corp_light` | `UnlitTwoTexture` | `-` | `map` | `0` | `avatars/player_corp_light` |
| `avatars/player_corp_medium` | `UnlitTwoTexture` | `-` | `map` | `0` | `avatars/player_corp_medium` |
| `avatars/player_punk_decker` | `UnlitTwoTexture` | `-` | `map` | `0` | `avatars/player_punk_decker` |
| `avatars/player_punk_heavy` | `UnlitTwoTexture` | `-` | `map` | `0` | `avatars/player_punk_heavy` |
| `avatars/player_punk_light` | `UnlitTwoTexture` | `-` | `map` | `0` | `avatars/player_punk_light` |
| `avatars/player_punk_medium` | `UnlitTwoTexture` | `-` | `map` | `0` | `avatars/player_punk_medium` |

### `broadcast`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `broadcast/bc_decalgraffiti01` | `LightmappedGeneric` | `-` | `decal` | `0` | `broadcast/graffiti/skull` |
| `broadcast/bc_decalgraffiti02` | `LightmappedGeneric` | `-` | `decal` | `0` | `broadcast/graffiti/crowd2` |
| `broadcast/bc_decalgraffiti03` | `LightmappedGeneric` | `-` | `decal` | `0` | `broadcast/graffiti/watching2` |
| `broadcast/cube_firewall` | `UnlitGeneric` | `-` | `map` | `1` | `broadcast/cube_firewall` |
| `broadcast/cyber_round_firewall` | `UnlitGeneric` | `-` | `map` | `1` | `broadcast/cyber_round_firewall` |
| `broadcast/dtsecBack` | `UnlitTwoTexture` | `-` | `map` | `0` | `broadcast/dtsecBack` |
| `broadcast/dys_bc_concrete_dark1` | `LightmappedGeneric` | `concrete` | `map` | `2` | `broadcast/concrete/concrete_dark1` |
| `broadcast/intruder` | `unlitgeneric` | `-` | `map` | `1` | `broadcast/intruder` |
| `broadcast/screens/decker_corp` | `unlitgeneric` | `-` | `map` | `1` | `broadcast/screens/decker_corp` |
| `broadcast/screens/decker_punk` | `unlitgeneric` | `-` | `map` | `3` | `broadcast/screens/decker_punk` |
| `broadcast/screens/electrical_hazard` | `unlitgeneric` | `-` | `map` | `1` | `broadcast/screens/electrical_hazard` |
| `broadcast/screens/elevator` | `UnlitGeneric` | `-` | `map` | `1` | `broadcast/screens/elevator` |
| `broadcast/screens/firewall` | `UnlitGeneric` | `-` | `map` | `1` | `broadcast/screens/firewall` |
| `broadcast/screens/firewall_block` | `unlitgeneric` | `-` | `map` | `1` | `broadcast/screens/firewall_block` |
| `broadcast/screens/punk_monitor1` | `Monitorscreen` | `glass` | `map` | `1` | `_rt_camera1` |
| `broadcast/screens/punk_monitor1_dx8` | `unlitgeneric` | `-` | `map` | `0` | `_rt_camera1` |
| `broadcast/screens/punk_monitor2` | `Monitorscreen` | `glass` | `map` | `0` | `_rt_camera2` |
| `broadcast/screens/punk_monitor2_dx8` | `unlitgeneric` | `-` | `map` | `0` | `_rt_camera2` |
| `broadcast/screens/punk_monitor3` | `Monitorscreen` | `glass` | `map` | `1` | `_rt_camera3` |
| `broadcast/screens/punk_monitor3_dx8` | `unlitgeneric` | `-` | `map` | `0` | `_rt_camera3` |
| `broadcast/screens/punk_monitor4` | `Monitorscreen` | `glass` | `map` | `1` | `_rt_camera4` |
| `broadcast/screens/punk_monitor4_dx8` | `unlitgeneric` | `-` | `map` | `0` | `_rt_camera4` |
| `broadcast/screens/scanline1` | `UnlitTwoTexture` | `no_decal` | `map` | `2` | `broadcast/screens/scanline` |
| `broadcast/screens/scanline2` | `UnlitTwoTexture` | `no_decal` | `map` | `1` | `broadcast/screens/scanline` |
| `broadcast/screens/sewer` | `UnlitGeneric` | `-` | `map` | `1` | `broadcast/screens/sewer` |
| `broadcast/screens/txscroll` | `unlitgeneric` | `-` | `map` | `1` | `broadcast/screens/txscroll` |
| `broadcast/water_clear` | `Water` | `water` | `map` | `1` | `-` |
| `broadcast/water_clear_dx8` | `unlitgeneric` | `-` | `map` | `0` | `tools/toolsblack` |
| `broadcast/water_refract` | `Refract` | `water` | `map` | `2` | `-` |

### `buildings`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `buildings/antn01` | `$basetexture` | `-` | `map` | `1` | `buildings/antn01` |
| `buildings/antn02` | `$basetexture` | `-` | `map` | `1` | `buildings/antn02` |
| `buildings/antn03` | `$basetexture` | `-` | `map` | `1` | `buildings/antn03` |
| `buildings/antn04` | `$basetexture` | `-` | `map` | `0` | `buildings/antn04` |
| `buildings/gen01` | `$basetexture` | `-` | `map` | `1` | `buildings/gen01` |
| `buildings/gen03` | `$basetexture` | `-` | `map` | `0` | `buildings/gen03` |
| `buildings/gen07` | `$basetexture` | `-` | `map` | `2` | `buildings/gen07` |
| `buildings/gen08` | `$basetexture` | `-` | `map` | `0` | `buildings/gen08` |
| `buildings/gen09` | `$basetexture` | `-` | `map` | `0` | `buildings/gen09` |
| `buildings/gen11` | `$basetexture` | `concrete` | `map` | `0` | `buildings/gen11` |
| `buildings/gen12` | `$basetexture` | `-` | `map` | `0` | `buildings/gen12` |
| `buildings/gen14` | `$basetexture` | `-` | `map` | `0` | `buildings/gen14` |
| `buildings/gen15` | `$basetexture` | `-` | `map` | `0` | `buildings/gen15` |
| `buildings/gen16` | `$basetexture` | `-` | `map` | `1` | `buildings/gen16` |
| `buildings/gen17` | `$basetexture` | `-` | `map` | `0` | `buildings/gen17` |
| `buildings/gen18` | `$basetexture` | `-` | `map` | `1` | `buildings/gen18` |
| `buildings/gen19` | `$basetexture` | `-` | `map` | `0` | `buildings/gen19` |
| `buildings/gen20` | `$basetexture` | `-` | `map` | `0` | `buildings/gen20` |
| `buildings/gen21` | `$basetexture` | `-` | `map` | `1` | `buildings/gen21` |
| `buildings/gen22` | `$basetexture` | `-` | `map` | `0` | `buildings/gen22` |
| `buildings/gen23` | `$basetexture` | `-` | `map` | `1` | `buildings/gen23` |
| `buildings/gen24` | `$basetexture` | `-` | `map` | `1` | `buildings/gen24` |
| `buildings/gen25` | `$basetexture` | `-` | `map` | `0` | `buildings/gen25` |

### `camera1`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `camera1` | `UnlitGeneric` | `-` | `map` | `0` | `_rt_camera1` |

### `camera2`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `camera2` | `UnlitGeneric` | `-` | `map` | `0` | `_rt_camera2` |

### `camera3`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `camera3` | `UnlitGeneric` | `-` | `map` | `0` | `_rt_camera3` |

### `camera4`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `camera4` | `UnlitGeneric` | `-` | `map` | `0` | `_rt_camera4` |

### `camera_rocket`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `camera_rocket` | `UnlitGeneric` | `-` | `map` | `0` | `_rt_camera_rocket` |

### `cesspool`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `cesspool/dys_cpd1` | `LightmappedGeneric` | `metal` | `map` | `2` | `cesspool/dys_cpd1` |
| `cesspool/dys_cpd2` | `LightmappedGeneric` | `metal` | `map` | `3` | `cesspool/dys_cpd2` |
| `cesspool/dys_cpd3` | `LightmappedGeneric` | `metal` | `map` | `3` | `cesspool/dys_cpd3` |
| `cesspool/dys_cpdoor1` | `LightmappedGeneric` | `metal` | `map` | `4` | `cesspool/dys_cpdoor1` |
| `cesspool/dys_cpdoor1_red` | `LightmappedGeneric` | `metal` | `map` | `3` | `cesspool/dys_cpdoor1_red` |
| `cesspool/dys_cpdoor4` | `LightmappedGeneric` | `metal` | `map` | `6` | `cesspool/dys_cpdoor4` |
| `cesspool/dys_cpw2` | `LightmappedGeneric` | `metal` | `map` | `4` | `cesspool/dys_cpw2` |
| `cesspool/dys_cpwall1` | `LightmappedGeneric` | `metal` | `map` | `3` | `cesspool/dys_cpwall1` |
| `cesspool/dys_cpwall2` | `LightmappedGeneric` | `metal` | `map` | `2` | `cesspool/dys_cpwall2` |
| `cesspool/dys_mf6` | `LightmappedGeneric` | `metal` | `map` | `3` | `cesspool/dys_mf6` |
| `cesspool/dys_mf7` | `LightmappedGeneric` | `metal` | `map` | `2` | `cesspool/dys_mf7` |

### `coast`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `coast/ceiling_panel01` | `LightMappedGeneric` | `concrete` | `map` | `0` | `coast/ceiling_panel01` |
| `coast/dys_laddernode_noscroll` | `UnlitGeneric` | `metal` | `map` | `0` | `vaccinert/dys_laddernode` |
| `coast/dys_turretnode_noscroll` | `UnlitGeneric` | `metal` | `map` | `0` | `vaccinert/dys_turretnode` |
| `coast/metal_tread` | `LightmappedGeneric` | `-` | `map` | `0` | `coast/metal_tread` |
| `coast/office_ceiling_tile` | `LightmappedGeneric` | `concrete` | `map` | `0` | `coast/office_ceiling_tile` |
| `coast/office_ceiling_tile_light` | `LightmappedGeneric` | `concrete` | `map` | `0` | `coast/office_ceiling_tile_light` |
| `coast/panel01` | `LightMappedGeneric` | `concrete` | `map` | `0` | `coast/panel01` |
| `coast/panel01a` | `LightMappedGeneric` | `concrete` | `map` | `0` | `coast/panel01a` |
| `coast/panel01b` | `LightMappedGeneric` | `concrete` | `map` | `0` | `coast/panel01b` |
| `coast/panel01c` | `LightMappedGeneric` | `concrete` | `map` | `0` | `coast/panel01c` |
| `coast/panel01e` | `LightMappedGeneric` | `concrete` | `map` | `0` | `coast/panel01e` |
| `coast/vac_door_orange` | `LightmappedGeneric` | `metal` | `map` | `0` | `coast/vac_door_orange` |
| `coast/zettasec` | `LightmappedGeneric` | `-` | `map` | `0` | `coast/zettasec` |
| `coast/zettasec_glass1` | `LightmappedGeneric` | `Glass` | `map` | `0` | `coast/zettasec_glass1` |
| `coast/zettasec_glass1_refract` | `Refract` | `glass` | `map` | `0` | `-` |
| `coast/zettasec_glass2_refract` | `Refract` | `glass` | `map` | `0` | `-` |
| `coast/zsec1` | `LightmappedGeneric` | `-` | `map` | `0` | `coast/zsec1` |
| `coast/zsec1a` | `LightmappedGeneric` | `-` | `map` | `0` | `coast/zsec1` |
| `coast/zsec2` | `LightmappedGeneric` | `-` | `map` | `0` | `coast/zsec2` |
| `coast/zsec3` | `LightmappedGeneric` | `-` | `map` | `0` | `coast/zsec3` |
| `coast/zsecdoor` | `LightmappedGeneric` | `metal` | `map` | `0` | `coast/zsecdoor` |
| `coast/zsecgrunge` | `LightmappedGeneric` | `-` | `map` | `0` | `coast/zsecgrunge` |
| `coast/zsecgrunge1` | `LightmappedGeneric` | `-` | `map` | `0` | `coast/zsecgrunge1` |

### `concrete`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `concrete/concrete_floor01` | `LightmappedGeneric` | `concrete` | `map` | `1` | `concrete/concrete_floor01` |
| `concrete/concrete_floor01_cheap` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concrete_floor01` |
| `concrete/concrete_floor02` | `LightmappedGeneric` | `concrete` | `map` | `1` | `concrete/concrete_floor02` |
| `concrete/concrete_floor02_cheap` | `LightmappedGeneric` | `concrete` | `map` | `1` | `concrete/concrete_floor02` |
| `concrete/concrete_paintline_large` | `Unknown` | `-` | `map` | `0` | `-` |
| `concrete/concrete_paintline_medium` | `Unknown` | `-` | `map` | `0` | `-` |
| `concrete/concrete_paintline_small` | `Unknown` | `-` | `map` | `0` | `-` |
| `concrete/concretefloor_001a_t` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concretefloor_001a_t` |
| `concrete/concretefloor_001a_t_cheap` | `LightmappedGeneric` | `concrete` | `map` | `1` | `concrete/concretefloor_001a_t` |
| `concrete/concretefloor_001b_t` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concretefloor_001b_t` |
| `concrete/concretefloor_001b_t_cheap` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concretefloor_001b_t` |
| `concrete/concretefloor_001c_t` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concretefloor_001c_t` |
| `concrete/concretefloor_001c_t_cheap` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concretefloor_001c_t` |
| `concrete/concretefloor_001d_t` | `LightmappedGeneric` | `concrete` | `map` | `1` | `concrete/concretefloor_001d_t` |
| `concrete/concretefloor_002a_t` | `LightmappedGeneric` | `concrete` | `map` | `1` | `concrete/concretefloor_002a_t` |
| `concrete/concretefloor_002a_t_cheap` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concretefloor_002a_t` |
| `concrete/concretefloor_002b_t` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concretefloor_002b_t` |
| `concrete/concretefloor_002b_t_cheap` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concretefloor_002b_t` |
| `concrete/concretefloor_002c_t` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concretefloor_002c_t` |
| `concrete/concretefloor_002c_t_cheap` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concretefloor_002c_t` |
| `concrete/s_concrete3` | `LightmappedGeneric` | `concrete` | `map` | `1` | `-` |

### `console`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `console/background01` | `UnlitGeneric` | `-` | `map` | `0` | `console/background01` |
| `console/background01_widescreen` | `UnlitGeneric` | `-` | `map` | `0` | `console/background01_widescreen` |
| `console/background02` | `UnlitGeneric` | `-` | `map` | `0` | `console/background02` |
| `console/background02_widescreen` | `UnlitGeneric` | `-` | `map` | `0` | `console/background02` |
| `console/background03` | `UnlitGeneric` | `-` | `map` | `0` | `console/background03` |
| `console/background03_widescreen` | `UnlitGeneric` | `-` | `map` | `0` | `console/background03_widescreen` |
| `console/background04` | `UnlitGeneric` | `-` | `map` | `0` | `console/background04` |
| `console/background04_widescreen` | `UnlitGeneric` | `-` | `map` | `0` | `console/background04_widescreen` |
| `console/background05` | `UnlitGeneric` | `-` | `map` | `0` | `console/background05` |
| `console/background05_widescreen` | `UnlitGeneric` | `-` | `map` | `0` | `console/background05` |
| `console/background06` | `UnlitGeneric` | `-` | `map` | `0` | `console/background06` |
| `console/background06_widescreen` | `UnlitGeneric` | `-` | `map` | `0` | `console/background06_widescreen` |
| `console/dysbackground` | `UnlitGeneric` | `-` | `map` | `0` | `console/dysbackground` |
| `console/dysbackground_widescreen` | `UnlitGeneric` | `-` | `map` | `0` | `console/dysbackground_widescreen` |
| `console/startup_loading` | `UnlitGeneric` | `-` | `map` | `0` | `console/startup_loading` |

### `cyberfade`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `cyberfade` | `UnlitGeneric` | `-` | `map` | `0` | `_rt_CyberBuffer` |

### `cyberspace`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `cyberspace/cube256` | `UnlitGeneric` | `metal` | `map` | `13` | `cyberspace/cube256` |
| `cyberspace/cube256fil` | `UnlitGeneric` | `metal` | `map` | `5` | `cyberspace/cube256fil` |
| `cyberspace/cube256fil.tga` | `UnlitGeneric` | `metal` | `map` | `7` | `cyberspace/cube256fil` |
| `cyberspace/cube_blue` | `UnlitGeneric` | `metal` | `map` | `10` | `cyberspace/cube_blue` |
| `cyberspace/cube_blue_1` | `UnlitGeneric` | `metal` | `map` | `11` | `cyberspace/cube_blue_1` |
| `cyberspace/cube_blue_2` | `UnlitGeneric` | `metal` | `map` | `1` | `cyberspace/cube_blue_2` |
| `cyberspace/cube_blue_trans` | `UnlitGeneric` | `metal` | `map` | `11` | `cyberspace/cube_blue` |
| `cyberspace/cube_green` | `UnlitGeneric` | `metal` | `map` | `9` | `cyberspace/cube_green` |
| `cyberspace/cube_green_2` | `UnlitGeneric` | `metal` | `map` | `11` | `cyberspace/cube_green_2` |
| `cyberspace/cube_green_trans` | `UnlitGeneric` | `metal` | `map` | `4` | `cyberspace/cube_green` |
| `cyberspace/cube_orange` | `UnlitGeneric` | `metal` | `map` | `6` | `cyberspace/cube_orange` |
| `cyberspace/cube_orange_1` | `UnlitGeneric` | `metal` | `map` | `0` | `cyberspace/cube_orange_1` |
| `cyberspace/cube_orange_2` | `UnlitGeneric` | `metal` | `map` | `3` | `cyberspace/cube_orange_2` |
| `cyberspace/cube_orange_trans` | `UnlitGeneric` | `metal` | `map` | `4` | `cyberspace/cube_orange` |
| `cyberspace/cube_purple` | `UnlitGeneric` | `metal` | `map` | `8` | `cyberspace/cube_purple` |
| `cyberspace/cube_purple_1` | `UnlitGeneric` | `metal` | `map` | `0` | `cyberspace/cube_purple_1` |
| `cyberspace/cube_purple_2` | `UnlitGeneric` | `metal` | `map` | `3` | `cyberspace/cube_purple_2` |
| `cyberspace/cube_purple_trans` | `UnlitGeneric` | `metal` | `map` | `4` | `cyberspace/cube_purple` |
| `cyberspace/cube_red` | `UnlitGeneric` | `metal` | `map` | `10` | `cyberspace/cube_red` |
| `cyberspace/cube_red_1` | `UnlitGeneric` | `metal` | `map` | `2` | `cyberspace/cube_red` |
| `cyberspace/cube_red_trans` | `UnlitGeneric` | `metal` | `map` | `6` | `cyberspace/cube_red` |
| `cyberspace/cube_yellow` | `UnlitGeneric` | `metal` | `map` | `8` | `cyberspace/cube_yellow` |
| `cyberspace/cube_yellow_1` | `UnlitGeneric` | `metal` | `map` | `1` | `cyberspace/cube_yellow_1` |
| `cyberspace/cube_yellow_2` | `UnlitGeneric` | `metal` | `map` | `1` | `cyberspace/cube_yellow_2` |
| `cyberspace/cube_yellow_trans` | `UnlitGeneric` | `metal` | `map` | `6` | `cyberspace/cube_yellow` |
| `cyberspace/cyb_base` | `UnlitGeneric` | `-` | `map` | `12` | `cyberspace/cyb_base` |
| `cyberspace/cyb_no` | `UnlitGeneric` | `-` | `map` | `2` | `cyberspace/cyb_no` |
| `cyberspace/cyb_psy1` | `UnlitGeneric` | `metal` | `map` | `0` | `cyberspace/cyb_psy1` |
| `cyberspace/cyb_psy1_glowy` | `UnlitGeneric` | `metal` | `map` | `0` | `cyberspace/cyb_psy1` |
| `cyberspace/cyb_yes` | `UnlitGeneric` | `-` | `map` | `1` | `cyberspace/cyb_yes` |
| `cyberspace/cyber_floor_greyswirl` | `UnlitGeneric` | `-` | `map` | `1` | `cyberspace/cyber_floor_greyswirl` |
| `cyberspace/cyber_floor_greyswirlnocull` | `UnlitGeneric` | `-` | `map` | `0` | `cyberspace/cyber_floor_greyswirl` |
| `cyberspace/cyber_projectile_jump_sign` | `UnlitGeneric` | `glass` | `map` | `2` | `cyberspace/cyber_projectile_jump_sign` |
| `cyberspace/cyberfade` | `UnlitGeneric` | `-` | `map` | `4` | `cyberspace/cyberfade` |
| `cyberspace/frostwall` | `UnlitGeneric` | `metal` | `map` | `1` | `cyberspace/frostwall` |
| `cyberspace/infocoredefense` | `UnlitGeneric` | `-` | `map` | `0` | `cyberspace/infocoredefense` |
| `cyberspace/infocoreshield` | `UnlitGeneric` | `-` | `map` | `0` | `cyberspace/infocoreshield` |
| `cyberspace/infofoyerspawn` | `UnlitGeneric` | `-` | `map` | `0` | `cyberspace/infofoyerspawn` |
| `cyberspace/infol2spawn` | `UnlitGeneric` | `-` | `map` | `0` | `cyberspace/infol2spawn` |
| `cyberspace/packetblock3` | `UnlitGeneric` | `metal` | `map` | `0` | `cyberspace/packetblock3` |
| `cyberspace/ping_attack` | `Sprite` | `computer` | `map` | `0` | `cyberspace/ping_attack` |
| `cyberspace/scroller_gibberish` | `UnlitGeneric` | `metal` | `map` | `14` | `cyberspace/scroller_gibberish` |
| `cyberspace/scroller_yellow` | `UnlitGeneric` | `metal` | `map` | `1` | `cyberspace/scroller_yellow` |
| `cyberspace/sky_01` | `UnlitGeneric` | `metal` | `map` | `2` | `cyberspace/sky_01` |
| `cyberspace/sky_02` | `UnlitGeneric` | `metal` | `map` | `4` | `cyberspace/sky_02` |
| `cyberspace/t_arrowsweeper1b` | `UnlitTwoTexture` | `no_decal` | `map` | `2` | `cysp2/sweeper` |
| `cyberspace/t_arrowsweeper1r` | `UnlitTwoTexture` | `no_decal` | `map` | `1` | `twincannon/sweeper3new_red` |
| `cyberspace/t_arrowsweeper2b` | `UnlitTwoTexture` | `no_decal` | `map` | `0` | `twincannon/sweeper3new_blue` |
| `cyberspace/t_arrowsweeper2r` | `UnlitTwoTexture` | `no_decal` | `map` | `0` | `detonate/exo_cs_sweeper2` |
| `cyberspace/t_cyspwall1_black` | `UnlitGeneric` | `-` | `map` | `5` | `cyberspace/t_cyspwall1_black` |
| `cyberspace/t_cyspwall1_black_a` | `UnlitGeneric` | `-` | `map` | `3` | `cyberspace/t_cyspwall1_black` |
| `cyberspace/t_cyspwall1_blue` | `UnlitGeneric` | `-` | `map` | `3` | `cyberspace/t_cyspwall1_blue` |
| `cyberspace/t_cyspwall1_blue_a` | `UnlitGeneric` | `-` | `map` | `3` | `cyberspace/t_cyspwall1_blue` |
| `cyberspace/t_cyspwall1_green` | `UnlitGeneric` | `-` | `map` | `1` | `cyberspace/t_cyspwall1_green` |
| `cyberspace/t_cyspwall1_green_a` | `UnlitGeneric` | `-` | `map` | `3` | `cyberspace/t_cyspwall1_green` |
| `cyberspace/t_cyspwall1_orange` | `UnlitGeneric` | `-` | `map` | `2` | `cyberspace/t_cyspwall1_orange` |
| `cyberspace/t_cyspwall1_orange_a` | `UnlitGeneric` | `-` | `map` | `3` | `cyberspace/t_cyspwall1_orange` |
| `cyberspace/t_cyspwall1_red` | `UnlitGeneric` | `-` | `map` | `2` | `cyberspace/t_cyspwall1_red` |
| `cyberspace/t_cyspwall1_red_a` | `UnlitGeneric` | `-` | `map` | `4` | `cyberspace/t_cyspwall1_red` |
| `cyberspace/wall_blueglow` | `UnlitGeneric` | `-` | `map` | `1` | `cyberspace/wall_blueglow` |
| `cyberspace/wall_blueline` | `UnlitGeneric` | `-` | `map` | `0` | `cyberspace/wall_blueline` |
| `cyberspace/wall_detailglow` | `UnlitGeneric` | `-` | `map` | `1` | `cyberspace/wall_detailglow` |
| `cyberspace/wall_squard` | `UnlitGeneric` | `-` | `map` | `1` | `cyberspace/wall_squard` |
| `cyberspace/wall_squaregrey` | `UnlitGeneric` | `cybergravity` | `map` | `12` | `cyberspace/wall_squaregrey` |
| `cyberspace/wall_squaresolid` | `UnlitGeneric` | `cybergravity` | `map` | `13` | `cyberspace/wall_squaresolid` |

### `cyfloorplan`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `cyfloorplan/cysp_floor_horiz` | `UnlitGeneric` | `metal` | `map` | `5` | `cyfloorplan/cysp_floor_horiz` |
| `cyfloorplan/cysp_floor_n2e` | `UnlitGeneric` | `metal` | `map` | `0` | `cyfloorplan/cysp_floor_n2e` |
| `cyfloorplan/cysp_floor_n2w` | `UnlitGeneric` | `metal` | `map` | `4` | `cyfloorplan/cysp_floor_n2w` |
| `cyfloorplan/cysp_floor_vert` | `UnlitGeneric` | `metal` | `map` | `0` | `cyfloorplan/cysp_floor_vert` |
| `cyfloorplan/cysp_floor_x` | `UnlitGeneric` | `metal` | `map` | `4` | `cyfloorplan/cysp_floor_x` |
| `cyfloorplan/cysp_floor_y` | `UnlitGeneric` | `metal` | `map` | `4` | `cyfloorplan/cysp_floor_y` |
| `cyfloorplan/cysp_psytry_1` | `UnlitGeneric` | `metal` | `map` | `2` | `cyfloorplan/cysp_psytry_1` |
| `cyfloorplan/cysp_psytry_2` | `UnlitGeneric` | `metal` | `map` | `0` | `cyfloorplan/cysp_psytry_2` |

### `cysp2`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `cysp2/ARROW1.VMT` | `unlitgeneric` | `-` | `map` | `1` | `cysp2/ARROW1` |
| `cysp2/ARROW2.VMT` | `unlitgeneric` | `-` | `map` | `0` | `cysp2/ARROW2` |
| `cysp2/NODEDIRECT.VMT` | `unlitgeneric` | `-` | `map` | `1` | `cysp2/NODEDIRECT` |
| `cysp2/NODEDIRECT2.VMT` | `unlitgeneric` | `-` | `map` | `0` | `cysp2/NODEDIRECT2` |
| `cysp2/cyber_round` | `unlitgeneric` | `-` | `map` | `9` | `cysp2/cyber_round` |
| `cysp2/green_base` | `unlitgeneric` | `-` | `map` | `4` | `cysp2/green_base` |
| `cysp2/ice_black` | `UnlitGeneric` | `metal` | `map` | `0` | `cysp2/ice_black` |
| `cysp2/ice_blackrefract` | `Refract` | `-` | `map` | `0` | `-` |
| `cysp2/nodeinfo1` | `unlitgeneric` | `-` | `map` | `1` | `cysp2/nodeinfo1` |
| `cysp2/nodeinfo2` | `unlitgeneric` | `-` | `map` | `1` | `cysp2/nodeinfo2` |
| `cysp2/nodeinfo3` | `unlitgeneric` | `-` | `map` | `1` | `cysp2/nodeinfo3` |
| `cysp2/nodeinfo4` | `unlitgeneric` | `-` | `map` | `1` | `cysp2/nodeinfo4` |
| `cysp2/orange_base` | `unlitgeneric` | `-` | `map` | `2` | `cysp2/orange_base` |
| `cysp2/red_base` | `unlitgeneric` | `-` | `map` | `5` | `cysp2/red_base` |
| `cysp2/round_bluew` | `unlitgeneric` | `-` | `map` | `2` | `cysp2/round_bluew` |
| `cysp2/round_bluew2` | `unlitgeneric` | `-` | `map` | `3` | `cysp2/round_bluew2` |
| `cysp2/sweeper` | `unlitgeneric` | `-` | `map` | `8` | `cysp2/sweeper` |
| `cysp2/sweeper2` | `unlitgeneric` | `-` | `map` | `9` | `cysp2/sweeper2` |
| `cysp2/sweeper3` | `unlitgeneric` | `-` | `map` | `7` | `cysp2/sweeper3` |
| `cysp2/sweeper4` | `unlitgeneric` | `-` | `map` | `0` | `cysp2/sweeper4` |

### `cyspfinal`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `cyspfinal/bitstream1a` | `UnlitGeneric` | `metal` | `map` | `6` | `cyspfinal/bitstream1a` |
| `cyspfinal/bitstream2a` | `UnlitGeneric` | `metal` | `map` | `0` | `cyspfinal/bitstream2a` |
| `cyspfinal/bitstream2a_solid` | `UnlitGeneric` | `metal` | `map` | `1` | `cyspfinal/bitstream2a` |
| `cyspfinal/circlet1` | `UnlitGeneric` | `-` | `map` | `9` | `cyspfinal/circlet1` |
| `cyspfinal/circlet2` | `UnlitGeneric` | `-` | `map` | `9` | `cyspfinal/circlet2` |
| `cyspfinal/circlet3` | `UnlitGeneric` | `-` | `map` | `11` | `cyspfinal/circlet3` |
| `cyspfinal/circlet4` | `UnlitGeneric` | `-` | `map` | `6` | `cyspfinal/circlet4` |
| `cyspfinal/circlet_green` | `UnlitGeneric` | `-` | `map` | `1` | `cyspfinal/circlet_green` |
| `cyspfinal/dys_hack01` | `UnlitGeneric` | `-` | `map` | `8` | `cyspfinal/dys_hack01` |
| `cyspfinal/dys_path01` | `UnlitGeneric` | `-` | `map` | `7` | `cyspfinal/dys_path01` |
| `cyspfinal/dys_path01_a` | `UnlitGeneric` | `-` | `map` | `1` | `cyspfinal/dys_path01` |
| `cyspfinal/dys_path02` | `UnlitGeneric` | `-` | `map` | `3` | `cyspfinal/dys_path02` |
| `cyspfinal/dys_path02_a` | `UnlitGeneric` | `-` | `map` | `2` | `cyspfinal/dys_path02` |
| `cyspfinal/dys_pathbg` | `UnlitGeneric` | `glass` | `map` | `4` | `cyspfinal/dys_pathbg` |
| `cyspfinal/dys_pathbg_a` | `UnlitGeneric` | `glass` | `map` | `8` | `cyspfinal/dys_pathbg` |
| `cyspfinal/dys_pathcorrupted01_a` | `UnlitGeneric` | `-` | `map` | `0` | `cyspfinal/dys_pathcorrupted01` |
| `cyspfinal/dys_pathcorrupted02` | `UnlitGeneric` | `-` | `map` | `2` | `cyspfinal/dys_pathcorrupted02` |
| `cyspfinal/dys_pathcorrupted02a` | `UnlitGeneric` | `-` | `map` | `1` | `cyspfinal/dys_pathcorrupted02` |
| `cyspfinal/dys_screen_feedback` | `UnlitGeneric` | `-` | `map` | `1` | `cyspfinal/dys_screen_feedback` |

### `decals`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `decals/decalborealispuddle001a` | `vertexlitgeneric` | `-` | `decal` | `0` | `Decals/decalborealispuddlemask001a` |
| `decals/decalsdecalstain006a` | `vertexlitgeneric` | `-` | `decal` | `0` | `Decals/decalborealispuddlemask001a` |
| `decals/plasmaglowfade` | `UnlitGeneric` | `-` | `decal` | `0` | `decals/plasmaglowalpha` |
| `decals/redglowfade` | `UnlitGeneric` | `-` | `decal` | `0` | `decals/redglowalpha` |
| `decals/redglowfademodel` | `VertexLitGeneric` | `-` | `decal` | `0` | `decals/redglowalpha` |
| `decals/rollermine_crater` | `vertexlitgeneric` | `-` | `decal` | `0` | `Decals/legbooster_blast` |
| `decals/rollermine_crater_subrect` | `vertexlitgeneric` | `-` | `decal` | `0` | `Decals/legbooster_blast` |
| `decals/sign_arrow_grunge` | `LightmappedGeneric` | `-` | `decal` | `0` | `decals/sign_arrow_grunge` |
| `decals/sign_arrow_tech` | `LightmappedGeneric` | `-` | `decal` | `0` | `decals/sign_arrow_tech` |
| `decals/sign_arrow_tech_corner` | `LightmappedGeneric` | `-` | `decal` | `0` | `decals/sign_arrow_tech_corner` |
| `decals/sign_objective_grunge` | `LightmappedGeneric` | `-` | `decal` | `0` | `decals/sign_objective_grunge` |
| `decals/sign_objective_tech` | `LightmappedGeneric` | `-` | `decal` | `0` | `decals/sign_objective_tech` |
| `decals/sign_sorehead` | `LightmappedGeneric` | `-` | `decal` | `0` | `decals/sign_sorehead` |
| `decals/spraypaint_sign_arrow_down` | `LightmappedGeneric` | `-` | `decal` | `0` | `decals/spraypaint_sign_arrow_down` |
| `decals/spraypaint_sign_arrow_left` | `LightmappedGeneric` | `-` | `decal` | `0` | `decals/spraypaint_sign_arrow_left` |
| `decals/spraypaint_sign_arrow_right` | `LightmappedGeneric` | `-` | `decal` | `0` | `decals/spraypaint_sign_arrow_right` |
| `decals/spraypaint_sign_exo1` | `LightmappedGeneric` | `-` | `decal` | `0` | `decals/spraypaint_sign_exo1` |
| `decals/spraypaint_sign_exo2` | `LightmappedGeneric` | `-` | `decal` | `0` | `decals/spraypaint_sign_exo2` |
| `decals/teslaglow` | `UnlitGeneric` | `-` | `decal` | `0` | `decals/smscorch3` |

### `detail`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `detail/detailsprites` | `UnlitGeneric` | `-` | `map` | `0` | `detail/detailsprites` |

### `detonate`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `detonate/billboard1` | `LightmappedGeneric` | `-` | `map` | `0` | `detonate/billboard1` |
| `detonate/billboard2` | `LightmappedGeneric` | `-` | `map` | `1` | `detonate/billboard2` |
| `detonate/billboard3` | `LightmappedGeneric` | `-` | `map` | `0` | `detonate/billboard3` |
| `detonate/billboard4` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `detonate/billboard5` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `detonate/billboard6` | `LightmappedGeneric` | `-` | `map` | `2` | `-` |
| `detonate/billboard7` | `LightmappedGeneric` | `-` | `map` | `0` | `-` |
| `detonate/billboard8` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `detonate/billboard_aciddrinks_3_grunge` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `detonate/billboardback` | `LightmappedGeneric` | `-` | `map` | `2` | `-` |
| `detonate/cube256` | `UnlitGeneric` | `metal` | `map` | `0` | `detonate/cube256` |
| `detonate/cube256b` | `UnlitGeneric` | `metal` | `map` | `2` | `detonate/cube256b` |
| `detonate/det_rustcrate` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rustcrate` |
| `detonate/det_rustfiller` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rustfiller` |
| `detonate/det_rustfloorbase` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rustfloorbase` |
| `detonate/det_rustfloorbase_grate` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rustfloorbase_grate` |
| `detonate/det_rustfloorbase_grate_dx8` | `LightmappedGeneric` | `metal` | `map` | `0` | `detonate/det_rustfloorbase_grate` |
| `detonate/det_rustfloordetail` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rustfloordetail` |
| `detonate/det_rustfloortile` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rustfloortile` |
| `detonate/det_rustmetalstair` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rustmetalstair` |
| `detonate/det_rustplate` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rustplate` |
| `detonate/det_rustshackdoor` | `LightmappedGeneric` | `metal` | `map` | `2` | `detonate/det_rustshackdoor` |
| `detonate/det_rusttechsupport` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rusttechsupport` |
| `detonate/det_rusttrim` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rusttrim` |
| `detonate/det_rusttrim2` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rusttrim2` |
| `detonate/det_rusttrim3` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rusttrim3` |
| `detonate/det_rustwalldetail` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/det_rustwalldetail` |
| `detonate/det_rustwindowtrim` | `LightmappedGeneric` | `metal` | `map` | `0` | `detonate/det_rustwindowtrim` |
| `detonate/detbrickwall01` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `detonate/detbrickwall02` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `detonate/detbrickwall03` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `detonate/detcretewall01` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `detonate/detcretewall02` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `detonate/detcretewall03` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `detonate/detcretewall04` | `LightmappedGeneric` | `-` | `map` | `0` | `-` |
| `detonate/detcretewall05` | `LightmappedGeneric` | `-` | `map` | `0` | `-` |
| `detonate/detmetaldoorauthaccess` | `LightmappedGeneric` | `metal` | `map` | `0` | `detonate/detmetaldoorauthaccess` |
| `detonate/detrollerdoor01` | `LightmappedGeneric` | `-` | `map` | `2` | `-` |
| `detonate/detrollerdoor02` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/detrollerdoor02` |
| `detonate/detrollerdoor03` | `LightmappedGeneric` | `metal` | `map` | `0` | `detonate/detrollerdoor03` |
| `detonate/detrollerdoor04` | `LightmappedGeneric` | `metal` | `map` | `0` | `detonate/detrollerdoor04` |
| `detonate/detrustwall1` | `LightmappedGeneric` | `metal` | `map` | `2` | `detonate/detrustwall1` |
| `detonate/detrustwall2` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/detrustwall2` |
| `detonate/detspawncorps` | `LightmappedGeneric` | `-` | `map` | `1` | `detonate/detspawncorps` |
| `detonate/detspawnpunk` | `LightmappedGeneric` | `-` | `map` | `1` | `detonate/detspawnpunk` |
| `detonate/exo_black` | `LightmappedGeneric` | `-` | `map` | `0` | `detonate/exo_black` |
| `detonate/exo_black2` | `LightmappedGeneric` | `-` | `map` | `0` | `detonate/exo_black2` |
| `detonate/exo_cs_blue1` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_blue1` |
| `detonate/exo_cs_blue2` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_blue2` |
| `detonate/exo_cs_blue3` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_blue3` |
| `detonate/exo_cs_gray2` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_gray2` |
| `detonate/exo_cs_green1` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_green1` |
| `detonate/exo_cs_green2` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_green2` |
| `detonate/exo_cs_green3` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_green3` |
| `detonate/exo_cs_green4` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_green4` |
| `detonate/exo_cs_green5` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_green5` |
| `detonate/exo_cs_red1` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_red1` |
| `detonate/exo_cs_red2` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_red2` |
| `detonate/exo_cs_red3` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_red3` |
| `detonate/exo_cs_red4` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_red4` |
| `detonate/exo_cs_sweeper` | `unlitgeneric` | `-` | `map` | `2` | `detonate/exo_cs_sweeper` |
| `detonate/exo_cs_sweeper2` | `unlitgeneric` | `-` | `map` | `0` | `detonate/exo_cs_sweeper2` |
| `detonate/exo_cs_white2` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_white2` |
| `detonate/exo_cs_yellow1` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_yellow1` |
| `detonate/exo_cs_yellow2` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_cs_yellow2` |
| `detonate/exo_diner` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_diner` |
| `detonate/exo_dirtrockblend` | `WorldVertexTransition` | `-` | `map` | `0` | `nature/dirtfloor013a` |
| `detonate/exo_ghettowall1` | `LightmappedGeneric` | `concrete` | `map` | `1` | `detonate/exo_ghettowall1` |
| `detonate/exo_ghettowall2` | `LightmappedGeneric` | `concrete` | `map` | `1` | `detonate/exo_ghettowall2` |
| `detonate/exo_ghettowall3` | `LightmappedGeneric` | `concrete` | `map` | `1` | `detonate/exo_ghettowall3` |
| `detonate/exo_ghettowall4` | `LightmappedGeneric` | `concrete` | `map` | `1` | `detonate/exo_ghettowall4` |
| `detonate/exo_metalfiller` | `LightmappedGeneric` | `metal` | `map` | `2` | `detonate/exo_metalfiller` |
| `detonate/exo_metaltrim1` | `LightmappedGeneric` | `metal` | `map` | `2` | `detonate/exo_metaltrim1` |
| `detonate/exo_metaltrim2` | `LightmappedGeneric` | `metal` | `map` | `3` | `detonate/exo_metaltrim2` |
| `detonate/exo_metaltrim3` | `LightmappedGeneric` | `metal` | `map` | `3` | `detonate/exo_metaltrim3` |
| `detonate/exo_metaltrim4` | `LightmappedGeneric` | `metal` | `map` | `3` | `detonate/exo_metaltrim4` |
| `detonate/exo_metalwall1` | `LightmappedGeneric` | `metal` | `map` | `1` | `detonate/exo_metalwall1` |
| `detonate/exo_metalwall2` | `LightmappedGeneric` | `metal` | `map` | `2` | `detonate/exo_metalwall2` |
| `detonate/exo_plaster` | `LightmappedGeneric` | `concrete` | `map` | `0` | `detonate/exo_plaster` |
| `detonate/exo_pubjip` | `UnlitGeneric` | `-` | `map` | `0` | `detonate/exo_pubjip` |
| `detonate/exo_pubjip2` | `UnlitGeneric` | `-` | `map` | `0` | `detonate/exo_pubjip2` |
| `detonate/exo_pubjipneon` | `UnlitGeneric` | `-` | `map` | `0` | `detonate/exo_pubjipneon` |
| `detonate/exo_pubjipneon2` | `UnlitGeneric` | `-` | `map` | `0` | `detonate/exo_pubjipneon2` |
| `detonate/exo_secorp` | `UnlitGeneric` | `-` | `map` | `0` | `detonate/exo_secorp` |
| `detonate/exo_stattrim` | `LightmappedGeneric` | `concrete` | `map` | `1` | `detonate/exo_stattrim` |
| `detonate/exo_statwall` | `LightmappedGeneric` | `concrete` | `map` | `1` | `detonate/exo_statwall` |
| `detonate/exo_statwall2` | `LightmappedGeneric` | `concrete` | `map` | `1` | `detonate/exo_statwall2` |
| `detonate/exo_window` | `LightmappedGeneric` | `glass` | `map` | `2` | `detonate/exo_window` |
| `detonate/exo_window_trans` | `LightmappedGeneric` | `glass` | `map` | `1` | `detonate/exo_window_trans` |
| `detonate/exo_xxx` | `UnlitGeneric` | `-` | `map` | `1` | `detonate/exo_xxx` |
| `detonate/exo_yellowhat` | `UnlitGeneric` | `-` | `map` | `0` | `detonate/exo_yellowhat` |
| `detonate/exo_yellowhat2` | `UnlitGeneric` | `-` | `map` | `0` | `detonate/exo_yellowhat2` |
| `detonate/neonclubx14` | `LightmappedGeneric` | `-` | `map` | `0` | `-` |
| `detonate/neoncpunk` | `LightmappedGeneric` | `-` | `map` | `0` | `-` |
| `detonate/neondelta` | `LightmappedGeneric` | `-` | `map` | `0` | `-` |
| `detonate/neonevolution` | `LightmappedGeneric` | `-` | `map` | `0` | `-` |
| `detonate/neonfps` | `LightmappedGeneric` | `-` | `map` | `0` | `-` |
| `detonate/neongoo` | `LightmappedGeneric` | `-` | `map` | `0` | `-` |

### `dev`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dev/dev_measuredoor01_silver` | `LightmappedGeneric` | `concrete` | `map` | `1` | `Dev/dev_measuredoor01_silver` |
| `dev/dev_measuredoor_blue` | `LightmappedGeneric` | `concrete` | `map` | `1` | `Dev/dev_measuredoor_blue` |
| `dev/dev_measuredoor_red` | `LightmappedGeneric` | `concrete` | `map` | `1` | `Dev/dev_measuredoor_red` |
| `dev/dev_measuregeneric_tan` | `LightmappedGeneric` | `concrete` | `map` | `1` | `Dev/dev_measuregeneric_tan` |
| `dev/dev_measurewall01_brown` | `LightmappedGeneric` | `concrete` | `map` | `1` | `Dev/dev_measurewall01_brown` |
| `dev/dev_measurewall01_green` | `LightmappedGeneric` | `concrete` | `map` | `1` | `Dev/dev_measurewall01_green` |

### `dtrustscreen`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dtrustscreen/Copy of screenbaseover` | `UnlitGeneric` | `-` | `map` | `0` | `dtrustscreen/screenbaseover` |
| `dtrustscreen/HSCUa_overlay` | `UnlitGeneric` | `glass` | `overlay` | `1` | `dtrustscreen/HCSUa_overlay` |
| `dtrustscreen/HSCUb_overlay` | `UnlitGeneric` | `glass` | `overlay` | `1` | `dtrustscreen/HCSUb_overlay` |
| `dtrustscreen/alyxmonitor_idle` | `UnlitTwoTexture` | `-` | `map` | `0` | `effects/alyxmonitor_idle` |
| `dtrustscreen/alyxmonitor_talk` | `UnlitTwoTexture` | `-` | `map` | `0` | `effects/alyxmonitor_talk` |
| `dtrustscreen/bg1` | `UnlitGeneric` | `-` | `map` | `0` | `dtrustscreen/bg1` |
| `dtrustscreen/dtrustbust` | `UnlitTwoTexture` | `-` | `map` | `3` | `dtrustscreen/dtrustbust` |
| `dtrustscreen/dtrustscreen1` | `UnlitGeneric` | `-` | `map` | `0` | `dtrustscreen/dtrustscreen1` |
| `dtrustscreen/dtrustspin` | `LightMappedGeneric` | `-` | `map` | `0` | `dtrustscreen/screenbaseover` |
| `dtrustscreen/dtrustspin2` | `UnlitTwoTexture` | `-` | `map` | `5` | `dtrustscreen/dtrustspin` |
| `dtrustscreen/noise1` | `UnlitTwoTexture` | `-` | `map` | `5` | `dtrustscreen/noise1` |
| `dtrustscreen/overlay_blank` | `UnlitGeneric` | `glass` | `overlay` | `3` | `dtrustscreen/overlay_blank` |
| `dtrustscreen/overlay_corps` | `UnlitGeneric` | `glass` | `overlay` | `3` | `dtrustscreen/overlay_corps` |
| `dtrustscreen/overlay_denied` | `UnlitGeneric` | `glass` | `overlay` | `3` | `dtrustscreen/overlay_denied` |
| `dtrustscreen/overlay_gen` | `UnlitGeneric` | `glass` | `overlay` | `4` | `dtrustscreen/overlay_gen` |
| `dtrustscreen/overlay_inprog` | `UnlitGeneric` | `glass` | `overlay` | `0` | `dtrustscreen/overlay_inprog` |
| `dtrustscreen/overlay_offline` | `UnlitGeneric` | `glass` | `overlay` | `3` | `dtrustscreen/overlay_offline` |
| `dtrustscreen/overlay_spawna` | `UnlitGeneric` | `glass` | `overlay` | `1` | `dtrustscreen/overlay_spawna` |
| `dtrustscreen/overlay_spawnb` | `UnlitGeneric` | `glass` | `overlay` | `1` | `dtrustscreen/overlay_spawnb` |
| `dtrustscreen/screenbaseover` | `UnlitGeneric` | `glass` | `map` | `0` | `dtrustscreen/screenbaseover` |

### `dys_blur`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_blur` | `dys_blur` | `-` | `map` | `0` | `-` |

### `dys_bwmonitor1a`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_bwmonitor1a` | `MonitorScreen` | `glass` | `map` | `0` | `_rt_camera1` |

### `dys_bwmonitor2a`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_bwmonitor2a` | `MonitorScreen` | `glass` | `map` | `0` | `_rt_camera2` |

### `dys_bwmonitor3a`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_bwmonitor3a` | `MonitorScreen` | `glass` | `map` | `0` | `_rt_camera3` |

### `dys_bwmonitor4a`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_bwmonitor4a` | `MonitorScreen` | `glass` | `map` | `0` | `_rt_camera4` |

### `dys_cyber_bloom`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_cyber_bloom` | `dys_cyber_bloom` | `-` | `map` | `0` | `-` |

### `dys_cyber_blurfilter_x`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_cyber_blurfilter_x` | `dys_cyber_blurfilter_x` | `-` | `map` | `0` | `-` |

### `dys_cyber_blurfilter_y`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_cyber_blurfilter_y` | `dys_cyber_blurfilter_y` | `-` | `map` | `0` | `-` |

### `dys_cyber_downsample`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_cyber_downsample` | `dys_cyber_downsample` | `-` | `map` | `0` | `-` |

### `dys_cybernetic`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_cybernetic/CS_BG_001` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/CS_BG_001` |
| `dys_cybernetic/Cross_girders` | `LightmappedGeneric` | `SolidMetal` | `map` | `0` | `dys_cybernetic/Cross_girders` |
| `dys_cybernetic/Light_trim` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/Light_trim` |
| `dys_cybernetic/access_display` | `UnlitGeneric` | `Glass` | `map` | `1` | `dys_cybernetic/access_display` |
| `dys_cybernetic/active_panal` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/active_panal` |
| `dys_cybernetic/bit_stream` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/bit_stream` |
| `dys_cybernetic/black_panal` | `LightmappedGeneric` | `-` | `map` | `1` | `dys_cybernetic/black_panal` |
| `dys_cybernetic/building_archology` | `VertexlitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/building_archology` |
| `dys_cybernetic/building_windows` | `LightmappedGeneric` | `-` | `map` | `1` | `dys_cybernetic/building_windows` |
| `dys_cybernetic/bushing` | `VertexLitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/bushing` |
| `dys_cybernetic/button_shield` | `UnlitGeneric` | `-` | `map` | `2` | `dys_cybernetic/button_shield` |
| `dys_cybernetic/caution_stripe` | `LightmappedGeneric` | `-` | `map` | `0` | `dys_cybernetic/caution_stripe` |
| `dys_cybernetic/ceiling_001` | `LightmappedGeneric` | `Metal` | `map` | `2` | `dys_cybernetic/ceiling_001` |
| `dys_cybernetic/ceiling_002` | `LightmappedGeneric` | `Metal` | `map` | `2` | `dys_cybernetic/ceiling_002` |
| `dys_cybernetic/ceiling_lights` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/ceiling_lights` |
| `dys_cybernetic/chem_processor_diff` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/chem_processor_diff` |
| `dys_cybernetic/computer_console` | `UnlitGeneric` | `glass` | `map` | `0` | `dys_cybernetic/computer_console` |
| `dys_cybernetic/computer_console_dark` | `UnlitGeneric` | `glass` | `map` | `0` | `dys_cybernetic/computer_console_dark` |
| `dys_cybernetic/concrete_pad` | `LightmappedGeneric` | `Concrete` | `map` | `1` | `dys_cybernetic/concrete_pad` |
| `dys_cybernetic/concrete_trim_001` | `LightmappedGeneric` | `Concrete` | `map` | `1` | `dys_cybernetic/concrete_trim_001` |
| `dys_cybernetic/concrete_wall_001` | `LightmappedGeneric` | `Concrete` | `map` | `0` | `dys_cybernetic/concrete_wall_001` |
| `dys_cybernetic/conduit_pipes` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/conduit_pipes` |
| `dys_cybernetic/console_keyboard` | `UnlitGeneric` | `glass` | `map` | `0` | `dys_cybernetic/console_keyboard` |
| `dys_cybernetic/conveyor_01` | `LightmappedGeneric` | `metal` | `map` | `2` | `dys_cybernetic/conveyor_01` |
| `dys_cybernetic/conveyor_01_100speed` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/conveyor_01` |
| `dys_cybernetic/conveyor_01_200speed` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/conveyor_01` |
| `dys_cybernetic/conveyor_01_400speed` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/conveyor_01` |
| `dys_cybernetic/crate_cybersyn_plain` | `VertexlitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/crate_cybersyn_plain` |
| `dys_cybernetic/cs_cubemap_blue` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cs_cubemap` |
| `dys_cybernetic/cs_cubemap_orange` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cs_cubemap` |
| `dys_cybernetic/cs_cubemap_red` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cs_cubemap` |
| `dys_cybernetic/cs_cubemap_tort` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cs_cubemap` |
| `dys_cybernetic/cs_tracer_001` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cs_tracer_001` |
| `dys_cybernetic/cyber_anitest` | `UnlitTwoTexture` | `-` | `map` | `0` | `dys_cybernetic/cyber_base_red` |
| `dys_cybernetic/cyber_base` | `UnlitGeneric` | `-` | `map` | `2` | `dys_cybernetic/cyber_base` |
| `dys_cybernetic/cyber_base_001` | `VertexLitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cyber_base_001` |
| `dys_cybernetic/cyber_base_blue` | `UnlitGeneric` | `-` | `map` | `2` | `dys_cybernetic/cyber_base_blue` |
| `dys_cybernetic/cyber_base_blue_trans` | `UnlitGeneric` | `-` | `map` | `3` | `dys_cybernetic/cyber_base_blue` |
| `dys_cybernetic/cyber_base_green` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cyber_base_green` |
| `dys_cybernetic/cyber_base_green_trans` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cyber_base_green` |
| `dys_cybernetic/cyber_base_orange` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_orange` |
| `dys_cybernetic/cyber_base_orange_trans` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_orange` |
| `dys_cybernetic/cyber_base_purple` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_purple` |
| `dys_cybernetic/cyber_base_purple_trans` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_purple` |
| `dys_cybernetic/cyber_base_red` | `UnlitGeneric` | `-` | `map` | `2` | `dys_cybernetic/cyber_base_red` |
| `dys_cybernetic/cyber_base_red_trans` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cyber_base_red` |
| `dys_cybernetic/cyber_base_tinted_blue` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base` |
| `dys_cybernetic/cyber_base_tinted_blue_bright` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_001` |
| `dys_cybernetic/cyber_base_tinted_blue_dull` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_001` |
| `dys_cybernetic/cyber_base_tinted_purple` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_001` |
| `dys_cybernetic/cyber_base_tinted_red` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base` |
| `dys_cybernetic/cyber_base_tinted_red_bright` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_001` |
| `dys_cybernetic/cyber_base_tinted_red_dull` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_001` |
| `dys_cybernetic/cyber_base_tinted_yellow_bright` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_001` |
| `dys_cybernetic/cyber_base_tort` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cyber_base_001` |
| `dys_cybernetic/cyber_base_tort_trans` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_turquoise` |
| `dys_cybernetic/cyber_base_trans` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base` |
| `dys_cybernetic/cyber_base_turquoise` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_turquoise` |
| `dys_cybernetic/cyber_base_turquoise_trans` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_base_turquoise` |
| `dys_cybernetic/cyber_base_yellow` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cyber_base_yellow` |
| `dys_cybernetic/cyber_base_yellow_trans` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cyber_base_yellow` |
| `dys_cybernetic/cyber_cube` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_cube` |
| `dys_cybernetic/cyber_cube_white` | `UnlitGeneric` | `-` | `map` | `2` | `dys_cybernetic/cyber_cube_white` |
| `dys_cybernetic/cyber_firewall_shield` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_firewall_shield` |
| `dys_cybernetic/cyber_flat_red` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cyber_flat_red` |
| `dys_cybernetic/cyber_flat_red_trans` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cyber_flat_red` |
| `dys_cybernetic/cyber_floor_ring` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_floor_ring` |
| `dys_cybernetic/cyber_floor_ring_ani` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_floor_ring_ani` |
| `dys_cybernetic/cyber_floor_ring_turquoise` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_floor_ring_turquoise` |
| `dys_cybernetic/cyber_floor_ring_turquoise_trans` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_floor_ring_turquoise` |
| `dys_cybernetic/cyber_glow_001` | `LightmappedGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_glow_001` |
| `dys_cybernetic/cyber_red_x` | `UnlitGeneric` | `Default` | `map` | `1` | `dys_cybernetic/cyber_red_x` |
| `dys_cybernetic/cyber_ring` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_ring` |
| `dys_cybernetic/cyber_sky` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cyber_sky` |
| `dys_cybernetic/cyber_turquoise_001` | `VertexLitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cyber_turquoise_001` |
| `dys_cybernetic/cyber_turret` | `VertexlitGeneric` | `Glass` | `map` | `0` | `dys_cybernetic/cyber_turret` |
| `dys_cybernetic/cybersyn_core_ani` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/cybersyn_core_ani` |
| `dys_cybernetic/cybersyn_logo` | `UnlitGeneric` | `Glass` | `map` | `1` | `dys_cybernetic/cybersyn_logo` |
| `dys_cybernetic/cybersyn_logo_blur` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/cybersyn_logo_blur` |
| `dys_cybernetic/cybersyn_screen1` | `UnlitGeneric` | `Glass` | `map` | `0` | `dys_cybernetic/cybersyn_screen1` |
| `dys_cybernetic/cybersyn_screen_large` | `UnlitGeneric` | `Glass` | `map` | `0` | `dys_cybernetic/cybersyn_screen_large` |
| `dys_cybernetic/cybersyn_screen_large2` | `UnlitGeneric` | `Glass` | `map` | `0` | `dys_cybernetic/cybersyn_screen_large2` |
| `dys_cybernetic/cybersyn_screen_opaq` | `UnlitGeneric` | `Glass` | `map` | `1` | `dys_cybernetic/cybersyn_screen1` |
| `dys_cybernetic/cybertech_dif` | `VertexLitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/cybertech_dif` |
| `dys_cybernetic/cynet_cs1` | `LightmappedGeneric` | `-` | `map` | `0` | `dys_cybernetic/cynet_cs1` |
| `dys_cybernetic/dark_building_windows` | `LightmappedGeneric` | `-` | `map` | `2` | `dys_cybernetic/dark_building_windows` |
| `dys_cybernetic/database_overlay` | `UnlitGeneric` | `Grass` | `overlay` | `0` | `dys_cybernetic/database_overlay` |
| `dys_cybernetic/database_overlay_ani` | `UnlitGeneric` | `-` | `overlay` | `0` | `dys_cybernetic/database_overlay_ani` |
| `dys_cybernetic/decal_chem_pro` | `LightmappedGeneric` | `-` | `decal` | `0` | `dys_cybernetic/decal_chem_pro` |
| `dys_cybernetic/decal_fusion` | `LightmappedGeneric` | `-` | `decal` | `0` | `dys_cybernetic/decal_fusion` |
| `dys_cybernetic/decal_level_1` | `LightmappedGeneric` | `-` | `decal` | `0` | `dys_cybernetic/decal_level_1` |
| `dys_cybernetic/decal_level_2` | `LightmappedGeneric` | `-` | `decal` | `0` | `dys_cybernetic/decal_level_2` |
| `dys_cybernetic/decal_level_3` | `LightmappedGeneric` | `-` | `decal` | `0` | `dys_cybernetic/decal_level_3` |
| `dys_cybernetic/decal_logo` | `LightmappedGeneric` | `-` | `decal` | `0` | `dys_cybernetic/decal_logo` |
| `dys_cybernetic/decal_logo2` | `LightmappedGeneric` | `-` | `decal` | `0` | `dys_cybernetic/decal_logo` |
| `dys_cybernetic/door_large_002` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/door_large_002` |
| `dys_cybernetic/double_door` | `LightmappedGeneric` | `-` | `map` | `1` | `dys_cybernetic/double_door` |
| `dys_cybernetic/double_doors_003` | `LightmappedGeneric` | `Default` | `map` | `1` | `dys_cybernetic/double_doors_003` |
| `dys_cybernetic/double_doors_004` | `LightmappedGeneric` | `Metal` | `map` | `2` | `dys_cybernetic/double_doors_004` |
| `dys_cybernetic/dys_cybernetic1` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/dys_cybernetic1` |
| `dys_cybernetic/dys_cybernetic2` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/dys_cybernetic2` |
| `dys_cybernetic/dys_cybernetic3` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/dys_cybernetic3` |
| `dys_cybernetic/dys_cybernetic4` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/dys_cybernetic4` |
| `dys_cybernetic/floor_black_glossy` | `LightmappedGeneric` | `Default` | `map` | `2` | `dys_cybernetic/floor_black_glossy` |
| `dys_cybernetic/floor_lab_001` | `LightmappedGeneric` | `Porcelain` | `map` | `0` | `dys_cybernetic/floor_lab_001` |
| `dys_cybernetic/floor_lab_003` | `LightmappedGeneric` | `Default` | `map` | `2` | `dys_cybernetic/floor_lab_003` |
| `dys_cybernetic/floor_lab_004` | `LightmappedGeneric` | `Tile` | `map` | `1` | `dys_cybernetic/floor_lab_004` |
| `dys_cybernetic/floor_lab_glow` | `LightmappedGeneric` | `-` | `map` | `0` | `dys_cybernetic/floor_lab_glow` |
| `dys_cybernetic/glass_cyber` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_cybernetic/glass_cyber` |
| `dys_cybernetic/glass_cyber_logo` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_cybernetic/glass_cyber_logo` |
| `dys_cybernetic/glass_cyber_stripe_end` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_cybernetic/glass_cyber_stripe_end` |
| `dys_cybernetic/glass_cyber_stripes` | `UnlitGeneric` | `glass` | `map` | `2` | `dys_cybernetic/glass_cyber_stripes` |
| `dys_cybernetic/glow_white_fade` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/glow_white_fade` |
| `dys_cybernetic/grav_lift_001` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/grav_lift_magnets` |
| `dys_cybernetic/grav_lift_1` | `LightmappedGeneric` | `Metal` | `map` | `2` | `dys_cybernetic/grav_lift_1` |
| `dys_cybernetic/grav_lift_lights` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/grav_lift_lights` |
| `dys_cybernetic/grav_lift_magnets` | `LightmappedGeneric` | `Metal` | `map` | `2` | `dys_cybernetic/grav_lift_magnets` |
| `dys_cybernetic/handrails1` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/handrails1` |
| `dys_cybernetic/icon_cyberdeck` | `UnlitGeneric` | `-` | `map` | `1` | `vgui/implants/corp_icon_cyberdeck` |
| `dys_cybernetic/lab_panala` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/lab_panala` |
| `dys_cybernetic/lift_panal` | `UnlitGeneric` | `-` | `map` | `2` | `dys_cybernetic/lift_panal` |
| `dys_cybernetic/light_glow_long` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/light_glow_long` |
| `dys_cybernetic/liquid_tank_diff` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/liquid_tank_diff` |
| `dys_cybernetic/logo_cybersyn2_ani` | `UnlitTwoTexture` | `-` | `map` | `0` | `dys_cybernetic/logo_cybersyn_ani` |
| `dys_cybernetic/logo_cybersyn2a_ani` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/logo_cybersyn_ani` |
| `dys_cybernetic/logo_cybersyn_ani` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/logo_cybersyn_ani` |
| `dys_cybernetic/metal_dark_indoors` | `LightmappedGeneric` | `metal` | `map` | `3` | `dys_cybernetic/metal_dark_indoors` |
| `dys_cybernetic/metal_detail` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/metal_detail` |
| `dys_cybernetic/metal_girder` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/metal_girder` |
| `dys_cybernetic/metal_grate1` | `LightmappedGeneric` | `metal` | `map` | `0` | `dys_cybernetic/metal_grate1` |
| `dys_cybernetic/metal_industrial` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/metal_industrial` |
| `dys_cybernetic/metal_large_door` | `LightmappedGeneric` | `metal` | `map` | `2` | `dys_cybernetic/metal_large_door` |
| `dys_cybernetic/metal_panal_single` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/metal_panal_single` |
| `dys_cybernetic/metal_panaling` | `LightmappedGeneric` | `metal` | `map` | `0` | `dys_cybernetic/metal_panaling` |
| `dys_cybernetic/metal_plate01` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/metal_plate01` |
| `dys_cybernetic/metal_plate_001` | `LightmappedGeneric` | `MetalPanel` | `map` | `0` | `dys_cybernetic/metal_plate_001` |
| `dys_cybernetic/metal_plate_002` | `LightmappedGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/metal_plate_002` |
| `dys_cybernetic/metal_segment_002` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/metal_segment_002` |
| `dys_cybernetic/metal_wall_black` | `LightmappedGeneric` | `Metal` | `map` | `2` | `dys_cybernetic/metal_wall_black` |
| `dys_cybernetic/metal_wall_teal` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/metal_wall_teal` |
| `dys_cybernetic/metal_white_stripe` | `LightmappedGeneric` | `-` | `map` | `1` | `dys_cybernetic/metal_white_stripe` |
| `dys_cybernetic/missile_diff` | `VertexLitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/missile_diff` |
| `dys_cybernetic/monitor_widescreen` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/monitor_widescreen` |
| `dys_cybernetic/node_info` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/node_info` |
| `dys_cybernetic/outer_metal_wall` | `LightmappedGeneric` | `metal` | `map` | `2` | `dys_cybernetic/outer_metal_wall` |
| `dys_cybernetic/outer_metal_wall_dark_painted` | `LightmappedGeneric` | `metal` | `map` | `2` | `dys_cybernetic/outer_metal_wall_dark_painted` |
| `dys_cybernetic/outer_metal_wall_painted` | `LightmappedGeneric` | `metal` | `map` | `0` | `dys_cybernetic/outer_metal_wall_painted` |
| `dys_cybernetic/outer_panal_double` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/outer_panal_double` |
| `dys_cybernetic/outer_panal_plane` | `LightmappedGeneric` | `-` | `map` | `0` | `dys_cybernetic/outer_panal_plane` |
| `dys_cybernetic/outer_panals` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/outer_panals` |
| `dys_cybernetic/overlay_console_001` | `UnlitGeneric` | `glass` | `overlay` | `0` | `dys_cybernetic/overlay_console_001` |
| `dys_cybernetic/overlay_console_002` | `UnlitGeneric` | `glass` | `overlay` | `0` | `dys_cybernetic/overlay_console_002` |
| `dys_cybernetic/pipe_black` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/pipe_black` |
| `dys_cybernetic/pipe_cluster` | `VertexLitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/pipe_cluster` |
| `dys_cybernetic/pipe_metal` | `VertexLitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/pipe_metal` |
| `dys_cybernetic/pipe_metal_clean` | `VertexLitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/pipe_metal_clean` |
| `dys_cybernetic/pipe_red` | `VertexLitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/pipe_red` |
| `dys_cybernetic/pipes/pipe_metal` | `VertexLitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/pipe_metal` |
| `dys_cybernetic/pipes/pipe_metal_clean` | `VertexLitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/pipe_metal_clean` |
| `dys_cybernetic/pipes/pipe_red` | `VertexLitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/pipe_red` |
| `dys_cybernetic/pipes_cluster` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/pipes_cluster` |
| `dys_cybernetic/pod_gurney` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/pod_gurney` |
| `dys_cybernetic/pod_mini_diff` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/pod_mini_diff` |
| `dys_cybernetic/profile_list` | `UnlitGeneric` | `glass` | `map` | `0` | `dys_cybernetic/profile_list` |
| `dys_cybernetic/repository_crane_diff` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/repository_crane_diff` |
| `dys_cybernetic/repository_pipes` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/repository_pipes` |
| `dys_cybernetic/repository_pipes2` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/repository_pipes2` |
| `dys_cybernetic/rotating_glow_ani` | `VertexLitGeneric` | `Glass` | `map` | `0` | `dys_cybernetic/rotating_glow_ani` |
| `dys_cybernetic/screen_display_bg` | `UnlitGeneric` | `Glass` | `map` | `0` | `dys_cybernetic/screen_display_bg` |
| `dys_cybernetic/screen_overlay_evac1` | `UnlitGeneric` | `Glass` | `overlay` | `0` | `dys_cybernetic/screen_overlay_evac1` |
| `dys_cybernetic/screen_overlay_large` | `UnlitGeneric` | `Glass` | `overlay` | `0` | `dys_cybernetic/screen_overlay_large` |
| `dys_cybernetic/scrolling_text` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/scrolling_text` |
| `dys_cybernetic/security_panal` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/security_panal` |
| `dys_cybernetic/sign_frame_hologram` | `VertexlitGeneric` | `metal` | `map` | `0` | `dys_cybernetic/sign_frame_hologram` |
| `dys_cybernetic/sign_laba1` | `UnlitGeneric` | `-` | `map` | `0` | `dys_cybernetic/sign_laba1` |
| `dys_cybernetic/skybox_cars1` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/skybox_cars1` |
| `dys_cybernetic/skybox_cars1_red` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/skybox_cars1_red` |
| `dys_cybernetic/sled_lamp` | `VertexLitGeneric` | `-` | `map` | `0` | `dys_cybernetic/sled_lamp` |
| `dys_cybernetic/staging_panal` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/staging_panal` |
| `dys_cybernetic/steammain` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/steammain` |
| `dys_cybernetic/stripe_arrow_red` | `LightmappedGeneric` | `-` | `map` | `0` | `dys_cybernetic/stripe_arrow_red` |
| `dys_cybernetic/switch_panel_001` | `LightmappedGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/switch_panel_001` |
| `dys_cybernetic/switch_panel_002` | `LightmappedGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/switch_panel_002` |
| `dys_cybernetic/switchboxes` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/switchboxes` |
| `dys_cybernetic/switchcabinet` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/switchcabinet` |
| `dys_cybernetic/switchcabinet1` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/switchcabinet1` |
| `dys_cybernetic/switchcabinet1_rust` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/switchcabinet1_rust` |
| `dys_cybernetic/teleport_panal` | `UnlitGeneric` | `-` | `map` | `1` | `dys_cybernetic/teleport_panal` |
| `dys_cybernetic/transformer_diff` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/transformer_diff` |
| `dys_cybernetic/transformer_diff2` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/transformer_diff` |
| `dys_cybernetic/transformer_notrans` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/transformer_trans` |
| `dys_cybernetic/transformer_trans` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/transformer_trans` |
| `dys_cybernetic/trim_cyber` | `LightmappedGeneric` | `Metal` | `map` | `4` | `dys_cybernetic/trim_cyber` |
| `dys_cybernetic/trim_cyber_highlight` | `LightmappedGeneric` | `Metal` | `map` | `3` | `dys_cybernetic/trim_cyber_highlight` |
| `dys_cybernetic/trim_cyber_vent` | `LightmappedGeneric` | `MetalGrate` | `map` | `1` | `dys_cybernetic/trim_cyber_vent` |
| `dys_cybernetic/trim_lights` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/trim_lights` |
| `dys_cybernetic/trim_lights_b` | `LightmappedGeneric` | `Metal` | `map` | `2` | `dys_cybernetic/trim_lights` |
| `dys_cybernetic/trim_red` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/trim_red` |
| `dys_cybernetic/turbine_skin_001` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/turbine_skin_001` |
| `dys_cybernetic/turbine_skin_001a` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/turbine_skin_001a` |
| `dys_cybernetic/turbine_skin_002` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/turbine_skin_002` |
| `dys_cybernetic/utility_panel_001` | `DecalModulate` | `-` | `decal` | `0` | `dys_cybernetic/utility_panel_001` |
| `dys_cybernetic/vent01` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_cybernetic/vent01` |
| `dys_cybernetic/vent02` | `LightmappedGeneric` | `metal` | `map` | `4` | `dys_cybernetic/vent02` |
| `dys_cybernetic/wall_interior` | `LightmappedGeneric` | `Default` | `map` | `0` | `dys_cybernetic/wall_interior` |
| `dys_cybernetic/wall_interior_001` | `LightmappedGeneric` | `Default` | `map` | `2` | `dys_cybernetic/wall_interior_001` |
| `dys_cybernetic/wall_interior_002` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/wall_interior_002` |
| `dys_cybernetic/wall_interior_004` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/wall_interior_004` |
| `dys_cybernetic/wall_interior_005` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/wall_interior_005` |
| `dys_cybernetic/wall_interior_005_cheap` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/wall_interior_005` |
| `dys_cybernetic/wall_interior_005a` | `LightmappedGeneric` | `Metal` | `map` | `2` | `dys_cybernetic/wall_interior_005a` |
| `dys_cybernetic/wall_interior_006` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/wall_interior_006` |
| `dys_cybernetic/wall_interior_007` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/wall_interior_007` |
| `dys_cybernetic/wall_interior_008` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/wall_interior_008` |
| `dys_cybernetic/wall_interior_009` | `LightmappedGeneric` | `Concrete` | `map` | `1` | `dys_cybernetic/wall_interior_009` |
| `dys_cybernetic/wall_interior_blowout` | `VertexlitGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/wall_interior_blowout` |
| `dys_cybernetic/wall_lab_001` | `LightmappedGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/wall_lab_001` |
| `dys_cybernetic/wall_lab_002` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/wall_lab_002` |
| `dys_cybernetic/wall_lab_003` | `LightmappedGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/wall_lab_003` |
| `dys_cybernetic/wall_lab_004` | `LightmappedGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/wall_lab_004` |
| `dys_cybernetic/wall_lab_005` | `LightmappedGeneric` | `Metal` | `map` | `0` | `dys_cybernetic/wall_lab_005` |
| `dys_cybernetic/wall_painting01` | `UnlitGeneric` | `Glass` | `map` | `1` | `dys_cybernetic/wall_painting01` |
| `dys_cybernetic/wall_painting2` | `UnlitGeneric` | `Glass` | `map` | `1` | `dys_cybernetic/wall_painting2` |
| `dys_cybernetic/wall_repository1` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/wall_repository1` |
| `dys_cybernetic/wall_respository_empty` | `LightmappedGeneric` | `Metal` | `map` | `1` | `dys_cybernetic/wall_respository_empty` |
| `dys_cybernetic/wall_white_001` | `LightmappedGeneric` | `Default` | `map` | `2` | `dys_cybernetic/wall_white_001` |

### `dys_emp_postprocess`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_emp_postprocess` | `dys_emp_postprocess` | `-` | `map` | `0` | `-` |

### `dys_fortress`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_fortress/blend-gravel-dirt` | `WorldVertexTransition` | `dirt` | `map` | `2` | `dys_fortress/gravel` |
| `dys_fortress/dys_fortress-blue_light` | `lightmappedGeneric` | `glass` | `map` | `2` | `vaccine2/detail1base` |
| `dys_fortress/dys_fortress-bluelaser` | `LightmappedGeneric` | `metal` | `map` | `1` | `sprites/bluelaser1` |
| `dys_fortress/dys_fortress-combineglass001a` | `LightmappedGeneric` | `glass` | `map` | `3` | `glass/combineglass001a` |
| `dys_fortress/dys_fortress-concrete` | `LightmappedGeneric` | `concrete` | `map` | `1` | `Concrete/concretewall019a` |
| `dys_fortress/dys_fortress-cybersign-bridgecontrol` | `UnlitGeneric` | `glass` | `map` | `2` | `dys_fortress/dys_fortress-cybersign-bridgecontrol` |
| `dys_fortress/dys_fortress-cybersign-closed` | `UnlitGeneric` | `glass` | `map` | `3` | `dys_fortress/dys_fortress-cybersign-closed` |
| `dys_fortress/dys_fortress-cybersign-datasecurity` | `UnlitGeneric` | `glass` | `map` | `3` | `dys_fortress/dys_fortress-cybersign-datasecurity` |
| `dys_fortress/dys_fortress-cybersign-doorcontrol` | `UnlitGeneric` | `glass` | `map` | `2` | `dys_fortress/dys_fortress-cybersign-doorcontrol` |
| `dys_fortress/dys_fortress-cybersign-elevatordoors` | `UnlitGeneric` | `glass` | `map` | `0` | `dys_fortress/dys_fortress-cybersign-elevatordoors` |
| `dys_fortress/dys_fortress-cybersign-elevtorampdoorcontrol` | `UnlitGeneric` | `glass` | `map` | `0` | `dys_fortress/dys_fortress-cybersign-elevtorampdoorcontrol` |
| `dys_fortress/dys_fortress-cybersign-offline` | `UnlitGeneric` | `glass` | `map` | `2` | `dys_fortress/dys_fortress-cybersign-offline` |
| `dys_fortress/dys_fortress-cybersign-online` | `UnlitGeneric` | `glass` | `map` | `2` | `dys_fortress/dys_fortress-cybersign-online` |
| `dys_fortress/dys_fortress-cybersign-opened` | `UnlitGeneric` | `glass` | `map` | `3` | `dys_fortress/dys_fortress-cybersign-opened` |
| `dys_fortress/dys_fortress-cybersign-reactorsecurity` | `UnlitGeneric` | `glass` | `map` | `2` | `dys_fortress/dys_fortress-cybersign-reactorsecurity` |
| `dys_fortress/dys_fortress-cybersign-seweraccess` | `UnlitGeneric` | `glass` | `map` | `0` | `dys_fortress/dys_fortress-cybersign-seweraccess` |
| `dys_fortress/dys_fortress-cybersign-sewergrates` | `UnlitGeneric` | `glass` | `map` | `0` | `dys_fortress/dys_fortress-cybersign-sewergrates` |
| `dys_fortress/dys_fortress-cybersign-spawncontrol` | `UnlitGeneric` | `glass` | `map` | `0` | `dys_fortress/dys_fortress-cybersign-spawncontrol` |
| `dys_fortress/dys_fortress-cybersign-turretstatus` | `UnlitGeneric` | `glass` | `map` | `2` | `dys_fortress/dys_fortress-cybersign-turretstatus` |
| `dys_fortress/dys_fortress-debris` | `LightmappedGeneric` | `dirt` | `map` | `5` | `concrete/concretefloor020a` |
| `dys_fortress/dys_fortress-dys_vacextwallsmall` | `LightmappedGeneric` | `metal` | `map` | `3` | `/dys_fortress/dys_fortress-dys_vacextwallsmall` |
| `dys_fortress/dys_fortress-exterior1` | `LightmappedGeneric` | `metal` | `map` | `3` | `dys_fortress/dys_fortress-exterior1` |
| `dys_fortress/dys_fortress-exterior2` | `LightmappedGeneric` | `metal` | `map` | `4` | `dys_fortress/dys_fortress-exterior2` |
| `dys_fortress/dys_fortress-helpoverlay-hackable` | `UnlitGeneric` | `glass` | `overlay` | `0` | `dys_fortress/dys_fortress-helpoverlay-hackable` |
| `dys_fortress/dys_fortress-helpoverlay-opens2` | `UnlitGeneric` | `glass` | `overlay` | `0` | `dys_fortress/dys_fortress-helpoverlay-opens2` |
| `dys_fortress/dys_fortress-helpoverlay-opens3` | `UnlitGeneric` | `glass` | `overlay` | `0` | `dys_fortress/dys_fortress-helpoverlay-opens3` |
| `dys_fortress/dys_fortress-helpoverlay-shutsoff4` | `UnlitGeneric` | `glass` | `overlay` | `0` | `dys_fortress/dys_fortress-helpoverlay-shutsoff4` |
| `dys_fortress/dys_fortress-metal_skirting003` | `Lightmappedgeneric` | `metal` | `map` | `4` | `vaccinecore/metal_skirting003` |
| `dys_fortress/dys_fortress-metala2` | `LightmappedGeneric` | `metal` | `map` | `2` | `dys_fortress/dys_wall_painted` |
| `dys_fortress/dys_fortress-metalpanel009a` | `LightmappedGeneric` | `metal` | `map` | `4` | `Props/metalpanel009a` |
| `dys_fortress/dys_fortress-metalpanel010a` | `LightmappedGeneric` | `metal` | `map` | `4` | `Props/metalpanel010a` |
| `dys_fortress/dys_fortress-metalpanel011a` | `LightmappedGeneric` | `metal` | `map` | `5` | `Props/metalpanel011a` |
| `dys_fortress/dys_fortress-metalroof_lighter` | `lightmappedGeneric` | `metal` | `map` | `1` | `dys_fortress/dys_fortress-metalroof_lighter` |
| `dys_fortress/dys_fortress-outside2dark` | `LightmappedGeneric` | `metal` | `map` | `4` | `dys_fortress/dys_fortress-outside2dark` |
| `dys_fortress/dys_fortress-redlaser` | `LightmappedGeneric` | `metal` | `map` | `1` | `sprites/purplelaser1` |
| `dys_fortress/dys_fortress-sign_bridgecontrol` | `LightmappedGeneric` | `glass` | `map` | `0` | `dys_fortress/dys_fortress-sign_bridgecontrol` |
| `dys_fortress/dys_fortress-sign_incomingmunitions` | `LightmappedGeneric` | `glass` | `map` | `1` | `dys_fortress/dys_fortress-sign_incomingmunitions` |
| `dys_fortress/dys_fortress-sign_reactorroom` | `LightmappedGeneric` | `glass` | `map` | `1` | `dys_fortress/dys_fortress-sign_reactorroom` |
| `dys_fortress/dys_fortress-sign_replicationlab` | `LightmappedGeneric` | `glass` | `map` | `1` | `dys_fortress/dys_fortress-sign_replicationlab` |
| `dys_fortress/dys_fortress-sign_supplycloset` | `LightmappedGeneric` | `glass` | `map` | `0` | `dys_fortress/dys_fortress-sign_supplycloset` |
| `dys_fortress/dys_fortress-sign_supplyroom` | `LightmappedGeneric` | `glass` | `map` | `0` | `/dys_fortress/dys_fortress-sign_supplyroom` |
| `dys_fortress/dys_fortress-spawnbox` | `lightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_spawnbox` |
| `dys_fortress/dys_fortress-spawnboxa` | `lightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_spawnboxa` |
| `dys_fortress/dys_fortress-tile` | `LightmappedGeneric` | `tile` | `map` | `3` | `Tile/tilewall009b` |
| `dys_fortress/dys_fortress-vacaldoor` | `lightmappedGeneric` | `metal` | `map` | `4` | `dys_fortress/dys_fortress-vacaldoor` |
| `dys_fortress/dys_fortress-vacaldoor_alpha` | `LightmappedGeneric` | `metal` | `map` | `0` | `dys_fortress/dys_fortress-vacaldoor_alpha` |
| `dys_fortress/dys_fortress-vaccine-detail1base` | `lightmappedGeneric` | `glass` | `map` | `1` | `vaccine2/detail1base` |
| `dys_fortress/dys_fortress-vaccine-detail2base` | `lightmappedGeneric` | `metal` | `map` | `1` | `vaccine2/detail2base` |
| `dys_fortress/dys_fortress-vaccine-detail3base` | `lightmappedGeneric` | `metal` | `map` | `2` | `vaccine2/detail3base` |
| `dys_fortress/dys_fortress-vaccine-detail6base` | `lightmappedGeneric` | `metal` | `map` | `4` | `vaccine2/detail6base` |
| `dys_fortress/dys_fortress-vaccine-dys_vactrim1` | `LightmappedGeneric` | `metal` | `map` | `5` | `vaccinert/dys_vactrim1` |
| `dys_fortress/dys_fortress-vaccine-plaswall` | `lightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_vac_plaswall` |
| `dys_fortress/dys_fortress-vactrim1_grey_alpha` | `LightmappedGeneric` | `metal` | `map` | `4` | `dys_fortress/dys_fortress-vactrim1_grey_alpha` |
| `dys_fortress/gravel` | `LightmappedGeneric` | `dirt` | `map` | `1` | `dys_fortress/gravel` |
| `dys_fortress/gravel2` | `LightmappedGeneric` | `dirt` | `map` | `0` | `dys_fortress/gravel2` |
| `dys_fortress/guidesigns/data_storage_left` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_fortress/guidesigns/data_storage_left` |
| `dys_fortress/guidesigns/data_storage_right` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_fortress/guidesigns/data_storage_right` |
| `dys_fortress/guidesigns/entrance_security_left` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_fortress/guidesigns/entrance_security_left` |
| `dys_fortress/guidesigns/entrance_security_right` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_fortress/guidesigns/entrance_security_right` |
| `dys_fortress/guidesigns/firewall_control` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_fortress/guidesigns/firewall_control` |
| `dys_fortress/guidesigns/reactor_control_left` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_fortress/guidesigns/reactor_control_left` |
| `dys_fortress/guidesigns/reactor_control_right` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_fortress/guidesigns/reactor_control_right` |
| `dys_fortress/metal_bridge` | `LightmappedGeneric` | `metal` | `map` | `4` | `dys_fortress/metal_bridge` |
| `dys_fortress/tile` | `LightmappedGeneric` | `tile` | `map` | `1` | `dys_fortress/tile` |
| `dys_fortress/tunnel_wall` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_fortress/tunnel_wall` |

### `dys_monitor1a`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_monitor1a` | `UnlitTwoTexture` | `glass` | `map` | `0` | `_rt_camera1` |

### `dys_monitor2a`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_monitor2a` | `UnlitTwoTexture` | `glass` | `map` | `0` | `_rt_camera2` |

### `dys_monitor3a`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_monitor3a` | `UnlitTwoTexture` | `glass` | `map` | `0` | `_rt_camera3` |

### `dys_monitor4a`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_monitor4a` | `UnlitTwoTexture` | `glass` | `map` | `0` | `_rt_camera4` |

### `dys_nameless`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_nameless/Brick_Wall_001` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Brick_Wall_001` |
| `dys_nameless/Concrete_001` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_001` |
| `dys_nameless/Concrete_001_brown` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_001_brown` |
| `dys_nameless/Concrete_002` | `LightmappedGeneric` | `concrete` | `map` | `0` | `dys_nameless/Concrete_002` |
| `dys_nameless/Concrete_003` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_003` |
| `dys_nameless/Concrete_004` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_004` |
| `dys_nameless/Concrete_004_Blue` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_004_Blue` |
| `dys_nameless/Concrete_004_Green` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_004_Green` |
| `dys_nameless/Concrete_004_Red` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_004_Red` |
| `dys_nameless/Concrete_004_bot` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_004_bot` |
| `dys_nameless/Concrete_005` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_005` |
| `dys_nameless/Concrete_006` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_006` |
| `dys_nameless/Concrete_006_bot` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_006_bot` |
| `dys_nameless/Concrete_006_mid` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_006_mid` |
| `dys_nameless/Concrete_Floor_001` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/Concrete_Floor_001` |
| `dys_nameless/Elevator_Door` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_nameless/Elevator_Door` |
| `dys_nameless/Graffiti_Fedio` | `LightmappedGeneric` | `-` | `map` | `0` | `dys_nameless/Graffiti_Fedio` |
| `dys_nameless/Graffiti_Shock` | `LightmappedGeneric` | `-` | `map` | `0` | `dys_nameless/Graffiti_Shock` |
| `dys_nameless/Graffiti_TheDude` | `LightmappedGeneric` | `-` | `map` | `0` | `dys_nameless/Graffiti_TheDude` |
| `dys_nameless/Metal_Green` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_nameless/Metal_Green` |
| `dys_nameless/Penguin` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_nameless/Penguin` |
| `dys_nameless/Plasma` | `unlitgeneric` | `-` | `map` | `0` | `dys_nameless/Plasma` |
| `dys_nameless/Plasma2` | `unlitgeneric` | `-` | `map` | `1` | `dys_nameless/Plasma2` |
| `dys_nameless/ReactorRoom` | `VertexlitGeneric` | `glass` | `map` | `1` | `dys_nameless/ReactorRoom` |
| `dys_nameless/RedPlasma2` | `unlitgeneric` | `-` | `map` | `1` | `dys_nameless/RedPlasma2` |
| `dys_nameless/Screen_Overlay` | `UnlitGeneric` | `glass` | `overlay` | `0` | `dys_nameless/Screen_Overlay` |
| `dys_nameless/Security` | `VertexlitGeneric` | `glass` | `map` | `1` | `dys_nameless/Security` |
| `dys_nameless/Security_Tele` | `VertexlitGeneric` | `glass` | `map` | `1` | `dys_nameless/Security_Tele` |
| `dys_nameless/Status_Locked` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_nameless/Status_Locked` |
| `dys_nameless/Status_Unlocked` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_nameless/Status_Unlocked` |
| `dys_nameless/Tele_Entrance` | `VertexlitGeneric` | `glass` | `map` | `1` | `dys_nameless/Tele_Entrance` |
| `dys_nameless/Tele_Exit` | `VertexlitGeneric` | `glass` | `map` | `1` | `dys_nameless/Tele_Exit` |
| `dys_nameless/Teleporter` | `VertexlitGeneric` | `glass` | `map` | `1` | `dys_nameless/Teleporter` |
| `dys_nameless/Terminal_1` | `LightmappedGeneric` | `glass` | `map` | `1` | `dys_nameless/Terminal_1` |
| `dys_nameless/Terminal_2` | `LightmappedGeneric` | `glass` | `map` | `1` | `dys_nameless/Terminal_2` |
| `dys_nameless/WeaponTest` | `VertexlitGeneric` | `glass` | `map` | `1` | `dys_nameless/WeaponTest` |
| `dys_nameless/Weapon_Reactor` | `VertexlitGeneric` | `glass` | `map` | `1` | `dys_nameless/Weapon_Reactor` |
| `dys_nameless/beam_over` | `UnlitGeneric` | `-` | `map` | `1` | `dys_nameless/beam_over` |
| `dys_nameless/fsn_Stairs` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/fsn_Stairs` |
| `dys_nameless/fusion_avatar_corp` | `unlitgeneric` | `-` | `map` | `0` | `dys_nameless/fusion_avatar_corp` |
| `dys_nameless/fusion_avatar_punk` | `unlitgeneric` | `-` | `map` | `0` | `dys_nameless/fusion_avatar_punk` |
| `dys_nameless/fusion_concrete_ceiling` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/fusion_concrete_ceiling` |
| `dys_nameless/fusion_concrete_floor` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/fusion_concrete_floor` |
| `dys_nameless/fusion_concrete_floor2` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/fusion_concrete_floor2` |
| `dys_nameless/fusion_concrete_floor_001` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/fusion_concrete_floor_001` |
| `dys_nameless/fusion_concrete_gray_wall` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/fusion_concrete_gray_wall` |
| `dys_nameless/fusion_concrete_gray_wall_bricks` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/fusion_concrete_gray_wall_bricks` |
| `dys_nameless/fusion_decal_yellow_paint` | `LightmappedGeneric` | `-` | `decal` | `0` | `dys_nameless/fusion_decal_yellow_paint` |
| `dys_nameless/metal_building02` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_nameless/metal_building02` |
| `dys_nameless/name_Door` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_nameless/name_Door` |
| `dys_nameless/name_TurretControl` | `VertexlitGeneric` | `glass` | `map` | `1` | `dys_nameless/name_TurretControl` |
| `dys_nameless/name_concretewall_red` | `LightmappedGeneric` | `concrete` | `map` | `0` | `dys_nameless/name_concretewall_red` |
| `dys_nameless/name_fusionscreen` | `UnlitGeneric` | `-` | `map` | `1` | `dys_nameless/name_fusionscreen` |
| `dys_nameless/name_grate` | `lightmappedGeneric` | `metal` | `map` | `1` | `dys_nameless/name_grate` |
| `dys_nameless/name_metal_panel` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_nameless/name_metal_panel` |
| `dys_nameless/name_quantumfloor` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/name_quantumfloor` |
| `dys_nameless/name_quantumflooroffset` | `LightmappedGeneric` | `concrete` | `map` | `0` | `dys_nameless/name_quantumflooroffset` |
| `dys_nameless/name_redconcretebeam2` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/name_redconcretebeam2` |
| `dys_nameless/name_secsign_lt` | `lightmappedGeneric` | `-` | `map` | `0` | `dys_nameless/name_secsign_lt` |
| `dys_nameless/name_secsign_rt` | `lightmappedGeneric` | `-` | `map` | `0` | `dys_nameless/name_secsign_rt` |
| `dys_nameless/name_sweeper2red` | `unlitgeneric` | `-` | `map` | `1` | `dys_nameless/name_sweeper2red` |
| `dys_nameless/name_telesign_lt` | `lightmappedGeneric` | `-` | `map` | `0` | `dys_nameless/name_telesign_lt` |
| `dys_nameless/name_telesign_rt` | `lightmappedGeneric` | `-` | `map` | `0` | `dys_nameless/name_telesign_rt` |
| `dys_nameless/name_thanks2` | `LightmappedGeneric` | `metal` | `map` | `1` | `dys_nameless/name_thanks2` |
| `dys_nameless/name_weaponcharging` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_nameless/name_weaponcharging` |
| `dys_nameless/name_weaponready` | `UnlitGeneric` | `glass` | `map` | `1` | `dys_nameless/name_weaponready` |
| `dys_nameless/name_whiteconc_beam` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/name_whiteconc_beam` |
| `dys_nameless/old_cement3` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/old_cement3` |
| `dys_nameless/quantum_overlay` | `UnlitGeneric` | `glass` | `overlay` | `1` | `dys_nameless/quantum_overlay` |
| `dys_nameless/sidewalk` | `LightmappedGeneric` | `concrete` | `map` | `1` | `dys_nameless/sidewalk` |

### `dys_thermal`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_thermal` | `Patch` | `-` | `map` | `0` | `-` |

### `dys_transmonitor_1`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_transmonitor_1` | `Unlittwotexture` | `glass` | `map` | `0` | `_rt_camera1` |

### `dys_transmonitor_2`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_transmonitor_2` | `Unlittwotexture` | `glass` | `map` | `0` | `_rt_camera2` |

### `dys_transmonitor_3`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_transmonitor_3` | `Unlittwotexture` | `glass` | `map` | `0` | `_rt_camera3` |

### `dys_transmonitor_4`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `dys_transmonitor_4` | `Unlittwotexture` | `glass` | `map` | `0` | `_rt_camera4` |

### `editor`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `editor/filter_team` | `Sprite` | `-` | `map` | `0` | `editor/filter_team` |
| `editor/objective` | `Sprite` | `-` | `map` | `0` | `editor/objective` |
| `editor/onscreeninfo` | `Sprite` | `-` | `map` | `0` | `editor/onscreeninfo` |
| `editor/spawn` | `Sprite` | `-` | `map` | `0` | `editor/spawn` |

### `effects`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `effects/EMP` | `Refract` | `-` | `effect` | `0` | `-` |
| `effects/EMP_dx8` | `UnlitTwoTexture` | `-` | `effect` | `0` | `effects/EMP_dx8` |
| `effects/ThermalEyes` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/ThermalEyes` |
| `effects/achieved` | `SpriteCard` | `no_decal` | `effect` | `0` | `Effects/achieved` |
| `effects/cyber_ragdoll` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/cyber_ragdoll` |
| `effects/deck-one` | `SpriteCard` | `no_decal` | `effect` | `0` | `Effects/deck-one` |
| `effects/deck-zero` | `SpriteCard` | `no_decal` | `effect` | `0` | `Effects/deck-zero` |
| `effects/disc` | `Refract` | `-` | `effect` | `0` | `models/props_c17/fisheyelensdx7` |
| `effects/greenglow1` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/greenglow1` |
| `effects/greenglow2` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/greenglow2` |
| `effects/ioncannon_impactparticle` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/ioncannon_impactparticle` |
| `effects/laserrifle_impactparticle` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/laserrifle_impactparticle` |
| `effects/medicbeam_curl` | `Spritecard` | `default` | `effect` | `0` | `Effects/medicbeam_curl` |
| `effects/sc_softglow` | `Spritecard` | `no_decal` | `effect` | `0` | `Effects/softglow` |
| `effects/sc_softglow_translucent` | `Spritecard` | `no_decal` | `effect` | `0` | `Effects/softglow_translucent` |
| `effects/softglow` | `UnlitGeneric` | `no_decal` | `effect` | `0` | `Effects/softglow` |
| `effects/softglow_translucent` | `UnlitGeneric` | `no_decal` | `effect` | `0` | `Effects/softglow_translucent` |
| `effects/softglow_translucent_fog` | `unlitgeneric` | `no_decal` | `effect` | `0` | `Effects/outline_translucent` |
| `effects/spawn` | `UnlitGeneric` | `-` | `effect` | `0` | `_rt_SpawnBuffer` |
| `effects/star001` | `SpriteCard` | `no_decal` | `effect` | `0` | `Effects/star001` |
| `effects/tracers/Assault` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/tracers/Assault` |
| `effects/tracers/Basilisk` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/tracers/Basilisk` |
| `effects/tracers/Duals` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/tracers/Duals` |
| `effects/tracers/MK808` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/tracers/MK808` |
| `effects/tracers/MachPistol` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/tracers/MachPistol` |
| `effects/tracers/Minigun` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/tracers/Minigun` |
| `effects/tracers/Shotgun` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/tracers/Shotgun` |
| `effects/tracers/Tracker` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/tracers/Tracker` |
| `effects/tracers/Turret` | `UnlitGeneric` | `-` | `effect` | `0` | `effects/tracers/Turret` |

### `example_model_material`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `example_model_material` | `Mod_Example_Model` | `metal` | `map` | `0` | `Models/props_c17/Oil_Drum001g` |

### `fedio`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `fedio/fusion/Brick_Wall_001` | `LightmappedGeneric` | `concrete` | `map` | `0` | `fedio/fusion/Brick_Wall_001` |
| `fedio/fusion/Sidewalk` | `LightmappedGeneric` | `concrete` | `map` | `0` | `fedio/fusion/Sidewalk` |
| `fedio/models/Button_Monitor` | `VertexlitGeneric` | `metal` | `map` | `0` | `fedio/models/Button_Monitor` |
| `fedio/models/CarStopper_Texture` | `VertexlitGeneric` | `concrete` | `map` | `0` | `fedio/models/CarStopper_Texture` |
| `fedio/models/Column_tex` | `VertexlitGeneric` | `concrete` | `map` | `0` | `fedio/models/Column_tex` |
| `fedio/models/FedTex_BeerCan` | `VertexlitGeneric` | `metal` | `map` | `0` | `fedio/models/FedTex_BeerCan` |
| `fedio/models/Model_CarBollard` | `VertexlitGeneric` | `metal` | `map` | `0` | `fedio/models/Model_CarBollard` |
| `fedio/models/Model_Circular_Support` | `VertexlitGeneric` | `metal` | `map` | `0` | `fedio/models/Model_Circular_Support` |
| `fedio/models/Model_Concrete_Support_Black` | `VertexlitGeneric` | `concrete` | `map` | `0` | `fedio/models/Model_Concrete_Support_Black` |
| `fedio/models/Model_Concrete_Support_Blue` | `VertexlitGeneric` | `concrete` | `map` | `0` | `fedio/models/Model_Concrete_Support_Blue` |
| `fedio/models/Model_Concrete_Support_Red` | `VertexlitGeneric` | `concrete` | `map` | `0` | `fedio/models/Model_Concrete_Support_Red` |
| `fedio/models/Model_Concrete_Support_White` | `VertexlitGeneric` | `concrete` | `map` | `0` | `fedio/models/Model_Concrete_Support_White` |
| `fedio/models/chevron1` | `VertexlitGeneric` | `Metal` | `map` | `0` | `fedio/models/chevron1` |
| `fedio/models/gen_base_1` | `VertexlitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_base_1` |
| `fedio/models/gen_metal_clean1a` | `VertexLitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_clean1b` |
| `fedio/models/gen_metal_clean1b` | `VertexLitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_clean1b` |
| `fedio/models/gen_metal_clean1c` | `VertexLitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_clean1b` |
| `fedio/models/gen_metal_clean1d` | `VertexLitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_clean1b` |
| `fedio/models/gen_metal_detail` | `VertexlitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_detail` |
| `fedio/models/gen_metal_panel1` | `VertexlitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_panel1` |
| `fedio/models/gen_metal_pipe` | `VertexlitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_pipe` |
| `fedio/models/gen_metal_pipe2` | `VertexlitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_pipe2` |
| `fedio/models/gen_metal_pipe3` | `VertexlitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_pipe3` |
| `fedio/models/gen_metal_stripe1` | `VertexLitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_stripe1` |
| `fedio/models/gen_metal_stripe1a` | `VertexLitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_stripe1` |
| `fedio/models/gen_metal_vent1` | `VertexlitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_metal_vent1` |
| `fedio/models/gen_vent1` | `VertexlitGeneric` | `Metal` | `map` | `0` | `fedio/models/gen_vent1` |
| `fedio/models/laser_container_1` | `VertexLitGeneric` | `metal` | `map` | `0` | `fedio/models/laser_container_1` |
| `fedio/models/laser_weapon_1` | `VertexlitGeneric` | `metal` | `map` | `0` | `fedio/models/laser_weapon_1` |
| `fedio/models/laser_weapon_2` | `VertexlitGeneric` | `metal` | `map` | `0` | `fedio/models/laser_weapon_2` |

### `graffiti`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `graffiti/decal_graffiti_bash` | `LightmappedGeneric` | `dirt` | `decal` | `0` | `graffiti/decal_graffiti_bash` |
| `graffiti/decal_graffiti_die` | `LightmappedGeneric` | `dirt` | `decal` | `0` | `graffiti/decal_graffiti_die` |
| `graffiti/decal_graffiti_rage` | `LightmappedGeneric` | `dirt` | `decal` | `0` | `graffiti/decal_graffiti_rage` |
| `graffiti/decal_graffiti_sista` | `LightmappedGeneric` | `dirt` | `decal` | `0` | `graffiti/decal_graffiti_sista` |
| `graffiti/decal_graffiti_space` | `LightmappedGeneric` | `dirt` | `decal` | `0` | `graffiti/decal_graffiti_space` |
| `graffiti/decal_graffiti_vice` | `LightmappedGeneric` | `dirt` | `decal` | `0` | `graffiti/decal_graffiti_vice` |

### `hatched_cyberspace`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `hatched_cyberspace/blackOnBlue` | `UnlitGeneric` | `metal` | `map` | `0` | `hatched_cyberspace/blackOnBlue` |
| `hatched_cyberspace/blackOnGreen` | `UnlitGeneric` | `metal` | `map` | `1` | `hatched_cyberspace/blackOnGreen` |
| `hatched_cyberspace/blackOnOrange` | `UnlitGeneric` | `metal` | `map` | `1` | `hatched_cyberspace/blackOnOrange` |
| `hatched_cyberspace/blackOnPurple` | `UnlitGeneric` | `metal` | `map` | `0` | `hatched_cyberspace/blackOnPurple` |
| `hatched_cyberspace/blackOnRed` | `UnlitGeneric` | `metal` | `map` | `2` | `hatched_cyberspace/blackOnRed` |
| `hatched_cyberspace/blackYellow` | `UnlitGeneric` | `metal` | `map` | `0` | `hatched_cyberspace/blackOnYellow` |
| `hatched_cyberspace/whiteOnBlue` | `UnlitGeneric` | `metal` | `map` | `0` | `hatched_cyberspace/whiteOnBlue` |
| `hatched_cyberspace/whiteOnGreen` | `UnlitGeneric` | `metal` | `map` | `0` | `hatched_cyberspace/whiteOnGreen` |
| `hatched_cyberspace/whiteOnOrange` | `UnlitGeneric` | `metal` | `map` | `0` | `hatched_cyberspace/whiteOnOrange` |
| `hatched_cyberspace/whiteOnPurple` | `UnlitGeneric` | `metal` | `map` | `0` | `hatched_cyberspace/whiteOnPurple` |
| `hatched_cyberspace/whiteOnRed` | `UnlitGeneric` | `metal` | `map` | `0` | `hatched_cyberspace/whiteOnRed` |
| `hatched_cyberspace/whiteOnYellow` | `UnlitGeneric` | `metal` | `map` | `0` | `hatched_cyberspace/whiteOnYellow` |

### `lightpole`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `lightpole/color` | `VertexLitGeneric` | `-` | `map` | `0` | `lightpole/color` |
| `lightpole/transperency` | `LightmappedGeneric` | `-` | `map` | `0` | `lightpole/trancperency` |

### `lobbytex`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `lobbytex/static` | `LightmappedGeneric` | `-` | `map` | `0` | `lobbytex/static` |
| `lobbytex/yui_door1` | `LightmappedGeneric` | `metal` | `map` | `1` | `lobbytex/yui_door1` |
| `lobbytex/yui_flur1` | `UnlitGeneric` | `metal` | `map` | `1` | `lobbytex/yui_flur1` |
| `lobbytex/yui_flur1_dark` | `UnlitGeneric` | `metal` | `map` | `0` | `lobbytex/yui_flur1_dark` |
| `lobbytex/yui_serverpanel001` | `LightmappedGeneric` | `metal` | `map` | `2` | `lobbytex/yui_serverpanel001` |
| `lobbytex/yui_widescreen1` | `UnlitGeneric` | `glass` | `map` | `0` | `lobbytex/yui_widescreen1` |
| `lobbytex/yui_wood1` | `LightmappedGeneric` | `wood` | `map` | `1` | `models/props_foliage/tree_deciduous_01a_trunk` |
| `lobbytex/yuiinfo1` | `UnlitGeneric` | `glass` | `map` | `0` | `lobbytex/yuiinfo1` |
| `lobbytex/yuiinfo2` | `UnlitGeneric` | `glass` | `map` | `0` | `lobbytex/yuiinfo2` |
| `lobbytex/yuioverlay` | `UnlitGeneric` | `glass` | `overlay` | `0` | `lobbytex/yuioverlay` |
| `lobbytex/yuioverlaySPLASH` | `UnlitGeneric` | `glass` | `overlay` | `0` | `lobbytex/yuioverlaySPLASH` |
| `lobbytex/yuiunderlay` | `UnlitGeneric` | `metal` | `map` | `0` | `lobbytex/yuiunderlay` |
| `lobbytex/yuiunderlayplus1` | `UnlitGeneric` | `metal` | `map` | `1` | `lobbytex/yuiunderlayplus1` |

### `metal`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `metal/metalbeam01` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalbeam01` |
| `metal/metalbeam02` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalbeam02` |
| `metal/metalbombdecal` | `lightmappedGeneric` | `-` | `decal` | `0` | `metal/metalbombdecal` |
| `metal/metalfloor_001a` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalfloor_001a_t` |
| `metal/metalfloor_001a_cheap` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalfloor_001a_t` |
| `metal/metalfloor_001b` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalfloor_001b_t` |
| `metal/metalfloor_001b_cheap` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalfloor_001b_t` |
| `metal/metalfloor_001c` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalfloor_001c_t` |
| `metal/metalfloor_001c_cheap` | `LightmappedGeneric` | `metal` | `map` | `2` | `metal/metalfloor_001c_t` |
| `metal/metalfloor_001d` | `LightmappedGeneric` | `metal` | `map` | `2` | `metal/metalfloor_001d_t` |
| `metal/metalfloor_001d_cheap` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalfloor_001d_t` |
| `metal/metalfloor_001e` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalfloor_001e_t` |
| `metal/metalfloor_001e_cheap` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalfloor_001e_t` |
| `metal/metalfloor_002a` | `LightmappedGeneric` | `metal` | `map` | `2` | `metal/metalfloor_002a_t` |
| `metal/metalfloor_002a_cheap` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalfloor_002a_t` |
| `metal/metalfloor_002b` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalfloor_002b_t` |
| `metal/metalfloor_002b_cheap` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalfloor_002b_t` |
| `metal/metalgrate_001a_t` | `LightmappedGeneric` | `metal` | `map` | `2` | `metal/metalgrate_001a_t` |
| `metal/metalgrate_001a_t_alphatest` | `LightmappedGeneric` | `metal` | `map` | `3` | `metal/metalgrate_001a_t` |
| `metal/metalgrate_001a_t_cheap` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalgrate_001a_t` |
| `metal/metalgrate_001b_t` | `LightmappedGeneric` | `metal` | `map` | `2` | `metal/metalgrate_001b_t` |
| `metal/metalgrate_001b_t_cheap` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalgrate_001b_t` |
| `metal/metalgrate_001c_t` | `LightmappedGeneric` | `metal` | `map` | `3` | `metal/metalgrate_001c_t` |
| `metal/metalgrate_001c_t_cheap` | `LightmappedGeneric` | `metal` | `map` | `2` | `metal/metalgrate_001c_t` |
| `metal/metalgrate_001d_t` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalgrate_001d_t` |
| `metal/metalgrate_001d_t_cheap` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalgrate_001d_t` |
| `metal/metalladder01` | `LightmappedGeneric` | `metal` | `map` | `2` | `metal/metalladder01` |
| `metal/metalladder01_cheap` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalladder01` |
| `metal/metalsupport_001a_t` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalsupport_001a_t` |
| `metal/metalsupport_001a_t_cheap` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalsupport_001a_t` |
| `metal/metalsupport_001a_t_dx8` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalsupport_001a_t` |
| `metal/metalsupport_001b_t` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalsupport_001b_t` |
| `metal/metalsupport_001b_t_cheap` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalsupport_001b_t` |
| `metal/metalsupport_001b_t_dx8` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalsupport_001b_t` |
| `metal/metalsupport_002a_t` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalsupport_002a_t` |
| `metal/metalsupport_002a_t_cheap` | `LightmappedGeneric` | `metal` | `map` | `2` | `metal/metalsupport_002a_t` |
| `metal/metalsupport_002a_t_dx8` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalsupport_002a_t` |
| `metal/metalsupport_002b_t` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalsupport_002b_t` |
| `metal/metalsupport_002b_t_cheap` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalsupport_002b_t` |
| `metal/metalsupport_002b_t_dx8` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalsupport_002b_t` |
| `metal/metaltruss017a_decal_overlay` | `LightmappedGeneric` | `metal` | `decal` | `0` | `Metal/metaltruss017a` |
| `metal/metalwall002a` | `LightmappedGeneric` | `-` | `map` | `4` | `-` |
| `metal/metalwall002a_dx8` | `LightmappedGeneric` | `metal` | `map` | `2` | `metal/metalwall002a` |
| `metal/metalwall002b` | `LightmappedGeneric` | `-` | `map` | `2` | `-` |
| `metal/metalwall002b_dx8` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalwall002b` |
| `metal/metalwall002c` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `metal/metalwall002c_dx8` | `LightmappedGeneric` | `metal` | `map` | `2` | `metal/metalwall002c` |
| `metal/metalwall003a` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `metal/metalwall003a_dx8` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalwall003a` |
| `metal/metalwall003b` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `metal/metalwall003b_dx8` | `LightmappedGeneric` | `metal` | `map` | `2` | `metal/metalwall003b` |
| `metal/metalwall003c` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `metal/metalwall003c_dx8` | `LightmappedGeneric` | `metal` | `map` | `3` | `metal/metalwall003c` |
| `metal/metalwall003d` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `metal/metalwall003d_dx8` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalwall003d` |
| `metal/metalwall003e` | `LightmappedGeneric` | `-` | `map` | `2` | `-` |
| `metal/metalwall003e_dx8` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalwall003e` |
| `metal/metalwall004` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |
| `metal/metalwall004_dx8` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalwall004` |
| `metal/metalwall_001a_off_t` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalwall_001a_off_t` |
| `metal/metalwall_001a_t` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalwall_001a_t` |
| `metal/metalwall_001a_t_cheap` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalwall_001a_t` |
| `metal/metalwall_001b_off_t` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalwall_001b_off_t` |
| `metal/metalwall_001b_t` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/metalwall_001b_t` |
| `metal/metalwall_001b_t_cheap` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalwall_001b_t` |
| `metal/metalwall_001c_off_t` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalwall_001c_off_t` |
| `metal/metalwall_001c_t` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalwall_001c_t` |
| `metal/metalwall_001c_t_cheap` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/metalwall_001c_t` |
| `metal/panels01` | `LightmappedGeneric` | `metal` | `map` | `0` | `metal/panels01` |
| `metal/panels01bumps` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/panels01bumps` |
| `metal/panels01split` | `LightmappedGeneric` | `metal` | `map` | `1` | `metal/panels01split` |
| `metal/s_metalslide` | `LightmappedGeneric` | `-` | `map` | `1` | `-` |

### `models`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `models/BaseDiffuse` | `VertexLitGeneric` | `-` | `model` | `0` | `models/BaseDiffuse` |
| `models/EUDiffuse` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/EUDiffuse` |
| `models/P_advertpole_pipe` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/p_advertpole_pipe` |
| `models/P_advertpole_pole01` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/urban/p_advertpole_pole01` |
| `models/P_advertpole_screen` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/urban/p_advertpole_screen` |
| `models/P_advertpole_visor` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/urban/p_advertpole_Visor` |
| `models/P_monitor_pole01` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/p_monitor_pole01` |
| `models/PipeDiffuse` | `VertexLitGeneric` | `-` | `model` | `0` | `models/PipeDiffuse` |
| `models/PumpDiffuse` | `VertexLitGeneric` | `-` | `model` | `0` | `models/PumpDiffuse` |
| `models/Radz/container_reskin/cargo_container05` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/Radz/container_reskin/cargo_container05"` |
| `models/Radz/container_reskin/cargo_container06` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/Radz/container_reskin/cargo_container06"` |
| `models/Radz/cryo_reskin/Cryotec_logo` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/Radz/cryo_reskin/Cryotec_logo` |
| `models/Radz/cryo_reskin/cryo_glow` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/Radz/cryo_reskin/cryo_glow` |
| `models/Radz/cryo_reskin/metalrail` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/Radz/cryo_reskin/metalrail` |
| `models/Radz/cryo_reskin/orange_glow` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/Radz/cryo_reskin/orange_glow` |
| `models/Radz/cryo_reskin/yellowHat_logo` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/Radz/cryo_reskin/yellowHat_logo` |
| `models/black_awning` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/black_awning` |
| `models/buildings/cb_wind_night02` | `VertexLitGeneric` | `concrete` | `model` | `1` | `models/buildings/cb_wind_night02` |
| `models/buildings/metal_building02` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/buildings/metal_building02` |
| `models/buildings/metal_panel` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/buildings/metal_panel` |
| `models/buildings/metal_rails2` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/buildings/metal_rails2` |
| `models/buildings/old_cement` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/buildings/old_cement` |
| `models/buildings/old_cement2` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/buildings/old_cement2` |
| `models/buildings/old_cement3_white` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/buildings/old_cement3_white` |
| `models/buildings/old_cement_white` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/buildings/old_cement_white` |
| `models/buildings/projects` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/buildings/projects` |
| `models/buildings/windows_night3` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/buildings/windows_night3` |
| `models/buildings/windows_night4` | `VertexLitGeneric` | `concrete` | `model` | `1` | `models/buildings/windows_night4` |
| `models/buildings/windows_vert` | `VertexLitGeneric` | `concrete` | `model` | `1` | `models/buildings/windows_vert` |
| `models/coast/coast_desk` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/coast_desk` |
| `models/coast/coast_pontoon` | `VertexlitGeneric` | `-` | `model` | `0` | `models/coast/coast_pontoon` |
| `models/coast/coast_pontoon_strap` | `VertexlitGeneric` | `-` | `model` | `0` | `models/coast/coast_pontoon_strap` |
| `models/coast/container01` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/container01` |
| `models/coast/container01_large` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/container01_large` |
| `models/coast/container01_large_open` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/container01_large_open` |
| `models/coast/container01_large_open_inside` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/container01_large_open_inside` |
| `models/coast/container01_open` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/container01_open` |
| `models/coast/container01_open_inside` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/container01_open_inside` |
| `models/coast/container02` | `vertexlitgeneric` | `-` | `model` | `0` | `models/cp_docks/container02` |
| `models/coast/container02_large` | `vertexlitgeneric` | `-` | `model` | `0` | `models/cp_docks/container02_large` |
| `models/coast/container03` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/container03` |
| `models/coast/container03_large` | `vertexlitgeneric` | `-` | `model` | `0` | `models/cp_docks/container03_large` |
| `models/coast/doorframe` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/doorframe` |
| `models/coast/forcefield` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/forcefield` |
| `models/coast/mooring` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/mooring` |
| `models/coast/plant_light_fibre` | `unlitgeneric` | `-` | `model` | `0` | `models/coast/plant_light_fibre` |
| `models/coast/plant_light_stem` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/plant_light_stem` |
| `models/coast/plant_pot_square` | `VertexlitGeneric` | `-` | `model` | `0` | `models/coast/plant_pot_square` |
| `models/coast/plant_pot_square1` | `VertexlitGeneric` | `-` | `model` | `0` | `models/coast/plant_pot_square1` |
| `models/coast/plant_pot_square2` | `VertexlitGeneric` | `-` | `model` | `0` | `models/coast/plant_pot_square2` |
| `models/coast/sculpture` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/sculpture` |
| `models/coast/stair_rail_middle` | `VertexlitGeneric` | `metal` | `model` | `0` | `models/coast/stair_rail_middle` |
| `models/coast/waste_bin` | `VertexlitGeneric` | `-` | `model` | `0` | `models/coast/waste_bin` |
| `models/coast/zettasec_box1` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/zettasec_box1` |
| `models/coast/zettasec_box1a` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/zettasec_box1a` |
| `models/coast/zettasec_box1b` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/zettasec_box1b` |
| `models/coast/zettasec_light` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/zettasec_light` |
| `models/coast/zettasec_light_glass` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/zettasec_light_glass` |
| `models/coast/zettasec_light_glass_refract` | `Refract` | `glass` | `model` | `0` | `-` |
| `models/coast/zettasec_logo` | `UnlitGeneric` | `-` | `model` | `0` | `models/coast/zettasec_logo` |
| `models/coast/zettasec_mat` | `vertexlitgeneric` | `-` | `model` | `0` | `models/coast/zettasec_mat` |
| `models/coast/zettasec_sign1` | `UnlitGeneric` | `-` | `model` | `0` | `models/coast/zettasec_sign1` |
| `models/coast/zettasec_sign2` | `UnlitGeneric` | `-` | `model` | `0` | `models/coast/zettasec_sign2` |
| `models/dys_bike/dystopia_bike` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/dys_bike/dystopia_bike` |
| `models/dys_bike/wheel` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/dys_bike/wheel` |
| `models/dys_bike/windshield` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/dys_bike/windshield` |
| `models/eu/BaseDiffuse` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/Eu/BaseDiffuse` |
| `models/eu/EUDiffuse` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/Eu/EUDiffuse` |
| `models/eu/PipeDiffuse` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/Eu/PipeDiffuse` |
| `models/eu/PumpDiffuse` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/Eu/PumpDiffuse` |
| `models/feanix/building01` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/feanix/building01Diffuse` |
| `models/feanix/building02` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/feanix/building02Diffuse` |
| `models/feanix/dnaScannerFlushScreenDisabled` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/feanix/dnaScannerFlushScreenDisabled` |
| `models/feanix/dnaScannerFlushScreenEnabled` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/feanix/dnaScannerFlushScreenEnabled` |
| `models/feanix/dnaScannerGooTube` | `UnlitGeneric` | `glass` | `model` | `0` | `models/feanix/dnaScannerGooTube` |
| `models/feanix/dnaScannerGooTubeExt` | `UnlitGeneric` | `glass` | `model` | `0` | `models/feanix/dnaScannerGooTube` |
| `models/feanix/dnaScannerMain` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/feanix/dnaScannerMainDiffuse` |
| `models/feanix/dnaScannerMainScreen` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/feanix/dnaScannerMainScreen` |
| `models/feanix/dnaScannerMainScreenIdleCorp` | `UnlitGeneric` | `glass` | `model` | `0` | `models/feanix/dnaScannerMainScreenIdleCorp` |
| `models/feanix/dnaScannerMainScreenIdlePunk` | `UnlitGeneric` | `glass` | `model` | `0` | `models/feanix/dnaScannerMainScreenIdlePunk` |
| `models/feanix/dnaScannerMainScreenReconfiguring` | `UnlitGeneric` | `glass` | `model` | `0` | `models/feanix/dnaScannerMainScreenReconfiguring` |
| `models/feanix/transportDiffuse` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/feanix/transportDiffuse` |
| `models/feanix/transportDiffuseDataTrust` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/feanix/transportDiffuseDatatrust` |
| `models/feanix/transportDiffuseQuetzuku` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/feanix/transportDiffuseQuetzuku` |
| `models/feanix/transportDiffuseUnmarked` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/feanix/transportDiffuseUnmarked` |
| `models/feanix/uhOhNautilusBeefCrunch` | `VertexLitGeneric` | `paper` | `model` | `0` | `models/feanix/ohOhNautilusBeefCrunchDiffuse` |
| `models/feanix/wallplates` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/feanix/wallplates` |
| `models/fortress/fence` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/fortress/fence` |
| `models/fortress/fort_arch` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/fortress/fort_arch` |
| `models/fortress/razor_page` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/fortress/razor_page` |
| `models/fortress/security_scanner` | `unlitGeneric` | `metal` | `model` | `0` | `models/fortress/security_scanner` |
| `models/items/Item_Bomb_armed` | `VertexlitGeneric` | `metal` | `model` | `0` | `models/items/Item_Bomb_armed` |
| `models/items/Item_Bomb_idle` | `VertexlitGeneric` | `metal` | `model` | `0` | `models/items/Item_Bomb_idle` |
| `models/items/Item_PDA` | `VertexlitGeneric` | `metal` | `model` | `0` | `models/items/Item_PDA` |
| `models/items/Item_PDA_Screen` | `VertexlitGeneric` | `metal` | `model` | `0` | `models/items/Item_PDA_Screen` |
| `models/items/datachunk` | `UnlitGeneric` | `-` | `model` | `0` | `models/items/datachunk` |
| `models/items/phistball_01` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/items/phistball_01` |
| `models/items/phistball_01_dx8` | `VertexLitGeneric` | `-` | `model` | `0` | `models/items/phistball_01` |
| `models/items/phistball_01_spec` | `VertexLitGeneric` | `-` | `model` | `0` | `models//items/phistball_01_spec` |
| `models/metal` | `vertexlitgeneric` | `-` | `model` | `0` | `models/metal` |
| `models/pillar01` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/urban/pillar01` |
| `models/player/corp_hands3` | `VertexLitGeneric` | `-` | `model` | `0` | `models/player/corp_hands3` |
| `models/player/corp_light_hands` | `VertexLitGeneric` | `-` | `model` | `0` | `models/player/corp_light_hands` |
| `models/player/cyber/cyberbabe` | `vertexlitgeneric` | `-` | `model` | `0` | `models/player/cyber/cyberbabe_blue` |
| `models/player/cyber/cyberbabe_punk` | `vertexlitgeneric` | `-` | `model` | `0` | `models/player/cyber/cyberbabe_red` |
| `models/player/gib_bone` | `VertexLitGeneric` | `-` | `model` | `0` | `models/player/gib_bone` |
| `models/player/gib_middle` | `VertexLitGeneric` | `-` | `model` | `0` | `models/player/gib_middle` |
| `models/player/gib_thermal` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/heavy_corp/corp_heavy_body` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/heavy_corp/corp_heavy_body` |
| `models/player/heavy_corp/corp_heavy_body_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/heavy_corp/corp_heavy_body` |
| `models/player/heavy_corp/corp_heavy_body_red` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/heavy_corp/corp_heavy_body_red` |
| `models/player/heavy_corp/corp_heavy_body_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/heavy_corp/corp_heavy_head` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/heavy_corp/corp_heavy_head` |
| `models/player/heavy_corp/corp_heavy_head_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/heavy_corp/corp_heavy_head` |
| `models/player/heavy_corp/corp_heavy_head_red` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/heavy_corp/corp_heavy_head_red` |
| `models/player/heavy_corp/corp_heavy_head_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/heavy_punk/body` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/heavy_punk/body` |
| `models/player/heavy_punk/body_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/heavy_punk/body` |
| `models/player/heavy_punk/body_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/heavy_punk/extras` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/heavy_punk/extras` |
| `models/player/heavy_punk/extras_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/heavy_punk/extras` |
| `models/player/heavy_punk/extras_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/ledgegrab/corp_hands3` | `VertexLitGeneric` | `-` | `model` | `0` | `models/player/ledgegrab/corp_hands3` |
| `models/player/ledgegrab/corp_light_hands` | `VertexLitGeneric` | `-` | `model` | `0` | `models/player/ledgegrab/corp_light_hands` |
| `models/player/ledgegrab/punk_hands3` | `VertexLitGeneric` | `-` | `model` | `0` | `models/player/ledgegrab/punk_hands3` |
| `models/player/ledgegrab/punk_light_hands` | `VertexLitGeneric` | `-` | `model` | `0` | `models/player/ledgegrab/punk_light_hands` |
| `models/player/light_corp/Corp_Headshot` | `vertexlitgeneric` | `-` | `model` | `0` | `models/player/light_corp/Corp_Headshot` |
| `models/player/light_corp/Corp_head` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/light_corp/Corp_Head` |
| `models/player/light_corp/Corp_head_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/light_corp/Corp_Head` |
| `models/player/light_corp/Corp_head_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/light_corp/Corp_vortwarp` | `VortWarp` | `-` | `model` | `0` | `models/player/light_corp/Corp_Bodya` |
| `models/player/light_corp/corp_body_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/light_corp/corp_bodya` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/light_corp/corp_Bodya` |
| `models/player/light_corp/corp_bodya_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/light_corp/corp_Bodya` |
| `models/player/light_corp/corp_bodya_gibbed` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/light_corp/corp_bodya_gibbed` |
| `models/player/light_punk/Punk_vortwarp` | `VortWarp` | `-` | `model` | `0` | `models/player/light_punk/dys_punkbody_light02` |
| `models/player/light_punk/dys_punkbody_light02` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/light_punk/dys_punkbody_light02` |
| `models/player/light_punk/dys_punkbody_light02_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/light_punk/dys_punkbody_light02` |
| `models/player/light_punk/dys_punkbody_light_gibbed` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/light_punk/dys_punkbody_light_gibbed` |
| `models/player/light_punk/dys_punkbody_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/light_punk/dys_punkhead_light02` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/light_punk/dys_punkhead_light02` |
| `models/player/light_punk/dys_punkhead_light02_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/light_punk/dys_punkhead_light02` |
| `models/player/light_punk/dys_punkhead_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/light_punk/dys_punkheadshot` | `vertexlitgeneric` | `-` | `model` | `0` | `models/player/light_punk/dys_punkheadshot` |
| `models/player/light_punk/dys_punkheadshot_thermal` | `vertexlitgeneric` | `-` | `model` | `0` | `models/player/light_punk/dys_punkheadshot_thermal` |
| `models/player/med_corp/c_trooper_medium_body` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/med_corp/c_trooper_medium_body` |
| `models/player/med_corp/c_trooper_medium_body_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/med_corp/c_trooper_medium_body` |
| `models/player/med_corp/c_trooper_medium_body_gibbed` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/med_corp/c_trooper_medium_body_gibbed` |
| `models/player/med_corp/c_trooper_medium_body_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/med_corp/c_trooper_medium_extras` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/med_corp/c_trooper_medium_extras` |
| `models/player/med_corp/c_trooper_medium_extras_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/med_corp/c_trooper_medium_extras` |
| `models/player/med_corp/c_trooper_medium_extras_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/med_corp/c_trooper_medium_head` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/med_corp/c_trooper_medium_head` |
| `models/player/med_corp/c_trooper_medium_head_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/player/med_corp/c_trooper_medium_head` |
| `models/player/med_corp/c_trooper_medium_head_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/med_corp/c_trooper_medium_headshot` | `vertexlitgeneric` | `-` | `model` | `0` | `models/player/med_corp/c_trooper_medium_headshot` |
| `models/player/med_punk/dys_punkhed` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/med_punk/dys_punkhed_new` |
| `models/player/med_punk/dys_punkhed_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/med_punk/dys_punkhed_new` |
| `models/player/med_punk/dys_punkhed_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/med_punk/dys_punkhedshot` | `vertexlitgeneric` | `-` | `model` | `0` | `models/player/med_punk/dys_punkhedshot` |
| `models/player/med_punk/dys_punkmed` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/med_punk/dys_punkmed_new` |
| `models/player/med_punk/dys_punkmed_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/med_punk/dys_punkmed_new` |
| `models/player/med_punk/dys_punkmed_gibbed` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/player/med_punk/dys_punkmed_gibbed` |
| `models/player/med_punk/dys_punkmed_therm` | `Patch` | `-` | `model` | `0` | `-` |
| `models/player/predator` | `Refract` | `flesh` | `model` | `0` | `-` |
| `models/player/predator_dx7` | `UnlitGeneric` | `flesh` | `model` | `0` | `models/player/predator` |
| `models/player/punk_hands2` | `VertexLitGeneric` | `-` | `model` | `0` | `models/player/punk_hands2` |
| `models/player/punk_hands3` | `VertexLitGeneric` | `-` | `model` | `0` | `models/player/punk_hands3` |
| `models/player/punk_light_hands` | `VertexLitGeneric` | `-` | `model` | `0` | `models/player/punk_light_hands` |
| `models/propper/assemble/cath_windows01` | `vertexlitgeneric` | `glass` | `model` | `0` | `termireal1/cath_windows01` |
| `models/propper/assemble/cath_windows02_round` | `vertexlitgeneric` | `glass` | `model` | `0` | `termireal1/cath_windows02_round` |
| `models/propper/assemble/stonetrim_001` | `vertexlitgeneric` | `concrete` | `model` | `0` | `stone/stonetrim_001` |
| `models/propper/assemble/stonewall_001` | `vertexlitgeneric` | `concrete` | `model` | `0` | `stone/stonewall_001` |
| `models/propper/assemble/stonewall_002` | `vertexlitgeneric` | `concrete` | `model` | `0` | `stone/stonewall_002` |
| `models/propper/cybernetic/cyb_node_datahouse/cyber_floor_ring_ani` | `unlitgeneric` | `-` | `model` | `0` | `dys_cybernetic/cyber_floor_ring_ani` |
| `models/propper/cybernetic/cyb_node_datahouse/sky_01` | `unlitgeneric` | `metal` | `model` | `0` | `cyberspace/sky_01` |
| `models/propper/cybernetic/cyb_node_datahouse/sweeper2` | `unlitgeneric` | `-` | `model` | `0` | `cysp2/sweeper2` |
| `models/propper/cybernetic/cyb_node_datahouse/twin_cyberwhite` | `unlitgeneric` | `metal` | `model` | `0` | `twincannon/twin_cyberwhite` |
| `models/propper/cybernetic/cyb_node_info1/cyber_ring` | `unlitgeneric` | `-` | `model` | `0` | `dys_cybernetic/cyber_ring` |
| `models/propper/cybernetic/cyb_node_info1/node_info` | `unlitgeneric` | `-` | `model` | `0` | `dys_cybernetic/node_info` |
| `models/propper/cybernetic/cyb_node_info2/cyber_ring` | `unlitgeneric` | `-` | `model` | `0` | `dys_cybernetic/cyber_ring` |
| `models/propper/cybernetic/cyb_node_info2/node_info` | `unlitgeneric` | `-` | `model` | `0` | `dys_cybernetic/node_info` |
| `models/propper/cybernetic/cyb_node_info3/node_info` | `unlitgeneric` | `-` | `model` | `0` | `dys_cybernetic/node_info` |
| `models/propper/cybernetic/cyb_sky_1/gen18` | `$basetexture` | `-` | `model` | `0` | `buildings/gen18` |
| `models/propper/cybernetic/cyb_sky_1/metalhull013a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalhull013a` |
| `models/propper/cybernetic/cyb_sky_1/metalroof008a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalroof008a` |
| `models/propper/cybernetic/cyb_sky_2/building_windows` | `vertexlitgeneric` | `-` | `model` | `0` | `dys_cybernetic/building_windows` |
| `models/propper/cybernetic/cyb_sky_2/dark_building_windows` | `vertexlitgeneric` | `-` | `model` | `0` | `dys_cybernetic/dark_building_windows` |
| `models/propper/cybernetic/cyb_sky_2/dys_fortress-dys_vacextwallsmall` | `vertexlitgeneric` | `metal` | `model` | `0` | `/dys_fortress/dys_fortress-dys_vacextwallsmall` |
| `models/propper/cybernetic/cyb_sky_2/grav_lift_lights` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_cybernetic/grav_lift_lights` |
| `models/propper/cybernetic/cyb_sky_2/metal_dark_indoors` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_cybernetic/metal_dark_indoors` |
| `models/propper/cybernetic/cyb_sky_2/metal_panal_single` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_cybernetic/metal_panal_single` |
| `models/propper/cybernetic/cyb_sky_2/metalhull013a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalhull013a` |
| `models/propper/cybernetic/cyb_sky_2/metalroof006a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalroof006a` |
| `models/propper/cybernetic/cyb_sky_2/metaltruss002a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metaltruss002a` |
| `models/propper/cybernetic/cyb_sky_2/metalwall060a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalwall060a` |
| `models/propper/cybernetic/cyb_sky_3/gen01` | `$basetexture` | `-` | `model` | `0` | `buildings/gen01` |
| `models/propper/cybernetic/cyb_sky_3/grav_lift_lights` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_cybernetic/grav_lift_lights` |
| `models/propper/cybernetic/cyb_sky_3/metalroof006a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalroof006a` |
| `models/propper/cybernetic/cyb_sky_4/concretewall065a` | `vertexlitgeneric` | `concrete` | `model` | `0` | `concrete/concretewall065a` |
| `models/propper/cybernetic/cyb_sky_4/gen01` | `$basetexture` | `-` | `model` | `0` | `buildings/gen01` |
| `models/propper/cybernetic/cyb_sky_4/gen16` | `$basetexture` | `-` | `model` | `0` | `buildings/gen16` |
| `models/propper/cybernetic/cyb_sky_4/metalroof006a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalroof006a` |
| `models/propper/cybernetic/cyb_sky_4/pipes_cluster` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_cybernetic/pipes_cluster` |
| `models/propper/cybernetic/cybernetic_junction/camera1` | `unlitgeneric` | `-` | `model` | `0` | `_rt_camera1` |
| `models/propper/cybernetic/cybernetic_junction/light_trim` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_cybernetic/light_trim` |
| `models/propper/cybernetic/cybernetic_junction/metal_plate01` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_cybernetic/metal_plate01` |
| `models/propper/cybernetic/cybernetic_junction/metalhull013a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalhull013a` |
| `models/propper/cybernetic/cybernetic_junction/metalwall_001a_t_cheap` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalwall_001a_t` |
| `models/propper/cybernetic/cybernetic_junction/pipes_cluster` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_cybernetic/pipes_cluster` |
| `models/propper/cybernetic/cybernetic_junction/turbine_skin_002` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_cybernetic/turbine_skin_002` |
| `models/propper/cybernetic/cybernetic_outside_pipes/dys_vac_iris` | `vertexlitgeneric` | `metal` | `model` | `0` | `vaccine/dys_vac_iris` |
| `models/propper/cybernetic/cybernetic_outside_pipes/metaldoor059a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metaldoor059a` |
| `models/propper/cybernetic/cybernetic_outside_pipes/metalroof004a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalroof004a` |
| `models/propper/cybernetic/cybernetic_outside_pipes/wall_interior_007` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_cybernetic/wall_interior_007` |
| `models/propper/cybernetic/metalbox/dys_fortress-exterior1` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_fortress/dys_fortress-exterior1` |
| `models/propper/cybernetic/metalbox/dys_fortress-exterior2` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_fortress/dys_fortress-exterior2` |
| `models/propper/cybernetic/metalbox/metal_detail` | `vertexlitgeneric` | `metal` | `model` | `0` | `dys_cybernetic/metal_detail` |
| `models/propper/cybernetic/metalbox/metalhull013a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalhull013a` |
| `models/propper/undermine/circlet1` | `unlitgeneric` | `-` | `model` | `0` | `cyspfinal/circlet1` |
| `models/propper/undermine/circlet2` | `unlitgeneric` | `-` | `model` | `0` | `cyspfinal/circlet2` |
| `models/propper/undermine/circlet3` | `unlitgeneric` | `-` | `model` | `0` | `cyspfinal/circlet3` |
| `models/propper/undermine/cube256b` | `unlitgeneric` | `metal` | `model` | `0` | `detonate/cube256b` |
| `models/propper/undermine/cube_blue` | `unlitgeneric` | `metal` | `model` | `0` | `cyberspace/cube_blue` |
| `models/propper/undermine/cube_green2dark` | `unlitgeneric` | `metal` | `model` | `0` | `twincannon/cube_green2dark` |
| `models/propper/undermine/cube_green3` | `unlitgeneric` | `metal` | `model` | `0` | `twincannon/cube_green3` |
| `models/propper/undermine/cube_green_trans` | `unlitgeneric` | `metal` | `model` | `0` | `cyberspace/cube_green` |
| `models/propper/undermine/cube_red` | `unlitgeneric` | `metal` | `model` | `0` | `cyberspace/cube_red` |
| `models/propper/undermine/cyber_round_red` | `unlitgeneric` | `-` | `model` | `0` | `radioshack/cyber_round_red` |
| `models/propper/undermine/dys_spawnglow_green` | `unlitgeneric` | `-` | `model` | `0` | `twincannon/dys_spawnglow_green` |
| `models/propper/undermine/dys_vaccorpfloor2_bump` | `vertexlitgeneric` | `metal` | `model` | `0` | `vaccinert/dys_vaccorpfloor2` |
| `models/propper/undermine/metalfloor005a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalfloor005a` |
| `models/propper/undermine/metalfloor007a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalfloor007a` |
| `models/propper/undermine/metalhull003a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalhull003a` |
| `models/propper/undermine/metalroof005a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalroof005a` |
| `models/propper/undermine/metaltruss004a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metaltruss004a` |
| `models/propper/undermine/metaltruss008a` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metaltruss008a` |
| `models/propper/undermine/metalwall005b` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalwall005b` |
| `models/propper/undermine/metalwall018b` | `vertexlitgeneric` | `metal` | `model` | `0` | `metal/metalwall018b` |
| `models/propper/undermine/round_bluew` | `unlitgeneric` | `-` | `model` | `0` | `cysp2/round_bluew` |
| `models/propper/undermine/round_bluew2` | `unlitgeneric` | `-` | `model` | `0` | `cysp2/round_bluew2` |
| `models/propper/undermine/twin_cyberblack` | `unlitgeneric` | `metal` | `model` | `0` | `tools/toolsblack` |
| `models/propper/undermine/twin_cyberred` | `unlitgeneric` | `metal` | `model` | `0` | `twincannon/twin_cyberred` |
| `models/propper/undermine/twin_cyberwhite` | `unlitgeneric` | `metal` | `model` | `0` | `twincannon/twin_cyberwhite` |
| `models/propper/undermine/woodbeam002a` | `vertexlitgeneric` | `wood` | `model` | `0` | `wood/woodbeam002a` |
| `models/propper/undermine/woodwall037a` | `vertexlitgeneric` | `wood` | `model` | `0` | `wood/woodwall037a` |
| `models/props/BruteDamaged_basetex1` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/BruteDamaged_basetex1` |
| `models/props/CoolingTankBubbles` | `VertexLitGeneric` | `-` | `model` | `0` | `models/props/CoolingTankBubbles` |
| `models/props/CoolingTankDiffuse` | `VertexLitGeneric` | `-` | `model` | `0` | `models/props/CoolingTankDiffuse` |
| `models/props/CoolingTankWater` | `Refract` | `water` | `model` | `0` | `-` |
| `models/props/Dys_VendingMachine01a` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/Dys_VendingMachine01a` |
| `models/props/Dys_VendingMachine01a_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/Dys_VendingMachine01a` |
| `models/props/Dys_VendingMachine01b` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/Dys_VendingMachine01b` |
| `models/props/Dys_VendingMachine01b_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/Dys_VendingMachine01b` |
| `models/props/Dys_VendingMachine01c` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/Dys_VendingMachine01c` |
| `models/props/Dys_VendingMachine01c_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/Dys_VendingMachine01c` |
| `models/props/Dys_VendingMachine01d` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/Dys_VendingMachine01d` |
| `models/props/Dys_VendingMachine01d_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/Dys_VendingMachine01d` |
| `models/props/ICBM` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/ICBM` |
| `models/props/RubbishBinTex` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/RubbishBinTex` |
| `models/props/aerialsTex` | `VertexLitGeneric` | `-` | `model` | `0` | `models/props/aerialsTex` |
| `models/props/ammo_disp_skin` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/ammo_disp_skin` |
| `models/props/ammo_disp_skin_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/ammo_disp_skin` |
| `models/props/core/dystopia_core` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/core/dystopia_core` |
| `models/props/core/dystopiacore_top` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/core/dystopiacore_top` |
| `models/props/core/spec_dystopia_core` | `VertexLitGeneric` | `-` | `model` | `0` | `models/props/core/spec_dystopia_core` |
| `models/props/core/spec_dystopiacore_top` | `VertexLitGeneric` | `-` | `model` | `0` | `models/props/core/spec_dystopiacore_top` |
| `models/props/cs_office/chair_office` | `$basetexture` | `-` | `model` | `0` | `models/props/cs_office/chair_office` |
| `models/props/cs_office/coffee_mug` | `$basetexture` | `-` | `model` | `0` | `models/props/cs_office/coffee_mug` |
| `models/props/cs_office/coffee_mug2` | `$basetexture` | `-` | `model` | `0` | `models/props/cs_office/coffee_mug2` |
| `models/props/cs_office/coffee_mug3` | `$basetexture` | `-` | `model` | `0` | `models/props/cs_office/coffee_mug3` |
| `models/props/cs_office/computer` | `$basetexture` | `-` | `model` | `0` | `models/props/cs_office/computer` |
| `models/props/cs_office/screen` | `$basetexture` | `-` | `model` | `0` | `models/props/cs_office/screen` |
| `models/props/cs_office/screenb` | `$basetexture` | `-` | `model` | `0` | `models/props/cs_office/screenb` |
| `models/props/cs_office/shelves_metal` | `$basetexture` | `-` | `model` | `0` | `models/props/cs_office/shelves_metal` |
| `models/props/cs_office/tv_plasma` | `$basetexture` | `-` | `model` | `0` | `models/props/cs_office/tv_plasma` |
| `models/props/cs_office/tv_plasma_p` | `$basetexture` | `-` | `model` | `0` | `models/props/cs_office/tv_plasma_p` |
| `models/props/curvedRailing_yellow` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/curvedRailing_yellow` |
| `models/props/cyberalarm` | `UnlitGeneric` | `metal` | `model` | `0` | `models/props/cyberalarm` |
| `models/props/cybermine` | `UnlitGeneric` | `metal` | `model` | `0` | `models/props/cybermine` |
| `models/props/cybershard` | `UnlitGeneric` | `metal` | `model` | `0` | `models/props/cybershard` |
| `models/props/cybershard_ring` | `UnlitGeneric` | `metal` | `model` | `0` | `models/props/cybershard_ring` |
| `models/props/de_train/barrel0001` | `$basetexture` | `-` | `model` | `0` | `models/props/de_train/barrel0001` |
| `models/props/de_train/barrel0002` | `$basetexture` | `-` | `model` | `0` | `models/props/de_train/barrel0002` |
| `models/props/de_train/barrel0003` | `$basetexture` | `-` | `model` | `0` | `models/props/de_train/barrel0003` |
| `models/props/de_train/barrel0004` | `$basetexture` | `-` | `model` | `0` | `models/props/de_train/barrel0004` |
| `models/props/de_train/barrel0005` | `$basetexture` | `-` | `model` | `0` | `models/props/de_train/barrel0005` |
| `models/props/de_train/barrel0006` | `$basetexture` | `-` | `model` | `0` | `models/props/de_train/barrel0006` |
| `models/props/de_train/barrel0007` | `$basetexture` | `-` | `model` | `0` | `models/props/de_train/barrel0007` |
| `models/props/de_train/barrel0008` | `$basetexture` | `-` | `model` | `0` | `models/props/de_train/barrel0008` |
| `models/props/dys_battery` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_battery` |
| `models/props/dys_battery_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_battery` |
| `models/props/dys_battery_grill` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_battery_grill` |
| `models/props/dys_dome_thingy` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_dome_thingy` |
| `models/props/dys_power_core` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_power_core` |
| `models/props/dys_power_core_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_power_core` |
| `models/props/dys_roof_dome` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_roof_dome` |
| `models/props/dys_roof_dome_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_roof_dome` |
| `models/props/dys_silo_transport` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_silo_transport` |
| `models/props/dys_turret` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_turret` |
| `models/props/dys_tv` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_tv` |
| `models/props/dys_tv_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/dys_tv` |
| `models/props/fort_arch` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/fort_arch` |
| `models/props/grey` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/grey` |
| `models/props/grey2` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/grey2` |
| `models/props/jackpoint` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/jackpoint` |
| `models/props/jackpoint2` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/jackpoint2` |
| `models/props/jackpoint2_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/jackpoint2` |
| `models/props/jackpoint_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/jackpoint` |
| `models/props/jackpoint_public` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/jackpoint_public` |
| `models/props/jackpoint_public_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/jackpoint_public` |
| `models/props/jackpoint_public_grid` | `VertexLitGeneric` | `-` | `model` | `0` | `models/props/jackpoint_public_grid` |
| `models/props/jackpoint_public_grid2_ba` | `UnlitTwoTexture` | `-` | `model` | `0` | `models/props/jackpoint_holo` |
| `models/props/jackpoint_public_grid2_bb` | `UnlitTwoTexture` | `-` | `model` | `0` | `models/props/jackpoint_holo` |
| `models/props/jackpoint_public_grid2_ra` | `UnlitTwoTexture` | `-` | `model` | `0` | `models/props/jackpoint_holo` |
| `models/props/jackpoint_public_grid2_rb` | `UnlitTwoTexture` | `-` | `model` | `0` | `models/props/jackpoint_holo` |
| `models/props/jackpoint_public_grid2_sb` | `UnlitTwoTexture` | `-` | `model` | `0` | `models/props/jackpoint_holo_sb` |
| `models/props/jackpoint_public_grid_ba` | `UnlitTwoTexture` | `-` | `model` | `0` | `models/props/jackpoint_public_grid_blue` |
| `models/props/jackpoint_public_grid_bb` | `UnlitTwoTexture` | `-` | `model` | `0` | `models/props/jackpoint_public_grid_blue` |
| `models/props/jackpoint_public_grid_ra` | `UnlitTwoTexture` | `-` | `model` | `0` | `models/props/jackpoint_public_grid` |
| `models/props/jackpoint_public_grid_rb` | `UnlitTwoTexture` | `-` | `model` | `0` | `models/props/jackpoint_public_grid` |
| `models/props/jackpoint_pubpunk` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/jackpoint_pubpunk` |
| `models/props/jackpoint_pubpunk2` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/jackpoint_pubpunk2` |
| `models/props/jackpoint_pubpunk2_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/jackpoint_pubpunk2` |
| `models/props/jackpoint_pubpunk_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/jackpoint_pubpunk` |
| `models/props/jackpoint_pubpunk_extras` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/jackpoint_pubpunk_extras` |
| `models/props/jackpoint_punk` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/jackpoint_punk` |
| `models/props/jackpoint_punk_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/jackpoint_punk` |
| `models/props/missile` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/missile` |
| `models/props/pipes_rad2` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/pipes_rad2` |
| `models/props/pipes_rad2_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/pipes_rad2` |
| `models/props/plastic` | `vertexlitgeneric` | `plastic` | `model` | `0` | `models/props/plastic` |
| `models/props/prop_city_trashcan1_01` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/prop_city_trashcan1_01` |
| `models/props/prop_city_trashcan1_normal` | `LightmappedGeneric` | `-` | `model` | `0` | `models/props/prop_city_trashcan1_normal` |
| `models/props/prop_trolley` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/prop_trolley` |
| `models/props/spawner` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/spawner` |
| `models/props/spawner_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/spawner` |
| `models/props/tube_prop` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/tube_prop` |
| `models/props/tube_prop_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/tube_prop` |
| `models/props/urbanScreen_awn` | `VertexLitGeneric` | `grate` | `model` | `0` | `models/props/urbanScreen_awn` |
| `models/props/urbanScreen_ide` | `VertexLitGeneric` | `-` | `model` | `0` | `models/props/urbanScreen_ide` |
| `models/props/urbanScreen_screen` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/props/urbanScreen_screen` |
| `models/props/ventLight` | `VertexLitGeneric` | `-` | `model` | `0` | `models/props/ventLight` |
| `models/props/zepSkin` | `VertexLitGeneric` | `-` | `model` | `0` | `models/props/zepSkin` |
| `models/props_buildings/factory_skybox001a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_buildings/factory_skybox001a` |
| `models/props_c17/chair_office01a` | `VertexLitGeneric` | `dirt` | `model` | `0` | `Models/props_c17/chair_office01a` |
| `models/props_junk/PopCan01a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan01a` |
| `models/props_junk/PopCan01b` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan01a` |
| `models/props_junk/PopCan02a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan02a` |
| `models/props_junk/PopCan03a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan03a` |
| `models/props_junk/PopCan04a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan04a` |
| `models/props_junk/PopCan05a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan05a` |
| `models/props_junk/PopCan06a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan06a` |
| `models/props_junk/PopCan07a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan07a` |
| `models/props_junk/PopCan08a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan08a` |
| `models/props_junk/PopCan09a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan09a` |
| `models/props_junk/PopCan10a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan10a` |
| `models/props_junk/PopCan11a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan11a` |
| `models/props_junk/PopCan12a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan12a` |
| `models/props_junk/PopCan13a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan13a` |
| `models/props_junk/PopCan14a` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_junk/PopCan14a` |
| `models/props_pipes/pipeset_metal` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/props_pipes/pipeset_metal` |
| `models/props_pipes/pipeset_metal02` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/props_pipes/pipeset_metal02` |
| `models/props_pipes/pipeset_metal02_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_pipes/pipeset_metal02` |
| `models/props_pipes/pipeset_metal_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/props_pipes/pipeset_metal` |
| `models/radioshack/DJboothTexMain` | `VertexLitGeneric` | `-` | `model` | `0` | `models/radioshack/DJboothTexMain` |
| `models/ryoku/lightpole_fixed/color` | `VertexLitGeneric` | `-` | `model` | `0` | `lightpole/color` |
| `models/ryoku/lightpole_fixed/transperency` | `LightmappedGeneric` | `-` | `model` | `0` | `lightpole/trancperency` |
| `models/screen_glow` | `UnlitGeneric` | `-` | `model` | `0` | `models/urban/screen_glow` |
| `models/shells/assault/assault` | `vertexlitgeneric` | `-` | `model` | `0` | `models/shells/assault/assault` |
| `models/shells/duals/duals` | `vertexlitgeneric` | `-` | `model` | `0` | `models/shells/duals/duals` |
| `models/shells/machpistol/machpistol` | `vertexlitgeneric` | `-` | `model` | `0` | `models/shells/machpistol/machpistol` |
| `models/shells/minigun/minigun` | `vertexlitgeneric` | `-` | `model` | `0` | `models/shells/minigun/minigun` |
| `models/shells/mk808/mk808` | `vertexlitgeneric` | `-` | `model` | `0` | `models/shells/mk808/mk808` |
| `models/shells/shotgun/shotgun_shell` | `vertexlitgeneric` | `-` | `model` | `0` | `models/shells/shotgun/shotgun_shell` |
| `models/spire/broadcast/Fan` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/Fan` |
| `models/spire/broadcast/bc_black` | `vertexlitgeneric` | `-` | `model` | `0` | `cable/black` |
| `models/spire/broadcast/bc_blocklight` | `unlitgeneric` | `-` | `model` | `0` | `tools/toolsblack` |
| `models/spire/broadcast/dna_details` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/dna_details` |
| `models/spire/broadcast/dna_pipes1` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/dna_pipes1` |
| `models/spire/broadcast/dna_pipes2` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/dna_pipes2` |
| `models/spire/broadcast/monitor01_arm` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor01_arm` |
| `models/spire/broadcast/monitor01_arm_dx8` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor01_arm` |
| `models/spire/broadcast/monitor01_cables` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor01_cables` |
| `models/spire/broadcast/monitor01_cables_dx8` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor01_cables` |
| `models/spire/broadcast/monitor01a` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor01a` |
| `models/spire/broadcast/monitor01a_dx8` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor01a` |
| `models/spire/broadcast/monitor01b` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor01b` |
| `models/spire/broadcast/monitor01b_dx8` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor01b` |
| `models/spire/broadcast/monitor02_arm` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor02_arm` |
| `models/spire/broadcast/monitor02_arm_dx8` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor02_arm` |
| `models/spire/broadcast/monitor02a` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor02a` |
| `models/spire/broadcast/monitor02a_dx8` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor02a` |
| `models/spire/broadcast/monitor02b` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor02b` |
| `models/spire/broadcast/monitor02b_dx8` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor02b` |
| `models/spire/broadcast/monitor_wallmount` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor_wallmount` |
| `models/spire/broadcast/monitor_wallmount_dx8` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/monitor_wallmount` |
| `models/spire/broadcast/punk_monitor1` | `vertexlitgeneric` | `-` | `model` | `0` | `_rt_camera1` |
| `models/spire/broadcast/punk_monitor1_dx8` | `unlitgeneric` | `-` | `model` | `0` | `_rt_camera1` |
| `models/spire/broadcast/punk_monitor2` | `vertexlitgeneric` | `-` | `model` | `0` | `_rt_camera2` |
| `models/spire/broadcast/punk_monitor2_dx8` | `unlitgeneric` | `-` | `model` | `0` | `_rt_camera2` |
| `models/spire/broadcast/punk_monitor3` | `vertexlitgeneric` | `-` | `model` | `0` | `_rt_camera3` |
| `models/spire/broadcast/punk_monitor3_dx8` | `unlitgeneric` | `-` | `model` | `0` | `_rt_camera3` |
| `models/spire/broadcast/punk_monitor4` | `vertexlitgeneric` | `-` | `model` | `0` | `_rt_camera4` |
| `models/spire/broadcast/punk_monitor4_dx8` | `unlitgeneric` | `-` | `model` | `0` | `_rt_camera4` |
| `models/spire/broadcast/punk_monitor_sb` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/punk_monitor_sb` |
| `models/spire/broadcast/s_pipeladder` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/broadcast/s_pipeladder` |
| `models/spire/broadcast/s_sewer1` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/s_sewer1` |
| `models/spire/broadcast/s_sewer2` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/s_sewer2` |
| `models/spire/broadcast/s_sewercover` | `vertexlitgeneric` | `concrete` | `model` | `0` | `models/spire/broadcast/s_sewercover` |
| `models/spire/broadcast/s_sewercover2` | `vertexlitgeneric` | `concrete` | `model` | `0` | `models/spire/broadcast/s_sewercover2` |
| `models/spire/broadcast/server/bc_server1` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/broadcast/server/bc_server1` |
| `models/spire/broadcast/server/bc_server2` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/broadcast/server/bc_server2` |
| `models/spire/broadcast/server/bc_server3` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/broadcast/server/bc_server3` |
| `models/spire/broadcast/server/bc_server_dtrust` | `unlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/server/bc_server_dtrust` |
| `models/spire/broadcast/server/bc_server_glass1` | `unlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/server/bc_server_glass` |
| `models/spire/broadcast/server/bc_server_glass2` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/server/bc_server_glass2` |
| `models/spire/broadcast/server/bc_server_glass3` | `unlitgeneric` | `-` | `model` | `0` | `tools/toolsblack` |
| `models/spire/broadcast/server/bc_server_glass_glow` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/server/bc_server_glass_glow` |
| `models/spire/broadcast/server/bc_servermount1` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/server/bc_servermount1` |
| `models/spire/broadcast/server/bc_servermount2` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/server/bc_servermount2` |
| `models/spire/broadcast/servergib/bc_server1` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/broadcast/servergib/bc_server1_gib` |
| `models/spire/broadcast/servergib/bc_server2` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/broadcast/servergib/bc_server2_gib` |
| `models/spire/broadcast/servergib/bc_server3` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/broadcast/server/bc_server3` |
| `models/spire/broadcast/servergib/bc_servermount1` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/broadcast/server/bc_servermount1` |
| `models/spire/broadcast/servergib/bc_servermount2` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/broadcast/servergib/bc_servermount2_gib` |
| `models/spire/broadcast/tech_glass` | `vertexlitgeneric` | `glass` | `model` | `0` | `models/spire/broadcast/tech_glass` |
| `models/spire/exogen` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/exogen` |
| `models/spire/exogen2` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/exogen2` |
| `models/spire/exogen_fins` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/exogen_fins` |
| `models/spire/goob1` | `Aftershock` | `-` | `model` | `0` | `-` |
| `models/spire/goob2` | `Aftershock` | `-` | `model` | `0` | `-` |
| `models/spire/neonsign` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/neonsign` |
| `models/spire/pipes/pipeset1_1` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/pipes/pipeset1_1` |
| `models/spire/pipes/pipeset1_2` | `vertexlitgeneric` | `-` | `model` | `0` | `models/spire/pipes/pipeset1_2` |
| `models/spire/pipes/pipeset1_corner1` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/pipes/pipeset1_corner1` |
| `models/spire/pipes/pipeset1_corner2` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/pipes/pipeset1_corner2` |
| `models/spire/pipes/pipeset1_end` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/pipes/pipeset1_end` |
| `models/spire/s_chair1` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/s_chair1` |
| `models/spire/s_chair1_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/s_chair1` |
| `models/spire/s_chair1p` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/s_chair1p` |
| `models/spire/s_chair1p_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/spire/s_chair1p` |
| `models/street_light01` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/street_light01` |
| `models/termi/t_arco_skybox` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_arco_skybox` |
| `models/termi/t_arco_skybox_big` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_arco_skybox_big` |
| `models/termi/t_arcoentry` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/termi/t_arcoentry` |
| `models/termi/t_asm_pipes` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_asm_pipes` |
| `models/termi/t_asmlaser_assembly` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_asmlaser_assembly` |
| `models/termi/t_asmlaser_base` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_asmlaser_base` |
| `models/termi/t_asmlaser_clamp` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_asmlaser_clamp` |
| `models/termi/t_asmlaser_gun` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_asmlaser_gun` |
| `models/termi/t_asmlaser_scope` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_asmlaser_scope` |
| `models/termi/t_asmpillar1` | `VertexLitGeneric` | `stone` | `model` | `0` | `models/termi/t_asmpillar1` |
| `models/termi/t_asmrails1` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_asmrails1` |
| `models/termi/t_asmrails1_cheap` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_asmrails1` |
| `models/termi/t_box_texture` | `VertexLitGeneric` | `wood` | `model` | `0` | `models/termi/t_box_texture` |
| `models/termi/t_cablelay1` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_cablelay1` |
| `models/termi/t_coolerbottom` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_coolerbottom` |
| `models/termi/t_coolertop` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_coolertop` |
| `models/termi/t_cr_cable_1` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_cr_cable_1` |
| `models/termi/t_cr_jipmount` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_cr_jipmount` |
| `models/termi/t_cr_roofdetail` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_cr_roofdetail` |
| `models/termi/t_cr_screen` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_cr_screen` |
| `models/termi/t_cratewpal` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_cratewpal` |
| `models/termi/t_cs_floorpipes` | `vertexlitGeneric` | `-` | `model` | `0` | `models/termi/t_cs_floorpipes2` |
| `models/termi/t_cs_pillars` | `vertexlitGeneric` | `-` | `model` | `0` | `models/termi/t_cs_pillars2` |
| `models/termi/t_cyberpod1_girl` | `VertexLitGeneric` | `flesh` | `model` | `0` | `models/termi/t_cyberpod1_girl` |
| `models/termi/t_cyberpod1_glass` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/termi/t_cyberpod1_pod` |
| `models/termi/t_cyberpod1_glass_opaque` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/termi/t_cyberpod1_pod` |
| `models/termi/t_cyberpod1_pod` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_cyberpod1_pod` |
| `models/termi/t_domething` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_domething` |
| `models/termi/t_domething_sphere` | `UnlitTwoTexture` | `no_decal` | `model` | `0` | `models/termi/t_domething_sphere` |
| `models/termi/t_dtrustcrate128` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_dtrustcrate128` |
| `models/termi/t_dtrustcrate48` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_dtrustcrate48` |
| `models/termi/t_exodusdish` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_exodusdish` |
| `models/termi/t_exoduspipes1` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/termi/t_exoduspipes1` |
| `models/termi/t_exoduspipes1_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/termi/t_exoduspipes1` |
| `models/termi/t_exodussecmon` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_exodussecmon` |
| `models/termi/t_exodussecmon2` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_exodussecmon2` |
| `models/termi/t_exofloorplates` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/termi/t_exofloorplates` |
| `models/termi/t_exofloorplates_dx8` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/termi/t_exodusfloorplates` |
| `models/termi/t_inj_cable1` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_inj_cable1` |
| `models/termi/t_inj_cable2` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_inj_cable2` |
| `models/termi/t_inj_cs_obj2` | `Vertexlitgeneric` | `-` | `model` | `0` | `models/termi/t_inj_cs_obj2_wave2` |
| `models/termi/t_inj_cs_obj2_dx8` | `Unlittwotexture` | `-` | `model` | `0` | `models/termi/t_inj_cs_obj2` |
| `models/termi/t_inj_cs_obj2_glass` | `UnlitGeneric` | `-` | `model` | `0` | `models/termi/t_inj_cs_obj2` |
| `models/termi/t_inj_doorframe` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_inj_doorframe` |
| `models/termi/t_inj_outsidefence` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_inj_outsidefence` |
| `models/termi/t_inj_pilons` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_inj_pilons` |
| `models/termi/t_inj_pilons_glass` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_inj_pilons` |
| `models/termi/t_inj_ring` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_inj_ring` |
| `models/termi/t_inj_wallbase` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_inj_wallbase` |
| `models/termi/t_inj_wallbit` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_inj_wallbit` |
| `models/termi/t_injec_skybox` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_injec_skybox` |
| `models/termi/t_injectiondoor` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_injectiondoor_clean` |
| `models/termi/t_injectiondoor_base` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_injectiondoor_base` |
| `models/termi/t_injectiondoor_dirty` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_injectiondoor_dirty` |
| `models/termi/t_keyboard02` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_keyboard02` |
| `models/termi/t_laser` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_laser` |
| `models/termi/t_light1` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_light1` |
| `models/termi/t_light_crate` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_light_crate` |
| `models/termi/t_monitor1a` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_monitor1a` |
| `models/termi/t_monitor1b` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_monitor1b` |
| `models/termi/t_monitor1c` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_monitor1c` |
| `models/termi/t_propcan1` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_propcan1` |
| `models/termi/t_qbox1_128` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_qbox1_128` |
| `models/termi/t_qbox1_40` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_qbox1_40` |
| `models/termi/t_qbox2_64` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_qbox2_64` |
| `models/termi/t_railing01` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_railing01` |
| `models/termi/t_railing01_corner` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_railing01_corner` |
| `models/termi/t_ringlight` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_ringlight` |
| `models/termi/t_satellite` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_satellite` |
| `models/termi/t_secorpsign` | `VertexLitGeneric` | `plastic` | `model` | `0` | `models/termi/t_secorpsign` |
| `models/termi/t_shippingcrate01` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_shippingcrate01` |
| `models/termi/t_shippingcrate02` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_shippingcrate02` |
| `models/termi/t_shippingcrate03` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_shippingcrate03` |
| `models/termi/t_shippingcrate04` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_shippingcrate04` |
| `models/termi/t_signhanger1` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_signhanger1` |
| `models/termi/t_spawncrate` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_spawncrate` |
| `models/termi/t_undermine_monitoring1` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_undermine_monitoring1` |
| `models/termi/t_undermine_monitoring1_cables1` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_undermine_monitoring1_cables1` |
| `models/termi/t_undermine_monitoring1_cables1_dark` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_undermine_monitoring1_cables1` |
| `models/termi/t_undermine_monitoring1_cables2` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_undermine_monitoring1_cables2` |
| `models/termi/t_undermine_monitoring1_cables2_dark` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_undermine_monitoring1_cables2` |
| `models/termi/t_undermine_monitoring1_dark` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_undermine_monitoring1` |
| `models/termi/t_undermine_monitoring1_holo1` | `UnlitTwoTexture` | `no_decal` | `model` | `0` | `models/termi/t_undermine_monitoring1_holomask` |
| `models/termi/t_undermine_monitoring1a` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_undermine_monitoring1a` |
| `models/termi/t_undermine_monitoring1a_dark` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_undermine_monitoring1a` |
| `models/termi/t_undermine_struts` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_undermine_struts` |
| `models/termi/t_vaccore_1` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/player/cyber/cyberbabe_blue` |
| `models/termi/t_vaccore_2` | `UnlitTwoTexture` | `no_decal` | `model` | `0` | `models/termi/t_vacccore` |
| `models/termi/t_wallthing1` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_wallthing1` |
| `models/termi/t_wallthing1a` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_wallthing1a` |
| `models/termi/t_wallvent1` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/termi/t_wallvent1` |
| `models/termi/t_wastebasket` | `VertexLitGeneric` | `-` | `model` | `0` | `models/termi/t_wastebasket` |
| `models/termi/test_vac_cooler` | `VertexLitGeneric` | `wood` | `model` | `0` | `models/termi/test_vac_cooler` |
| `models/termi/wood_debris1` | `VertexLitGeneric` | `wood` | `model` | `0` | `Wood/woodfloor007a` |
| `models/termi/wood_debris2` | `VertexLitGeneric` | `wood` | `model` | `0` | `Wood/woodfloor001a` |
| `models/twincannon/ServerRackTex` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/ServerRackTex` |
| `models/twincannon/ball` | `vertexlitgeneric` | `plastic` | `model` | `0` | `models/twincannon/ball` |
| `models/twincannon/crate_datatrust` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/crate_datatrust_diffuse` |
| `models/twincannon/crate_dmt` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/crate_dmt_diffuse` |
| `models/twincannon/cyber_crystal1` | `UnlitGeneric` | `metal` | `model` | `0` | `models/twincannon/cyber_crystal1` |
| `models/twincannon/cyber_crystal2` | `UnlitGeneric` | `metal` | `model` | `0` | `models/twincannon/cyber_crystal2` |
| `models/twincannon/cyber_crystal3` | `UnlitGeneric` | `metal` | `model` | `0` | `models/twincannon/cyber_crystal3` |
| `models/twincannon/cyber_crystal4` | `UnlitGeneric` | `metal` | `model` | `0` | `models/twincannon/cyber_crystal4` |
| `models/twincannon/dys_fortress_curve` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/dys_fortress_curve` |
| `models/twincannon/dys_fortress_ffcable` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/dys_fortress_ffcable` |
| `models/twincannon/dys_fortress_ffglow` | `UnlitTwoTexture` | `no_decal` | `model` | `0` | `models/twincannon/dys_fortress_ffglow` |
| `models/twincannon/dys_fortress_forcefield` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/dys_fortress_forcefield` |
| `models/twincannon/dys_fortress_tollbarrier` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/dys_fortress_tollbarrier` |
| `models/twincannon/dys_office_filingcabinet` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/dys_office_filingcabinet` |
| `models/twincannon/dys_office_painting` | `vertexlitgeneric` | `wood` | `model` | `0` | `models/twincannon/dys_office_painting` |
| `models/twincannon/dys_office_painting_2` | `vertexlitgeneric` | `wood` | `model` | `0` | `models/twincannon/dys_office_painting_2` |
| `models/twincannon/dys_office_painting_3` | `vertexlitgeneric` | `wood` | `model` | `0` | `models/twincannon/dys_office_painting_3` |
| `models/twincannon/dys_office_painting_4` | `vertexlitgeneric` | `wood` | `model` | `0` | `models/twincannon/dys_office_painting_4` |
| `models/twincannon/dys_office_painting_5` | `vertexlitgeneric` | `wood` | `model` | `0` | `models/twincannon/dys_office_painting_5` |
| `models/twincannon/dys_office_painting_6` | `vertexlitgeneric` | `wood` | `model` | `0` | `models/twincannon/dys_office_painting_6` |
| `models/twincannon/dys_office_stapler` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/dys_office_stapler` |
| `models/twincannon/dys_office_toilet` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/dys_office_toilet` |
| `models/twincannon/dys_office_tracklight_holder` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/dys_office_tracklight_holder` |
| `models/twincannon/dys_office_tracklight_light` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/dys_office_tracklight_light` |
| `models/twincannon/dys_wallmonitor` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/dys_wallmonitor` |
| `models/twincannon/dys_wallmonitor_nodtrust` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/dys_wallmonitor_nodtrust` |
| `models/twincannon/eu_top_light` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/eu_top_light` |
| `models/twincannon/ham` | `vertexlitgeneric` | `plastic` | `model` | `0` | `models/twincannon/ham` |
| `models/twincannon/plush_heavy` | `vertexlitgeneric` | `plush` | `model` | `0` | `models/twincannon/plush_heavy` |
| `models/twincannon/plush_heavy2` | `vertexlitgeneric` | `plush` | `model` | `0` | `models/twincannon/plush_heavy2` |
| `models/twincannon/stopsign` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/stopsign` |
| `models/twincannon/um_3screenconsole` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/twincannon/um_3screenconsole` |
| `models/urban/Cryotec_logo` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/Cryotec_logo` |
| `models/urban/P_advertpole_pipe` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/p_advertpole_pipe` |
| `models/urban/P_advertpole_pole01` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/urban/p_advertpole_pole01` |
| `models/urban/P_advertpole_screen` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/urban/p_advertpole_screen` |
| `models/urban/P_advertpole_visor` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/urban/p_advertpole_Visor` |
| `models/urban/P_monitor_pole01` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/p_monitor_pole01` |
| `models/urban/Storefront_Template001a` | `VertexLitGeneric` | `concrete` | `model` | `0` | `Storefront_Template/Storefront_Template001a` |
| `models/urban/Storefront_Template001g` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/urban/Storefront_Template001g` |
| `models/urban/advert_baked01` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/advert_baked01` |
| `models/urban/black_awning` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/black_awning` |
| `models/urban/cryo_glow` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/cryo_glow` |
| `models/urban/glasswindow070c` | `VertexLitGeneric` | `glass` | `model` | `0` | `Glass/glasswindow070c` |
| `models/urban/lightpole_glow1` | `unlitGeneric` | `glass` | `model` | `1` | `models/urban/lightpole_glow1` |
| `models/urban/metalrail` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/metalrail` |
| `models/urban/orange_glow` | `VertexLitGeneric` | `glass` | `model` | `0` | `models/urban/orange_glow` |
| `models/urban/pillar01` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/urban/pillar01` |
| `models/urban/powerpole` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/powerpole` |
| `models/urban/rubbertrainfloor001a` | `VertexLitGeneric` | `rubber` | `model` | `0` | `models/urban/rubbertrainfloor001a` |
| `models/urban/screen_glow` | `UnlitGeneric` | `-` | `model` | `0` | `models/urban/screen_glow` |
| `models/urban/street_light01` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/street_light01` |
| `models/urban/tall01` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/urban/tall01` |
| `models/urban/tall02` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/urban/tall02` |
| `models/urban/tall03` | `VertexLitGeneric` | `concrete` | `model` | `0` | `models/urban/tall03` |
| `models/urban/tilefloor016a` | `VertexLitGeneric` | `tile` | `model` | `0` | `models/urban/tilefloor016a` |
| `models/urban/white_awning` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/white_awning` |
| `models/urban/yellow_stripes` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/yellow_stripes` |
| `models/urbanrisk/urbanrisk_pilon` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urbanrisk/urbanrisk_pilon` |
| `models/vehicles/brute_darkgrey` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/vehicles/brute_darkgrey` |
| `models/vehicles/transportSkin` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/vehicles/transportSkin` |
| `models/warby/dys_prop_warby_core_01` | `VertexLitGeneric` | `-` | `model` | `0` | `models/warby/dys_prop_warby_core_01` |
| `models/warby/dys_prop_warby_furnace_metal_01` | `VertexLitGeneric` | `-` | `model` | `0` | `models/warby/dys_prop_warby_furnace_metal_01` |
| `models/warby/dys_prop_warby_furnace_pollution_scroll_01` | `UnlitTwoTexture` | `-` | `model` | `0` | `models/warby/dys_prop_warby_furnace_pollution_scroll_01_mask` |
| `models/warby/dys_prop_warby_laser_fence_01` | `unlitgeneric` | `-` | `model` | `0` | `models/warby/dys_prop_warby_laser_fence_01` |
| `models/warby/dys_prop_warby_laser_fence_metal_01` | `VertexLitGeneric` | `-` | `model` | `0` | `models/warby/dys_prop_warby_laser_fence_metal_01` |
| `models/warby/dys_prop_warby_pipes_01` | `VertexLitGeneric` | `-` | `model` | `0` | `models/warby/dys_prop_warby_pipes_01` |
| `models/warby/dys_prop_warby_police_van_01` | `VertexLitGeneric` | `-` | `model` | `0` | `models/warby/dys_prop_warby_police_van_01` |
| `models/warby/dys_prop_warby_police_van_tire_01` | `VertexLitGeneric` | `-` | `model` | `0` | `models/warby/dys_prop_warby_police_van_tire_01` |
| `models/warby/dys_prop_warby_spider_tank_01` | `VertexLitGeneric` | `-` | `model` | `0` | `models/warby/dys_prop_warby_spider_tank_01` |
| `models/warby/dys_prop_warby_support_beam_01` | `VertexLitGeneric` | `-` | `model` | `0` | `models/warby/dys_prop_warby_support_beam_01` |
| `models/weapons/MK_405_Clip` | `VertexLitGeneric` | `-` | `model` | `0` | `models/Weapons/MK_405_Clip` |
| `models/weapons/MK_405_Uv01` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/MK_405_Uv01` |
| `models/weapons/RL_skin` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/RL_skin` |
| `models/weapons/RL_skin_light` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/RL_skin_light` |
| `models/weapons/Spider_nade_skin` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/Weapons/Spider_nade_skin` |
| `models/weapons/Spider_nade_skin_dx8` | `VertexLitGeneric` | `-` | `model` | `0` | `models/Weapons/Spider_nade_skin` |
| `models/weapons/Tesla_Trans` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/tesla_trans` |
| `models/weapons/assault_tst6` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/assault_tst6` |
| `models/weapons/bas_bomb` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/bas_bomb` |
| `models/weapons/basilisk_shell` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/basilisk_shell` |
| `models/weapons/cyberspace/anti-virus` | `UnlitGeneric` | `metal` | `model` | `0` | `models/weapons/cyberspace/anti-virus` |
| `models/weapons/cyberspace/dope01` | `UnlitGeneric` | `flesh` | `model` | `0` | `models/weapons/cyberspace/dope01` |
| `models/weapons/cyberspace/dope02` | `UnlitGeneric` | `flesh` | `model` | `0` | `models/weapons/cyberspace/dope02` |
| `models/weapons/cyberspace/dope03` | `UnlitGeneric` | `flesh` | `model` | `0` | `models/weapons/cyberspace/dope03` |
| `models/weapons/cyberspace/sparky_ball` | `Refract` | `-` | `model` | `0` | `-` |
| `models/weapons/cyberspace/virus` | `UnlitGeneric` | `metal` | `model` | `0` | `models/weapons/cyberspace/virus` |
| `models/weapons/dys_bolt_projectile` | `VertexLitGeneric` | `-` | `model` | `0` | `models/weapons/dys_bolt_projectile` |
| `models/weapons/dys_boltg` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/Weapons/dys_boltg` |
| `models/weapons/dys_boltg_dx8` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/dys_boltg` |
| `models/weapons/dys_emp` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/Weapons/dys_emp` |
| `models/weapons/dys_emp_dx8` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/dys_emp` |
| `models/weapons/dys_frag` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/Weapons/dys_frag` |
| `models/weapons/dys_frag_dx8` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/dys_frag` |
| `models/weapons/dys_frag_tossed` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/Weapons/dys_frag_tossed` |
| `models/weapons/dys_frag_tossed_dx8` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/dys_frag_tossed` |
| `models/weapons/dys_machpistol` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/Weapons/dys_machpistol` |
| `models/weapons/dys_machpistol_dx8` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/dys_machpistol` |
| `models/weapons/dys_pistol2` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/dys_pistol2` |
| `models/weapons/dystopia_gl_high` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/dystopia_gl_high` |
| `models/weapons/gl_gren1` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/gl_gren1` |
| `models/weapons/gl_gren1_primed` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/gl_gren1` |
| `models/weapons/gl_gren2` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/gl_gren2` |
| `models/weapons/gl_gren2_primed` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/gl_gren2` |
| `models/weapons/gren_launcher` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/gren_launcher` |
| `models/weapons/gren_launcher_dx8` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/gren_launcher` |
| `models/weapons/ioncan_skin` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/ioncan_skin` |
| `models/weapons/ioncannon_corp` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/Weapons/ioncannon_corp` |
| `models/weapons/ioncannon_dx8` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/ioncannon_corp` |
| `models/weapons/ioncannon_punk` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/Weapons/ioncannon_punk` |
| `models/weapons/katana/katana_01` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/Weapons/katana/katana_01` |
| `models/weapons/katana/katana_01_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/Weapons/katana/katana_01` |
| `models/weapons/katana/katana_02` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/Weapons/katana/katana_02` |
| `models/weapons/katana/katana_02_dx8` | `VertexLitGeneric` | `metal` | `model` | `0` | `Models/Weapons/katana/katana_02` |
| `models/weapons/laser` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/laser` |
| `models/weapons/laser_rifle` | `vertexlitgeneric` | `metal` | `model` | `0` | `Models/Weapons/laser_rifle` |
| `models/weapons/laser_rifle_dx8` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/laser_rifle` |
| `models/weapons/mini_gun_skin` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/mini_gun_skin` |
| `models/weapons/mk405_side` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/mk405_side` |
| `models/weapons/mk_808_clip` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/mk_808_clip` |
| `models/weapons/mk_808_main` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/mk_808_main` |
| `models/weapons/p_models/eq_fraggrenade/fraggrenade` | `vertexlitgeneric` | `-` | `model` | `0` | `models/weapons/p_models/eq_fraggrenade/fraggrenade` |
| `models/weapons/plasma_tex02` | `UnlitGeneric` | `-` | `model` | `0` | `models/Weapons/plasma_tex02` |
| `models/weapons/plasma_tex03` | `UnlitGeneric` | `-` | `model` | `0` | `models/Weapons/plasma_tex03` |
| `models/weapons/rocket/gl_gren1` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/gl_gren1` |
| `models/weapons/rocket/missile2` | `vertexlitgeneric` | `metal` | `model` | `0` | `models/props/missile` |
| `models/weapons/shotgun` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/shotgun` |
| `models/weapons/shotty2` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/shotty2` |
| `models/weapons/tempest` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/tempest` |
| `models/weapons/tesla` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/Tesla` |
| `models/weapons/tesla_rings` | `vertexlitgeneric` | `-` | `model` | `0` | `models/weapons/tesla_rings_dark` |
| `models/weapons/v_lance01` | `VertexLitGeneric` | `-` | `model` | `0` | `Models/Weapons/v_lance01` |
| `models/weapons/v_models/eq_fraggrenade/fraggrenade` | `$basetexture` | `-` | `model` | `0` | `models/weapons/v_models/eq_fraggrenade/fraggrenade` |
| `models/weapons/v_models/eq_fraggrenade/fraggrenade_normal` | `vertexlitgeneric` | `-` | `model` | `0` | `models/weapons/v_models/eq_fraggrenade/fraggrenade_normal` |
| `models/weapons/v_models/hands/HandTemp` | `vertexlitgeneric` | `-` | `model` | `0` | `models/weapons/v_models/hands/HandTemp` |
| `models/weapons/v_models/hands/v_hands` | `$basetexture` | `-` | `model` | `0` | `models/weapons/v_models/hands/v_hands` |
| `models/weapons/v_models/hands/v_hands_normal` | `vertexlitgeneric` | `-` | `model` | `0` | `models/weapons/v_models/hands/v_hands_normal` |
| `models/weapons/v_models/hands/view_finger` | `VertexLitGeneric` | `-` | `model` | `0` | `models/OLD_weapons/v_models/hands/view_finger` |
| `models/weapons/v_models/hands/view_glove` | `VertexLitGeneric` | `-` | `model` | `0` | `models/OLD_weapons/v_models/hands/view_glove` |
| `models/weapons/v_models/hands/view_skin` | `VertexLitGeneric` | `-` | `model` | `0` | `models/OLD_weapons/v_models/hands/view_skin` |
| `models/weapons/v_models/mach_m249para/mach_m249para` | `$basetexture` | `-` | `model` | `0` | `models/weapons/v_models/mach_m249para/mach_m249para` |
| `models/weapons/v_models/shot_m3super90/shot_m3super90` | `$basetexture` | `-` | `model` | `0` | `models/weapons/v_models/shot_m3super90/shot_m3super90` |
| `models/weapons/v_models/smg_mp5/MP5_1` | `$basetexture` | `-` | `model` | `0` | `models/weapons/v_models/smg_mp5/mp5_1` |
| `models/weapons/v_models/smg_mp5/MP5_1_normal` | `vertexlitgeneric` | `-` | `model` | `0` | `models/weapons/v_models/smg_MP5/MP5_1_normal` |
| `models/weapons/w_models/w_eq_fraggrenade/w_eq_fraggrenade` | `vertexlitgeneric` | `-` | `model` | `0` | `models/weapons/w_models/w_eq_fraggrenade/w_eq_fraggrenade` |
| `models/weapons/w_models/w_mach_m249/w_mach_m249` | `vertexlitgeneric` | `-` | `model` | `0` | `models/weapons/w_models/w_mach_m249/w_mach_m249` |
| `models/weapons/w_models/w_shot_m3super90/w_shot_m3super90` | `vertexlitgeneric` | `-` | `model` | `0` | `models/weapons/w_models/w_shot_m3super90/w_shot_m3super90` |
| `models/weapons/w_models/w_smg_mp5/w_smg_mp5` | `vertexlitgeneric` | `-` | `model` | `0` | `models/weapons/w_models/w_smg_mp5/w_smg_mp5` |
| `models/white_awning` | `VertexLitGeneric` | `metal` | `model` | `0` | `models/urban/white_awning` |

### `nature`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `nature/blend_grass01_dirt01` | `worldvertextransition` | `grass` | `map` | `1` | `nature/grass01` |
| `nature/blend_grass01_dirt01_with_normal` | `worldvertextransition` | `grass` | `map` | `0` | `nature/grass01` |
| `nature/dirt01` | `LightmappedGeneric` | `dirt` | `map` | `1` | `nature/dirt01` |
| `nature/dirt01_with_normal` | `LightmappedGeneric` | `dirt` | `map` | `0` | `nature/dirt01` |
| `nature/grass01` | `LightmappedGeneric` | `grass` | `map` | `0` | `nature/grass01` |
| `nature/grass01_with_normal` | `LightmappedGeneric` | `grass` | `map` | `0` | `nature/grass01` |
| `nature/grass02` | `LightmappedGeneric` | `grass` | `map` | `0` | `nature/grass02` |

### `neon`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `neon/Building_TemplateCorp` | `LightmappedGeneric` | `concrete` | `map` | `0` | `Neon/Building_TemplateCorp` |
| `neon/concretefloor033k` | `LightmappedGeneric` | `concrete` | `map` | `0` | `concrete/concretefloor033k` |
| `neon/dog_invisible` | `LightmappedGeneric` | `-` | `map` | `0` | `neon/dog_invisible` |
| `neon/dog_logo1` | `LightmappedGeneric` | `-` | `map` | `0` | `neon/dog_logo1` |
| `neon/dog_map` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_map` |
| `neon/dog_map1` | `VertexLitGeneric` | `-` | `map` | `0` | `neon/dog_map1` |
| `neon/dog_neon1` | `LightmappedGeneric` | `glass` | `map` | `1` | `neon/dog_neon1` |
| `neon/dog_neon10` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon10` |
| `neon/dog_neon11` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon11` |
| `neon/dog_neon12` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon12` |
| `neon/dog_neon13` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon13` |
| `neon/dog_neon14` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon14` |
| `neon/dog_neon15` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon15` |
| `neon/dog_neon16` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon16` |
| `neon/dog_neon17` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon17` |
| `neon/dog_neon18` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon18` |
| `neon/dog_neon19` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon19` |
| `neon/dog_neon2` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon2` |
| `neon/dog_neon20` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon20` |
| `neon/dog_neon21` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon21` |
| `neon/dog_neon22` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon22` |
| `neon/dog_neon23` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon23` |
| `neon/dog_neon24` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon24` |
| `neon/dog_neon25` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon25` |
| `neon/dog_neon26` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon26` |
| `neon/dog_neon27` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon27` |
| `neon/dog_neon28` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon28` |
| `neon/dog_neon29` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon29` |
| `neon/dog_neon3` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon3` |
| `neon/dog_neon30` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon30` |
| `neon/dog_neon31` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon31` |
| `neon/dog_neon32` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon32` |
| `neon/dog_neon33` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon33` |
| `neon/dog_neon34` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon34` |
| `neon/dog_neon35` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon35` |
| `neon/dog_neon36` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon36` |
| `neon/dog_neon37` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon37` |
| `neon/dog_neon38` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon38` |
| `neon/dog_neon39` | `LightMappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon39` |
| `neon/dog_neon4` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon4` |
| `neon/dog_neon40` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon40` |
| `neon/dog_neon42` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon42` |
| `neon/dog_neon43` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon43` |
| `neon/dog_neon44` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon44` |
| `neon/dog_neon45` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon45` |
| `neon/dog_neon46` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon46` |
| `neon/dog_neon5` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon5` |
| `neon/dog_neon6` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon6` |
| `neon/dog_neon7a` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon7a` |
| `neon/dog_neon7b` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon7b` |
| `neon/dog_neon8` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon8` |
| `neon/dog_neon8b` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon8b` |
| `neon/dog_neon9` | `LightmappedGeneric` | `glass` | `map` | `0` | `neon/dog_neon9` |
| `neon/dog_ntscroll1` | `LightmappedGeneric` | `-` | `map` | `0` | `neon/dog_ntscroll1` |
| `neon/dog_ntscroll2` | `LightmappedGeneric` | `-` | `map` | `0` | `neon/dog_ntscroll2` |
| `neon/dog_ntscroll3` | `LightmappedGeneric` | `-` | `map` | `0` | `neon/dog_ntscroll3` |
| `neon/dog_ntscroll4` | `LightmappedGeneric` | `-` | `map` | `0` | `neon/dog_ntscroll4` |
| `neon/dog_vincent238_phoenix` | `VertexLitGeneric` | `-` | `map` | `0` | `neon/dog_vincent238_phoenix` |
| `neon/dog_vincent238phoenix2` | `VertexLitGeneric` | `-` | `map` | `0` | `neon/dog_vincent238_phoenix2` |
| `neon/dys_neon_hotel` | `unlitgeneric` | `-` | `map` | `1` | `neon/dys_neon_hotel` |
| `neon/dys_radioshack_neon_girls` | `unlitgeneric` | `-` | `map` | `2` | `neon/dys_radioshack_neon_girls` |
| `neon/dys_radioshack_neon_jimmys` | `unlitgeneric` | `-` | `map` | `2` | `neon/dys_radioshack_neon_jimmys` |
| `neon/dys_radioshack_neon_noWeapons` | `unlitgeneric` | `-` | `map` | `1` | `neon/dys_radioshack_neon_noWeapons` |
| `neon/dys_radioshack_neon_staffOnly` | `unlitgeneric` | `-` | `map` | `1` | `neon/dys_radioshack_neon_staffOnly` |
| `neon/dys_radioshack_neon_switchblade` | `unlitgeneric` | `-` | `map` | `1` | `neon/dys_radioshack_neon_switchblade` |
| `neon/laserplane_blue` | `UnlitGeneric` | `-` | `map` | `0` | `neon/laserplane_blue` |
| `neon/lasersmoke_blue` | `UnlitGeneric` | `-` | `map` | `0` | `neon/lasersmoke_blue` |
| `neon/neon_bar_real_alchohol` | `unlitgeneric` | `-` | `map` | `0` | `neon/neon_bar_real_alchohol` |
| `neon/neon_burgers` | `UnlitGeneric` | `-` | `map` | `1` | `neon/neon_burgers` |
| `neon/neon_datasmith` | `unlitgeneric` | `-` | `map` | `0` | `neon/neon_datasmith` |
| `neon/neon_delhiSpices` | `UnlitGeneric` | `-` | `map` | `1` | `neon/neon_delhiSpices` |
| `neon/neon_downtownFacemods` | `UnlitGeneric` | `-` | `map` | `2` | `neon/neon_downtownFacemods` |
| `neon/neon_late_night_takeaway` | `unlitgeneric` | `-` | `map` | `1` | `neon/neon_late_night_takeaway` |
| `neon/neon_rafikis` | `UnlitGeneric` | `-` | `map` | `2` | `neon/neon_rafikis` |
| `neon/neon_thdsm` | `UnlitGeneric` | `-` | `map` | `2` | `neon/neon_thdsm` |
| `neon/neon_xxx_video` | `unlitgeneric` | `-` | `map` | `0` | `neon/neon_xxx_video` |
| `neon/s_neon1` | `unlittwotexture` | `glass` | `map` | `3` | `neon/s_neon1` |
| `neon/s_neon2` | `unlittwotexture` | `glass` | `map` | `2` | `neon/s_neon2` |
| `neon/s_neon3` | `unlittwotexture` | `glass` | `map` | `3` | `neon/s_neon3` |
| `neon/s_neon4` | `unlittwotexture` | `glass` | `map` | `2` | `neon/s_neon4` |
| `neon/s_neon5` | `unlittwotexture` | `glass` | `map` | `3` | `neon/s_neon5` |
| `neon/s_neon_diner` | `unlittwotexture` | `glass` | `map` | `2` | `neon/s_neon_diner` |
| `neon/s_neon_monorail` | `unlittwotexture` | `glass` | `map` | `1` | `neon/s_neon_monorail` |
| `neon/s_neon_netexcess` | `unlittwotexture` | `glass` | `map` | `1` | `neon/s_neon_netexcess` |
| `neon/servers_disp` | `VertexLitGeneric` | `-` | `map` | `0` | `neon/servers_disp` |
| `neon/urbanrisk_pilon` | `LightmappedGeneric` | `-` | `map` | `0` | `Documents and Settings/JIMMY BOY/Desktop/urbanrisk_pilon/urbanrisk_pilon` |

### `newmenu`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `newmenu/menu_background` | `UnlitGeneric` | `-` | `map` | `0` | `vgui/newmenu/menu_background` |
| `newmenu/menu_basilisk` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_basilisk` |
| `newmenu/menu_crossbow` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_crossbow` |
| `newmenu/menu_grenade` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_grenade` |
| `newmenu/menu_ion` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_ion` |
| `newmenu/menu_laser` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_laser` |
| `newmenu/menu_minigun` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_minigun` |
| `newmenu/menu_mk405` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_mk405` |
| `newmenu/menu_mk808` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_mk808` |
| `newmenu/menu_rocket` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_rocket` |
| `newmenu/menu_shotgun` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_shotgun` |
| `newmenu/menu_smartlocks` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_smartlocks` |
| `newmenu/menu_tesla` | `UnlitGeneric` | `-` | `map` | `0` | `VGUI/newmenu/menu_tesla` |

### `oaf`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `oaf/cs/solidred01` | `UnlitGeneric` | `metal` | `map` | `0` | `oaf/cs/solidred01` |
| `oaf/quotepyramid` | `LightmappedGeneric` | `metal` | `map` | `0` | `oaf/quotepyramid` |
| `oaf/reddoor` | `LightmappedGeneric` | `metal` | `map` | `0` | `oaf/reddoor` |
| `oaf/screen/int/gencontrolscreen` | `UnlitGeneric` | `glass` | `map` | `0` | `oaf/screen/int/gencontrolscreen` |
| `oaf/screen/int/systemcontrol` | `UnlitGeneric` | `glass` | `map` | `0` | `oaf/screen/int/systemcontrol` |

### `overviews`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `overviews/dys_assemble` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_assemble` |
| `overviews/dys_broadcast` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_broadcast` |
| `overviews/dys_broadcast1` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_broadcast1` |
| `overviews/dys_broadcast2` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_broadcast2` |
| `overviews/dys_detonate` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_detonate` |
| `overviews/dys_detonate2` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_detonate2` |
| `overviews/dys_exodus1` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_exodus1` |
| `overviews/dys_exodus2` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_exodus2` |
| `overviews/dys_exodus3` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_exodus3` |
| `overviews/dys_exodus4` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_exodus4` |
| `overviews/dys_fortress1` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_fortress1` |
| `overviews/dys_fortress2` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_fortress2` |
| `overviews/dys_fortress3` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_fortress3` |
| `overviews/dys_fusion1` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_fusion1` |
| `overviews/dys_fusion2` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_fusion2` |
| `overviews/dys_fusion4` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_fusion4` |
| `overviews/dys_injection1` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_injection2` |
| `overviews/dys_injection2` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_injection1` |
| `overviews/dys_injection3` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_injection3` |
| `overviews/dys_injection3a` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_injection3a` |
| `overviews/dys_injection4` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_injection4` |
| `overviews/dys_injection5` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_injection5` |
| `overviews/dys_injection7` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_injection7` |
| `overviews/dys_silo1` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_silo1` |
| `overviews/dys_silo2` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_silo2` |
| `overviews/dys_silo3` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_silo3` |
| `overviews/dys_silo4` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_silo4` |
| `overviews/dys_undermine` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_undermine` |
| `overviews/dys_vaccine1` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_vaccine1` |
| `overviews/dys_vaccine2` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_vaccine2` |
| `overviews/dys_vaccine3` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_vaccine3` |
| `overviews/dys_vaccine4` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_vaccine4` |
| `overviews/dys_vaccine5` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/dys_vaccine5` |
| `overviews/pb_dojo1` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/pb_dojo1` |
| `overviews/pb_rooftop1` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/pb_rooftop1` |
| `overviews/pb_rooftop2` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/pb_rooftop2` |
| `overviews/pb_round1` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/pb_round1` |
| `overviews/pb_urbandome1` | `UnlitGeneric` | `-` | `map` | `0` | `overviews/pb_urbandome1` |

### `particle`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `particle/particledefault` | `UnlitGeneric` | `-` | `map` | `0` | `particle/particledefault` |

### `particles`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `particles/binary_0` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/binary_0` |
| `particles/binary_1` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/binary_1` |
| `particles/blackfade_p` | `SpriteCard` | `-` | `particle` | `0` | `particles/blackfade` |
| `particles/dys_Particle_Glow_04_Additive` | `UnlitGeneric` | `-` | `particle` | `0` | `particle/particle_glow_04` |
| `particles/dys_beam1` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_beam1` |
| `particles/dys_beam2` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_beam2` |
| `particles/dys_beam3` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_beam3` |
| `particles/dys_beam3_long` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_beam3_long` |
| `particles/dys_beam4` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_beam4` |
| `particles/dys_beam4_red` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_beam4_red` |
| `particles/dys_beam_big_rect` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_beam_big_rect` |
| `particles/dys_beam_big_square` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_beam_big_square` |
| `particles/dys_beam_big_square_inv` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_beam_big_square_inv` |
| `particles/dys_medicross` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_medicross` |
| `particles/dys_medicross_red` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_medicross` |
| `particles/dys_powerwarp_warp` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_powerwarp_warp` |
| `particles/dys_powerwarp_warp2` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_powerwarp_warp2` |
| `particles/dys_ringparticle1` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_ringparticle1` |
| `particles/dys_ringparticle2` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_ringparticle2` |
| `particles/dys_ringparticle3` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_ringparticle3` |
| `particles/dys_ringparticle4` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_ringparticle4` |
| `particles/dys_squareparticle1` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_squareparticle1` |
| `particles/dys_squareparticle2` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_squareparticle2` |
| `particles/dys_squareparticle3` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_squareparticle3` |
| `particles/dys_squareparticle4` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_squareparticle4` |
| `particles/dys_squareparticle4_nocull` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/dys_squareparticle4` |
| `particles/dys_transscreenparticle` | `Unlittwotexture` | `glass` | `particle` | `0` | `_rt_camera1` |
| `particles/dys_transscreenparticle1` | `Unlittwotexture` | `glass` | `particle` | `0` | `_rt_camera1` |
| `particles/dys_transscreenparticle2` | `Unlittwotexture` | `glass` | `particle` | `0` | `_rt_camera2` |
| `particles/dys_transscreenparticle3` | `Unlittwotexture` | `glass` | `particle` | `0` | `_rt_camera3` |
| `particles/dys_transscreenparticle4` | `Unlittwotexture` | `glass` | `particle` | `0` | `_rt_camera4` |
| `particles/dys_warptex1` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_warptex1` |
| `particles/dys_warptex_blue1` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_warptex_blue1` |
| `particles/dys_warptex_blue2` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_warptex_blue2` |
| `particles/dys_warptex_blue3` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_warptex_blue3` |
| `particles/dys_warptex_red1` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_warptex_red1` |
| `particles/dys_warptex_red2` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_warptex_red2` |
| `particles/dys_warptex_red3` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_warptex_red3` |
| `particles/dys_warptex_twist` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_warptex_twist` |
| `particles/dys_warptex_twist1` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_warptex_twist1` |
| `particles/dys_warptex_twist2` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_warptex_twist2` |
| `particles/dys_warptex_twist3` | `SpriteCard` | `-` | `particle` | `0` | `particles/dys_warptex_twist3` |
| `particles/lightning1` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/lightning1` |
| `particles/lightning2` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/lightning2` |
| `particles/lightning3` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/lightning3` |
| `particles/lightning4` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/lightning4` |
| `particles/lightning5` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/lightning5` |
| `particles/lightning6` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/lightning6` |
| `particles/lightning7` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/lightning7` |
| `particles/mappath` | `UnlitGeneric` | `-` | `particle` | `0` | `particles/mappath_mask` |
| `particles/mappath_beam` | `spritecard` | `-` | `particle` | `0` | `particles/mappath_beam` |
| `particles/mappath_ring` | `spritecard` | `-` | `particle` | `0` | `particles/mappath_ring` |
| `particles/rain` | `UnlitGeneric` | `-` | `particle` | `0` | `particle/rain` |

### `phistball`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `phistball/Copy of ud_score_p` | `unlitgeneric` | `-` | `map` | `0` | `phistball/ud_score_p` |
| `phistball/ud_score_c` | `unlitgeneric` | `-` | `map` | `0` | `phistball/ud_score_c` |

### `posters`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `posters/billboard_hazmat01` | `lightmappedgeneric` | `metal` | `map` | `2` | `posters/billboard_hazmat01` |
| `posters/billboard_medicare01` | `lightmappedgeneric` | `metal` | `map` | `2` | `posters/billboard_medicare01` |
| `posters/dys_routerAccess` | `lightmappedgeneric` | `-` | `map` | `0` | `posters/dys_routerAccess` |
| `posters/poster_dys_noGuns_worn` | `lightmappedgeneric` | `-` | `map` | `0` | `posters/poster_dys_noGuns_worn` |
| `posters/poster_dys_walktek_worn` | `lightmappedgeneric` | `-` | `map` | `0` | `posters/poster_dys_walktek_worn` |
| `posters/poster_dys_zeroCrimeTolerance_worn` | `lightmappedgeneric` | `-` | `map` | `0` | `posters/poster_dys_zeroCrimeTolerance_worn` |

### `pro1`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `pro1/pro_010` | `LightMappedGeneric` | `-` | `map` | `1` | `pro1/pro_010` |
| `pro1/pro_020` | `LightMappedGeneric` | `-` | `map` | `1` | `pro1/pro_030` |
| `pro1/pro_030` | `LightMappedGeneric` | `-` | `map` | `1` | `pro1/pro_020` |

### `radioshack`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `radioshack/contrabanned` | `UnlitGeneric` | `-` | `map` | `0` | `radioshack/contrabanned` |
| `radioshack/cyberGraf01` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/cyberGraf01` |
| `radioshack/cyberGraf02` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/cyberGraf02` |
| `radioshack/cyberGraf03` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/cyberGraf03` |
| `radioshack/cyberGraf04` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/cyberGraf04` |
| `radioshack/cyberGraf05` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/cyberGraf05` |
| `radioshack/cyberGraf06` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/cyberGraf06` |
| `radioshack/cyberGraf07` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/cyberGraf07` |
| `radioshack/cyberGraf08` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/cyberGraf08` |
| `radioshack/cyberGraf09` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/cyberGraf09` |
| `radioshack/cyberGraf10` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/cyberGraf10` |
| `radioshack/cyberSign_ServerDefences_hop` | `unlitgeneric` | `-` | `map` | `1` | `radioshack/cyberSign_ServerDefences_hop` |
| `radioshack/cyberSign_branch_obj1Spawn_obj2DoorLock_spawnNode` | `unlitgeneric` | `-` | `map` | `1` | `radioshack/cyberSign_branch_obj1Spawn_obj2DoorLock_spawnNode` |
| `radioshack/cyberSign_fireEscape_sewerElevator` | `unlitgeneric` | `-` | `map` | `1` | `radioshack/cyberSign_fireEscape_sewerElevator` |
| `radioshack/cyberSign_obj1Spawn_obj1DoorLock` | `unlitgeneric` | `-` | `map` | `1` | `radioshack/cyberSign_obj1Spawn_obj1DoorLock` |
| `radioshack/cyberSign_power_ventilation` | `unlitgeneric` | `-` | `map` | `1` | `radioshack/cyberSign_power_ventilation` |
| `radioshack/cyberSign_power_ventilation_serverDefences` | `unlitgeneric` | `-` | `map` | `1` | `radioshack/cyberSign_power_ventilation_serverDefences` |
| `radioshack/cyberSign_serverDefences` | `unlitgeneric` | `-` | `map` | `1` | `radioshack/cyberSign_serverDefences` |
| `radioshack/cyberSign_spawnNode` | `unlitgeneric` | `-` | `map` | `1` | `radioshack/cyberSign_spawnNode` |
| `radioshack/cyber_round_red` | `unlitgeneric` | `-` | `map` | `3` | `radioshack/cyber_round_red` |
| `radioshack/dnaDoor` | `LightmappedGeneric` | `metal` | `map` | `1` | `radioshack/dnaDoorDiffuse` |
| `radioshack/dnaDoorBlack` | `LightmappedGeneric` | `metal` | `map` | `1` | `radioshack/dnaDoorBlackDiffuse` |
| `radioshack/dnaDoorBlue` | `LightmappedGeneric` | `metal` | `map` | `1` | `radioshack/dnaDoorBlueDiffuse` |
| `radioshack/dnaDoorGreen` | `LightmappedGeneric` | `metal` | `map` | `1` | `radioshack/dnaDoorGreenDiffuse` |
| `radioshack/dnaDoorWhite` | `LightmappedGeneric` | `metal` | `map` | `2` | `radioshack/dnaDoorWhiteDiffuse` |
| `radioshack/dys_radioshack_capture_awaitingt` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_capture_awaitingt` |
| `radioshack/dys_radioshack_capture_cancel` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_capture_cancel` |
| `radioshack/dys_radioshack_capture_corps` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_capture_corps` |
| `radioshack/dys_radioshack_capture_plswait` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_capture_plswait` |
| `radioshack/dys_radioshack_capture_progressBar` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_capture_progressBar` |
| `radioshack/dys_radioshack_capture_progressBorder` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_capture_progressBorder` |
| `radioshack/dys_radioshack_capture_punks` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_capture_punks` |
| `radioshack/dys_radioshack_capture_reconfigure` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_capture_reconfigure` |
| `radioshack/dys_radioshack_capture_title` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_capture_title` |
| `radioshack/dys_radioshack_chalkboard` | `lightmappedgeneric` | `Wood_lowdensity` | `map` | `1` | `radioshack/dys_radioshack_chalkboard` |
| `radioshack/dys_radioshack_cs_alley_label` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_alley_label` |
| `radioshack/dys_radioshack_cs_club_label` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_club_label` |
| `radioshack/dys_radioshack_cs_control_label` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_control_label` |
| `radioshack/dys_radioshack_cs_fans_label` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_fans_label` |
| `radioshack/dys_radioshack_cs_firewall_label` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_firewall_label` |
| `radioshack/dys_radioshack_cs_fp_label` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_fp_label` |
| `radioshack/dys_radioshack_cs_function_elevator` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_function_elevator` |
| `radioshack/dys_radioshack_cs_function_entryDefence` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_function_entryDefence` |
| `radioshack/dys_radioshack_cs_function_fireescape` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_function_fireescape` |
| `radioshack/dys_radioshack_cs_function_interiorSpawn` | `unlitgeneric` | `-` | `map` | `0` | `maps/dys_radioshack_cs_function_interiorSpawn` |
| `radioshack/dys_radioshack_cs_function_perimeterSpawn` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_function_perimeterSpawn` |
| `radioshack/dys_radioshack_cs_function_powerControl` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_function_powerControl` |
| `radioshack/dys_radioshack_cs_function_serverDefencel` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_function_serverDefencel` |
| `radioshack/dys_radioshack_cs_function_ventilationControl` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_function_ventilationControl` |
| `radioshack/dys_radioshack_cs_power_label` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_power_label` |
| `radioshack/dys_radioshack_cs_security_label` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_security_label` |
| `radioshack/dys_radioshack_cs_serverJack_label` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_serverJack_label` |
| `radioshack/dys_radioshack_cs_server_label` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_server_label` |
| `radioshack/dys_radioshack_cs_sewer_label` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_sewer_label` |
| `radioshack/dys_radioshack_cs_sewer_label2` | `unlitgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_cs_sewer_label2` |
| `radioshack/dys_radioshack_dance` | `unlitgeneric` | `-` | `map` | `1` | `radioshack/dys_radioshack_dance` |
| `radioshack/dys_radioshack_girlPoster` | `UnlitTwoTexture` | `-` | `map` | `1` | `radioshack/dys_radioshack_girlPoster` |
| `radioshack/dys_radioshack_girlPoster2` | `UnlitTwoTexture` | `-` | `map` | `1` | `radioshack/dys_radioshack_girlPoster2` |
| `radioshack/dys_radioshack_outOfOrder` | `UnlitTwoTexture` | `-` | `map` | `1` | `radioshack/dys_radioshack_outOfOrder` |
| `radioshack/dys_radioshack_policeBarrier` | `lightmappedgeneric` | `-` | `map` | `0` | `radioshack/dys_radioshack_policeBarrier` |
| `radioshack/elevBack` | `UnlitTwoTexture` | `-` | `map` | `0` | `radioshack/elevBack` |
| `radioshack/graffiti_iAmFree` | `lightmappedgeneric` | `-` | `map` | `0` | `radioshack/graffiti_iAmFree` |
| `radioshack/radioshack_cyberLabel_P` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberLabel_P` |
| `radioshack/radioshack_cyberLabel_PS` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberLabel_PS` |
| `radioshack/radioshack_cyberLabel_SD` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberLabel_SD` |
| `radioshack/radioshack_cyberLabel_SE` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberLabel_SE` |
| `radioshack/radioshack_cyberLabel_SL` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberLabel_SL` |
| `radioshack/radioshack_cyberLabel_ST` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberLabel_ST` |
| `radioshack/radioshack_cyberLabel_V` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberLabel_V` |
| `radioshack/radioshack_cyberSign_FP` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberSign_FP` |
| `radioshack/radioshack_cyberSign_PS` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberSign_PS` |
| `radioshack/radioshack_cyberSign_SD` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberSign_SD` |
| `radioshack/radioshack_cyberSign_TE` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberSign_TE` |
| `radioshack/radioshack_cyberSign_split` | `unlitGeneric` | `-` | `map` | `0` | `radioshack/radioshack_cyberSign_split` |
| `radioshack/radioshack_dglPanels` | `unlitgeneric` | `-` | `map` | `3` | `radioshack/radioshack_dglPanels` |
| `radioshack/speaker` | `lightmappedgeneric` | `-` | `map` | `1` | `radioshack/speaker` |
| `radioshack/tcf` | `lightmappedgeneric` | `-` | `map` | `0` | `radioshack/tcf` |
| `radioshack/ted` | `lightmappedgeneric` | `-` | `map` | `0` | `radioshack/ted` |

### `screens`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `screens/punkLockedUnlocked` | `UnlitGeneric` | `-` | `map` | `1` | `screens/punkLockedUnlocked` |

### `screenwidea`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `screenwidea/screenwidea` | `LightmappedGeneric` | `-` | `map` | `0` | `screenwidea/screenwidea` |
| `screenwidea/screenwidea_wover` | `UnlitTwoTexture` | `-` | `map` | `1` | `screenwidea/screenwidea` |

### `sfx`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `sfx/exodus_genoverlay` | `UnlitGeneric` | `glass` | `overlay` | `0` | `sfx/exodus_genoverlay` |
| `sfx/exodus_gentop` | `UnlitGeneric` | `glass` | `map` | `0` | `sfx/exodus_gentop` |
| `sfx/exodus_genwaiting` | `Unlittwotexture` | `-` | `map` | `1` | `sfx/exodus_genunderlay` |

### `signs`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `signs/abit_logo` | `LightmappedGeneric` | `glass` | `map` | `0` | `signs/abit_logo` |
| `signs/altech` | `LightmappedGeneric` | `metal` | `map` | `0` | `signs/altech` |
| `signs/black` | `LightmappedGeneric` | `glass` | `map` | `0` | `signs/black` |
| `signs/os_s1_glow` | `LightmappedGeneric` | `glass` | `map` | `2` | `signs/os_s1_glow` |
| `signs/osaka_sign01` | `LightmappedGeneric` | `glass` | `map` | `4` | `signs/osaka_sign01` |
| `signs/sign02` | `LightmappedGeneric` | `wood` | `map` | `1` | `signs/sign02` |
| `signs/sign03` | `LightmappedGeneric` | `wood` | `map` | `0` | `signs/sign03` |
| `signs/sign06` | `LightmappedGeneric` | `wood` | `map` | `0` | `signs/sign06` |
| `signs/sign_cheapMovies` | `UnlitGeneric` | `-` | `map` | `1` | `signs/sign_cheapMovies` |
| `signs/sign_cyberdeckUpgrades` | `UnlitGeneric` | `-` | `map` | `1` | `signs/sign_cyberdeckUpgrades` |
| `signs/sign_demolitionwarning` | `LightmappedGeneric` | `-` | `map` | `0` | `signs/sign_demolitionwarning` |
| `signs/sign_livres` | `UnlitGeneric` | `-` | `map` | `1` | `signs/sign_livres` |
| `signs/sign_netexcess01` | `UnlitGeneric` | `glass` | `map` | `1` | `signs/sign_netexcess01` |
| `signs/sign_netexcess02` | `UnlitGeneric` | `glass` | `map` | `1` | `signs/sign_netexcess02` |
| `signs/sign_netexcess03` | `UnlitGeneric` | `glass` | `map` | `1` | `signs/sign_netexcess03` |
| `signs/sign_qualityMeat` | `UnlitGeneric` | `metal` | `map` | `1` | `signs/sign_qualityMeat` |
| `signs/sign_valvbSoftware` | `UnlitGeneric` | `metal` | `map` | `1` | `signs/sign_valvbSoftware` |
| `signs/sign_wokThisWay` | `UnlitGeneric` | `-` | `map` | `1` | `signs/sign_wokThisWay` |

### `silotex`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `silotex/guidebg` | `LightmappedGeneric` | `metal` | `map` | `1` | `silotex/guidebg` |
| `silotex/guidesign1` | `UnlitGeneric` | `-` | `map` | `1` | `silotex/guidesign1` |
| `silotex/guidesign2` | `UnlitGeneric` | `-` | `map` | `1` | `silotex/guidesign2` |
| `silotex/guidesign3` | `UnlitGeneric` | `-` | `map` | `1` | `silotex/guidesign3` |
| `silotex/guidesign4` | `UnlitGeneric` | `-` | `map` | `0` | `silotex/guidesign4` |
| `silotex/node_air` | `UnlitGeneric` | `metal` | `map` | `1` | `silotex/node_air` |
| `silotex/node_aux` | `UnlitGeneric` | `metal` | `map` | `0` | `silotex/node_aux` |
| `silotex/node_gas` | `UnlitGeneric` | `metal` | `map` | `1` | `silotex/node_gas` |
| `silotex/node_power1` | `UnlitGeneric` | `metal` | `map` | `1` | `silotex/node_power1` |
| `silotex/node_spawn1` | `UnlitGeneric` | `metal` | `map` | `1` | `silotex/node_spawn1` |
| `silotex/node_turret` | `UnlitGeneric` | `metal` | `map` | `1` | `silotex/node_turret` |
| `silotex/node_vent` | `UnlitGeneric` | `metal` | `map` | `1` | `silotex/node_vent` |
| `silotex/o7_screen_bg1` | `UnlitGeneric` | `metal` | `map` | `0` | `silotex/o7_screen_bg1` |
| `silotex/o7_screen_overlay` | `UnlitGeneric` | `metal` | `overlay` | `0` | `silotex/o7_screen_overlay` |
| `silotex/o7_screen_overlay_3` | `UnlitGeneric` | `metal` | `overlay` | `0` | `silotex/o7_screen_overlay_3` |
| `silotex/o7_screen_overlay_centre` | `UnlitGeneric` | `metal` | `overlay` | `0` | `silotex/o7_screen_overlay_centre` |
| `silotex/o7_screen_sidescroll` | `UnlitGeneric` | `metal` | `map` | `0` | `silotex/o7_screen_sidescroll` |
| `silotex/paintsigns1` | `lightmappedGeneric` | `-` | `map` | `0` | `silotex/paintsigns1` |
| `silotex/paintsigns2` | `lightmappedGeneric` | `-` | `map` | `1` | `silotex/paintsigns2` |
| `silotex/paintsigns3` | `lightmappedGeneric` | `-` | `map` | `1` | `silotex/paintsigns3` |
| `silotex/particle_fire` | `UnlitGeneric` | `-` | `map` | `0` | `silotex/particle_fire` |
| `silotex/particle_smoke` | `UnlitGeneric` | `-` | `map` | `0` | `silotex/particle_smoke` |
| `silotex/pipelightmapped` | `LightmappedGeneric` | `metal` | `map` | `1` | `Models/props_pipes/PipeMetal004a` |
| `silotex/sand1` | `LightmappedGeneric` | `dirt` | `map` | `0` | `silotex/sand1` |
| `silotex/sand2` | `LightmappedGeneric` | `dirt` | `map` | `1` | `silotex/sand2` |
| `silotex/sand3` | `LightmappedGeneric` | `dirt` | `map` | `0` | `silotex/sand3` |
| `silotex/silo_bannerafter` | `UnlitTwoTexture` | `glass` | `map` | `1` | `silotex/silo_bannerafter` |
| `silotex/silo_bannerbefore` | `UnlitTwoTexture` | `glass` | `map` | `1` | `silotex/silo_bannerbefore` |
| `silotex/silo_bannerbefore_add` | `UnlitTwoTexture` | `glass` | `map` | `1` | `silotex/silo_bannerbefore` |
| `silotex/silo_brandscreen1` | `UnlitTwoTexture` | `glass` | `map` | `2` | `silotex/silo_brandscreen1` |
| `silotex/silo_brandscreen1_POP` | `UnlitTwoTexture` | `glass` | `map` | `2` | `silotex/silo_brandscreen1_POP` |
| `silotex/silo_screen_grid` | `UnlitGeneric` | `-` | `map` | `1` | `silotex/silo_screen_grid` |
| `silotex/silo_screen_grid_active` | `UnlitGeneric` | `-` | `map` | `1` | `silotex/silo_screen_grid_active` |
| `silotex/silo_valvewarning` | `UnlitGeneric` | `-` | `map` | `1` | `silotex/silo_screen_valvewarning` |
| `silotex/siloblend12` | `WorldVertexTransition` | `dirt` | `map` | `1` | `silotex/sand1` |
| `silotex/siloblend13` | `WorldVertexTransition` | `dirt` | `map` | `1` | `silotex/sand1` |
| `silotex/siloblend23` | `WorldVertexTransition` | `dirt` | `map` | `1` | `silotex/sand2` |
| `silotex/silodoor` | `LightmappedGeneric` | `metal` | `map` | `2` | `silotex/silodoor` |
| `silotex/silscreen1` | `UnlitTwoTexture` | `glass` | `map` | `1` | `silotex/silscreen1` |
| `silotex/silscreen1_busted` | `UnlitTwoTexture` | `-` | `map` | `1` | `silotex/silscreen1_busted` |
| `silotex/silscreen1_hax` | `UnlitTwoTexture` | `glass` | `map` | `1` | `silotex/silscreen1_hax` |
| `silotex/t_newcliff` | `LightmappedGeneric` | `rock` | `map` | `1` | `silotex/t_newcliff` |
| `silotex/t_newconc1` | `LightmappedGeneric` | `concrete` | `map` | `1` | `silotex/t_newconc1` |
| `silotex/t_newconc2` | `LightmappedGeneric` | `concrete` | `map` | `1` | `silotex/t_newconc2` |
| `silotex/t_newconc3` | `LightmappedGeneric` | `concrete` | `map` | `1` | `silotex/t_newconc3` |
| `silotex/t_newtile` | `LightmappedGeneric` | `concrete` | `map` | `2` | `silotex/t_newtile` |
| `silotex/vent_laser` | `UnlitGeneric` | `-` | `map` | `1` | `silotex/vent_laser` |

### `sky`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `sky/exosky_01` | `sky` | `-` | `map` | `0` | `sky/exosky_01` |
| `sky/exosky_01bk` | `Unknown` | `-` | `map` | `1` | `-` |
| `sky/exosky_01dn` | `Unknown` | `-` | `map` | `0` | `-` |
| `sky/exosky_01ft` | `Unknown` | `-` | `map` | `1` | `-` |
| `sky/exosky_01lf` | `Unknown` | `-` | `map` | `1` | `-` |
| `sky/exosky_01rt` | `Unknown` | `-` | `map` | `1` | `-` |
| `sky/exosky_01up` | `Unknown` | `-` | `map` | `1` | `-` |
| `sky/stars` | `Unknown` | `-` | `map` | `3` | `-` |

### `skybox`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `skybox/district_cloudsbk` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/district_cloudsdn` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/district_cloudsft` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/district_cloudslf` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/district_cloudsrt` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/district_cloudsup` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/dys_cloudyskybk` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/dys_cloudyskybk` |
| `skybox/dys_cloudyskydn` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/dys_cloudyskydn` |
| `skybox/dys_cloudyskyft` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/dys_cloudyskyft` |
| `skybox/dys_cloudyskylf` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/dys_cloudyskylf` |
| `skybox/dys_cloudyskyrt` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/dys_cloudyskyrt` |
| `skybox/dys_cloudyskyup` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/dys_cloudyskyup` |
| `skybox/exosky_01` | `sky` | `-` | `skybox` | `0` | `skybox/exosky_01` |
| `skybox/exosky_01bk` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/exosky_01dn` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/exosky_01ft` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/exosky_01lf` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/exosky_01rt` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/exosky_01up` | `$nofog` | `-` | `skybox` | `0` | `-` |
| `skybox/sky_ep01_02_hdrbk` | `sky` | `-` | `skybox` | `0` | `skybox/sky_ep01_02bk` |
| `skybox/sky_ep01_02_hdrdn` | `sky` | `-` | `skybox` | `0` | `skybox/sky_ep01_02dn` |
| `skybox/sky_ep01_02_hdrft` | `sky` | `-` | `skybox` | `0` | `skybox/sky_ep01_02ft` |
| `skybox/sky_ep01_02_hdrlf` | `sky` | `-` | `skybox` | `0` | `skybox/sky_ep01_02lf` |
| `skybox/sky_ep01_02_hdrrt` | `sky` | `-` | `skybox` | `0` | `skybox/sky_ep01_02rt` |
| `skybox/sky_ep01_02_hdrup` | `sky` | `-` | `skybox` | `0` | `skybox/sky_ep01_02up` |
| `skybox/sky_ep01_02bk` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/sky_ep01_02bk` |
| `skybox/sky_ep01_02dn` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/sky_ep01_02dn` |
| `skybox/sky_ep01_02ft` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/sky_ep01_02ft` |
| `skybox/sky_ep01_02lf` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/sky_ep01_02lf` |
| `skybox/sky_ep01_02rt` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/sky_ep01_02rt` |
| `skybox/sky_ep01_02up` | `UnlitGeneric` | `-` | `skybox` | `0` | `skybox/sky_ep01_02up` |

### `skybox_cards`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `skybox_cards/buildingsCard_01` | `UnlitGeneric` | `-` | `map` | `4` | `skybox_cards/buildingsCard_01` |
| `skybox_cards/buildingsCard_02` | `UnlitGeneric` | `-` | `map` | `5` | `skybox_cards/buildingsCard_02` |
| `skybox_cards/buildingsCard_03` | `UnlitGeneric` | `-` | `map` | `4` | `skybox_cards/buildingsCard_03` |
| `skybox_cards/groundFog` | `UnlitGeneric` | `-` | `map` | `1` | `skybox_cards/groundFog` |
| `skybox_cards/skybox_urban_buildings_card` | `LightmappedGeneric` | `-` | `map` | `3` | `skybox_cards/skybox_urban_buildings_card` |
| `skybox_cards/skybox_urban_buildings_card_destroyed` | `LightmappedGeneric` | `-` | `map` | `2` | `skybox_cards/skybox_urban_buildings_card_destroyed` |

### `sprites`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `sprites/arrow` | `UnlitGeneric` | `-` | `sprite` | `0` | `sprites/arrow` |
| `sprites/circle1` | `Sprite` | `-` | `sprite` | `0` | `sprites/circle1` |
| `sprites/circle2` | `Sprite` | `-` | `sprite` | `0` | `sprites/circle2` |
| `sprites/circle3` | `Sprite` | `-` | `sprite` | `0` | `sprites/circle3` |
| `sprites/cyber_laser` | `Sprite` | `-` | `sprite` | `0` | `sprites/cyber_laser` |
| `sprites/cyber_ragdoll` | `Sprite` | `-` | `sprite` | `0` | `sprites/cyber_ragdoll` |
| `sprites/cyber_trail` | `Sprite` | `-` | `sprite` | `0` | `sprites/cyber_trail` |
| `sprites/dys_point_spotlight_beam` | `Sprite` | `-` | `sprite` | `0` | `sprites/dys_point_spotlight_beam` |
| `sprites/dys_point_spotlight_glow` | `Sprite` | `-` | `sprite` | `0` | `sprites/dys_point_spotlight_glow` |
| `sprites/firestream` | `Sprite` | `-` | `sprite` | `0` | `sprites/firestream` |
| `sprites/friendlycrosshair` | `UnlitGeneric` | `-` | `sprite` | `0` | `sprites/friendlycrosshair` |
| `sprites/gl_blue` | `Sprite` | `-` | `sprite` | `0` | `sprites/gl_blue` |
| `sprites/gl_orange` | `Sprite` | `-` | `sprite` | `0` | `sprites/gl_orange` |
| `sprites/glow04_noz` | `UnlitGeneric` | `-` | `sprite` | `0` | `sprites/glow04` |
| `sprites/glow_test02` | `Sprite` | `-` | `sprite` | `0` | `sprites/glow_test02` |
| `sprites/ion_beam` | `Sprite` | `-` | `sprite` | `0` | `sprites/ion_beam` |
| `sprites/jumppad1` | `Sprite` | `-` | `sprite` | `0` | `sprites/jumppad1` |
| `sprites/jumppad1_color` | `Sprite` | `-` | `sprite` | `0` | `sprites/jumppad1_color` |
| `sprites/jumppad1_translucent` | `Sprite` | `-` | `sprite` | `0` | `sprites/jumppad1_translucent` |
| `sprites/laser` | `Sprite` | `-` | `sprite` | `0` | `sprites/laser` |
| `sprites/line1` | `Sprite` | `-` | `sprite` | `0` | `sprites/line1` |
| `sprites/line2` | `Sprite` | `-` | `sprite` | `0` | `sprites/line2` |
| `sprites/line3` | `Sprite` | `-` | `sprite` | `0` | `sprites/line3` |
| `sprites/medi_beam` | `Sprite` | `-` | `sprite` | `0` | `sprites/medi_beam` |
| `sprites/orangecore1` | `UnlitGeneric` | `-` | `sprite` | `0` | `sprites/orangecore1` |
| `sprites/orangecore2` | `UnlitGeneric` | `-` | `sprite` | `0` | `sprites/orangecore2` |
| `sprites/orangeflare1` | `UnlitGeneric` | `-` | `sprite` | `0` | `sprites/orangeflare1` |
| `sprites/orangelight1` | `Sprite` | `-` | `sprite` | `0` | `sprites/orangelight1` |
| `sprites/orangelight1_noz` | `Sprite` | `-` | `sprite` | `0` | `sprites/orangelight1` |
| `sprites/redglow1` | `UnlitGeneric` | `-` | `sprite` | `0` | `sprites/redglow1` |
| `sprites/spritetrail` | `Sprite` | `-` | `sprite` | `0` | `sprites/spritetrail` |
| `sprites/square1` | `Sprite` | `-` | `sprite` | `0` | `sprites/square1` |
| `sprites/square2` | `Sprite` | `-` | `sprite` | `0` | `sprites/square2` |
| `sprites/square3` | `Sprite` | `-` | `sprite` | `0` | `sprites/square3` |

### `stealth`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `stealth` | `Refract` | `-` | `map` | `0` | `-` |

### `stealth_dx7`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `stealth_dx7` | `Refract` | `-` | `map` | `0` | `-` |

### `stealth_new`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `stealth_new` | `Aftershock` | `-` | `map` | `0` | `-` |

### `stealth_new_dx8`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `stealth_new_dx8` | `Refract` | `-` | `map` | `0` | `-` |

### `stone`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `stone/stonefloor_001` | `LightmappedGeneric` | `stone` | `map` | `0` | `stone/stonefloor_001` |
| `stone/stonetrim_001` | `LightmappedGeneric` | `concrete` | `map` | `1` | `stone/stonetrim_001` |
| `stone/stonewall_001` | `LightmappedGeneric` | `concrete` | `map` | `1` | `stone/stonewall_001` |
| `stone/stonewall_002` | `LightmappedGeneric` | `concrete` | `map` | `1` | `stone/stonewall_002` |

### `t_asmwalls`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `t_asmwalls/t_alldeet3` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_walldeet3` |
| `t_asmwalls/t_asmcrate` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_asmcrate` |
| `t_asmwalls/t_asmcratebase` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_asmcratebase` |
| `t_asmwalls/t_asmcratebase_bump` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_asmcratebase` |
| `t_asmwalls/t_asmplate001` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_asmplate001` |
| `t_asmwalls/t_asmplate001_nobump` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_asmplate001` |
| `t_asmwalls/t_door_001` | `LightmappedGeneric` | `metal` | `map` | `3` | `t_asmwalls/t_door_001` |
| `t_asmwalls/t_filler1` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_filler1` |
| `t_asmwalls/t_filler1_vent` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_filler1_vent` |
| `t_asmwalls/t_floorbase01` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_floorbase01` |
| `t_asmwalls/t_floorbase01_grate` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_floorbase01_grate` |
| `t_asmwalls/t_floorbase01_grate_dx8` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_floorbase01_grate` |
| `t_asmwalls/t_floorbase01_logo` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_floorbase01_logo` |
| `t_asmwalls/t_floorbase01_nolights` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_floorbase01_nolights` |
| `t_asmwalls/t_floorbase01_warning` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_floorbase01_warning` |
| `t_asmwalls/t_floordetail01` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_floordetail01` |
| `t_asmwalls/t_floordetail01_fx` | `Unlittwotexture` | `-` | `map` | `1` | `t_asmwalls/t_floordetail01_fx` |
| `t_asmwalls/t_floortile01` | `LightmappedGeneric` | `metal` | `map` | `3` | `t_asmwalls/t_floortile01` |
| `t_asmwalls/t_floortile02` | `LightmappedGeneric` | `metal` | `map` | `4` | `t_asmwalls/t_floortile02` |
| `t_asmwalls/t_grate256_1` | `LightmappedGeneric` | `metalgrate` | `map` | `3` | `t_asmwalls/t_grate256_1` |
| `t_asmwalls/t_grate256_1_dx8` | `LightmappedGeneric` | `metalgrate` | `map` | `0` | `t_asmwalls/t_grate256_1` |
| `t_asmwalls/t_metalburnt` | `LightmappedGeneric` | `metal` | `map` | `3` | `wood/woodburnt001a` |
| `t_asmwalls/t_metalstair001a` | `LightmappedGeneric` | `metal` | `map` | `3` | `t_asmwalls/t_metalstair001a` |
| `t_asmwalls/t_spawnerbox` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_spawnerbox` |
| `t_asmwalls/t_techsupport01` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_techsupport01` |
| `t_asmwalls/t_techsupport01_flash` | `Unlittwotexture` | `-` | `map` | `0` | `t_asmwalls/doortest_fx` |
| `t_asmwalls/t_techsupport01_fx` | `Unlittwotexture` | `-` | `map` | `1` | `t_asmwalls/t_techsupport01_sweep` |
| `t_asmwalls/t_trim2` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_trim2` |
| `t_asmwalls/t_trim2_blank2` | `LightmappedGeneric` | `metal` | `map` | `3` | `t_asmwalls/t_trim2_blank2` |
| `t_asmwalls/t_trim2_blank2a` | `LightmappedGeneric` | `metal` | `map` | `3` | `t_asmwalls/t_trim2_blank2a` |
| `t_asmwalls/t_trim2_bump` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_trim2` |
| `t_asmwalls/t_trim2_warn` | `LightmappedGeneric` | `metal` | `map` | `4` | `t_asmwalls/t_trim2_warn` |
| `t_asmwalls/t_trim2a` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_trim2a` |
| `t_asmwalls/t_walldeet1` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_walldeet1` |
| `t_asmwalls/t_walldeet1_logo` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_walldeet1_logo` |
| `t_asmwalls/t_walldeet2` | `LightmappedGeneric` | `metal` | `map` | `5` | `t_asmwalls/t_walldeet2` |
| `t_asmwalls/t_walldeet2_line_blue` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_walldeet2_line_blue` |
| `t_asmwalls/t_walldeet2_line_both` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_walldeet2_line_both` |
| `t_asmwalls/t_walldeet2_line_red` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_walldeet2_line_red` |
| `t_asmwalls/t_walldeet2_line_text` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_walldeet2_line_text` |
| `t_asmwalls/t_walldeet2_logo` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_walldeet2_logo` |
| `t_asmwalls/t_walldetail01` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_walldetail01` |
| `t_asmwalls/t_walldetail02` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_walldetail02` |
| `t_asmwalls/t_walldetail03` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_walldetail03` |
| `t_asmwalls/t_walldetail04` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_walldetail04` |
| `t_asmwalls/t_walldetail05` | `LightmappedGeneric` | `metal` | `map` | `5` | `t_asmwalls/t_walldetail05` |
| `t_asmwalls/t_walldetail06` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_walldetail06` |
| `t_asmwalls/t_walldetail07` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_walldetail07` |
| `t_asmwalls/t_walldetail08` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_walldetail08` |
| `t_asmwalls/t_walldetail09` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_walldetail09` |
| `t_asmwalls/t_walldetail10` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_walldetail10` |
| `t_asmwalls/t_wallgrate1` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_wallgrate1` |
| `t_asmwalls/t_wallgrate1_dx8` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_wallgrate1` |
| `t_asmwalls/t_wallgrate2` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_asmwalls/t_wallgrate2` |
| `t_asmwalls/t_wallgrate2_dx8` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_wallgrate2` |
| `t_asmwalls/t_wallgrate2_nobumpnocull` | `LightmappedGeneric` | `metal` | `map` | `2` | `t_asmwalls/t_wallgrate2` |

### `t_exodustex`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `t_exodustex/t_exocrete01` | `LightmappedGeneric` | `concrete` | `map` | `1` | `t_exodustex/t_exocrete01` |
| `t_exodustex/t_exocrete01a` | `LightmappedGeneric` | `concrete` | `map` | `1` | `t_exodustex/t_exocrete01a` |
| `t_exodustex/t_exocrete02` | `LightmappedGeneric` | `concrete` | `map` | `2` | `t_exodustex/t_exocrete02` |
| `t_exodustex/t_exocrete03` | `LightmappedGeneric` | `concrete` | `map` | `1` | `t_exodustex/t_exocrete03` |
| `t_exodustex/t_exocrete04` | `LightmappedGeneric` | `concrete` | `map` | `1` | `t_exodustex/t_exocrete01` |
| `t_exodustex/text1` | `UnlitGeneric` | `-` | `map` | `1` | `t_exodustex/text1` |
| `t_exodustex/text1_screen` | `UnlitTwoTexture` | `-` | `map` | `1` | `t_exodustex/text1` |
| `t_exodustex/text2` | `UnlitGeneric` | `-` | `map` | `1` | `t_exodustex/text2` |
| `t_exodustex/text3` | `UnlitTwoTexture` | `-` | `map` | `1` | `t_exodustex/text3` |

### `t_grate256_1`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `t_grate256_1` | `LightmappedGeneric` | `metalgrate` | `map` | `0` | `t_asmwalls/t_grate256_1` |

### `t_lobbyset`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `t_lobbyset/dys_lobby_conc1` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_lobbyset/dys_lobby_conc1` |
| `t_lobbyset/dys_lobby_conc1_noseam` | `LightmappedGeneric` | `metal` | `map` | `3` | `t_lobbyset/dys_lobby_conc1_noseam` |
| `t_lobbyset/dys_lobby_conc2` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_lobbyset/dys_lobby_conc2` |
| `t_lobbyset/dys_lobby_conc2_noseam` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_lobbyset/dys_lobby_conc2_noseam` |
| `t_lobbyset/dys_lobby_conc3` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_lobbyset/dys_lobby_conc3` |
| `t_lobbyset/dys_lobby_conc3_noseam` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_lobbyset/dys_lobby_conc3_noseam` |

### `t_quetzuku`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `t_quetzuku/q_vgui_disabled` | `UnlitGeneric` | `-` | `map` | `0` | `t_quetzuku/q_vgui_disabled` |
| `t_quetzuku/q_vgui_enabled` | `UnlitGeneric` | `-` | `map` | `0` | `t_quetzuku/q_vgui_enabled` |
| `t_quetzuku/q_vgui_hover` | `UnlitGeneric` | `-` | `map` | `0` | `t_quetzuku/q_vgui_hover` |
| `t_quetzuku/q_vgui_pushed` | `UnlitGeneric` | `-` | `map` | `0` | `t_quetzuku/q_vgui_pushed` |
| `t_quetzuku/t_decal_prop1` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_prop1` |
| `t_quetzuku/t_decal_prop2` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_prop2` |
| `t_quetzuku/t_decal_prop3` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_prop3` |
| `t_quetzuku/t_decal_prop4` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_prop4` |
| `t_quetzuku/t_decal_prop5` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_prop5` |
| `t_quetzuku/t_decal_sign1` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign1` |
| `t_quetzuku/t_decal_sign1a` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign1a` |
| `t_quetzuku/t_decal_sign1b` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign1b` |
| `t_quetzuku/t_decal_sign1c` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign1c` |
| `t_quetzuku/t_decal_sign2` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign2` |
| `t_quetzuku/t_decal_sign2a` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign2a` |
| `t_quetzuku/t_decal_sign2b` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign2b` |
| `t_quetzuku/t_decal_sign2c` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign2c` |
| `t_quetzuku/t_decal_sign3` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign3` |
| `t_quetzuku/t_decal_sign3a` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign3a` |
| `t_quetzuku/t_decal_sign3b` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign3b` |
| `t_quetzuku/t_decal_sign3c` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign3c` |
| `t_quetzuku/t_decal_sign3d` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign3d` |
| `t_quetzuku/t_decal_sign4` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign4` |
| `t_quetzuku/t_decal_sign4a` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_sign4a` |
| `t_quetzuku/t_decal_warn1` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_decal_warn1` |
| `t_quetzuku/t_door01` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_quetzuku/t_door01` |
| `t_quetzuku/t_door01a` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_quetzuku/t_door01a` |
| `t_quetzuku/t_injdoor1` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_quetzuku/t_injdoor1` |
| `t_quetzuku/t_metalwall01a` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_quetzuku/t_metalwall01a` |
| `t_quetzuku/t_metalwall01b` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_quetzuku/t_metalwall01b` |
| `t_quetzuku/t_metalwall01c` | `LightmappedGeneric` | `metal` | `map` | `3` | `t_quetzuku/t_metalwall01c` |
| `t_quetzuku/t_quetdecal1` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_quetdecal1` |
| `t_quetzuku/t_quetdecal2` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_quetdecal2` |
| `t_quetzuku/t_quetdecal2_dirty` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_quetdecal2_dirty` |
| `t_quetzuku/t_quetdecal3` | `LightmappedGeneric` | `-` | `decal` | `0` | `t_quetzuku/t_quetdecal3` |
| `t_quetzuku/t_quetfloor001` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_quetzuku/t_quetfloor001` |
| `t_quetzuku/t_quetfloor002` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_quetzuku/t_quetfloor002` |
| `t_quetzuku/t_quetgraf1` | `LightmappedGeneric` | `-` | `map` | `0` | `t_quetzuku/t_quetgraf1` |
| `t_quetzuku/t_quetgraf2` | `LightmappedGeneric` | `-` | `map` | `0` | `t_quetzuku/t_quetgraf2` |
| `t_quetzuku/t_quetwall001` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_quetzuku/t_quetwall001` |
| `t_quetzuku/t_quetwall002` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_quetzuku/t_quetwall002` |
| `t_quetzuku/t_quetwall003` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_quetzuku/t_quetwall003` |
| `t_quetzuku/t_quetwall004` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_quetzuku/t_quetwall004` |
| `t_quetzuku/t_quetwall005` | `LightmappedGeneric` | `metal` | `map` | `1` | `t_quetzuku/t_quetwall005` |
| `t_quetzuku/vguibg1` | `unlitgeneric` | `-` | `map` | `0` | `t_quetzuku/vguibg1` |
| `t_quetzuku/vguibg2` | `unlitgeneric` | `-` | `map` | `0` | `t_quetzuku/vguibg2` |
| `t_quetzuku/vguibg3` | `unlitgeneric` | `-` | `map` | `0` | `t_quetzuku/vguibg3` |
| `t_quetzuku/vguibg4` | `unlitgeneric` | `-` | `map` | `0` | `-` |
| `t_quetzuku/vguibgwarn_l` | `unlitgeneric` | `-` | `map` | `0` | `-` |
| `t_quetzuku/vguibgwarn_r` | `unlitgeneric` | `-` | `map` | `0` | `-` |

### `t_wallgrate1`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `t_wallgrate1` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_wallgrate1` |

### `t_wallgrate2`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `t_wallgrate2` | `LightmappedGeneric` | `metal` | `map` | `0` | `t_asmwalls/t_wallgrate2` |

### `termireal1`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `termireal1/cath_windows01` | `LightmappedGeneric` | `glass` | `map` | `1` | `termireal1/cath_windows01` |
| `termireal1/cath_windows01_unlit` | `LightmappedGeneric` | `glass` | `map` | `0` | `termireal1/cath_windows01` |
| `termireal1/cath_windows02_round` | `LightmappedGeneric` | `glass` | `map` | `1` | `termireal1/cath_windows02_round` |
| `termireal1/t_aspestos` | `LightmappedGeneric` | `concrete` | `map` | `0` | `termireal1/t_aspestos` |
| `termireal1/t_brick` | `LightmappedGeneric` | `concrete` | `map` | `2` | `termireal1/t_brick` |
| `termireal1/t_brick2` | `LightmappedGeneric` | `concrete` | `map` | `1` | `termireal1/t_brick2` |
| `termireal1/t_concrete1` | `LightmappedGeneric` | `concrete` | `map` | `2` | `termireal1/t_concrete1` |
| `termireal1/t_concrete2` | `LightmappedGeneric` | `concrete` | `map` | `0` | `termireal1/t_concrete2` |
| `termireal1/t_concrete2to3` | `LightmappedGeneric` | `concrete` | `map` | `0` | `termireal1/t_concrete2to3` |
| `termireal1/t_concrete3` | `LightmappedGeneric` | `concrete` | `map` | `0` | `termireal1/t_concrete3` |
| `termireal1/t_door1` | `LightmappedGeneric` | `metal` | `map` | `1` | `termireal1/t_door1` |
| `termireal1/t_door2` | `LightmappedGeneric` | `metal` | `map` | `2` | `termireal1/t_door2` |
| `termireal1/t_door3` | `LightmappedGeneric` | `metal` | `map` | `1` | `termireal1/t_door3` |
| `termireal1/t_pillarblack1` | `LightmappedGeneric` | `concrete` | `map` | `1` | `termireal1/t_pillarblack1` |
| `termireal1/t_pillarblack1_not` | `LightmappedGeneric` | `concrete` | `map` | `0` | `termireal1/t_pillarblack1not` |
| `termireal1/t_pillarblack1not` | `LightmappedGeneric` | `concrete` | `map` | `0` | `termireal1/t_pillarblack1not` |
| `termireal1/t_trashfloor` | `LightmappedGeneric` | `concrete` | `map` | `1` | `termireal1/t_trashfloor` |
| `termireal1/t_tunnelwall` | `LightmappedGeneric` | `concrete` | `map` | `0` | `termireal1/t_tunnelwall` |
| `termireal1/t_vent1` | `LightmappedGeneric` | `metal` | `map` | `2` | `termireal1/t_vent1` |
| `termireal1/t_vent2` | `LightmappedGeneric` | `metal` | `map` | `2` | `termireal1/t_vent2` |

### `termitex`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `termitex/bioidindicator` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/bioidindicator` |
| `termitex/blackfade` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/blackfade` |
| `termitex/blackfade2` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/blackfade2` |
| `termitex/bustout` | `unlitgeneric` | `-` | `map` | `1` | `termitex/bustout` |
| `termitex/bustout_overlay` | `UnlitGeneric` | `-` | `overlay` | `0` | `termitex/bustout_overlay` |
| `termitex/concretefloor031a_detail` | `LightmappedGeneric` | `concrete` | `map` | `2` | `Concrete/concretefloor031a` |
| `termitex/concretewall004a_detail` | `LightmappedGeneric` | `concrete` | `map` | `1` | `Concrete/concretewall004a` |
| `termitex/concretewall004b_detail` | `LightmappedGeneric` | `concrete` | `map` | `2` | `Concrete/concretewall004b` |
| `termitex/concretewall004c_detail` | `LightmappedGeneric` | `concrete` | `map` | `1` | `Concrete/concretewall004c` |
| `termitex/concretewall008a_detail` | `LightmappedGeneric` | `concrete` | `map` | `2` | `Concrete/concretewall008a` |
| `termitex/concretewall008b_detail` | `LightmappedGeneric` | `concrete` | `map` | `0` | `Concrete/concretewall008b` |
| `termitex/concretewall008c_detail` | `LightmappedGeneric` | `concrete` | `map` | `0` | `Concrete/concretewall008c` |
| `termitex/cyberstonewall036a` | `unlitgeneric` | `-` | `map` | `0` | `stone/stonewall036a` |
| `termitex/cyberstonewall050d` | `unlitgeneric` | `-` | `map` | `0` | `stone/stonewall050d` |
| `termitex/cysp_floor01` | `unlitgeneric` | `-` | `map` | `5` | `termitex/cysp_floor01` |
| `termitex/cysp_floor01_trans` | `unlitgeneric` | `-` | `map` | `1` | `termitex/cysp_floor01` |
| `termitex/cysp_floor02` | `unlitgeneric` | `-` | `map` | `0` | `termitex/cysp_floor02` |
| `termitex/cysp_floor02_trans` | `unlitgeneric` | `-` | `map` | `0` | `termitex/cysp_floor02` |
| `termitex/cysp_floor03` | `UnlitGeneric` | `glass` | `map` | `0` | `termitex/cysp_floor03` |
| `termitex/cysp_floor03_blue` | `UnlitGeneric` | `glass` | `map` | `5` | `termitex/cysp_floor03_blue` |
| `termitex/cysp_floor03_blue_trans` | `UnlitGeneric` | `glass` | `map` | `2` | `termitex/cysp_floor03_blue` |
| `termitex/cysp_floor03_purple` | `UnlitGeneric` | `glass` | `map` | `3` | `termitex/cysp_floor03_purple` |
| `termitex/cysp_floor03_purple_trans` | `UnlitGeneric` | `glass` | `map` | `1` | `termitex/cysp_floor03_purple` |
| `termitex/cysp_floor03_red` | `UnlitGeneric` | `glass` | `map` | `1` | `termitex/cysp_floor03_red` |
| `termitex/cysp_floor03_red_trans` | `UnlitGeneric` | `glass` | `map` | `0` | `termitex/cysp_floor03_red` |
| `termitex/cysp_floor03_trans` | `UnlitGeneric` | `glass` | `map` | `0` | `termitex/cysp_floor03` |
| `termitex/cysp_floor03_white` | `UnlitGeneric` | `glass` | `map` | `1` | `termitex/cysp_floor03_white` |
| `termitex/cysp_floor03_white_trans` | `UnlitGeneric` | `glass` | `map` | `2` | `termitex/cysp_floor03_white` |
| `termitex/cysp_floor04_blue` | `UnlitGeneric` | `glass` | `map` | `5` | `termitex/cysp_floor04_blue` |
| `termitex/cysp_floor04_blue_trans` | `UnlitGeneric` | `glass` | `map` | `1` | `termitex/cysp_floor04_blue` |
| `termitex/cysp_floor04_purple` | `UnlitGeneric` | `glass` | `map` | `2` | `termitex/cysp_floor04_purple` |
| `termitex/cysp_floor04_purple_trans` | `UnlitGeneric` | `glass` | `map` | `1` | `termitex/cysp_floor04_purple` |
| `termitex/cysp_floor04_red` | `UnlitGeneric` | `glass` | `map` | `3` | `termitex/cysp_floor04_red` |
| `termitex/cysp_floor04_red_trans` | `UnlitGeneric` | `glass` | `map` | `0` | `termitex/cysp_floor04_red` |
| `termitex/cysp_glow1` | `UnlitGeneric` | `glass` | `map` | `3` | `termitex/cysp_glow1` |
| `termitex/cysp_liners01` | `UnlitGeneric` | `glass` | `map` | `2` | `termitex/cysp_liners01` |
| `termitex/cysp_liners02` | `UnlitGeneric` | `glass` | `map` | `2` | `termitex/cysp_liners02` |
| `termitex/cysp_newscroll_blue` | `Unlittwotexture` | `-` | `map` | `4` | `termitex/cysp_newscroll_fx` |
| `termitex/cysp_newscroll_blue2` | `Unlittwotexture` | `-` | `map` | `6` | `termitex/cysp_newscroll_fx2` |
| `termitex/cysp_scroller01` | `UnlitGeneric` | `glass` | `map` | `2` | `termitex/cysp_scroller01` |
| `termitex/cysp_scroller01_trans` | `UnlitGeneric` | `glass` | `map` | `6` | `termitex/cysp_scroller01` |
| `termitex/cysp_scroller02` | `UnlitGeneric` | `glass` | `map` | `1` | `termitex/cysp_scroller02` |
| `termitex/cysp_scroller02_trans` | `UnlitGeneric` | `glass` | `map` | `7` | `termitex/cysp_scroller02` |
| `termitex/cysp_scroller03` | `UnlitGeneric` | `glass` | `map` | `3` | `termitex/cysp_scroller03` |
| `termitex/cysp_scroller03_trans` | `UnlitGeneric` | `glass` | `map` | `2` | `termitex/cysp_scroller03` |
| `termitex/cysp_wall_decal1` | `UnlitGeneric` | `-` | `decal` | `0` | `termitex/cysp_wall_decal1` |
| `termitex/digits1` | `UnlitGeneric` | `-` | `map` | `1` | `termitex/digits1` |
| `termitex/digits2` | `UnlitGeneric` | `-` | `map` | `1` | `termitex/digits2` |
| `termitex/digits_vgui_disabled` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/digits_vgui_disabled` |
| `termitex/digits_vgui_enabled` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/digits_vgui_enabled` |
| `termitex/digits_vgui_hover` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/digits_vgui_hover` |
| `termitex/digits_vgui_pushed` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/digits_vgui_pushed` |
| `termitex/finallaser1` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/finallaser1` |
| `termitex/finallaser1_red` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/finallaser1_red` |
| `termitex/finallaser1_sprite` | `Sprite` | `-` | `map` | `0` | `termitex/finallaser1_sprite` |
| `termitex/icon_door` | `unlitgeneric` | `-` | `map` | `1` | `termitex/icon_door` |
| `termitex/icon_lock` | `unlitgeneric` | `-` | `map` | `3` | `termitex/icon_lock` |
| `termitex/icon_turret` | `unlitgeneric` | `-` | `map` | `2` | `termitex/icon_turret` |
| `termitex/meatscreen_bg` | `UnlitGeneric` | `metal` | `map` | `0` | `termitex/meatscreen_bg` |
| `termitex/meatscreen_overlay` | `UnlitGeneric` | `glass` | `overlay` | `2` | `termitex/meatscreen_overlay` |
| `termitex/meatscreen_underlay` | `UnlitGeneric` | `glass` | `map` | `0` | `termitex/meatscreen_underlay` |
| `termitex/padbg` | `UnlitGeneric` | `metal` | `map` | `1` | `termitex/padbg` |
| `termitex/padunderlay` | `UnlitGeneric` | `metal` | `map` | `0` | `termitex/padunderlay` |
| `termitex/power_beam_blue` | `vertexlitgeneric` | `-` | `map` | `1` | `termitex/powerwarp1_underlayer2` |
| `termitex/power_beam_blue_dx8` | `unlitgeneric` | `-` | `map` | `0` | `termitex/powerwarp1_underlayer` |
| `termitex/power_beam_red` | `vertexlitgeneric` | `-` | `map` | `1` | `termitex/powerwarp1_underlayer2_red` |
| `termitex/power_beam_red_dx8` | `unlitgeneric` | `-` | `map` | `0` | `termitex/powerwarp1_red` |
| `termitex/powerbeam_1_alpha` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/powerwarp1_red` |
| `termitex/powerbeam_1_bw` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/powerbeam_1_bw` |
| `termitex/powerwarp1` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/powerwarp1` |
| `termitex/powerwarp1_red` | `Cloud` | `-` | `map` | `0` | `termitex/powerwarp1_red` |
| `termitex/powerwarp1a` | `Cloud` | `-` | `map` | `0` | `termitex/powerwarp1_underlayer` |
| `termitex/powerwarp1a_e` | `Cloud` | `-` | `map` | `0` | `termitex/powerwarp1_underlayer` |
| `termitex/powerwarp1a_n` | `Cloud` | `-` | `map` | `0` | `termitex/powerwarp1_underlayer` |
| `termitex/powerwarp1a_red` | `Cloud` | `-` | `map` | `0` | `termitex/powerwarp1_red` |
| `termitex/powerwarp1a_s` | `Cloud` | `-` | `map` | `0` | `termitex/powerwarp1_underlayer` |
| `termitex/powerwarp1a_w` | `Cloud` | `-` | `map` | `0` | `termitex/powerwarp1_underlayer` |
| `termitex/stonewall036a_cyber` | `unlitgeneric` | `-` | `map` | `1` | `termitex/stonewall036a_cyber` |
| `termitex/stonewall036a_transition0` | `unlitgeneric` | `-` | `map` | `1` | `termitex/stonewall036a_transition0` |
| `termitex/stonewall036a_transition1` | `unlitgeneric` | `-` | `map` | `1` | `termitex/stonewall036a_transition1` |
| `termitex/stonewall036a_transition2` | `unlitgeneric` | `-` | `map` | `1` | `termitex/stonewall036a_transition2` |
| `termitex/stonewall050d_cyber` | `unlitgeneric` | `-` | `map` | `1` | `termitex/stonewall050d_cyber` |
| `termitex/stonewall050d_transition0` | `unlitgeneric` | `-` | `map` | `1` | `termitex/stonewall050d_transition0` |
| `termitex/stonewall050d_transition1` | `unlitgeneric` | `-` | `map` | `1` | `termitex/stonewall050d_transition1` |
| `termitex/stonewall050d_transition2` | `unlitgeneric` | `-` | `map` | `1` | `termitex/stonewall050d_transition2` |
| `termitex/t_conveyer` | `LightmappedGeneric` | `metal` | `map` | `2` | `termitex/t_conveyer` |
| `termitex/t_forcefield` | `Refract` | `metal` | `map` | `1` | `-` |
| `termitex/t_forcefield_dx7` | `UnlitTwoTexture` | `metal` | `map` | `0` | `models/props_combine/stasisshield_dx7` |
| `termitex/t_metallight` | `LightmappedGeneric` | `-` | `map` | `2` | `termitex/t_metallight` |
| `termitex/t_warnbandrecycle` | `LightmappedGeneric` | `metal` | `map` | `2` | `termitex/t_warnbandrecycle` |
| `termitex/thxcontre` | `lightmappedGeneric` | `-` | `map` | `0` | `termitex/thxcontre` |
| `termitex/transblack` | `UnlitGeneric` | `-` | `map` | `1` | `termitex/transblack` |
| `termitex/turretinfo` | `UnlitGeneric` | `-` | `map` | `1` | `termitex/turretinfo` |
| `termitex/whitefade1` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/whitefade1` |
| `termitex/whitefade2` | `UnlitGeneric` | `-` | `map` | `0` | `termitex/whitefade2` |

### `thermal_overlay`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `thermal_overlay` | `Modulate` | `-` | `overlay` | `0` | `thermal_overlay` |

### `turretshape`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `turretshape/skina` | `VertexLitGeneric` | `-` | `map` | `0` | `turretshape/skina` |

### `twincannon`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `twincannon/TUBE_NOCULL-cube256` | `UnlitGeneric` | `metal` | `map` | `1` | `cyberspace/cube256` |
| `twincannon/TUBE_NOCULL-twin_cyberred_trans_squares` | `UnlitGeneric` | `metal` | `map` | `4` | `twincannon/twin_cyberred_trans_squares` |
| `twincannon/TUBE_NOCULL-wall_squaregrey` | `UnlitGeneric` | `cybergravity` | `map` | `1` | `cyberspace/wall_squaregrey` |
| `twincannon/asphaltcrack` | `LightmappedGeneric` | `concrete` | `map` | `0` | `twincannon/asphaltcrack` |
| `twincannon/billboard_bigmax` | `LightmappedGeneric` | `concrete` | `map` | `2` | `twincannon/billboard_bigmax` |
| `twincannon/billboard_science_adf` | `LightmappedGeneric` | `concrete` | `map` | `0` | `twincannon/billboard_science_adf` |
| `twincannon/billboard_science_mcl` | `LightmappedGeneric` | `concrete` | `map` | `1` | `twincannon/billboard_science_mcl` |
| `twincannon/black512` | `UnlitGeneric` | `metal` | `map` | `0` | `twincannon/black512` |
| `twincannon/brushblockmetal` | `UnlitGeneric` | `metal` | `map` | `5` | `twincannon/brushblockmetal` |
| `twincannon/cautionsticker_overlay` | `LightmappedGeneric` | `metal` | `overlay` | `0` | `twincannon/cautionsticker_overlay` |
| `twincannon/concretefloor009a_fixed` | `LightmappedGeneric` | `concrete` | `map` | `1` | `Concrete/concretefloor009a` |
| `twincannon/csterrain2` | `LightmappedGeneric` | `-` | `map` | `0` | `-` |
| `twincannon/csterrain2_dark` | `UnlitGeneric` | `metal` | `map` | `2` | `twincannon/csterrain2_dark` |
| `twincannon/csterrain_green` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/csterrain_green` |
| `twincannon/cube_green2` | `UnlitGeneric` | `metal` | `map` | `0` | `twincannon/cube_green2` |
| `twincannon/cube_green2dark` | `UnlitGeneric` | `metal` | `map` | `2` | `twincannon/cube_green2dark` |
| `twincannon/cube_green3` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/cube_green3` |
| `twincannon/cube_white` | `UnlitGeneric` | `metal` | `map` | `2` | `twincannon/cube_white` |
| `twincannon/cube_white_trans` | `UnlitGeneric` | `metal` | `map` | `0` | `twincannon/cube_white_trans` |
| `twincannon/cyber_arrow_scroll` | `UnlitTwoTexture` | `no_decal` | `map` | `3` | `twincannon/cyber_arrow_scroll` |
| `twincannon/cyber_brightorange` | `UnlitGeneric` | `metal` | `map` | `2` | `twincannon/cyber_brightorange` |
| `twincannon/cyber_sprite_test` | `UnlitGeneric` | `-` | `map` | `1` | `twincannon/cyber_sprite_test` |
| `twincannon/cyber_sprite_test2` | `UnlitGeneric` | `-` | `map` | `0` | `twincannon/cyber_sprite_test` |
| `twincannon/cybergoo_scroll` | `unlitgeneric` | `-` | `map` | `1` | `twincannon/cybergoo_scroll` |
| `twincannon/cybergoo_scroll_additive` | `unlitgeneric` | `-` | `map` | `3` | `twincannon/cybergoo_scroll` |
| `twincannon/cybergoo_scroll_with1024mask` | `UnlitTwoTexture` | `metal` | `map` | `1` | `twincannon/cybergoo_scroll` |
| `twincannon/cybergoo_scroll_with1024mask2` | `UnlitTwoTexture` | `metal` | `map` | `1` | `twincannon/cybergoo_scroll` |
| `twincannon/cybergoo_scroll_with1024mask3` | `UnlitTwoTexture` | `metal` | `map` | `1` | `twincannon/cybergoo_scroll` |
| `twincannon/cybergoo_scroll_with1024mask4` | `UnlitTwoTexture` | `metal` | `map` | `0` | `twincannon/cybergoo_scroll` |
| `twincannon/cybergoo_scroll_with1024mask5` | `UnlitTwoTexture` | `metal` | `map` | `0` | `twincannon/cybergoo_scroll` |
| `twincannon/cybergoo_scroll_withskymask` | `UnlitTwoTexture` | `metal` | `map` | `1` | `twincannon/cybergoo_scroll` |
| `twincannon/cybergreenblend` | `WorldVertexTransition` | `metal` | `map` | `0` | `cyberspace/cube_green` |
| `twincannon/datatrustposters/dailygrind` | `LightmappedGeneric` | `-` | `map` | `0` | `twincannon/datatrustposters/dailygrind` |
| `twincannon/datatrustposters/dailygrind_torn` | `LightmappedGeneric` | `-` | `map` | `0` | `twincannon/datatrustposters/dailygrind_torn` |
| `twincannon/datatrustposters/datawhoweare` | `LightmappedGeneric` | `-` | `map` | `0` | `twincannon/datatrustposters/datawhoweare` |
| `twincannon/datatrustposters/datawhoweare_torn` | `LightmappedGeneric` | `-` | `map` | `0` | `twincannon/datatrustposters/datawhoweare_torn` |
| `twincannon/datatrustposters/decker` | `LightmappedGeneric` | `-` | `map` | `0` | `twincannon/datatrustposters/decker` |
| `twincannon/datatrustposters/decker_torn` | `LightmappedGeneric` | `-` | `map` | `0` | `twincannon/datatrustposters/decker_torn` |
| `twincannon/datatrustposters/obedience` | `LightmappedGeneric` | `-` | `map` | `0` | `twincannon/datatrustposters/obedience` |
| `twincannon/datatrustposters/obedience_torn` | `LightmappedGeneric` | `-` | `map` | `0` | `twincannon/datatrustposters/obedience_torn` |
| `twincannon/dmtcrate` | `LightmappedGeneric` | `metal` | `map` | `1` | `twincannon/dmtcrate` |
| `twincannon/dmtcrate_side` | `LightmappedGeneric` | `metal` | `map` | `1` | `twincannon/dmtcrate_side` |
| `twincannon/dmtcrate_top` | `LightmappedGeneric` | `metal` | `map` | `2` | `twincannon/dmtcrate_top` |
| `twincannon/dojo/brushblockwood` | `UnlitGeneric` | `wood` | `map` | `0` | `twincannon/brushblockmetal` |
| `twincannon/dojo/dojocarpet` | `LightmappedGeneric` | `carpet` | `map` | `0` | `twincannon/dojo/dojocarpet` |
| `twincannon/dojo/dojocarpet_blue` | `LightmappedGeneric` | `carpet` | `map` | `0` | `twincannon/dojo/dojocarpet_blue` |
| `twincannon/dojo/dojocarpet_purple` | `LightmappedGeneric` | `carpet` | `map` | `0` | `twincannon/dojo/dojocarpet_purple` |
| `twincannon/dojo/dojograss` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dojo/dojograss` |
| `twincannon/dojo/dojopaper` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dojo/dojopaper` |
| `twincannon/dojo/dojopaper_squares` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dojo/dojopaper_squares` |
| `twincannon/dojo/dojopaper_squares_trans` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dojo/dojopaper_squares_trans` |
| `twincannon/dojo/dojopaper_trans` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dojo/dojopaper_trans` |
| `twincannon/dojo/dojopaper_trans_broke` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dojo/dojopaper_trans_broke` |
| `twincannon/dojo/dojoscore_corp0` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_corp0` |
| `twincannon/dojo/dojoscore_corp1` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_corp1` |
| `twincannon/dojo/dojoscore_corp2` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_corp2` |
| `twincannon/dojo/dojoscore_corp3` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_corp3` |
| `twincannon/dojo/dojoscore_corp4` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_corp4` |
| `twincannon/dojo/dojoscore_corp5` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_corp5` |
| `twincannon/dojo/dojoscore_corp6` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_corp6` |
| `twincannon/dojo/dojoscore_corp7` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_corp7` |
| `twincannon/dojo/dojoscore_corp8` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_corp8` |
| `twincannon/dojo/dojoscore_punk0` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_punk0` |
| `twincannon/dojo/dojoscore_punk1` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_punk1` |
| `twincannon/dojo/dojoscore_punk2` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_punk2` |
| `twincannon/dojo/dojoscore_punk3` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_punk3` |
| `twincannon/dojo/dojoscore_punk4` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_punk4` |
| `twincannon/dojo/dojoscore_punk5` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_punk5` |
| `twincannon/dojo/dojoscore_punk6` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_punk6` |
| `twincannon/dojo/dojoscore_punk7` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_punk7` |
| `twincannon/dojo/dojoscore_punk8` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/dojo/dojoscore_punk8` |
| `twincannon/dojo/floorboard2` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/floorboard2` |
| `twincannon/dojo/floorboard2_noshine` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/floorboard2` |
| `twincannon/dojo/floorboard2dark` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/floorboard2dark` |
| `twincannon/dojo/floorboard2dark_noshine` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/floorboard2dark` |
| `twincannon/dojo/gong_blue` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/dojo/gong_blue` |
| `twincannon/dojo/gong_red` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/dojo/gong_red` |
| `twincannon/dojo/rocktiles` | `LightmappedGeneric` | `concrete` | `map` | `0` | `twincannon/dojo/rocktiles` |
| `twincannon/dojo/stumptop` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/stumptop` |
| `twincannon/dojo/tcwh` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dojo/tcwh` |
| `twincannon/dojo/wallscroll1` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dojo/wallscroll1` |
| `twincannon/dojo/wallscroll2` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dojo/wallscroll2` |
| `twincannon/dojo/whitestucco` | `LightmappedGeneric` | `cardboard` | `map` | `0` | `twincannon/dojo/whitestucco` |
| `twincannon/dojo/wood_floorboard` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/wood_floorboard` |
| `twincannon/dojo/woodchips` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dojo/woodchips` |
| `twincannon/dojo/woodlog` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/woodlog` |
| `twincannon/dojo/woodplank` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/woodplank` |
| `twincannon/dojo/woodplank2` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/woodplank2` |
| `twincannon/dojo/woodplank3` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/woodplank3` |
| `twincannon/dojo/woodplank_tiled` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/woodplank_tiled` |
| `twincannon/dojo/yinyang5` | `LightmappedGeneric` | `wood` | `map` | `0` | `twincannon/dojo/yinyang5` |
| `twincannon/dys_cleanwall2_grey` | `LightmappedGeneric` | `metal` | `map` | `2` | `twincannon/dys_cleanwall2_grey` |
| `twincannon/dys_cpd1_green` | `LightmappedGeneric` | `metal` | `map` | `1` | `twincannon/dys_cpd1_green` |
| `twincannon/dys_cpd2_green` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/dys_cpd2_green` |
| `twincannon/dys_office/cubicle_curved_side` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dys_office/cubicle_curved_side` |
| `twincannon/dys_office/cubicle_side` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dys_office/cubicle_side` |
| `twincannon/dys_office/dys_office_concretewall013a_with_selfillum` | `LightmappedGeneric` | `concrete` | `map` | `0` | `twincannon/dys_office/dys_office_concretewall013a_with_selfillum` |
| `twincannon/dys_office/dys_wall_painted_frost` | `LightmappedGeneric` | `metal` | `map` | `1` | `twincannon/dys_office/dys_wall_painted_frost` |
| `twincannon/dys_office/metalwall045a_ventsound` | `LightmappedGeneric` | `metalvent` | `map` | `8` | `Metal/metalwall045a` |
| `twincannon/dys_office/office_ceiling_tile` | `LightmappedGeneric` | `concrete` | `map` | `0` | `twincannon/dys_office/office_ceiling_tile` |
| `twincannon/dys_office/office_ceiling_tile_light` | `LightmappedGeneric` | `concrete` | `map` | `0` | `twincannon/dys_office/office_ceiling_tile_light` |
| `twincannon/dys_office/office_forcefield_corp_outer` | `UnlitTwoTexture` | `no_decal` | `map` | `3` | `twincannon/dys_office/office_forcefield_corp_outer` |
| `twincannon/dys_office/office_wall` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dys_office/office_wall` |
| `twincannon/dys_office/office_wall2` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dys_office/office_wall2` |
| `twincannon/dys_office/office_wall2_red` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/dys_office/office_wall2_red` |
| `twincannon/dys_office/overlay_anonymous` | `LightmappedGeneric` | `concrete` | `overlay` | `0` | `twincannon/dys_office/overlay_anonymous` |
| `twincannon/dys_office/overlay_frost` | `LightmappedGeneric` | `concrete` | `overlay` | `0` | `twincannon/dys_office/overlay_frost` |
| `twincannon/dys_office/overlay_wiring` | `LightmappedGeneric` | `concrete` | `overlay` | `0` | `twincannon/dys_office/overlay_wiring` |
| `twincannon/dys_office/overlay_wiring2` | `LightmappedGeneric` | `concrete` | `overlay` | `0` | `twincannon/dys_office/overlay_wiring2` |
| `twincannon/dys_office/overlay_wiring3` | `LightmappedGeneric` | `concrete` | `overlay` | `0` | `twincannon/dys_office/overlay_wiring3` |
| `twincannon/dys_office/window_outline` | `LightmappedGeneric` | `concrete` | `map` | `0` | `twincannon/dys_office/window_outline` |
| `twincannon/dys_office/windowsill_test` | `LightmappedGeneric` | `concrete` | `map` | `0` | `twincannon/dys_office/windowsill_test` |
| `twincannon/dys_spawnglow_green` | `UnlitGeneric` | `-` | `map` | `1` | `twincannon/dys_spawnglow_green` |
| `twincannon/dys_spawnglow_red` | `UnlitGeneric` | `-` | `map` | `2` | `twincannon/dys_spawnglow_red` |
| `twincannon/dys_vacaldoor_nologo` | `LightmappedGeneric` | `metal` | `map` | `2` | `twincannon/dys_vacaldoor_nologo` |
| `twincannon/dys_vacextwall4_green` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/dys_vacextwall4_green` |
| `twincannon/dys_vacextwall4_green_dark` | `LightmappedGeneric` | `metal` | `map` | `1` | `twincannon/dys_vacextwall4_green_dark` |
| `twincannon/dys_vacextwall_trimdark` | `LightmappedGeneric` | `metal` | `map` | `2` | `twincannon/dys_vacextwall_trimdark` |
| `twincannon/dz` | `LightmappedGeneric` | `concrete` | `map` | `0` | `twincannon/dz` |
| `twincannon/fortress_new_punk_forcefield` | `UnlitTwoTexture` | `no_decal` | `map` | `4` | `twincannon/fortress_new_punk_forcefield` |
| `twincannon/hexfloortex` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/hexfloortex` |
| `twincannon/melteddoorblend` | `WorldVertexTransition` | `metal` | `map` | `0` | `vaccinert/dys_vacaldoor` |
| `twincannon/metal_cover_overlay` | `LightmappedGeneric` | `metal` | `overlay` | `0` | `twincannon/metal_cover_overlay` |
| `twincannon/metalfloor001a_vent` | `LightmappedGeneric` | `metalvent` | `map` | `2` | `metal/metalfloor001a` |
| `twincannon/metalfloor003a_vent` | `LightmappedGeneric` | `metalvent` | `map` | `3` | `metal/metalfloor003a` |
| `twincannon/mine_cybertext_busy` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_busy` |
| `twincannon/mine_cybertext_eu1` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_eu1` |
| `twincannon/mine_cybertext_eu2` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_eu2` |
| `twincannon/mine_cybertext_eu3` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_eu3` |
| `twincannon/mine_cybertext_offline` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_offline` |
| `twincannon/mine_cybertext_online` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_online` |
| `twincannon/mine_cybertext_open` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_open` |
| `twincannon/mine_cybertext_override` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_override` |
| `twincannon/mine_cybertext_port1` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_port1` |
| `twincannon/mine_cybertext_port1busybandwithoverride` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_port1busybandwithoverride` |
| `twincannon/mine_cybertext_port2` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_port2` |
| `twincannon/mine_cybertext_port2busybandwithoverride` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_port2busybandwithoverride` |
| `twincannon/mine_cybertext_power` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_power` |
| `twincannon/mine_cybertext_powerofflinescreen` | `UnlitGeneric` | `metal` | `map` | `0` | `twincannon/mine_cybertext_powerofflinescreen` |
| `twincannon/mine_cybertext_poweronlinescreen` | `UnlitGeneric` | `metal` | `map` | `0` | `twincannon/mine_cybertext_poweronlinescreen` |
| `twincannon/mine_cybertext_security` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_security` |
| `twincannon/mine_cybertext_standard` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/mine_cybertext_standard` |
| `twincannon/mine_futuredmtscreen_blank` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/mine_futuredmtscreen_blank` |
| `twincannon/mine_futuredmtscreen_eu1leftarrow` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/mine_futuredmtscreen_eu1leftarrow` |
| `twincannon/mine_futuredmtscreen_eu1rightarrow` | `UnlitGeneric` | `glass` | `map` | `0` | `twincannon/mine_futuredmtscreen_eu1rightarrow` |
| `twincannon/mine_futuredmtscreen_eu2leftarrow` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/mine_futuredmtscreen_eu2leftarrow` |
| `twincannon/mine_futuredmtscreen_eu2rightarrow` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/mine_futuredmtscreen_eu2rightarrow` |
| `twincannon/mine_futuredmtscreen_eu3leftarrow` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/mine_futuredmtscreen_eu3leftarrow` |
| `twincannon/mine_futuredmtscreen_eu3rightarrow` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/mine_futuredmtscreen_eu3rightarrow` |
| `twincannon/mine_futuredmtscreen_laserleftarrow` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/mine_futuredmtscreen_laserleftarrow` |
| `twincannon/mine_futuredmtscreen_laserrightarrow` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/mine_futuredmtscreen_laserrightarrow` |
| `twincannon/mine_map` | `LightmappedGeneric` | `glass` | `map` | `1` | `twincannon/mine_map` |
| `twincannon/mine_map2` | `LightmappedGeneric` | `glass` | `map` | `0` | `twincannon/mine_map2` |
| `twincannon/mine_punkscreen` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/mine_punkscreen` |
| `twincannon/moltenrock` | `LightmappedGeneric` | `dirt` | `map` | `0` | `twincannon/moltenrock` |
| `twincannon/new/blend_gravel_road` | `WorldVertexTransition` | `dirt` | `map` | `2` | `twincannon/new/road1024x512` |
| `twincannon/new/currentstatus_datatrustdoor` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/new/currentstatus_datatrustdoor` |
| `twincannon/new/currentstatus_locked` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/new/currentstatus_locked` |
| `twincannon/new/currentstatus_unlocked` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/new/currentstatus_unlocked` |
| `twincannon/new/fortress_tumbler_arrows` | `UnlitGeneric` | `metal` | `map` | `0` | `twincannon/new/fortress_tumbler_arrows` |
| `twincannon/new/luc_crate_front` | `LightMappedGeneric` | `wood` | `map` | `1` | `twincannon/new/luc_crate_front` |
| `twincannon/new/luc_crate_front_nodecal` | `LightMappedGeneric` | `wood` | `decal` | `2` | `twincannon/new/luc_crate_front_nodecal` |
| `twincannon/new/luc_crate_side` | `LightMappedGeneric` | `wood` | `map` | `1` | `twincannon/new/luc_crate_side` |
| `twincannon/new/luc_crate_side_nodecal` | `LightMappedGeneric` | `wood` | `decal` | `1` | `twincannon/new/luc_crate_side_nodecal` |
| `twincannon/new/paper` | `LightMappedGeneric` | `concrete` | `map` | `0` | `twincannon/new/paper` |
| `twincannon/new/punkforcefield` | `UnlitTwoTexture` | `no_decal` | `map` | `3` | `models/props_combine/stasisshield_dx7` |
| `twincannon/new/road1024x512` | `LightMappedGeneric` | `concrete` | `map` | `0` | `twincannon/new/road1024x512` |
| `twincannon/new/road1024x512_lot` | `LightMappedGeneric` | `concrete` | `map` | `0` | `twincannon/new/road1024x512_lot` |
| `twincannon/new/road1024x512_lot_overlay` | `LightMappedGeneric` | `concrete` | `overlay` | `0` | `twincannon/new/road1024x512_lot_overlay` |
| `twincannon/new/static` | `UnlitGeneric` | `glass` | `map` | `4` | `twincannon/new/static` |
| `twincannon/new/yara` | `LightMappedGeneric` | `concrete` | `map` | `0` | `twincannon/new/yara` |
| `twincannon/nodecal_copies/brickwall052b_nodecal` | `LightmappedGeneric` | `brick` | `decal` | `1` | `Brick/brickwall052b` |
| `twincannon/nodecal_copies/concretewall004b_nodecal` | `LightmappedGeneric` | `concrete` | `decal` | `2` | `Concrete/concretewall004b` |
| `twincannon/nodecal_copies/concretewall008a_nodecal` | `LightmappedGeneric` | `concrete` | `decal` | `3` | `Concrete/concretewall008a` |
| `twincannon/nodecal_copies/dys_fortress-tile_nodecal` | `LightmappedGeneric` | `tile` | `decal` | `1` | `Tile/tilewall009b` |
| `twincannon/nodecal_copies/metalfloor005a_nodecal` | `LightmappedGeneric` | `metal` | `decal` | `3` | `Metal/metalfloor005a` |
| `twincannon/nodecal_copies/orange_base` | `unlitgeneric` | `glass` | `decal` | `1` | `cysp2/orange_base` |
| `twincannon/overlay_dirttest` | `LightmappedGeneric` | `dirt` | `overlay` | `0` | `twincannon/overlay_dirttest` |
| `twincannon/overlay_dirttest2` | `LightmappedGeneric` | `dirt` | `overlay` | `0` | `twincannon/overlay_dirttest2` |
| `twincannon/overlay_futuredmt_shitty` | `LightmappedGeneric` | `metal` | `overlay` | `0` | `twincannon/overlay_futuredmt_shitty` |
| `twincannon/overlay_handle` | `LightmappedGeneric` | `metal` | `overlay` | `0` | `twincannon/overlay_handle` |
| `twincannon/overlay_metalcover` | `LightmappedGeneric` | `metal` | `overlay` | `0` | `twincannon/overlay_metalcover` |
| `twincannon/overlay_puddle_decal` | `UnlitGeneric` | `-` | `decal` | `0` | `-` |
| `twincannon/overlay_rust` | `LightmappedGeneric` | `metal` | `overlay` | `0` | `twincannon/overlay_rust` |
| `twincannon/overlay_turret_paint` | `LightmappedGeneric` | `metal` | `overlay` | `0` | `twincannon/overlay_turret_paint` |
| `twincannon/overlay_turret_paint_long` | `LightmappedGeneric` | `metal` | `overlay` | `0` | `twincannon/overlay_turret_paint_long` |
| `twincannon/overlay_vent` | `LightmappedGeneric` | `metal` | `overlay` | `0` | `twincannon/overlay_vent` |
| `twincannon/road_asphalt` | `LightmappedGeneric` | `concrete` | `map` | `0` | `twincannon/road_asphalt` |
| `twincannon/road_asphalt2` | `LightmappedGeneric` | `concrete` | `map` | `1` | `twincannon/road_asphalt2` |
| `twincannon/road_yellowline` | `LightmappedGeneric` | `concrete` | `map` | `1` | `twincannon/road_yellowline` |
| `twincannon/scanline_additive` | `UnlitGeneric` | `glass` | `map` | `1` | `dev/dev_scanline` |
| `twincannon/sewerlid` | `LightmappedGeneric` | `metal` | `map` | `1` | `twincannon/sewerlid` |
| `twincannon/speedpad_arrow_scroller` | `UnlitGeneric` | `-` | `map` | `1` | `twincannon/speedpad_arrow_scroller` |
| `twincannon/std` | `unlitgeneric` | `-` | `map` | `1` | `twincannon/std` |
| `twincannon/sweeper3new_blue` | `unlitgeneric` | `-` | `map` | `3` | `twincannon/sweeper3new_blue` |
| `twincannon/sweeper3new_red` | `unlitgeneric` | `-` | `map` | `4` | `twincannon/sweeper3new_red` |
| `twincannon/teal_gradient_additive` | `UnlitGeneric` | `-` | `map` | `1` | `twincannon/teal_gradient_additive` |
| `twincannon/tile_blocky_hex_blue` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/tile_blocky_hex_blue` |
| `twincannon/toll_barrier_wood` | `LightmappedGeneric` | `wood` | `map` | `2` | `twincannon/toll_barrier_wood` |
| `twincannon/toxicslime_walkable_nodecal` | `LightmappedGeneric` | `slipperyslime` | `decal` | `0` | `Nature/toxicslime002a` |
| `twincannon/trespass_sign_back` | `LightmappedGeneric` | `wood` | `map` | `1` | `twincannon/trespass_sign_back` |
| `twincannon/trespass_sign_front` | `LightmappedGeneric` | `wood` | `map` | `1` | `twincannon/trespass_sign_front` |
| `twincannon/trespass_sign_woodplank` | `LightmappedGeneric` | `wood` | `map` | `1` | `twincannon/trespass_sign_woodplank` |
| `twincannon/twin_blendcliffdirt` | `WorldVertexTransition` | `dirt` | `map` | `1` | `nature/dirtfloor001a` |
| `twincannon/twin_blendoutsiderockdirt` | `WorldVertexTransition` | `dirt` | `map` | `1` | `nature/rockfloor005a` |
| `twincannon/twin_blendoutsiderockgrass` | `WorldVertexTransition` | `dirt` | `map` | `1` | `nature/rockfloor005a` |
| `twincannon/twin_caveblend` | `WorldVertexTransition` | `dirt` | `map` | `1` | `nature/dirtfloor001a` |
| `twincannon/twin_caveblend_bump` | `WorldVertexTransition` | `dirt` | `map` | `1` | `nature/dirtfloor001a` |
| `twincannon/twin_caveblend_bump_moltenrock` | `WorldVertexTransition` | `dirt` | `map` | `1` | `nature/dirtfloor001a` |
| `twincannon/twin_caveblend_moltenrock` | `WorldVertexTransition` | `dirt` | `map` | `1` | `nature/dirtfloor001a` |
| `twincannon/twin_caveblend_rockfloor` | `WorldVertexTransition` | `dirt` | `map` | `1` | `nature/dirtfloor001a` |
| `twincannon/twin_caveblend_rockfloor2` | `WorldVertexTransition` | `dirt` | `map` | `1` | `nature/rockwall001a` |
| `twincannon/twin_caveblend_rockfloor3` | `WorldVertexTransition` | `dirt` | `map` | `1` | `nature/rockwall001a` |
| `twincannon/twin_cavefloorblend` | `WorldVertexTransition` | `dirt` | `map` | `1` | `nature/dirtfloor001a` |
| `twincannon/twin_cyberblack` | `UnlitGeneric` | `metal` | `map` | `5` | `tools/toolsblack` |
| `twincannon/twin_cyberblue` | `UnlitGeneric` | `metal` | `map` | `8` | `twincannon/twin_cyberblue` |
| `twincannon/twin_cyberblue_trans` | `UnlitGeneric` | `metal` | `map` | `4` | `twincannon/twin_cyberblue_trans` |
| `twincannon/twin_cyberblue_trans_additive` | `UnlitGeneric` | `metal` | `map` | `2` | `twincannon/twin_cyberblue_trans` |
| `twincannon/twin_cyberblue_trans_additive_nocull` | `UnlitGeneric` | `metal` | `map` | `3` | `twincannon/twin_cyberblue_trans` |
| `twincannon/twin_cybergreen` | `UnlitGeneric` | `metal` | `map` | `5` | `twincannon/twin_cybergreen` |
| `twincannon/twin_cybergreen2_trans_additive` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/twin_cybergreen2_trans_additive` |
| `twincannon/twin_cybergreen3_trans` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/twin_cybergreen3_trans_additive` |
| `twincannon/twin_cybergreen3_trans_additive` | `UnlitGeneric` | `metal` | `map` | `0` | `twincannon/twin_cybergreen3_trans_additive` |
| `twincannon/twin_cybergreen3_trans_culled` | `UnlitGeneric` | `metal` | `map` | `0` | `twincannon/twin_cybergreen3_trans_additive` |
| `twincannon/twin_cybergreen4_trans` | `UnlitGeneric` | `metal` | `map` | `0` | `twincannon/twin_cybergreen4_trans` |
| `twincannon/twin_cybergreen_trans_additive` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/twin_cybergreen_trans_additive` |
| `twincannon/twin_cybergreen_trans_additive_with1024mask` | `UnlitTwoTexture` | `metal` | `map` | `1` | `twincannon/twin_cybergreen_trans_additive` |
| `twincannon/twin_cybergrey3` | `UnlitGeneric` | `metal` | `map` | `7` | `twincannon/twin_cybergrey3` |
| `twincannon/twin_cyberorange` | `UnlitGeneric` | `metal` | `map` | `5` | `twincannon/twin_cyberorange` |
| `twincannon/twin_cyberorange_additive` | `UnlitGeneric` | `metal` | `map` | `2` | `twincannon/twin_cyberorange_additive` |
| `twincannon/twin_cyberpurple` | `UnlitGeneric` | `metal` | `map` | `2` | `twincannon/twin_cyberpurple` |
| `twincannon/twin_cyberred` | `UnlitGeneric` | `metal` | `map` | `8` | `twincannon/twin_cyberred` |
| `twincannon/twin_cyberred_trans` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/twin_cyberred_trans` |
| `twincannon/twin_cyberred_trans_squares` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/twin_cyberred_trans_squares` |
| `twincannon/twin_cyberwhite` | `UnlitGeneric` | `metal` | `map` | `7` | `twincannon/twin_cyberwhite` |
| `twincannon/twin_cyberwhite_trans_squares` | `UnlitGeneric` | `metal` | `map` | `2` | `twincannon/twin_cyberwhite_trans_squares` |
| `twincannon/twin_cyberwhite_trans_squares_nocull` | `UnlitGeneric` | `metal` | `map` | `2` | `twincannon/twin_cyberwhite_trans_squares` |
| `twincannon/twin_cyberyellow` | `UnlitGeneric` | `metal` | `map` | `2` | `twincannon/twin_cyberyellow` |
| `twincannon/twin_cyberyellow_additive` | `UnlitGeneric` | `metal` | `map` | `1` | `twincannon/twin_cyberyellow_additive` |
| `twincannon/twin_dirtfloor001a` | `LightmappedGeneric` | `dirt` | `map` | `2` | `nature/dirtfloor001a` |
| `twincannon/undermine/biggaydoor` | `LightmappedGeneric` | `metal` | `map` | `2` | `twincannon/undermine/biggaydoor` |
| `twincannon/undermine/biggaymelteddoorblend` | `WorldVertexTransition` | `metal` | `map` | `1` | `twincannon/undermine/biggaydoor` |
| `twincannon/undermine/decal_dmt_eu` | `LightmappedGeneric` | `-` | `decal` | `0` | `twincannon/undermine/decal_dmt_eu` |
| `twincannon/undermine/decal_dmt_inner` | `LightmappedGeneric` | `-` | `decal` | `0` | `twincannon/undermine/decal_dmt_inner` |
| `twincannon/undermine/decal_dmt_lab` | `LightmappedGeneric` | `-` | `decal` | `0` | `twincannon/undermine/decal_dmt_lab` |
| `twincannon/undermine/decal_dmt_loading` | `LightmappedGeneric` | `-` | `decal` | `0` | `twincannon/undermine/decal_dmt_loading` |
| `twincannon/undermine/decal_dmt_secpoint` | `LightmappedGeneric` | `-` | `decal` | `0` | `twincannon/undermine/decal_dmt_secpoint` |
| `twincannon/undermine/decal_dmt_terminal` | `LightmappedGeneric` | `-` | `decal` | `0` | `twincannon/undermine/decal_dmt_terminal` |
| `twincannon/undermine/eu_status_bottom` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/eu_status_bottom` |
| `twincannon/undermine/eu_status_normal` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/eu_status_normal` |
| `twincannon/undermine/eu_status_offline` | `UnlitGeneric` | `glass` | `map` | `2` | `twincannon/undermine/eu_status_offline` |
| `twincannon/undermine/eu_status_online` | `UnlitGeneric` | `glass` | `map` | `2` | `twincannon/undermine/eu_status_online` |
| `twincannon/undermine/eu_status_override` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/eu_status_override` |
| `twincannon/undermine/eu_status_top_eu1` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/eu_status_top_eu1` |
| `twincannon/undermine/eu_status_top_eu2` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/eu_status_top_eu2` |
| `twincannon/undermine/eu_status_top_eu3` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/eu_status_top_eu3` |
| `twincannon/undermine/port1busy` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/port1busy` |
| `twincannon/undermine/port1open` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/port1open` |
| `twincannon/undermine/port1status` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/port1status` |
| `twincannon/undermine/port2busy` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/port2busy` |
| `twincannon/undermine/port2open` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/port2open` |
| `twincannon/undermine/port2status` | `UnlitGeneric` | `glass` | `map` | `1` | `twincannon/undermine/port2status` |
| `twincannon/undermine/um_concbarrier` | `LightmappedGeneric` | `concrete` | `map` | `1` | `twincannon/undermine/um_concbarrier` |
| `twincannon/undermine/um_concwall` | `LightmappedGeneric` | `concrete` | `map` | `1` | `twincannon/undermine/um_concwall` |
| `twincannon/undermine/um_concwall2` | `LightmappedGeneric` | `concrete` | `map` | `1` | `twincannon/undermine/um_concwall2` |
| `twincannon/undermine/um_concwall3` | `LightmappedGeneric` | `concrete` | `map` | `1` | `twincannon/undermine/um_concwall3` |
| `twincannon/undermine/um_metaltrim` | `LightmappedGeneric` | `metal` | `map` | `1` | `twincannon/undermine/um_metaltrim` |
| `twincannon/undermine/um_metalwall` | `LightmappedGeneric` | `metal` | `map` | `1` | `twincannon/undermine/um_metalwall` |
| `twincannon/undermine/um_metalwallchipped` | `LightmappedGeneric` | `metal` | `map` | `1` | `twincannon/undermine/um_metalwallchipped` |
| `twincannon/vent_text_arrow` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/vent_text_arrow` |
| `twincannon/vent_text_extraction` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/vent_text_extraction` |
| `twincannon/vent_text_innerbase` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/vent_text_innerbase` |
| `twincannon/vent_text_laser` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/vent_text_laser` |
| `twincannon/vent_text_unit1` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/vent_text_unit1` |
| `twincannon/vent_text_unit2` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/vent_text_unit2` |
| `twincannon/vent_text_unit3` | `LightmappedGeneric` | `metal` | `map` | `0` | `twincannon/vent_text_unit3` |

### `uctex`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `uctex/dyscal_graffitti001` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_graffitti001` |
| `uctex/dyscal_graffitti002` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_graffitti002` |
| `uctex/dyscal_graffitti003` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_graffitti003` |
| `uctex/dyscal_grafitti001` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_grafitti001` |
| `uctex/dyscal_grafitti002` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_grafitti002` |
| `uctex/dyscal_lucile001` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_lucile001` |
| `uctex/dyscal_lucile002` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_lucile002` |
| `uctex/dyscal_lucille001` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_lucille002` |
| `uctex/dyscal_lucille002` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_lucille002` |
| `uctex/dyscal_lucille003` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_lucille003` |
| `uctex/dyscal_lucille004` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_lucille004` |
| `uctex/dyscal_mplate001_es` | `LightmappedGeneric` | `metal` | `map` | `0` | `uctex/dyscal_mplate001_es` |
| `uctex/dyscal_mplate001_lg` | `LightmappedGeneric` | `metal` | `map` | `0` | `uctex/dyscal_mplate001_lg` |
| `uctex/dyscal_mplate001_md` | `LightmappedGeneric` | `metal` | `map` | `0` | `uctex/dyscal_mplate001_md` |
| `uctex/dyscal_mplate001_sm` | `LightmappedGeneric` | `metal` | `map` | `0` | `uctex/dyscal_mplate001_sm` |
| `uctex/dyscal_mplate002_es` | `LightmappedGeneric` | `metal` | `map` | `0` | `uctex/dyscal_mplate002_es` |
| `uctex/dyscal_mplate002_lg` | `LightmappedGeneric` | `metal` | `map` | `0` | `uctex/dyscal_mplate002_lg` |
| `uctex/dyscal_mplate002_lg_termix1` | `LightmappedGeneric` | `metal` | `map` | `1` | `uctex/dyscal_mplate002_lg_termix1` |
| `uctex/dyscal_mplate002_lg_termix2` | `LightmappedGeneric` | `metal` | `map` | `1` | `uctex/dyscal_mplate002_lg_termix2` |
| `uctex/dyscal_mplate002_lg_termix3` | `LightmappedGeneric` | `metal` | `map` | `1` | `uctex/dyscal_mplate002_lg_termix3` |
| `uctex/dyscal_mplate002_md` | `LightmappedGeneric` | `metal` | `map` | `0` | `uctex/dyscal_mplate002_md` |
| `uctex/dyscal_mplate002_sm` | `LightmappedGeneric` | `metal` | `map` | `0` | `uctex/dyscal_mplate002_sm` |
| `uctex/dyscal_mplate003_lg` | `LightmappedGeneric` | `metal` | `map` | `0` | `uctex/dyscal_mplate003_lg` |
| `uctex/dyscal_mplate003_md` | `LightmappedGeneric` | `metal` | `map` | `0` | `uctex/dyscal_mplate003_md` |
| `uctex/dyscal_mplate003_sm` | `LightmappedGeneric` | `metal` | `map` | `0` | `uctex/dyscal_mplate003_sm` |
| `uctex/dyscal_poster002` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster002` |
| `uctex/dyscal_poster003` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster003` |
| `uctex/dyscal_poster004` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster004` |
| `uctex/dyscal_poster005` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster005` |
| `uctex/dyscal_poster006` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster006` |
| `uctex/dyscal_poster007` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster007` |
| `uctex/dyscal_poster008` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster008` |
| `uctex/dyscal_poster009` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster009` |
| `uctex/dyscal_poster010` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster010` |
| `uctex/dyscal_poster011` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster011` |
| `uctex/dyscal_poster012` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster012` |
| `uctex/dyscal_poster013` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster013` |
| `uctex/dyscal_poster014` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster014` |
| `uctex/dyscal_poster015` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster015` |
| `uctex/dyscal_poster016` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster016` |
| `uctex/dyscal_poster017` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster017` |
| `uctex/dyscal_poster018` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_poster018` |
| `uctex/dyscal_roadsign001` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_roadsign001` |
| `uctex/dyscal_roadsign002` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_roadsign002` |
| `uctex/dyscal_roadsign003` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_roadsign003` |
| `uctex/dyscal_roadsign004` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_roadsign004` |
| `uctex/dyscal_roadsign005` | `UnlitGeneric` | `-` | `map` | `1` | `uctex/dyscal_roadsign005` |
| `uctex/dyscal_roadsign006` | `UnlitGeneric` | `-` | `map` | `1` | `uctex/dyscal_roadsign006` |
| `uctex/dyscal_roadsign007` | `UnlitGeneric` | `-` | `map` | `1` | `uctex/dyscal_roadsign007` |
| `uctex/dyscal_roadsign008` | `UnlitGeneric` | `-` | `map` | `1` | `uctex/dyscal_roadsign008` |
| `uctex/dyscal_roadsign009` | `UnlitGeneric` | `-` | `map` | `1` | `uctex/dyscal_roadsign009` |
| `uctex/dyscal_roadsign010` | `UnlitGeneric` | `-` | `map` | `2` | `uctex/dyscal_roadsign010` |
| `uctex/dyscal_roadsign011` | `UnlitGeneric` | `-` | `map` | `2` | `uctex/dyscal_roadsign011` |
| `uctex/dyscal_spraypaint001` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_spraypaint001` |
| `uctex/dyscal_spraypaint002` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_spraypaint002` |
| `uctex/dyscal_spraypaint003` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_spraypaint003` |
| `uctex/dyscal_spraypaint004` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_spraypaint004` |
| `uctex/dyscal_spraypaint005` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_spraypaint005` |
| `uctex/dyscal_spraypaint006` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_spraypaint006` |
| `uctex/dyscal_spraypaint007` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_spraypaint007` |
| `uctex/dyscal_spraypaint008` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_spraypaint008` |
| `uctex/dyscal_spraypaint009` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_spraypaint009` |
| `uctex/dyscal_spraypaint010` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_spraypaint010` |
| `uctex/dyscal_spraypaint011` | `LightmappedGeneric` | `-` | `map` | `0` | `uctex/dyscal_spraypaint011` |
| `uctex/dyscal_wood001_lg` | `LightmappedGeneric` | `wood` | `map` | `0` | `uctex/dyscal_wood001_lg` |
| `uctex/dyscal_wood001_md` | `LightmappedGeneric` | `wood` | `map` | `0` | `uctex/dyscal_wood001_md` |
| `uctex/dyscal_wood001_sm` | `LightmappedGeneric` | `wood` | `map` | `0` | `uctex/dyscal_wood001_sm` |
| `uctex/dyscal_wood002_lg` | `LightmappedGeneric` | `wood` | `map` | `0` | `uctex/dyscal_wood002_lg` |
| `uctex/dyscal_wood002_md` | `LightmappedGeneric` | `wood` | `map` | `0` | `uctex/dyscal_wood002_md` |
| `uctex/dyscal_wood002_sm` | `LightmappedGeneric` | `wood` | `map` | `0` | `uctex/dyscal_wood002_sm` |

### `urban`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `urban/advert_baked01` | `VertexLitGeneric` | `metal` | `map` | `0` | `models/urban/advert_baked01` |
| `urban/brick01footer` | `LightmappedGeneric` | `concrete` | `map` | `3` | `urban/brick01footer` |
| `urban/brick01header` | `LightmappedGeneric` | `concrete` | `map` | `2` | `urban/brick01header` |
| `urban/brick01wall` | `LightmappedGeneric` | `concrete` | `map` | `1` | `urban/brick01wall` |
| `urban/colorbrick01header` | `LightmappedGeneric` | `concrete` | `map` | `2` | `urban/colorbrick01header` |
| `urban/colorbrick01wall` | `LightmappedGeneric` | `concrete` | `map` | `2` | `urban/colorbrick01wall` |
| `urban/conc_clean` | `LightmappedGeneric` | `concrete` | `map` | `3` | `urban/conc_clean` |
| `urban/conc_clean2` | `LightmappedGeneric` | `concrete` | `map` | `0` | `urban/conc_clean_mask` |
| `urban/conc_gutter_rubbish` | `LightmappedGeneric` | `concrete` | `map` | `1` | `urban/conc_gutter_rubbish` |
| `urban/concrete3` | `LightmappedGeneric` | `concrete` | `map` | `0` | `urban/concrete3` |
| `urban/dirty_road02` | `LightmappedGeneric` | `concrete` | `map` | `7` | `urban/dirty_road02` |
| `urban/dys_urban_chipboard_01` | `LightmappedGeneric` | `wood` | `map` | `2` | `urban/dys_urban_chipboard_01` |
| `urban/dys_urban_chipboard_02` | `LightmappedGeneric` | `wood` | `map` | `1` | `urban/dys_urban_chipboard_02` |
| `urban/dys_urban_chipboard_03` | `LightmappedGeneric` | `wood` | `map` | `1` | `urban/dys_urban_chipboard_03` |
| `urban/dys_urban_chipboard_04` | `LightmappedGeneric` | `wood` | `map` | `0` | `urban/dys_urban_chipboard_04` |
| `urban/dys_urban_door_01` | `LightmappedGeneric` | `metal` | `map` | `2` | `urban/dys_urban_door_01` |
| `urban/dys_urban_metaldoor_blue` | `LightmappedGeneric` | `metal` | `map` | `1` | `urban/metaldoor_blue` |
| `urban/dys_urban_metaldoor_green` | `LightmappedGeneric` | `metal` | `map` | `1` | `urban/metaldoor_green` |
| `urban/dys_urban_metaldoor_red` | `LightmappedGeneric` | `metal` | `map` | `1` | `urban/metaldoor_red` |
| `urban/gleamybrick01` | `LightmappedGeneric` | `concrete` | `map` | `1` | `urban/gleamybrick01` |
| `urban/graph_building` | `LightmappedGeneric` | `concrete` | `map` | `2` | `urban/graph_building` |
| `urban/grate2` | `LightmappedGeneric` | `metal` | `map` | `0` | `urban/grate2` |
| `urban/grate_long` | `LightmappedGeneric` | `metal` | `map` | `1` | `urban/grate_long` |
| `urban/grate_long2` | `LightmappedGeneric` | `metal` | `map` | `2` | `urban/grate_long2` |
| `urban/graybrick01` | `LightmappedGeneric` | `concrete` | `map` | `1` | `urban/graybrick01` |
| `urban/graybrick01header` | `LightmappedGeneric` | `concrete` | `map` | `1` | `urban/graybrick01header` |
| `urban/light_blast` | `Unlitgeneric` | `-` | `map` | `0` | `urban/light_blast` |
| `urban/metal_panel_l` | `LightmappedGeneric` | `metal` | `map` | `3` | `urban/metal_panel_l` |
| `urban/old_cement3` | `LightmappedGeneric` | `concrete` | `map` | `1` | `urban/old_cement3` |
| `urban/old_cement4` | `LightmappedGeneric` | `concrete` | `map` | `3` | `urban/old_cement4` |
| `urban/oldgarage` | `LightmappedGeneric` | `metal` | `map` | `1` | `urban/oldgarage` |
| `urban/osaka_sewer_lid` | `LightmappedGeneric` | `metal` | `map` | `0` | `urban/osaka_sewer_lid` |
| `urban/plasterwall01_blue` | `LightmappedGeneric` | `plaster` | `map` | `0` | `urban/plasterwall01_blue` |
| `urban/plasterwall01_brown` | `LightmappedGeneric` | `plaster` | `map` | `1` | `urban/plasterwall01_brown` |
| `urban/plasterwall01_red` | `LightmappedGeneric` | `plaster` | `map` | `1` | `urban/plasterwall01_red` |
| `urban/plasterwall01_teal` | `LightmappedGeneric` | `plaster` | `map` | `0` | `urban/plasterwall01_teal` |
| `urban/projects` | `LightmappedGeneric` | `concrete` | `map` | `0` | `urban/projects` |
| `urban/redbrick01alittlewindow` | `LightmappedGeneric` | `concrete` | `map` | `1` | `urban/redbrick01alittlewindow` |
| `urban/redbrick01header` | `LightmappedGeneric` | `concrete` | `map` | `2` | `urban/redbrick01header` |
| `urban/redbrick01littlewindow` | `LightmappedGeneric` | `concrete` | `map` | `0` | `urban/redbrick01littlewindow` |
| `urban/redbrick01wall` | `LightmappedGeneric` | `concrete` | `map` | `1` | `urban/redbrick01wall` |
| `urban/redbrick01windowbot` | `LightmappedGeneric` | `concrete` | `map` | `2` | `urban/redbrick01windowbot` |
| `urban/redbrick01windowmid` | `LightmappedGeneric` | `concrete` | `map` | `1` | `urban/redbrick01windowmid` |
| `urban/redbrick01windowtop` | `LightmappedGeneric` | `concrete` | `map` | `2` | `urban/redbrick01windowtop` |
| `urban/road_rubbish01` | `LightmappedGeneric` | `concrete` | `map` | `0` | `urban/road_rubbish01` |
| `urban/rotatingFans` | `LightmappedGeneric` | `metal` | `map` | `4` | `urban/rotatingFans` |
| `urban/round_light` | `LightmappedGeneric` | `glass` | `map` | `3` | `urban/round_light` |
| `urban/rubbish1` | `LightmappedGeneric` | `-` | `map` | `0` | `urban/rubbish1` |
| `urban/rubbish2` | `LightmappedGeneric` | `-` | `map` | `0` | `urban/rubbish2` |
| `urban/rubbish3` | `LightmappedGeneric` | `-` | `map` | `0` | `urban/rubbish3` |
| `urban/sidewalk` | `LightmappedGeneric` | `concrete` | `map` | `2` | `urban/sidewalk` |
| `urban/sign_14a` | `LightmappedGeneric` | `glass` | `map` | `0` | `urban/sign_14a` |
| `urban/windows_dark` | `LightmappedGeneric` | `concrete` | `map` | `2` | `urban/windows_dark` |
| `urban/windows_dirty` | `LightmappedGeneric` | `concrete` | `map` | `2` | `urban/windows_dirty` |
| `urban/windows_grey` | `LightmappedGeneric` | `concrete` | `map` | `0` | `urban/windows_grey` |
| `urban/windows_grey2` | `LightmappedGeneric` | `concrete` | `map` | `0` | `urban/windows_grey2` |
| `urban/windows_offices` | `LightmappedGeneric` | `concrete` | `map` | `3` | `urban/windows_offices` |
| `urban/windows_offset` | `LightmappedGeneric` | `concrete` | `map` | `1` | `urban/windows_offset` |
| `urban/windows_scum2` | `LightmappedGeneric` | `concrete` | `map` | `2` | `urban/windows_scum2` |
| `urban/windows_scumy` | `LightmappedGeneric` | `concrete` | `map` | `3` | `urban/windows_scumy` |
| `urban/windows_striped` | `LightmappedGeneric` | `concrete` | `map` | `3` | `urban/windows_striped` |
| `urban/windows_vert` | `LightmappedGeneric` | `concrete` | `map` | `0` | `urban/windows_vert` |
| `urban/windows_yellow` | `LightmappedGeneric` | `concrete` | `map` | `1` | `urban/windows_yellow` |
| `urban/xodus` | `LightmappedGeneric` | `concrete` | `map` | `0` | `urban/xodus` |
| `urban/xodus_sml` | `LightmappedGeneric` | `concrete` | `map` | `0` | `urban/xodus_sml` |

### `urbanrisk`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `urbanrisk/dog_cyber1` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber1` |
| `urbanrisk/dog_cyber10` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber10` |
| `urbanrisk/dog_cyber11` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber11` |
| `urbanrisk/dog_cyber12` | `UnlitGeneric` | `-` | `map` | `1` | `urbanrisk/dog_cyber12` |
| `urbanrisk/dog_cyber13` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber13` |
| `urbanrisk/dog_cyber2` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber2` |
| `urbanrisk/dog_cyber3` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber3` |
| `urbanrisk/dog_cyber4` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber4` |
| `urbanrisk/dog_cyber5` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber5` |
| `urbanrisk/dog_cyber6` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber6` |
| `urbanrisk/dog_cyber7` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber7` |
| `urbanrisk/dog_cyber8` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber8` |
| `urbanrisk/dog_cyber9` | `UnlitGeneric` | `-` | `map` | `0` | `urbanrisk/dog_cyber9` |
| `urbanrisk/urbanrisk_tile1` | `LightmappedGeneric` | `metal` | `map` | `0` | `urbanrisk/urbanrisk_tile1` |
| `urbanrisk/urbanrisk_tile1_cheap` | `LightmappedGeneric` | `tile` | `map` | `0` | `urbanrisk/urbanrisk_tile1` |
| `urbanrisk/urbanrisk_tile2` | `LightmappedGeneric` | `tile` | `map` | `0` | `urbanrisk/urbanrisk_tile2` |
| `urbanrisk/urbanrisk_tile2_cheap` | `LightmappedGeneric` | `tile` | `map` | `0` | `urbanrisk/urbanrisk_tile2` |
| `urbanrisk/urbanrisk_tile3` | `LightmappedGeneric` | `tile` | `map` | `0` | `urbanrisk/urbanrisk_tile3` |
| `urbanrisk/urbanrisk_tile4` | `LightmappedGeneric` | `tile` | `map` | `0` | `urbanrisk/urbanrisk_tile4` |

### `vaccine`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `vaccine/coolscreen` | `UnlitGeneric` | `glass` | `map` | `1` | `vaccine/coolscreen` |
| `vaccine/coolscreen2` | `UnlitGeneric` | `glass` | `map` | `1` | `vaccine/coolscreen2` |
| `vaccine/coresfx1` | `Lightmappedgeneric` | `glass` | `map` | `0` | `vaccine/coresfx1` |
| `vaccine/coresfx2` | `LightmappedGeneric` | `glass` | `map` | `1` | `vaccine/coresfx2` |
| `vaccine/coresfx2_normal` | `LightmappedGeneric` | `-` | `map` | `0` | `vaccine/coresfx2_normal` |
| `vaccine/dtrustbillboard1` | `UnlitGeneric` | `-` | `map` | `3` | `vaccine/dtrustbillboard1` |
| `vaccine/dtrustbillboard2` | `UnlitGeneric` | `glass` | `map` | `0` | `vaccine/dtrustbillboard2` |
| `vaccine/dtrustbillboard3` | `UnlitGeneric` | `glass` | `map` | `0` | `vaccine/dtrustbillboard3` |
| `vaccine/dtwall1` | `LightmappedGeneric` | `plaster` | `map` | `1` | `vaccine/dtwall1` |
| `vaccine/dtwall2` | `LightmappedGeneric` | `plaster` | `map` | `1` | `vaccine/dtwall2` |
| `vaccine/dtwall3` | `LightmappedGeneric` | `plaster` | `map` | `0` | `vaccine/dtwall3` |
| `vaccine/dtwall4` | `LightmappedGeneric` | `plaster` | `map` | `1` | `vaccine/dtwall4` |
| `vaccine/dys_conc1` | `LightmappedGeneric` | `concrete` | `map` | `3` | `vaccine/dys_conc1` |
| `vaccine/dys_conc_a` | `LightmappedGeneric` | `concrete` | `map` | `2` | `vaccine/dys_conc_a` |
| `vaccine/dys_conc_b` | `LightmappedGeneric` | `concrete` | `map` | `0` | `vaccine/dys_conc_b` |
| `vaccine/dys_conc_c` | `LightmappedGeneric` | `concrete` | `map` | `0` | `vaccine/dys_conc_c` |
| `vaccine/dys_coolplate1` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_coolplate1` |
| `vaccine/dys_coolvent1` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_coolvent1` |
| `vaccine/dys_crate` | `LightmappedGeneric` | `plaster` | `map` | `1` | `vaccine/dys_crate4` |
| `vaccine/dys_crate1` | `LightmappedGeneric` | `plaster` | `map` | `2` | `vaccine/dys_crate1` |
| `vaccine/dys_crate1_2` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccine/dys_crate1_2` |
| `vaccine/dys_crate1_3` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/dys_crate1_3` |
| `vaccine/dys_crate1_4` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/dys_crate1_4` |
| `vaccine/dys_crate1_5` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/dys_crate1_5` |
| `vaccine/dys_crate1_6` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/dys_crate1_6` |
| `vaccine/dys_crate1_7` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/dys_crate1_7` |
| `vaccine/dys_crate1_8` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/dys_crate1_8` |
| `vaccine/dys_crate2` | `LightmappedGeneric` | `plaster` | `map` | `2` | `vaccine/dys_crate2` |
| `vaccine/dys_crate3` | `LightmappedGeneric` | `plaster` | `map` | `1` | `vaccine/dys_crate3` |
| `vaccine/dys_crate4` | `LightmappedGeneric` | `plaster` | `map` | `0` | `vaccine/dys_crate4` |
| `vaccine/dys_curvedesk1` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dys_curvedesk1` |
| `vaccine/dys_curvedesk2` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dys_curvedesk2` |
| `vaccine/dys_deskdraw` | `LightmappedGeneric` | `plaster` | `map` | `2` | `vaccine/dys_deskdraw` |
| `vaccine/dys_deskside` | `LightmappedGeneric` | `plaster` | `map` | `3` | `vaccine/dys_deskside` |
| `vaccine/dys_desktop` | `LightmappedGeneric` | `plaster` | `map` | `2` | `vaccine/dys_desktop` |
| `vaccine/dys_diplate_a` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_diplate_a` |
| `vaccine/dys_diplate_c` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_diplate_c` |
| `vaccine/dys_diplate_cd` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_diplate_cd` |
| `vaccine/dys_dirt1` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_dirt1` |
| `vaccine/dys_glass1` | `LightmappedGeneric` | `glass` | `map` | `9` | `vaccine/dys_glass1` |
| `vaccine/dys_glass2` | `LightmappedGeneric` | `glass` | `map` | `7` | `vaccine/dys_glass2` |
| `vaccine/dys_grass1` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_grass1` |
| `vaccine/dys_grey1` | `LightmappedGeneric` | `metal` | `map` | `5` | `vaccine/dys_grey1` |
| `vaccine/dys_grey2` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/dys_grey2` |
| `vaccine/dys_grey3` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/dys_grey3` |
| `vaccine/dys_lightflur1` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/dys_lightflur2` |
| `vaccine/dys_lightflur2` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_lightflur2` |
| `vaccine/dys_lightflur3` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_lightflur3` |
| `vaccine/dys_lightflur4` | `UnlitGeneric` | `metal` | `map` | `7` | `vaccine/dys_lightflur4` |
| `vaccine/dys_lightflur4_off` | `UnlitGeneric` | `metal` | `map` | `1` | `vaccine/dys_lightflur4_off` |
| `vaccine/dys_lightflur5` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_lightflur5` |
| `vaccine/dys_metal1` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_metal1` |
| `vaccine/dys_metal10` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_metal10` |
| `vaccine/dys_metal11` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/dys_metal11` |
| `vaccine/dys_metal12` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_metal12` |
| `vaccine/dys_metal2` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_metal2` |
| `vaccine/dys_metal3` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_metal3` |
| `vaccine/dys_metal4` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccine/dys_metal4` |
| `vaccine/dys_metal5` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_metal5` |
| `vaccine/dys_metal6` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_metal6` |
| `vaccine/dys_metal7` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_metal7` |
| `vaccine/dys_metal8` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_metal8` |
| `vaccine/dys_metal9` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_metal9` |
| `vaccine/dys_metala1` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_metala1` |
| `vaccine/dys_metala2` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_metala2` |
| `vaccine/dys_metala3` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_metala3` |
| `vaccine/dys_metalroof` | `LightmappedGeneric` | `metal` | `map` | `5` | `vaccine/dys_metalroof` |
| `vaccine/dys_partic1` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dys_partic1` |
| `vaccine/dys_rock1` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_rock1` |
| `vaccine/dys_spawnbox` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dys_spawnbox` |
| `vaccine/dys_spawnboxa` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dys_spawnboxa` |
| `vaccine/dys_spawnboxside` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dys_spawnboxside` |
| `vaccine/dys_spawnboxside2` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dys_spawnboxside2` |
| `vaccine/dys_spawnboxside3` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dys_spawnboxside3` |
| `vaccine/dys_vac_iris` | `LightmappedGeneric` | `metal` | `map` | `6` | `vaccine/dys_vac_iris` |
| `vaccine/dys_vac_plasdoor1` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dys_vac_plasdoor1` |
| `vaccine/dys_vac_plaswall` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_vac_plaswall` |
| `vaccine/dys_vac_plaswall1a` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine/dys_vac_plaswall1a` |
| `vaccine/dys_vac_plaswall1b` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine/dys_vac_plaswall1b` |
| `vaccine/dys_vac_plaswall1c` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine/dys_vac_plaswall1c` |
| `vaccine/dys_vac_plaswall1d` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine/dys_vac_plaswall1d` |
| `vaccine/dys_vac_plaswall1e` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine/dys_vac_plaswall1e` |
| `vaccine/dys_vac_plaswall1f` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine/dys_vac_plaswall1f` |
| `vaccine/dys_vac_wallnew1` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dys_vac_wallnew1` |
| `vaccine/dys_vac_wallnew2` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dys_vac_wallnew2` |
| `vaccine/dys_vaccore1` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/dys_vaccore1` |
| `vaccine/dys_vaccore2` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/dys_vaccore2` |
| `vaccine/dys_vactrim1` | `Lightmappedgeneric` | `metal` | `map` | `4` | `vaccine/dys_vactrim1` |
| `vaccine/dys_vent1` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/dys_vent1` |
| `vaccine/dysdoor` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dysdoor` |
| `vaccine/dysdoor1` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dysdoor1` |
| `vaccine/dysdoor2` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dysdoor2` |
| `vaccine/dysdoor3` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dysdoor3` |
| `vaccine/dysdoor4` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dysdoor4` |
| `vaccine/dysdoor5` | `Lightmappedgeneric` | `-` | `map` | `1` | `vaccine/dysdoor5` |
| `vaccine/dysdoor6` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dysdoor6` |
| `vaccine/dysdoor7` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccine/dysdoor7` |
| `vaccine/greynoshade` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/greynoshade` |
| `vaccine/roofplate` | `LightmappedGeneric` | `glass` | `map` | `0` | `vaccine/roofplate` |
| `vaccine/screenbg1` | `UnlitGeneric` | `-` | `map` | `0` | `vaccine/screenbg1` |
| `vaccine/vac_floor1` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/vac_floor1` |
| `vaccine/vac_floor2` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/vac_floor2` |
| `vaccine/vac_floor3` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/vac_floor3` |
| `vaccine/vac_floor4` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/vac_floor4` |
| `vaccine/vac_floor5` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/vac_floor5` |
| `vaccine/vac_floor6` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/vac_floor6` |
| `vaccine/vac_floor7` | `LightmappedGeneric` | `metal` | `map` | `6` | `vaccine/vac_floor7` |
| `vaccine/vac_outside1` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/vac_outside1` |
| `vaccine/vac_outside2` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/vac_outside2` |
| `vaccine/vac_outside3` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/vac_outside3` |
| `vaccine/vac_outside4` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccine/vac_outside4` |
| `vaccine/vac_outside5` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccine/vac_outside5` |
| `vaccine/vac_rubber` | `LightmappedGeneric` | `rubber` | `map` | `0` | `vaccine/vac_rubber` |
| `vaccine/vac_trans1` | `LightmappedGeneric` | `glass` | `map` | `0` | `vaccine/vac_trans1` |
| `vaccine/vac_trim` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/vac_trim` |
| `vaccine/vac_trim1` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/vac_trim` |
| `vaccine/vac_trim2` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccine/vac_trim` |
| `vaccine/vacscreen1` | `UnlitGeneric` | `-` | `map` | `0` | `vaccine/vacscreen1` |
| `vaccine/vacscreen1_broken` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine/vacscreen1_broken` |
| `vaccine/vacscreen2` | `UnlitGeneric` | `-` | `map` | `0` | `vaccine/vacscreen2` |
| `vaccine/vacscreen_brokeoverlay` | `LightmappedGeneric` | `-` | `overlay` | `1` | `vaccine/vacscreen_brokeoverlay` |
| `vaccine/vacshield_002` | `Unlittwotexture` | `glass` | `map` | `1` | `Effects/com_shield002a` |

### `vaccine2`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `vaccine2/detail1base` | `lightmappedGeneric` | `-` | `map` | `3` | `vaccine2/detail1base` |
| `vaccine2/detail2base` | `lightmappedGeneric` | `-` | `map` | `3` | `vaccine2/detail2base` |
| `vaccine2/detail3base` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/detail3base` |
| `vaccine2/detail4base` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/detail4base` |
| `vaccine2/detail5base` | `lightmappedGeneric` | `-` | `map` | `1` | `vaccine2/detail5base` |
| `vaccine2/detail6base` | `lightmappedGeneric` | `-` | `map` | `1` | `vaccine2/detail6base` |
| `vaccine2/vac_arrow_down` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine2/vac_arrow_down` |
| `vaccine2/vac_arrow_h` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine2/vac_arrow_h` |
| `vaccine2/vac_arrow_up` | `UnlitGeneric` | `-` | `map` | `0` | `vaccine2/vac_arrow_up` |
| `vaccine2/vac_sign1` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine2/vac_sign1` |
| `vaccine2/vac_sign10` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine2/vac_sign10` |
| `vaccine2/vac_sign11` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine2/vac_sign11` |
| `vaccine2/vac_sign2` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine2/vac_sign2` |
| `vaccine2/vac_sign3` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine2/vac_sign3` |
| `vaccine2/vac_sign4` | `UnlitGeneric` | `-` | `map` | `0` | `vaccine2/vac_sign4` |
| `vaccine2/vac_sign5` | `UnlitGeneric` | `-` | `map` | `0` | `vaccine2/vac_sign5` |
| `vaccine2/vac_sign6` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine2/vac_sign6` |
| `vaccine2/vac_sign7` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine2/vac_sign7` |
| `vaccine2/vac_sign8` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine2/vac_sign8` |
| `vaccine2/vac_sign9` | `UnlitGeneric` | `-` | `map` | `1` | `vaccine2/vac_sign9` |
| `vaccine2/vac_wallsign1` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/vac_wallsign1` |
| `vaccine2/vac_wallsign10` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/vac_wallsign10` |
| `vaccine2/vac_wallsign11` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/vac_wallsign11` |
| `vaccine2/vac_wallsign2` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/vac_wallsign2` |
| `vaccine2/vac_wallsign3` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/vac_wallsign3` |
| `vaccine2/vac_wallsign4` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/vac_wallsign4` |
| `vaccine2/vac_wallsign5` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/vac_wallsign5` |
| `vaccine2/vac_wallsign6` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/vac_wallsign6` |
| `vaccine2/vac_wallsign7` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/vac_wallsign7` |
| `vaccine2/vac_wallsign8` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/vac_wallsign8` |
| `vaccine2/vac_wallsign9` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccine2/vac_wallsign9` |

### `vaccinecore`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `vaccinecore/dys_spawnglow` | `UnlitGeneric` | `-` | `map` | `12` | `vaccinecore/dys_spawnglow` |
| `vaccinecore/metal_panelsmall_001` | `Lightmappedgeneric` | `-` | `map` | `3` | `vaccinecore/metal_panelsmall_001` |
| `vaccinecore/metal_panelsmall_002` | `Lightmappedgeneric` | `-` | `map` | `3` | `vaccinecore/metal_panelsmall_002` |
| `vaccinecore/metal_panelsmall_003` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelsmall_003` |
| `vaccinecore/metal_panelsmall_003a` | `Lightmappedgeneric` | `-` | `map` | `2` | `vaccinecore/metal_panelsmall_003a` |
| `vaccinecore/metal_panelsmall_003b` | `Lightmappedgeneric` | `-` | `map` | `1` | `vaccinecore/metal_panelsmall_003b` |
| `vaccinecore/metal_panelsmall_003c` | `Lightmappedgeneric` | `-` | `map` | `1` | `vaccinecore/metal_panelsmall_003c` |
| `vaccinecore/metal_panelsmall_003d` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelsmall_003d` |
| `vaccinecore/metal_panelsmall_003e` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelsmall_003e` |
| `vaccinecore/metal_panelsmall_003f` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelsmall_003f` |
| `vaccinecore/metal_panelsmall_003g` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelsmall_003g` |
| `vaccinecore/metal_panelsmall_003h` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelsmall_003h` |
| `vaccinecore/metal_panelsmall_003i` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelsmall_003i` |
| `vaccinecore/metal_panelsmall_003j` | `Lightmappedgeneric` | `-` | `map` | `1` | `vaccinecore/metal_panelsmall_003j` |
| `vaccinecore/metal_panelsmall_003k` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelsmall_003k` |
| `vaccinecore/metal_panelsmall_003l` | `Lightmappedgeneric` | `-` | `map` | `1` | `vaccinecore/metal_panelsmall_003l` |
| `vaccinecore/metal_panelsmall_003m` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelsmall_003m` |
| `vaccinecore/metal_panelsmall_004` | `Lightmappedgeneric` | `-` | `map` | `2` | `vaccinecore/metal_panelsmall_004` |
| `vaccinecore/metal_panelwall_001` | `Lightmappedgeneric` | `-` | `map` | `1` | `vaccinecore/metal_panelwall_001` |
| `vaccinecore/metal_panelwall_002` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelwall_002` |
| `vaccinecore/metal_panelwall_003` | `Lightmappedgeneric` | `-` | `map` | `1` | `vaccinecore/metal_panelwall_003` |
| `vaccinecore/metal_panelwall_101` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelwall_101` |
| `vaccinecore/metal_panelwall_102` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelwall_102` |
| `vaccinecore/metal_panelwall_103` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelwall_103` |
| `vaccinecore/metal_panelwall_103a` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelwall_103a` |
| `vaccinecore/metal_panelwall_103b` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelwall_103b` |
| `vaccinecore/metal_panelwall_103c` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelwall_103c` |
| `vaccinecore/metal_panelwall_103glow` | `UnlitGeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelwall_103glow` |
| `vaccinecore/metal_panelwall_103light` | `lightmappedGeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelwall_103light` |
| `vaccinecore/metal_panelwall_104` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_panelwall_104` |
| `vaccinecore/metal_skirting001` | `Lightmappedgeneric` | `-` | `map` | `1` | `vaccinecore/metal_skirting001` |
| `vaccinecore/metal_skirting001_cheap` | `Lightmappedgeneric` | `metal` | `map` | `1` | `vaccinecore/metal_skirting001_cheap` |
| `vaccinecore/metal_skirting001_normal` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_skirting001_normal` |
| `vaccinecore/metal_skirting002` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/metal_skirting002` |
| `vaccinecore/metal_skirting003` | `Lightmappedgeneric` | `-` | `map` | `3` | `vaccinecore/metal_skirting003` |
| `vaccinecore/tile_floor001` | `Lightmappedgeneric` | `tile` | `map` | `3` | `vaccinecore/tile_floor001` |
| `vaccinecore/tile_floor001_normal` | `Lightmappedgeneric` | `-` | `map` | `0` | `vaccinecore/tile_floor001_normal` |

### `vaccinert`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `vaccinert/dys_camnode` | `UnlitGeneric` | `metal` | `map` | `0` | `vaccinert/dys_camnode` |
| `vaccinert/dys_cleanwall` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_cleanwall` |
| `vaccinert/dys_cleanwall2` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_cleanwall2` |
| `vaccinert/dys_corenode` | `UnlitGeneric` | `metal` | `map` | `2` | `vaccinert/dys_corenode` |
| `vaccinert/dys_coreroomvent1` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_coreroomvent1` |
| `vaccinert/dys_coreroomvent2` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_coreroomvent2` |
| `vaccinert/dys_floor1` | `LightmappedGeneric` | `metal` | `map` | `6` | `vaccinert/dys_floor1` |
| `vaccinert/dys_foyernode` | `UnlitGeneric` | `metal` | `map` | `2` | `vaccinert/dys_foyernode` |
| `vaccinert/dys_laddernode` | `UnlitGeneric` | `metal` | `map` | `1` | `vaccinert/dys_laddernode` |
| `vaccinert/dys_loadingnode` | `UnlitGeneric` | `metal` | `map` | `1` | `vaccinert/dys_loadingnode` |
| `vaccinert/dys_mainnode` | `UnlitGeneric` | `metal` | `map` | `1` | `vaccinert/dys_mainnode` |
| `vaccinert/dys_mf1` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_mf1` |
| `vaccinert/dys_mf2` | `LightmappedGeneric` | `metal` | `map` | `4` | `vaccinert/dys_mf2` |
| `vaccinert/dys_officewalldes1` | `LightmappedGeneric` | `default` | `map` | `0` | `vaccinert/dys_officewalldes1` |
| `vaccinert/dys_officewalldes2` | `LightmappedGeneric` | `default` | `map` | `0` | `vaccinert/dys_officewalldes2` |
| `vaccinert/dys_regennode` | `UnlitGeneric` | `metal` | `map` | `1` | `vaccinert/dys_regennode` |
| `vaccinert/dys_tealwall` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_tealwall` |
| `vaccinert/dys_trim2` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_trim2` |
| `vaccinert/dys_trim3` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_trim3` |
| `vaccinert/dys_turretnode` | `UnlitGeneric` | `metal` | `map` | `3` | `vaccinert/dys_turretnode` |
| `vaccinert/dys_vacaldoor` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacaldoor` |
| `vaccinert/dys_vacclean1` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacclean1` |
| `vaccinert/dys_vacclean2` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacclean2` |
| `vaccinert/dys_vacclean3` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacclean3` |
| `vaccinert/dys_vaccleanlight` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vaccleanlight` |
| `vaccinert/dys_vaccorpcarpet1` | `LightmappedGeneric` | `default` | `map` | `3` | `vaccinert/dys_vaccorpcarpet1` |
| `vaccinert/dys_vaccorpcarpet2` | `LightmappedGeneric` | `default` | `map` | `2` | `vaccinert/dys_vaccorpcarpet2` |
| `vaccinert/dys_vaccorpcarpet3` | `LightmappedGeneric` | `default` | `map` | `5` | `vaccinert/dys_vaccorpcarpet3` |
| `vaccinert/dys_vaccorpcarpet4` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_vaccorpcarpet4` |
| `vaccinert/dys_vaccorpfloor1` | `LightmappedGeneric` | `metal` | `map` | `7` | `vaccinert/dys_vaccorpfloor1` |
| `vaccinert/dys_vaccorpfloor1_bump` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vaccorpfloor1` |
| `vaccinert/dys_vaccorpfloor2` | `LightmappedGeneric` | `metal` | `map` | `5` | `vaccinert/dys_vaccorpfloor2` |
| `vaccinert/dys_vaccorpfloor2_bump` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vaccorpfloor2` |
| `vaccinert/dys_vaccorpfloor3` | `LightmappedGeneric` | `metal` | `map` | `4` | `vaccinert/dys_vaccorpfloor3` |
| `vaccinert/dys_vaccorpfloor3_bump` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vaccorpfloor3` |
| `vaccinert/dys_vaccorpfloor4` | `LightmappedGeneric` | `metal` | `map` | `4` | `vaccinert/dys_vaccorpfloor4` |
| `vaccinert/dys_vaccorpfloor4_bump` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_vaccorpfloor4` |
| `vaccinert/dys_vaccorpfloor5` | `LightmappedGeneric` | `metal` | `map` | `4` | `vaccinert/dys_vaccorpfloor5` |
| `vaccinert/dys_vaccorpwall1` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_vaccorpwall1` |
| `vaccinert/dys_vaccorpwall2` | `LightmappedGeneric` | `default` | `map` | `5` | `vaccinert/dys_vaccorpwall2` |
| `vaccinert/dys_vaccorpwall2_orange` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vaccorpwall2_orange` |
| `vaccinert/dys_vaccorpwall3` | `LightmappedGeneric` | `default` | `map` | `2` | `vaccinert/dys_vaccorpwall3` |
| `vaccinert/dys_vaccorpwall4` | `LightmappedGeneric` | `default` | `map` | `3` | `vaccinert/dys_vaccorpwall4` |
| `vaccinert/dys_vaccorpwall4_orange` | `LightmappedGeneric` | `default` | `map` | `2` | `vaccinert/dys_vaccorpwall4_orange` |
| `vaccinert/dys_vacdetail1` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdetail1` |
| `vaccinert/dys_vacdetail10` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacdetail10` |
| `vaccinert/dys_vacdetail11` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdetail11` |
| `vaccinert/dys_vacdetail12` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdetail12` |
| `vaccinert/dys_vacdetail12_orange` | `LightmappedGeneric` | `default` | `map` | `0` | `vaccinert/dys_vacdetail12_orange` |
| `vaccinert/dys_vacdetail13` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacdetail13` |
| `vaccinert/dys_vacdetail14` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vacdetail14` |
| `vaccinert/dys_vacdetail15` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacdetail15` |
| `vaccinert/dys_vacdetail16` | `LightmappedGeneric` | `metal` | `map` | `4` | `vaccinert/dys_vacdetail16` |
| `vaccinert/dys_vacdetail2` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdetail2` |
| `vaccinert/dys_vacdetail3` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacdetail3` |
| `vaccinert/dys_vacdetail4` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacdetail4` |
| `vaccinert/dys_vacdetail5` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vacdetail5` |
| `vaccinert/dys_vacdetail6` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdetail6` |
| `vaccinert/dys_vacdetail7` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdetail7` |
| `vaccinert/dys_vacdetail8` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdetail8` |
| `vaccinert/dys_vacdetail9` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdetail9` |
| `vaccinert/dys_vacdoor1` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vacdoor1` |
| `vaccinert/dys_vacdoor1_fixed` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacdoor1_fixed` |
| `vaccinert/dys_vacdoor2` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacdoor2` |
| `vaccinert/dys_vacdoor2_fixed` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacdoor2_fixed` |
| `vaccinert/dys_vacdoor3` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vacdoor3` |
| `vaccinert/dys_vacdoor3_fixed` | `LightmappedGeneric` | `metal` | `map` | `4` | `vaccinert/dys_vacdoor3_fixed` |
| `vaccinert/dys_vacdoor3_fixed_burnt` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdoor3_fixed_burnt` |
| `vaccinert/dys_vacdoor4` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vacdoor4` |
| `vaccinert/dys_vacdoor4_fixed` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacdoor4_fixed` |
| `vaccinert/dys_vacdoor5` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacdoor5` |
| `vaccinert/dys_vacdoor5_fixed` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdoor5_fixed` |
| `vaccinert/dys_vacdoor6` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacdoor6` |
| `vaccinert/dys_vacdoor6_fixed` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacdoor6_fixed` |
| `vaccinert/dys_vacdoor7` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdoor7` |
| `vaccinert/dys_vacdoor7_fixed` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacdoor7_fixed` |
| `vaccinert/dys_vacextwall1` | `LightmappedGeneric` | `metal` | `map` | `4` | `vaccinert/dys_vacextwall1` |
| `vaccinert/dys_vacextwall1_orange` | `LightmappedGeneric` | `metal` | `map` | `4` | `vaccinert/dys_vacextwall1_orange` |
| `vaccinert/dys_vacextwall2` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacextwall3` |
| `vaccinert/dys_vacextwall3` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacextwall3` |
| `vaccinert/dys_vacextwall3_orange` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vacextwall3_orange` |
| `vaccinert/dys_vacextwall4` | `LightmappedGeneric` | `metal` | `map` | `4` | `vaccinert/dys_vacextwall4` |
| `vaccinert/dys_vacextwall4_orange` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacextwall4_orange` |
| `vaccinert/dys_vacoffice2` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacoffice2` |
| `vaccinert/dys_vacoffice3` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacoffice2` |
| `vaccinert/dys_vacoffice4` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacoffice2` |
| `vaccinert/dys_vacofficewall1` | `LightmappedGeneric` | `default` | `map` | `4` | `vaccinert/dys_vacofficewall1` |
| `vaccinert/dys_vactilefloor` | `LightmappedGeneric` | `tile` | `map` | `7` | `vaccinert/dys_vactilefloor` |
| `vaccinert/dys_vactilestep` | `LightmappedGeneric` | `tile` | `map` | `4` | `vaccinert/dys_vactilestep` |
| `vaccinert/dys_vactrim1` | `LightmappedGeneric` | `default` | `map` | `4` | `vaccinert/dys_vactrim1` |
| `vaccinert/dys_vactrim1light` | `LightmappedGeneric` | `metal` | `map` | `4` | `vaccinert/dys_vactrim1light` |
| `vaccinert/dys_vactrim1light_orange` | `LightmappedGeneric` | `metal` | `map` | `5` | `vaccinert/dys_vactrim1light_orange` |
| `vaccinert/dys_vactrim2` | `LightmappedGeneric` | `default` | `map` | `4` | `vaccinert/dys_vactrim2` |
| `vaccinert/dys_vactrim2light` | `LightmappedGeneric` | `metal` | `map` | `6` | `vaccinert/dys_vactrim2light` |
| `vaccinert/dys_vactrim2light_orange` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vactrim2light_orange` |
| `vaccinert/dys_vactrim3` | `LightmappedGeneric` | `default` | `map` | `2` | `vaccinert/dys_vactrim3` |
| `vaccinert/dys_vactrim3light` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vactrim3light` |
| `vaccinert/dys_vactrim4` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vactrim4` |
| `vaccinert/dys_vactrim5` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vactrim5` |
| `vaccinert/dys_vactrim5light` | `LightmappedGeneric` | `metal` | `map` | `5` | `vaccinert/dys_vactrim5light` |
| `vaccinert/dys_vactrim6` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vactrim6` |
| `vaccinert/dys_vacwall1` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vacwall1` |
| `vaccinert/dys_vacwall2` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacwall2` |
| `vaccinert/dys_vacwall3` | `LightmappedGeneric` | `metal` | `map` | `3` | `vaccinert/dys_vacwall3` |
| `vaccinert/dys_vacwall4` | `LightmappedGeneric` | `metal` | `map` | `4` | `vaccinert/dys_vacwall4` |
| `vaccinert/dys_vacwall5` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacwall5` |
| `vaccinert/dys_vacwall5_bump` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacwall5` |
| `vaccinert/dys_vacwall6` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vacwall6` |
| `vaccinert/vmtz/dys_cleanwall` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_cleanwall` |
| `vaccinert/vmtz/dys_cleanwall2` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_cleanwall2` |
| `vaccinert/vmtz/dys_cleanwall_NOBUMP` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_cleanwall` |
| `vaccinert/vmtz/dys_trim2` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_trim2` |
| `vaccinert/vmtz/dys_trim3` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_trim3` |
| `vaccinert/vmtz/dys_vacclean1` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacclean1` |
| `vaccinert/vmtz/dys_vacclean2` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacclean2` |
| `vaccinert/vmtz/dys_vacclean3` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacclean3` |
| `vaccinert/vmtz/dys_vaccorpcarpet1` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_vaccorpcarpet1` |
| `vaccinert/vmtz/dys_vaccorpcarpet2` | `LightmappedGeneric` | `default` | `map` | `0` | `vaccinert/dys_vaccorpcarpet2` |
| `vaccinert/vmtz/dys_vaccorpcarpet4` | `LightmappedGeneric` | `default` | `map` | `0` | `vaccinert/dys_vaccorpcarpet4` |
| `vaccinert/vmtz/dys_vaccorpfloor1` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vaccorpfloor1` |
| `vaccinert/vmtz/dys_vaccorpfloor2` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vaccorpfloor2` |
| `vaccinert/vmtz/dys_vaccorpfloor3` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vaccorpfloor3` |
| `vaccinert/vmtz/dys_vaccorpfloor4` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vaccorpfloor4` |
| `vaccinert/vmtz/dys_vaccorpfloor5` | `LightmappedGeneric` | `metal` | `map` | `2` | `vaccinert/dys_vaccorpfloor5` |
| `vaccinert/vmtz/dys_vaccorpwall1` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_vaccorpwall1` |
| `vaccinert/vmtz/dys_vaccorpwall2` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_vaccorpwall2` |
| `vaccinert/vmtz/dys_vaccorpwall2_orange` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_vaccorpwall2_orange` |
| `vaccinert/vmtz/dys_vaccorpwall3` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_vaccorpwall3` |
| `vaccinert/vmtz/dys_vaccorpwall4` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_vaccorpwall4` |
| `vaccinert/vmtz/dys_vacextwall1` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacextwall1` |
| `vaccinert/vmtz/dys_vacextwall1_orange` | `LightmappedGeneric` | `default` | `map` | `0` | `vaccinert/dys_vacextwall1_orange` |
| `vaccinert/vmtz/dys_vacextwall2` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacextwall3` |
| `vaccinert/vmtz/dys_vacextwall3` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacextwall3` |
| `vaccinert/vmtz/dys_vacextwall3_orange` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_vacextwall3_orange` |
| `vaccinert/vmtz/dys_vacextwall4` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vacextwall4` |
| `vaccinert/vmtz/dys_vacextwall4_orange` | `LightmappedGeneric` | `default` | `map` | `0` | `vaccinert/dys_vacextwall4_orange` |
| `vaccinert/vmtz/dys_vacofficewall1` | `LightmappedGeneric` | `default` | `map` | `0` | `vaccinert/dys_vacofficewall1` |
| `vaccinert/vmtz/dys_vactilefloor` | `LightmappedGeneric` | `tile` | `map` | `0` | `vaccinert/dys_vactilefloor` |
| `vaccinert/vmtz/dys_vactilestep` | `LightmappedGeneric` | `tile` | `map` | `0` | `vaccinert/dys_vactilestep` |
| `vaccinert/vmtz/dys_vactrim1` | `LightmappedGeneric` | `default` | `map` | `2` | `vaccinert/dys_vactrim1` |
| `vaccinert/vmtz/dys_vactrim2` | `LightmappedGeneric` | `default` | `map` | `1` | `vaccinert/dys_vactrim2` |
| `vaccinert/vmtz/dys_vactrim2light` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vactrim2light` |
| `vaccinert/vmtz/dys_vactrim2light_orange` | `LightmappedGeneric` | `default` | `map` | `0` | `vaccinert/dys_vactrim2light_orange` |
| `vaccinert/vmtz/dys_vactrim3` | `LightmappedGeneric` | `default` | `map` | `0` | `vaccinert/dys_vactrim3` |
| `vaccinert/vmtz/dys_vactrim3light` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vactrim3light` |
| `vaccinert/vmtz/dys_vactrim4` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vactrim4` |
| `vaccinert/vmtz/dys_vactrim5` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vactrim5` |
| `vaccinert/vmtz/dys_vactrim5light` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vactrim5light` |
| `vaccinert/vmtz/dys_vactrim6` | `LightmappedGeneric` | `metal` | `map` | `1` | `vaccinert/dys_vactrim6` |
| `vaccinert/vmtz/dys_vacwall1` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacwall1` |
| `vaccinert/vmtz/dys_vacwall2` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacwall2` |
| `vaccinert/vmtz/dys_vacwall3` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacwall3` |
| `vaccinert/vmtz/dys_vacwall4` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacwall4` |
| `vaccinert/vmtz/dys_vacwall5` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacwall5` |
| `vaccinert/vmtz/dys_vacwall6` | `LightmappedGeneric` | `metal` | `map` | `0` | `vaccinert/dys_vacwall6` |

### `vgui`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_ASSAULT_RIFLE_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_ASSAULT_RIFLE_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_BASILISK_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_BASILISK_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_BOLTGUN_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_BOLTGUN_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_CORTEX_BOMB_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_CORTEX_BOMB_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_CYBER_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_CYBER_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_CYBER_AMOUNT_locked` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_CYBER_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_FATMAN_FIST_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_FATMAN_FIST_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_FRAG_GRENADE_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_FRAG_GRENADE_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_GL_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_GL_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_ION_CANNON_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_ION_CANNON_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_LASER_RIFLE_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_LASER_RIFLE_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_LIGHT_KATANA_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_LIGHT_KATANA_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_MACHINE_PISTOL_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_MACHINE_PISTOL_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_MACHINE_PISTOL_AMOUNT_locked` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_MACHINE_PISTOL_AMOUNT_locked` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_MEDIUM_KATANA_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_MEDIUM_KATANA_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_MINIGUN_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_MINIGUN_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_MK808_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_MK808_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_ROCKET_LAUNCHER_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_ROCKET_LAUNCHER_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_SHOTGUN_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_SHOTGUN_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_SMARTLOCKS_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_SMARTLOCKS_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_SPIDER_GRENADE_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_SPIDER_GRENADE_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_TESLA_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_DAMAGE_TESLA_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_HIT_EMP_GRENADE_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_HIT_EMP_GRENADE_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_ASSAULT_RIFLE_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_ASSAULT_RIFLE_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_BASILISK_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_BASILISK_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_BOLTGUN_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_BOLTGUN_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_CORTEX_BOMB_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_CORTEX_BOMB_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_CYBER_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_CYBER_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_EMP_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_EMP_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_FATMAN_FIST_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_FATMAN_FIST_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_FRAG_GRENADE_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_FRAG_GRENADE_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_GRENADE_LAUNCHER_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_GRENADE_LAUNCHER_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_ION_CANNON_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_ION_CANNON_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_LASER_RIFLE_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_LASER_RIFLE_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_LIGHT_KATANA_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_LIGHT_KATANA_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_MACHINE_PISTOL_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_MACHINE_PISTOL_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_MEDIUM_KATANA_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_MEDIUM_KATANA_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_MINIGUN_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_MINIGUN_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_MK808_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_MK808_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_ROCKET_LAUNCHER_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_ROCKET_LAUNCHER_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_SHOTGUN_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_SHOTGUN_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_SMARTLOCK_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_SMARTLOCK_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_SPIDER_GRENADE_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_SPIDER_GRENADE_AMOUNT` |
| `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_TESLA_RIFLE_AMOUNT` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/achievements/ACHIEVEMENT_DYSTOPIA_KILL_TESLA_RIFLE_AMOUNT` |
| `vgui/awards/globals/dev` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/dev` |
| `vgui/awards/globals/gaward_implant_cortex` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_implant_cortex` |
| `vgui/awards/globals/gaward_implant_cyberdeck` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_implant_cyberdeck` |
| `vgui/awards/globals/gaward_implant_legboosters` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_implant_legboosters` |
| `vgui/awards/globals/gaward_implant_mediplant` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_implant_mediplant` |
| `vgui/awards/globals/gaward_implant_soundsupp` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_implant_soundsupp` |
| `vgui/awards/globals/gaward_implant_stealth` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_implant_stealth` |
| `vgui/awards/globals/gaward_implant_swt` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_implant_swt` |
| `vgui/awards/globals/gaward_implant_tac` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_implant_tac` |
| `vgui/awards/globals/gaward_implant_thermal` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_implant_thermal` |
| `vgui/awards/globals/gaward_weap_assault` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_assault` |
| `vgui/awards/globals/gaward_weap_basilisk` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_basilisk` |
| `vgui/awards/globals/gaward_weap_boltgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_boltgun` |
| `vgui/awards/globals/gaward_weap_cyber` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_cyber` |
| `vgui/awards/globals/gaward_weap_emp` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_emp` |
| `vgui/awards/globals/gaward_weap_fist` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_fist` |
| `vgui/awards/globals/gaward_weap_frag` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_frag` |
| `vgui/awards/globals/gaward_weap_grenlauncher` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_grenlauncher` |
| `vgui/awards/globals/gaward_weap_ion` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_ion` |
| `vgui/awards/globals/gaward_weap_katana` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_katana` |
| `vgui/awards/globals/gaward_weap_katana_light` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_katana_light` |
| `vgui/awards/globals/gaward_weap_laserrifle` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_laserrifle` |
| `vgui/awards/globals/gaward_weap_machp` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_machp` |
| `vgui/awards/globals/gaward_weap_minigun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_minigun` |
| `vgui/awards/globals/gaward_weap_mk808` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_mk808` |
| `vgui/awards/globals/gaward_weap_rocket` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_rocket` |
| `vgui/awards/globals/gaward_weap_shotgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_shotgun` |
| `vgui/awards/globals/gaward_weap_smartlocks` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_smartlocks` |
| `vgui/awards/globals/gaward_weap_spider` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_spider` |
| `vgui/awards/globals/gaward_weap_tesla` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/gaward_weap_tesla` |
| `vgui/awards/globals/supporter` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/supporter` |
| `vgui/awards/globals/tester` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/globals/tester` |
| `vgui/awards/icon_award_corp_accuracy` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_corp_accuracy` |
| `vgui/awards/icon_award_corp_damage` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_corp_damage` |
| `vgui/awards/icon_award_corp_deaths` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_corp_deaths` |
| `vgui/awards/icon_award_corp_energy` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_corp_energy` |
| `vgui/awards/icon_award_corp_headshots` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_corp_headshots` |
| `vgui/awards/icon_award_corp_hits` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_corp_hits` |
| `vgui/awards/icon_award_corp_killrate` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_corp_killrate` |
| `vgui/awards/icon_award_corp_kills` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_corp_kills` |
| `vgui/awards/icon_award_corp_points` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_corp_points` |
| `vgui/awards/icon_award_corp_shots` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_corp_shots` |
| `vgui/awards/icon_award_corp_time` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_corp_time` |
| `vgui/awards/icon_award_punk_accuracy` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_punk_accuracy` |
| `vgui/awards/icon_award_punk_damage` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_punk_damage` |
| `vgui/awards/icon_award_punk_deaths` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_punk_deaths` |
| `vgui/awards/icon_award_punk_energy` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_punk_energy` |
| `vgui/awards/icon_award_punk_headshots` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_punk_headshots` |
| `vgui/awards/icon_award_punk_hits` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_punk_hits` |
| `vgui/awards/icon_award_punk_killrate` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_punk_killrate` |
| `vgui/awards/icon_award_punk_kills` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_punk_kills` |
| `vgui/awards/icon_award_punk_points` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_punk_points` |
| `vgui/awards/icon_award_punk_shots` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_punk_shots` |
| `vgui/awards/icon_award_punk_time` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/awards/icon_award_punk_time` |
| `vgui/circle_damage` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/circle_damage` |
| `vgui/circuit` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/circuit` |
| `vgui/crosshair_bg` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/crosshair_bg` |
| `vgui/crosshairs` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/crosshairs` |
| `vgui/crosshairs/crosshair1` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/crosshairs/crosshair1` |
| `vgui/crosshairs/crosshair2` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/crosshairs/crosshair2` |
| `vgui/crosshairs/crosshair3` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/crosshairs/crosshair3` |
| `vgui/crosshairs/crosshair4` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/crosshairs/crosshair4` |
| `vgui/crosshairs/crosshair5` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/crosshairs/crosshair5` |
| `vgui/crosshairs/crosshair6` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/crosshairs/crosshair6` |
| `vgui/crosshairs/crosshair7` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/crosshairs/crosshair7` |
| `vgui/crosshairs/crosshair8` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/crosshairs/crosshair8` |
| `vgui/crosshairs/crosshair9` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/crosshairs/crosshair9` |
| `vgui/dead` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/dead` |
| `vgui/dead64` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/dead64` |
| `vgui/hourglass` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/hourglass` |
| `vgui/hourglass64` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/hourglass64` |
| `vgui/hud/icon_locked` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/hud/icon_locked` |
| `vgui/hud_respawn` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/hud_respawn` |
| `vgui/iffcircle` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/iffcircle` |
| `vgui/iffcircleInner` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/iffcircleInner` |
| `vgui/iffcircleOuter` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/iffcircleOuter` |
| `vgui/implants/corp_icon_coldsuit` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_coldsuit` |
| `vgui/implants/corp_icon_cortex` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_cortex` |
| `vgui/implants/corp_icon_cortexbomb` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_cortexbomb` |
| `vgui/implants/corp_icon_cyberdeck` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_cyberdeck` |
| `vgui/implants/corp_icon_cyberdeck2` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_cyberdeck2` |
| `vgui/implants/corp_icon_iffinfo` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_iffinfo` |
| `vgui/implants/corp_icon_legboost` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_legboost` |
| `vgui/implants/corp_icon_legboosters` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_legboosters` |
| `vgui/implants/corp_icon_mediplant` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_mediplant` |
| `vgui/implants/corp_icon_mediplant_without_cross` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_mediplant_without_cross` |
| `vgui/implants/corp_icon_reflexes` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_reflexes` |
| `vgui/implants/corp_icon_scs` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_scs` |
| `vgui/implants/corp_icon_soundsupp` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_soundsupp` |
| `vgui/implants/corp_icon_stealth` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_stealth` |
| `vgui/implants/corp_icon_swt` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_swt` |
| `vgui/implants/corp_icon_tac` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_tac` |
| `vgui/implants/corp_icon_tac_bg` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_tac_bg` |
| `vgui/implants/corp_icon_tacscanner` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_tacscanner` |
| `vgui/implants/corp_icon_thermal` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/corp_icon_thermal` |
| `vgui/implants/icon_cyberdeck2_glow` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/icon_cyberdeck2_glow` |
| `vgui/implants/icon_cyberdeck_glow` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/icon_cyberdeck_glow` |
| `vgui/implants/icon_mediplant_cross` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/icon_mediplant_cross` |
| `vgui/implants/icon_tac_arm` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/icon_tac_arm` |
| `vgui/implants/icon_x` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/icon_x` |
| `vgui/implants/punk_icon_coldsuit` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_coldsuit` |
| `vgui/implants/punk_icon_cortex` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_cortex` |
| `vgui/implants/punk_icon_cortexbomb` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_cortexbomb` |
| `vgui/implants/punk_icon_cyberdeck` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_cyberdeck` |
| `vgui/implants/punk_icon_cyberdeck2` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_cyberdeck2` |
| `vgui/implants/punk_icon_iffinfo` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_iffinfo` |
| `vgui/implants/punk_icon_legboost` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_legboost` |
| `vgui/implants/punk_icon_legboosters` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_legboosters` |
| `vgui/implants/punk_icon_mediplant` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_mediplant` |
| `vgui/implants/punk_icon_mediplant_without_cross` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_mediplant_without_cross` |
| `vgui/implants/punk_icon_reflexes` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_reflexes` |
| `vgui/implants/punk_icon_scs` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_scs` |
| `vgui/implants/punk_icon_soundsupp` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_soundsupp` |
| `vgui/implants/punk_icon_stealth` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_stealth` |
| `vgui/implants/punk_icon_swt` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_swt` |
| `vgui/implants/punk_icon_tac` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_tac` |
| `vgui/implants/punk_icon_tac_bg` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_tac_bg` |
| `vgui/implants/punk_icon_tacscanner` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_tacscanner` |
| `vgui/implants/punk_icon_thermal` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/implants/punk_icon_thermal` |
| `vgui/infoicons/breakable` | `Patch` | `-` | `ui` | `0` | `vgui/infoicons/breakable` |
| `vgui/infoicons/defend` | `Patch` | `-` | `ui` | `0` | `vgui/infoicons/defend` |
| `vgui/infoicons/delivery` | `Patch` | `-` | `ui` | `0` | `vgui/infoicons/delivery` |
| `vgui/infoicons/door_closed` | `Patch` | `-` | `ui` | `0` | `vgui/infoicons/door_closed` |
| `vgui/infoicons/door_open` | `Patch` | `-` | `ui` | `0` | `vgui/infoicons/door_open` |
| `vgui/infoicons/item` | `Patch` | `-` | `ui` | `0` | `vgui/infoicons/item` |
| `vgui/infoicons/jip` | `Patch` | `-` | `ui` | `0` | `vgui/infoicons/jip` |
| `vgui/infoicons/turret_friendly` | `Patch` | `-` | `ui` | `0` | `vgui/infoicons/turret_friendly` |
| `vgui/infoicons/turret_hostile` | `Patch` | `-` | `ui` | `0` | `vgui/infoicons/turret_hostile` |
| `vgui/item` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/item` |
| `vgui/loading` | `UnlitGeneric` | `-` | `ui` | `0` | `loading/loading` |
| `vgui/logos/UI/cacotopia` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/cacotopia` |
| `vgui/logos/UI/commandopoop` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/commandopoop` |
| `vgui/logos/UI/frostythepyro` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/frostythepyro` |
| `vgui/logos/UI/gir1` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/gir1` |
| `vgui/logos/UI/gir2` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/gir2` |
| `vgui/logos/UI/herostratos2` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/herostratos2` |
| `vgui/logos/UI/herostratos3` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/herostratos3` |
| `vgui/logos/UI/herostratos4` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/herostratos4` |
| `vgui/logos/UI/novalux1` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/novalux1` |
| `vgui/logos/UI/novalux4` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/novalux4` |
| `vgui/logos/UI/omnigord2` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/omnigord2` |
| `vgui/logos/UI/omnigord3` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/omnigord3` |
| `vgui/logos/UI/omnigord4` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/omnigord4` |
| `vgui/logos/UI/omnigord5` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/omnigord5` |
| `vgui/logos/UI/omnigord6` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/omnigord6` |
| `vgui/logos/UI/r3d` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/r3d` |
| `vgui/logos/UI/siberia` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/siberia` |
| `vgui/logos/UI/spray` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/spray` |
| `vgui/logos/UI/thxcontre` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/thxcontre` |
| `vgui/logos/UI/tr0mb0ne1` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/tr0mb0ne1` |
| `vgui/logos/UI/tr0mb0ne10` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/tr0mb0ne10` |
| `vgui/logos/UI/tr0mb0ne2` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/tr0mb0ne2` |
| `vgui/logos/UI/tr0mb0ne3` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/tr0mb0ne3` |
| `vgui/logos/UI/tr0mb0ne4` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/tr0mb0ne4` |
| `vgui/logos/UI/tr0mb0ne5` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/tr0mb0ne5` |
| `vgui/logos/UI/tr0mb0ne6` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/tr0mb0ne6` |
| `vgui/logos/UI/tr0mb0ne7` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/tr0mb0ne7` |
| `vgui/logos/UI/tr0mb0ne9` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/tr0mb0ne9` |
| `vgui/logos/UI/warragul_buzzsaw` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/warragul_buzzsaw` |
| `vgui/logos/UI/warragul_cogs_digits` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/logos/warragul_cogs_digits` |
| `vgui/logos/cacotopia` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/cacotopia` |
| `vgui/logos/commandopoop` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/commandopoop` |
| `vgui/logos/frostythepyro` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/frostythepyro` |
| `vgui/logos/gir1` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/gir1` |
| `vgui/logos/gir2` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/gir2` |
| `vgui/logos/herostratos2` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/herostratos2` |
| `vgui/logos/herostratos3` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/herostratos3` |
| `vgui/logos/herostratos4` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/herostratos4` |
| `vgui/logos/novalux1` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/novalux1` |
| `vgui/logos/novalux4` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/novalux4` |
| `vgui/logos/omnigord2` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/omnigord2` |
| `vgui/logos/omnigord3` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/omnigord3` |
| `vgui/logos/omnigord4` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/omnigord4` |
| `vgui/logos/omnigord5` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/omnigord5` |
| `vgui/logos/omnigord6` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/omnigord6` |
| `vgui/logos/r3d` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/r3d` |
| `vgui/logos/siberia` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/siberia` |
| `vgui/logos/spray` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/logos/lelhase` |
| `vgui/logos/thxcontre` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/thxcontre` |
| `vgui/logos/tr0mb0ne1` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/tr0mb0ne1` |
| `vgui/logos/tr0mb0ne10` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/tr0mb0ne10` |
| `vgui/logos/tr0mb0ne2` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/tr0mb0ne2` |
| `vgui/logos/tr0mb0ne3` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/tr0mb0ne3` |
| `vgui/logos/tr0mb0ne4` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/tr0mb0ne4` |
| `vgui/logos/tr0mb0ne5` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/tr0mb0ne5` |
| `vgui/logos/tr0mb0ne6` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/tr0mb0ne6` |
| `vgui/logos/tr0mb0ne7` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/tr0mb0ne7` |
| `vgui/logos/tr0mb0ne9` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/tr0mb0ne9` |
| `vgui/logos/warragul_buzzsaw` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/warragul_buzzsaw` |
| `vgui/logos/warragul_cogs_digits` | `$basetexture` | `-` | `ui` | `0` | `vgui/logos/warragul_cogs_digits` |
| `vgui/maps/menu_thumb_dys_assemble` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_assemble` |
| `vgui/maps/menu_thumb_dys_broadcast` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_broadcast` |
| `vgui/maps/menu_thumb_dys_cybernetic` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_cybernetic` |
| `vgui/maps/menu_thumb_dys_desert` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_desert` |
| `vgui/maps/menu_thumb_dys_detonate` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_detonate` |
| `vgui/maps/menu_thumb_dys_exodus` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_exodus` |
| `vgui/maps/menu_thumb_dys_fortress` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_fortress` |
| `vgui/maps/menu_thumb_dys_fusion` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_fusion` |
| `vgui/maps/menu_thumb_dys_infect` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_infect` |
| `vgui/maps/menu_thumb_dys_parallax` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_parallax` |
| `vgui/maps/menu_thumb_dys_silo` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_silo` |
| `vgui/maps/menu_thumb_dys_tower` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_tower` |
| `vgui/maps/menu_thumb_dys_undermine` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_undermine` |
| `vgui/maps/menu_thumb_dys_vaccine` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/maps/menu_thumb_dys_vaccine` |
| `vgui/medic` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/medic` |
| `vgui/obits/objective` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/obits/objective` |
| `vgui/offscreeniconarrow` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/offscreeniconarrow` |
| `vgui/players/menu_heavy_c_basilisk` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_c_basilisk` |
| `vgui/players/menu_heavy_c_coilgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_c_coilgun` |
| `vgui/players/menu_heavy_c_ion` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_c_ion` |
| `vgui/players/menu_heavy_c_minigun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_c_minigun` |
| `vgui/players/menu_heavy_c_rocket` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_c_rocket` |
| `vgui/players/menu_heavy_c_silhouette` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_c_silhouette` |
| `vgui/players/menu_heavy_p_basilisk` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_p_basilisk` |
| `vgui/players/menu_heavy_p_coilgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_p_coilgun` |
| `vgui/players/menu_heavy_p_ion` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_p_ion` |
| `vgui/players/menu_heavy_p_minigun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_p_minigun` |
| `vgui/players/menu_heavy_p_rocket` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_p_rocket` |
| `vgui/players/menu_heavy_p_silhouette` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_heavy_p_silhouette` |
| `vgui/players/menu_light_c_boltgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_light_c_boltgun` |
| `vgui/players/menu_light_c_laser` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_light_c_laser` |
| `vgui/players/menu_light_c_shotgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_light_c_shotgun` |
| `vgui/players/menu_light_c_silhouette` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_light_c_silhouette` |
| `vgui/players/menu_light_c_smartlocks` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_light_c_smartlocks` |
| `vgui/players/menu_light_p_boltgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_light_p_boltgun` |
| `vgui/players/menu_light_p_laser` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_light_p_laser` |
| `vgui/players/menu_light_p_shotgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_light_p_shotgun` |
| `vgui/players/menu_light_p_silhouette` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_light_p_silhouette` |
| `vgui/players/menu_light_p_smartlocks` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_light_p_smartlocks` |
| `vgui/players/menu_med_c_grenade` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_med_c_grenade` |
| `vgui/players/menu_med_c_mk405` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_med_c_mk405` |
| `vgui/players/menu_med_c_mk808` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_med_c_mk808` |
| `vgui/players/menu_med_c_silhouette` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_med_c_silhouette` |
| `vgui/players/menu_med_c_tesla` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_med_c_tesla` |
| `vgui/players/menu_med_p_grenade` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_med_p_grenade` |
| `vgui/players/menu_med_p_mk405` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_med_p_mk405` |
| `vgui/players/menu_med_p_mk808` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_med_p_mk808` |
| `vgui/players/menu_med_p_silhouette` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_med_p_silhouette` |
| `vgui/players/menu_med_p_tesla` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/players/menu_med_p_tesla` |
| `vgui/programs/corps` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/programs/corps` |
| `vgui/programs/p1` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/programs/p1` |
| `vgui/programs/p2` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/programs/p2` |
| `vgui/programs/p3` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/programs/p3` |
| `vgui/programs/p4` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/programs/p4` |
| `vgui/programs/p5` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/programs/p5` |
| `vgui/programs/p6` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/programs/p6` |
| `vgui/programs/p7` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/programs/p7` |
| `vgui/programs/p8` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/programs/p8` |
| `vgui/programs/punks` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/programs/punks` |
| `vgui/radar/ammo` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/radar/ammo` |
| `vgui/radar/grid` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/radar/grid` |
| `vgui/radar/info` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/radar/info` |
| `vgui/radar/objective` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/radar/objective` |
| `vgui/radar/player` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/radar/player` |
| `vgui/radar/spawn` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/radar/spawn` |
| `vgui/radar/sub_objective_corp` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/radar/sub_objective_corp` |
| `vgui/radar/sub_objective_punk` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/radar/sub_objective_punk` |
| `vgui/radar/terminal` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/radar/terminal` |
| `vgui/radar/vehicle` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/radar/vehicle` |
| `vgui/resource/downarrow` | `UnlitGeneric` | `default` | `ui` | `0` | `vgui/resource/downarrow` |
| `vgui/resource/mic_meter_dead` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/resource/mic_meter_dead` |
| `vgui/resource/mic_meter_live` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/resource/mic_meter_live` |
| `vgui/screens/c4panel_bg` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/c4panel_bg` |
| `vgui/screens/cyber_tag` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/cyber_tag` |
| `vgui/screens/cyberpanel_bg` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/cyberpanel_bg` |
| `vgui/screens/encryption` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/encryption` |
| `vgui/screens/password` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/password` |
| `vgui/screens/programbg` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/programbg` |
| `vgui/screens/rocketscreen` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/rocketscreen` |
| `vgui/screens/rocketscreenoutline` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/rocketscreenoutline` |
| `vgui/screens/secorp_bg1` | `unlitgeneric` | `-` | `ui` | `1` | `vgui/screens/secorp_bg1` |
| `vgui/screens/secorp_bg1a` | `unlitgeneric` | `-` | `ui` | `1` | `vgui/screens/secorp_bg1a` |
| `vgui/screens/secorp_bg2` | `unlitgeneric` | `-` | `ui` | `0` | `vgui/screens/secorp_bg2` |
| `vgui/screens/transparent` | `Modulate` | `-` | `ui` | `0` | `VGUI/screens/transparent` |
| `vgui/screens/vgui_bg` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_bg` |
| `vgui/screens/vgui_button2_disabled` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_button2_disabled` |
| `vgui/screens/vgui_button2_enabled` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_button2_enabled` |
| `vgui/screens/vgui_button2_hover` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_button2_hover` |
| `vgui/screens/vgui_button2_pushed` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_button2_pushed` |
| `vgui/screens/vgui_button_disabled` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_button_disabled` |
| `vgui/screens/vgui_button_enabled` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_button_enabled` |
| `vgui/screens/vgui_button_hover` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_button_hover` |
| `vgui/screens/vgui_button_pushed` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_button_pushed` |
| `vgui/screens/vgui_octagonal_button_enable` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_octagonal_button_enable` |
| `vgui/screens/vgui_octagonal_button_hover` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_octagonal_button_hover` |
| `vgui/screens/vgui_octagonal_button_pressed` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/screens/vgui_octagonal_button_pressed` |
| `vgui/screens/vgui_overlay` | `Modulate` | `-` | `ui` | `0` | `vgui/screens/vgui_overlay` |
| `vgui/skull` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/skull` |
| `vgui/speaker` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/speaker` |
| `vgui/textbubble` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/textbubble` |
| `vgui/weapons/hud/icon_boltgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_boltgun` |
| `vgui/weapons/hud/icon_empgren` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_empgren` |
| `vgui/weapons/hud/icon_fist` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_fist` |
| `vgui/weapons/hud/icon_fraggren` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_fraggren` |
| `vgui/weapons/hud/icon_grenade` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_grenade` |
| `vgui/weapons/hud/icon_ion` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_ion` |
| `vgui/weapons/hud/icon_katana` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_katana` |
| `vgui/weapons/hud/icon_laser` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_laser` |
| `vgui/weapons/hud/icon_machinepistol` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_machinepistol` |
| `vgui/weapons/hud/icon_minigun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_minigun` |
| `vgui/weapons/hud/icon_mk405` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_mk405` |
| `vgui/weapons/hud/icon_mk808` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_mk808` |
| `vgui/weapons/hud/icon_rocket` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_rocket` |
| `vgui/weapons/hud/icon_shotgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_shotgun` |
| `vgui/weapons/hud/icon_spidergren` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/hud/icon_spidergren` |
| `vgui/weapons/menu_basilisk` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_basilisk` |
| `vgui/weapons/menu_crossbow` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_crossbow` |
| `vgui/weapons/menu_grenade` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_grenade` |
| `vgui/weapons/menu_ion` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_ion` |
| `vgui/weapons/menu_laser` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_laser` |
| `vgui/weapons/menu_minigun` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_minigun` |
| `vgui/weapons/menu_mk405` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_mk405` |
| `vgui/weapons/menu_mk808` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_mk808` |
| `vgui/weapons/menu_rocket` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_rocket` |
| `vgui/weapons/menu_shotgun` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_shotgun` |
| `vgui/weapons/menu_smartlocks` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_smartlocks` |
| `vgui/weapons/menu_tesla` | `UnlitGeneric` | `-` | `ui` | `0` | `VGUI/weapons/menu_tesla` |
| `vgui/weapons/obits/icon_basilisk` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_basilisk` |
| `vgui/weapons/obits/icon_basilisk_alt` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_basilisk_alt` |
| `vgui/weapons/obits/icon_boltgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_boltgun` |
| `vgui/weapons/obits/icon_boltgun_alt` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_boltgun_alt` |
| `vgui/weapons/obits/icon_cortex` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_cortex` |
| `vgui/weapons/obits/icon_cyber` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_cyber` |
| `vgui/weapons/obits/icon_cyber_dumpshock` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_cyber_dumpshock` |
| `vgui/weapons/obits/icon_emped_from_cyber` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_emped_from_cyber` |
| `vgui/weapons/obits/icon_empgren` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_empgren` |
| `vgui/weapons/obits/icon_fist` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_fist` |
| `vgui/weapons/obits/icon_fraggren` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_fraggren` |
| `vgui/weapons/obits/icon_grenade` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_grenade` |
| `vgui/weapons/obits/icon_grenade_alt` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_grenade_alt` |
| `vgui/weapons/obits/icon_ion` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_ion` |
| `vgui/weapons/obits/icon_katana` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_katana` |
| `vgui/weapons/obits/icon_laser` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_laser` |
| `vgui/weapons/obits/icon_legboosters` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_legboosters` |
| `vgui/weapons/obits/icon_machinepistol` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_machinepistol` |
| `vgui/weapons/obits/icon_minigun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_minigun` |
| `vgui/weapons/obits/icon_mk405` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_mk405` |
| `vgui/weapons/obits/icon_mk808` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_mk808` |
| `vgui/weapons/obits/icon_phistball` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_phistball` |
| `vgui/weapons/obits/icon_rocket` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_rocket` |
| `vgui/weapons/obits/icon_shotgun` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_shotgun` |
| `vgui/weapons/obits/icon_smartlocks` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_smartlocks` |
| `vgui/weapons/obits/icon_spidergren` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_spidergren` |
| `vgui/weapons/obits/icon_tesla` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_tesla` |
| `vgui/weapons/obits/icon_tesla_alt` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_tesla_alt` |
| `vgui/weapons/obits/icon_turret` | `UnlitGeneric` | `-` | `ui` | `0` | `vgui/weapons/obits/icon_turret` |

### `waterfix`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `waterfix/concretewall010c` | `LightmappedGeneric` | `concrete` | `map` | `2` | `concrete/concretewall010c` |
| `waterfix/concretewall022a_nodecal` | `LightmappedGeneric` | `concrete` | `decal` | `1` | `concrete/concretewall022a` |
| `waterfix/metalpipe008a_nodecal` | `LightmappedGeneric` | `metal` | `decal` | `1` | `metal/metalpipe008a` |
| `waterfix/metalwall030a_nodecal` | `LightmappedGeneric` | `metal` | `decal` | `1` | `metal/metalwall030a` |

### `windows`

| Material | Shader | Surface | Usage | Used In Maps | Base Texture |
|---|---|---|---|---|---|
| `windows/building_window_1` | `LightmappedGeneric` | `concrete` | `map` | `0` | `windows/building_window_1` |
| `windows/building_window_4` | `LightmappedGeneric` | `concrete` | `map` | `3` | `windows/building_window_4` |
| `windows/building_window_5` | `LightmappedGeneric` | `concrete` | `map` | `0` | `windows/building_window_5` |
| `windows/building_window_6` | `LightmappedGeneric` | `concrete` | `map` | `0` | `windows/building_window_6` |
| `windows/building_window_8` | `LightmappedGeneric` | `concrete` | `map` | `2` | `windows/building_window_8` |
| `windows/building_window_9` | `LightmappedGeneric` | `concrete` | `map` | `2` | `windows/building_window_9` |
| `windows/cb_wind_night01` | `LightmappedGeneric` | `concrete` | `map` | `2` | `windows/cb_wind_night01` |
| `windows/cb_wind_night02` | `LightmappedGeneric` | `concrete` | `map` | `1` | `windows/cb_wind_night02` |
| `windows/powercore_glass` | `LightmappedGeneric` | `glass` | `map` | `2` | `windows/powercore_glass` |
| `windows/window_white` | `LightmappedGeneric` | `-` | `map` | `0` | `windows/window_white` |
