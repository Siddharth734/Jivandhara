# Testing

No automated tests are present. `code/test.py` is empty, and no pytest/unittest configuration or test dependency was found.

Available verification is manual:

1. Start the game using the documented command from `code/`.
2. Verify window creation and event handling.
3. Exercise movement, attacks, magic, pause/upgrades, enemy damage, and game-over behavior.
4. Watch for missing relative asset paths and audio initialization failures.

Do not report a test as passed unless it was actually run in the current environment.
