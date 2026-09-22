# Asset Map

| Asset path | Loaded by | Purpose |
|---|---|---|
| `graphics/playerAnbu/<state>/` | `Player.import_player_assets()` | Player directional, idle, and attack animation frames |
| `graphics/monsters/<name>/<state>/` | `Enemy.import_graphics()` | Enemy idle, move, and attack frames |
| `graphics/objects/` | `support.import_folder()` from `Level.create_map()` | CSV object tile surfaces |
| `graphics/grass/` (repository directory; code requests `graphics/Grass/`) | `support.import_folder()` from `Level.create_map()` | Random grass tile surfaces |
| `graphics/tilemap/ground.png` | `YSortCameraGroup.__init__()` | Repeating/world floor surface drawn beneath sprites |
| `graphics/weapons/<weapon>/` | `Weapon` and `UI` | Directional attack sprites and selected weapon icons |
| `graphics/particles/flame/frames/` | `AnimationPlayer` | Flame magic frames |
| `graphics/particles/heal/frames/` | `AnimationPlayer` | Healing frames |
| `graphics/particles/aura/` | `AnimationPlayer` | Healing aura frames |
| `graphics/particles/{claw,slash,sparkle,leaf_attack,thunder}/` | `AnimationPlayer` | Attack effect frames |
| `graphics/particles/{smoke_orange,raccoon,nova,bamboo}/` | `AnimationPlayer` | Monster death effects |
| `graphics/particles/leaf1` through `leaf6` | `AnimationPlayer` | Grass destruction leaf effects, including reflected frames |
| `graphics/font/joystix.ttf` | `UI`, `Upgrade`, `GAMEOVER` | HUD/menu/game-over text |
| `audio/Theme.ogg` | `Level` | Main background music |
| `audio/rick.wav` | `Level` | Game-over music |
| `audio/{sword,heal,fire,hit,death}.wav` | `Player`, `MagicPlayer`, `Enemy` | Player and combat sound effects |
| `audio/attack/` | `monster_data` and `Enemy` | Configured enemy attack sounds |
