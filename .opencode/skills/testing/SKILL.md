---
name: project-j-testing
description: Verify changes to the Jivandhara prototype honestly when no automated suite exists.
---

# Testing Skill

## Use When

Use for validation, regression checks, test planning, or reporting results.

## Current Test Surface

`code/test.py` is empty. No automated test runner or test configuration exists. The primary available check is a manual launch from `code/` using `python main.py`.

## Verification

Choose the narrowest check available, then manually exercise the changed path: input, map loading, sprite creation, collision, combat, HUD, pause, or game over. Report exactly what ran and distinguish static inspection from runtime verification. Read `docs/development/testing.md`.
