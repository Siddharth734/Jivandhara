# Setup

No requirements file, `pyproject.toml`, Poetry file, uv file, or lockfile is present.

The README documents installing Pygame with:

```text
pip install pygame
```

The observed bootstrap environment has Python 3.13.0 and Pygame-CE 2.5.2. Those are observations, not project-pinned requirements.

Because imports are flat and asset paths are relative, use the `code/` directory as the working directory when launching the game. The source imports `pytmx.util_pygame`, although the current map loading path uses CSV and no active `pytmx` API call.
