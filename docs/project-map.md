# PROJECT J Repository Map

PROJECT J is the Jivandhara 2D action-adventure prototype.

## Root

- `code/`: executable Python modules. Run the game from this directory because source uses relative paths such as `graphics/...`, `audio/...`, and `map/...`.
- `graphics/`: fonts, player and monster animation frames, objects, particles, tilemap art, and weapon art.
- `audio/`: music and sound effects, including the `attack/` effects directory.
- `map/`: CSV map layers consumed by `Level.create_map()`.
- `README.md`: project description, controls, installation note, and credits.
- `AGENTS.md`: permanent instructions for AI changes.
- `docs/`: generated project knowledge for future agents.
- `docs/gameplay/roadmap.md`: requested but unimplemented gameplay features, including character switching and signature abilities.
- `.opencode/`: project-specific skills and commands for AI-assisted work.

## Executable Modules

- `code/main.py`: `Game` entry point, window, event loop, display update, and shutdown.
- `code/settings.py`: Pygame import, constants, paths/data tables for weapons, magic, and monsters.
- `code/level.py`: `Level`, map creation, groups, combat coordination, pause/game-over branching, and `YSortCameraGroup`.
- `code/entity.py`: shared movement, hitbox collision, direction, animation timing, and vulnerability timer.
- `code/player.py`: `Player`, input, player stats, weapon/magic selection, attacks, and animation.
- `code/enemy.py`: `Enemy`, data-driven monster setup, radius-based AI, attacks, damage, knockback, and death.
- `code/tile.py`: tile sprites and tile hitboxes.
- `code/weapon.py`: one-shot weapon attack sprite positioned from player direction.
- `code/magic.py`: heal and flame abilities.
- `code/signature_abilities.py`: loosely coupled Stage 1 character abilities and temporary Anbu clone sprites.
- `code/particles.py`: frame-based `ParticleEffect` and `AnimationPlayer`.
- `code/ui.py`: health/energy HUD, experience, weapon and magic overlays.
- `code/upgrade.py`: pause upgrade menu and stat purchasing.
- `code/gameover.py`: game-over overlay and text.
- `code/timee.py`: millisecond timer helper.
- `code/support.py`: CSV layout and image-folder loading helpers.
- `code/debug.py`: simple on-screen debug text helper.
- `code/test.py`: empty; no automated tests are implemented.
- `code/solves.txt`: developer notes and experiments, not runtime code.

## Map Layers

`Level.create_map()` loads `map_FloorBlocks.csv` as boundaries, `map_Grass.csv` as grass, `map_Objects.csv` as objects, and `map_Entities.csv` as player/enemy placement. The other CSV files exist in the repository but are not loaded by the current `create_map()` implementation.
