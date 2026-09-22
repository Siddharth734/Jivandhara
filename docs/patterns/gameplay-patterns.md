# Gameplay Patterns

## New Enemy Variant

Pattern -> add a monster entry in `settings.monster_data` -> ensure matching animation and attack asset folders exist -> map an entity CSV ID in `Level.create_map()` if needed -> reuse `Enemy` AI and callbacks.

## New Player Ability

Pattern -> add configuration in `settings.py` when values are data-driven -> implement the behavior in `MagicPlayer` or a matching existing gameplay class -> create sprites/effects through Level groups -> integrate selection/cost/cooldown through Player.

## Damage

Pattern -> check the target vulnerability timer -> reduce health -> activate vulnerability -> create an effect -> let the owning class handle death. Preserve the existing split between `Level.damage_player()` and `Enemy.get_damage()`.

## Mode Changes

Pattern -> use `Level.game_paused` and `Level.run()` branches for the current upgrade mode, and the health condition for game over. There is no scene registry to extend.
