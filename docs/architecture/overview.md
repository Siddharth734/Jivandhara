# Architecture Overview

Jivandhara is a small object-oriented Pygame game. `Game` owns the application window and outer loop. `Level` owns the active world, sprite groups, map instantiation, gameplay coordination, and high-level modes. `Player`, `Enemy`, `Tile`, `Weapon`, and `ParticleEffect` are Pygame sprites or sprite subclasses.

The implementation is coordinator-based rather than scene-framework-based. `Level.run()` selects normal gameplay, upgrade/pause rendering, or game-over rendering. Shared entity movement lives in `Entity`; content values live in dictionaries in `settings.py`; CSV files determine map placement.

## Main Relationships

```text
Game
  -> Level
      -> map CSV loaders and Tile/Player/Enemy creation
      -> sprite groups and YSortCameraGroup
      -> Player, Enemy, Weapon, MagicPlayer, UI, Upgrade, GAMEOVER
      -> combat callbacks and particle effects
```

Rendering uses a camera-aware custom group. World sprites are drawn after a floor surface and sorted by `rect.centery`. UI is drawn separately in screen coordinates.

The game has no package structure, dependency lockfile, formal scene base class, audio manager, or automated test suite.
