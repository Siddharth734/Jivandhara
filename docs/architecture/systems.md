# Systems

## World and Map

`Level.create_map()` maps CSV cells to 64-pixel positions. Boundary cells create invisible obstacles; grass and objects create tiles; entity IDs create the player or data-driven enemies.

## Sprite Groups

- `visible_sprites`: custom camera/Y-sort group for rendered world sprites.
- `obstacle_sprites`: collision obstacles.
- `attack_sprites`: active player weapon and magic attack sprites.
- `attackable_sprites`: enemies and grass targets that can receive attack collision.

## Entities

`Entity` supplies direction, animation index/speed, a vulnerability timer, movement, and horizontal/vertical collision resolution. `Player` and `Enemy` specialize it.

## Combat

`Level` provides callbacks used by Player and Enemy. Player-created attacks enter `attack_sprites`; collision against `attackable_sprites` calls either grass removal or `Enemy.get_damage()`. Enemy attacks call `Level.damage_player()`.

## Effects

`AnimationPlayer` loads frame folders and creates short-lived `ParticleEffect` sprites. Particle effects update every frame and kill themselves after their frame sequence ends.

## UI and Modes

`UI` renders the HUD in screen coordinates. `Upgrade` renders the pause/upgrade overlay. `GAMEOVER` renders the terminal health state. These are coordinated by `Level.run()`.
