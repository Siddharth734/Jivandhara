---
name: project-j-pygame-development
description: Extend PROJECT J using its existing Pygame-CE loop, sprites, groups, timing, and rendering conventions.
---

# Pygame Development Skill

## Use When

Use for sprite, rendering, input, timing, animation, camera, or Pygame asset changes.

## Conventions

- Construct sprites with explicit group membership.
- Use `Entity.move()` for actor movement and its hitbox/rect collision path.
- Use `visible_sprites`, `obstacle_sprites`, `attack_sprites`, and `attackable_sprites` according to their existing responsibilities.
- Use `YSortCameraGroup.draw()` for world rendering and `UI` for screen-space HUD.
- Load animation folders through `support.import_folder()` where the existing system does so.
- Timers use Pygame millisecond ticks; animation uses `dt`.

Read `docs/architecture/game-loop.md` and `docs/patterns/pygame-patterns.md`. Validate with a focused manual run when possible; no automated tests exist.
