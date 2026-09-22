---
name: project-j-performance
description: Investigate performance-sensitive paths in the existing Jivandhara Pygame implementation.
---

# Performance Skill

## Use When

Use for frame-rate, memory, particle, collision, or asset-loading concerns.

## Observed Hot Paths

- `Level.run()` updates and draws the visible group every frame.
- `YSortCameraGroup.draw()` sorts all visible sprites by vertical position every frame.
- `Entity.collision()` loops over obstacle sprites for each horizontal and vertical movement pass.
- `Level.player_attack_logic()` checks each attack sprite against attackable sprites.
- Particle effects update every frame and allocate sprites when effects are triggered.
- Image and sound assets are loaded during object construction rather than via a shared cache.

Measure or reproduce before changing behavior. Do not optimize by redesigning groups or asset loading without evidence and a request. Read `docs/architecture/systems.md` and the source path involved.
