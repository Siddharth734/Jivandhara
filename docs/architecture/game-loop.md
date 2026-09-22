# Game Loop

## Initialization

`code/main.py` constructs `Game`, calls `pygame.init()`, creates a resizable 1280x720 display, creates `pygame.time.Clock`, constructs `Level`, and starts `Level.main_sound` in a loop.

`Level.__init__()` creates sprite groups, loads the CSV map, creates UI/upgrade/game-over objects, and initializes particle/magic helpers.

## Per-Iteration Flow

```text
Game.run()
  -> read Pygame events
  -> fill display with WATER_COLOR
  -> Level.run(dt)
       -> game-over branch OR paused branch OR normal gameplay updates
       -> draw world and camera-sorted sprites
       -> draw HUD
       -> resolve player attack collisions
  -> pygame.display.update()
```

Events handled by `Game` are QUIT, ESC (toggle upgrade/pause mode), and F11 (toggle fullscreen). Player key state and just-pressed keys are read inside `Player.input()` during the update path.

In normal gameplay, `Level.run()` updates the weapon lifetime timer, invokes enemy AI through `visible_sprites.enemy_update(player)`, updates all visible sprites, applies weapon jitter, draws the world, draws UI, and processes attack collisions.

`pygame.quit()` runs after the loop exits.

## Timing

`FPS = 60` and `pygame.time.Clock()` are configured. However, the current code calls `clock.tick(FPS) / 1000` once before entering the `while` loop, so the same `dt` is reused. Timers themselves use `pygame.time.get_ticks()` and are independent of `dt`.
