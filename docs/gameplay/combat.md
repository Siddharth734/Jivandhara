# Combat

## Player Attacks

`Player.input()` invokes `Level.create_attack()` for Space or `Level.create_magic()` for Left Ctrl. `Weapon` creates a directional image sprite from the selected weapon folder and adds it to `visible_sprites` and `attack_sprites`.

Magic is implemented by `MagicPlayer`. Healing consumes energy and changes player health. Flame consumes energy and creates five directional flame particle placements.

## Hit Detection

`Level.player_attack_logic()` runs after drawing and uses `pygame.sprite.spritecollide()` with `pygame.sprite.collide_mask` between every attack sprite and `attackable_sprites`. Grass targets are removed with leaf particles; enemies receive `get_damage()`.

Movement collision separately uses rectangular hitboxes and `colliderect()`.

## Damage and Protection

Weapon damage is player attack plus weapon damage. Magic damage is player magic plus magic strength. Enemy damage is read from `monster_data`. Player and enemy vulnerability timers prevent repeated damage for 1000 ms and drive flashing alpha feedback.

Enemy vulnerability reverses its movement direction and scales it by resistance for knockback. Enemy death awards configured experience. Player health at or below 1 enters the game-over branch.
