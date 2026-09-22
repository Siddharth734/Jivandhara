---
name: project-j-architecture
description: Understand and safely modify the existing Jivandhara architecture.
---

# Architecture Skill

## Use When

Use for changes crossing `Game`, `Level`, sprite groups, map loading, camera drawing, or game modes.

## Project Knowledge

- `Game` in `code/main.py` owns the window and outer loop.
- `Level` in `code/level.py` coordinates map creation, groups, combat callbacks, UI, pause, and game over.
- `YSortCameraGroup` owns camera offset and Y-sorted world drawing.
- There is no formal scene or service framework.

Read `docs/architecture/overview.md`, `game-loop.md`, and `systems.md` before editing.

## Workflow

Trace the caller and the relevant group or callback, make the smallest local change, and manually verify the affected mode. Preserve relative paths and flat module imports.
