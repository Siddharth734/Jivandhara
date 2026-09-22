# Game States

There is no formal scene class. `Level.run()` implements the active modes.

## Gameplay

When not paused and the player is alive, timers update, enemy AI runs, visible sprites update, the world is drawn, the HUD is drawn, and player attack collisions are resolved.

## Upgrade/Pause Mode

`Game` handles an ESC keydown and calls `Level.toggle_menu()`. With `game_paused` true, gameplay sprite updates stop and `Upgrade.display()` renders a dark overlay, upgrade title, stat columns, and keyboard navigation. ESC toggles back.

## Game Over

When `player.health <= 1`, `Level` delays once, stops the theme, starts `rick.wav`, and calls `GAMEOVER.update(dt)`. The current game-over screen only renders text and an overlay; it has no restart or quit interaction.
