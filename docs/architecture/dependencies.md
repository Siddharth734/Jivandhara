# Dependencies and Runtime Assumptions

The repository has no dependency manifest or lockfile. `README.md` documents `pip install pygame`. The active environment observed during bootstrap reported Python 3.13.0 and Pygame-CE 2.5.2.

Runtime imports include:

- `pygame`
- Python standard-library modules: `sys`, `os.walk`, `os.path`, `math`, `random`, and `csv`
- `pytmx.util_pygame.load_pygame` is imported in `settings.py` but is not used by the current map loader.

The game expects its working directory to make `code/` imports and relative `graphics/`, `audio/`, and `map/` paths resolve. The README's launch command is `python main.py`, implying execution from `code/`.

Do not infer a supported Python or Pygame version from the source beyond the observed environment; no project file pins versions.
