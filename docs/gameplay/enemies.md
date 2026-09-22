# Enemies

`Enemy` is defined in `code/enemy.py` and extends `Entity`. Monster values are selected from `monster_data` in `code/settings.py`.

Current configured types are `squid`, `raccoon`, `spirit`, and `bamboo`. Their configuration supplies health, experience reward, damage, attack effect/sound, speed, resistance, attack radius, and notice radius.

## Spawning

`Level.create_map()` reads `map/map_Entities.csv`. ID `394` creates the player. IDs `390`, `391`, and `392` create bamboo, spirit, and raccoon; other non-player entity values create squid.

## AI

`YSortCameraGroup.enemy_update()` selects sprites with `sprite_type == 'enemy'` and calls `enemy_update(player)`. Each enemy chooses idle, move, or attack based on player distance. Move direction is a normalized vector toward the player. There is no patrol or multi-state AI framework.

Enemies animate from `graphics/monsters/<name>/{idle,move,attack}/`. On death they kill themselves, spawn a type-specific particle effect, award experience, and play a sound.
