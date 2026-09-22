---
name: project-j-gameplay
description: Add or debug Jivandhara player, enemy, combat, progression, or mode behavior.
---

# Gameplay Skill

## Use When

Use for mechanics involving Player, Enemy, weapons, magic, damage, effects, experience, upgrades, or game modes.

## Project Knowledge

- Player and Enemy extend `Entity`.
- `Level` supplies callbacks for attack creation, damage, particles, and experience.
- Combat uses mask collision for attack sprites and rectangular hitboxes for movement.
- Vulnerability timers gate repeated damage.
- Monster, weapon, and magic values are configured in `settings.py`.

Read `docs/gameplay/player.md`, `enemies.md`, `combat.md`, and `game-states.md` before editing. Reuse existing callbacks and groups; do not invent state systems or mechanics without an explicit request.
