# Data Flow

## Startup

```text
code/main.py
  -> Game
  -> Level
  -> import_csv_layout()
  -> Tile / Player / Enemy instances
  -> sprite groups
```

## Player Input to Attack

```text
Pygame key state
  -> Player.input()
  -> attack cooldown / selected weapon or magic
  -> Level.create_attack() or Level.create_magic()
  -> Weapon or ParticleEffect sprites
  -> attack_sprites / visible_sprites
  -> Level.player_attack_logic()
  -> mask collision
  -> enemy damage or grass removal
```

## Player Movement

```text
keyboard direction
  -> Player.direction
  -> Entity.move(speed, dt)
  -> hitbox movement
  -> obstacle_sprites colliderect checks
  -> rect.center synchronized to hitbox.center
  -> Player.animate(dt)
```

## Enemy Behavior

```text
Level.run()
  -> YSortCameraGroup.enemy_update(player)
  -> Enemy.get_status(player)
  -> Enemy.actions(player)
  -> direction or attack callback
  -> Enemy.update(dt)
  -> movement, animation, death check
```

## Damage and Death

```text
attack collision or enemy attack
  -> vulnerability timer check
  -> health reduction
  -> hit/death particles and sound
  -> enemy kill + experience OR player game-over branch
```
