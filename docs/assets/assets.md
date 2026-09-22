# Assets

Assets are loaded directly through relative paths with `pygame.image.load()`, `pygame.font.Font()`, or `pygame.mixer.Sound()`. Folder traversal is centralized in `support.import_folder()` for animation directories.

- `graphics/font/`: UI font. `settings.UI_FONT` points to `graphics/font/joystix.ttf`.
- `graphics/playerAnbu/`: active Player animation states.
- `graphics/player/`, `graphics/playerFrog/`: additional player asset sets present in the repository; the current Player implementation loads `playerAnbu`.
- `graphics/monsters/`: monster animation folders by type and state.
- `graphics/objects/`: map object surfaces.
- `graphics/particles/`: magic, attack, death, and grass effects.
- `graphics/weapons/`: directional weapon images and HUD graphics.
- `graphics/tilemap/`: floor surface used by the camera group.
- `audio/`: theme, game-over music, player effects, enemy effects, and attack effects.

Asset loading occurs during object construction, not through an asset manager or cache.
