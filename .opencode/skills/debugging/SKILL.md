---
name: project-j-debugging
description: Trace and fix Jivandhara runtime bugs with minimal, source-backed changes.
---

# Debugging Skill

## Use When

Use for crashes, missing assets, wrong collisions, state bugs, timing issues, or gameplay regressions.

## Workflow

1. Reproduce the issue.
2. Identify the owning path among `Game`, `Level`, `Entity`, `Player`, `Enemy`, or helpers.
3. Trace groups, callbacks, asset paths, and timers.
4. Make the smallest root-cause fix.
5. Run a focused check and manually exercise the affected path.

Use `code/debug.py`'s `Debug()` only when an on-screen value is useful. Check working-directory assumptions and the one-time `dt` calculation early when timing appears wrong. Read `docs/development/debugging.md`.
