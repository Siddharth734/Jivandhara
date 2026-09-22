# Code Patterns

## Data-Driven Content

Pattern -> `monster_data`, `weapons_data`, and `magic_data` in `code/settings.py` -> runtime classes read values by content name -> reuse when adding a configured content variant -> do not duplicate constants across gameplay classes.

## Callback-Based Coordination

Pattern -> `Level` passes `create_attack`, `create_magic`, `damage_player`, `trigger_death_particles`, and `add_exp` into sprites -> sprites request world actions without owning the whole level -> reuse for behavior that needs Level coordination -> do not create a second global coordinator.

## Shared Entity Base

Pattern -> `Entity` owns direction, timers, movement, collision, and common animation fields -> `Player` and `Enemy` specialize input/AI and content behavior -> reuse `Entity` for actors with the same movement model -> do not bypass its hitbox/rect synchronization without understanding the collision path.
