---
name: project-j-assets
description: Safely work with PROJECT J graphics, audio, fonts, particles, weapons, and CSV map assets.
---

# Assets Skill

## Use When

Use when adding or changing asset references, animation frames, sounds, particles, weapons, or map placement.

## Project Knowledge

Assets are loaded through relative paths. `support.import_folder()` loads image directories. Player and enemy animation folder names are state-sensitive. Map placement is CSV-driven with 64-pixel tiles and numeric entity IDs.

Read `docs/assets/assets.md`, `asset-map.md`, and `docs/project-map.md`. Confirm every referenced path exists and do not invent asset filenames or map IDs.
