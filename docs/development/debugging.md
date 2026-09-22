# Debugging

`code/debug.py` exposes `Debug(info, y=10, x=10)`, which renders text onto the current display surface using a default Pygame font. It is the only dedicated runtime debug helper found.

For a reported bug, reproduce it, identify the owning path (`Game`, `Level`, `Entity`, `Player`, `Enemy`, or a helper), trace the relevant sprite group and callback, make a minimal change, and manually verify the affected behavior.

Common repository-specific failure points are relative working-directory errors, missing asset filenames, absent animation frames, incorrect CSV IDs, mixer initialization/audio files, and assumptions that all map CSV files are loaded. Remember that `dt` is currently calculated once before the main loop, while timers use `pygame.time.get_ticks()`.
