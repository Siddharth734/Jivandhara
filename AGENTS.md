# PROJECT J Agent Guide

PROJECT J is the existing Jivandhara game: a Python and Pygame-CE project. The current game is the source of truth.

## Core Rule

Extend the existing game. Do not rebuild it, redesign its architecture, or change gameplay behavior unless the user explicitly requests that work.

## Before Editing

1. Read the relevant implementation in `code/`.
2. Trace related callers, sprite groups, assets, and map data.
3. Reuse the local Pygame patterns and data structures.
4. Make the smallest change that satisfies the request.
5. Validate the affected behavior and check for regressions.

## Project Constraints

- Do not modify unrelated gameplay or asset files.
- Do not invent assets, map IDs, mechanics, states, or dependencies.
- Do not remove existing functionality.
- Do not overwrite user work.
- Preserve relative asset paths and the expected `code/` working directory.
- Keep `Level` as the gameplay coordinator unless a request explicitly changes that architecture.
- Preserve the existing `pygame.sprite.Sprite` and `pygame.sprite.Group` patterns.
- Use `Entity.move()` and the existing hitbox collision approach for entity movement.
- Use the existing attack and attackable groups for combat integration.
- Keep animation frames loaded from the established graphics folders.

## Validation

- Run the narrowest available check for the changed code.
- The repository has no automated tests; `code/test.py` is empty.
- Do not claim that the game was launched or tested unless it was actually run.
- Report environment limitations and unverified behavior clearly.

## Documentation Map

- Repository map: `docs/project-map.md`
- Architecture: `docs/architecture/`
- Gameplay: `docs/gameplay/`
- Assets: `docs/assets/`
- Development: `docs/development/`
- Existing patterns: `docs/patterns/`
- Architecture decisions: `docs/decisions/README.md`

## Feature Workflow

Understand -> Locate -> Plan -> Implement -> Test -> Review
