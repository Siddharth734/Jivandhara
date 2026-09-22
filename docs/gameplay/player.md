# Player

`Player` is defined in `code/player.py` and extends `Entity`.

## Controls

- Arrow keys or WASD: movement.
- Space: create the selected weapon attack.
- Left Ctrl: cast the selected magic ability.
- Tab: cycle weapons.
- Q: cycle magic.
- C: cycle character variants. Switching has a 60-second cooldown.
- V: activate the current character's signature ability.
- ESC: handled by `Game` to enter/leave the upgrade mode.

## State and Stats

The player tracks direction, a directional animation state, health, energy, experience, weapon/magic selection, and stats for health, energy, attack, magic, and speed. Initial stats and limits are defined directly in `Player.__init__()`.

## Movement and Animation

Movement uses `Entity.move()` with obstacle hitboxes. Assets are loaded from the active character's `graphics/<character>/<state>/` directory. The state is changed from direction and attack cooldown; attack states append `_attack` to the facing state. Frame indices advance using `animation_speed * dt`.

## Abilities

Weapon attacks create `Weapon` sprites. Magic is delegated to `MagicPlayer`: `heal` restores health for energy, and `flame` creates flame particle effects in the facing direction. Timers control attack and selection cooldowns.

Signature abilities are provided by `code/signature_abilities.py` and selected independently from the player sprite. Player, PlayerAnbu, and PlayerFrog have separate ability implementations.
