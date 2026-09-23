# Planned Gameplay Features

This document records requested gameplay stages and their implementation status. The existing runtime code remains the source of truth.

## Implementation Stages

The requested gameplay changes are to be implemented one stage at a time. Stage 1 and Stage 2 are documented below. Additional stages will be added separately when provided.

## Stage 1: Character Switching and Signature Abilities

**Status: implemented.**

## Character Switching

### Planned Behavior

The player should be able to switch between three playable character variants:

- `Player`
- `PlayerAnbu`
- `PlayerFrog`

Each character should have its own signature ability.

### Switching Cooldown

- Press `C` to cycle through the available character variants.
- After the player switches characters, another character switch must be unavailable for one minute.
- The one-minute cooldown applies to switching characters, not to signature ability cooldowns.
- A switch attempt during the cooldown is rejected.

### Existing Asset Context

The repository already contains separate asset directories:

- `graphics/player/`
- `graphics/playerAnbu/`
- `graphics/playerFrog/`

The current runtime `Player` implementation loads animation frames from `graphics/playerAnbu/`. Character switching and the complete runtime use of the other player asset sets are not currently implemented.

## Signature Abilities

### Player

- Push back all surrounding enemies.
- After the pushback, slow all enemies.
- The ability should remain unavailable until its cooldown period ends.
- The signature skill must be loosely coupled to the player sprite, because the sprite is expected to change independently.

Press `V` to activate it. The current implementation affects enemies within 220 pixels, pushes them for 250 ms, slows them to 50% speed for 5 seconds, and uses a 30-second ability cooldown. The skill operates through the enemy effect interface rather than depending directly on a specific player sprite.

### PlayerAnbu

- Create smaller, greyscale copies of the `PlayerAnbu` sprite.
- The copies should attack the nearest enemy.
- Each copy should deal small damage.
- The copies should be temporary and controlled by the ability cooldown/lifetime.

Press `V` to activate it. The implementation creates four half-size greyscale Anbu clones for 8 seconds. They seek the nearest enemy and deal 3 damage every 800 ms. The ability cooldown is 30 seconds.

### PlayerFrog

- Temporarily become larger.
- Use the Frog sprite during the ability period.
- Double defense during the ability period.
- Slightly increase attack during the ability period.
- Revert to the normal character state when the cooldown/effect period ends.

Press `V` to activate it. The implementation scales the active Frog animation by 1.5, doubles incoming-defense mitigation, and adds 10% of the attack stat to weapon damage for 10 seconds. The ability cooldown is 30 seconds. The effect then restores the previous modifiers.

## Stage 2: Increased Enemy Difficulty

This stage is planned but **not implemented**.

### Planned Behavior

- Increase enemy movement speed so enemies are more threatening and harder to avoid.
- Make attacking enemies more difficult by reducing how easily the player can land repeated attacks on them.
- Enemies must not remain static while they are being attacked. They should continue moving, repositioning, or otherwise responding during incoming attacks instead of becoming stationary targets.
- Preserve enemy-specific behavior and ensure the difficulty increase applies through the existing enemy movement/combat flow rather than making enemies permanently immobile or invulnerable.

### Open Stage 2 Decisions

- Whether movement speed increases are global, per enemy type, or difficulty-dependent.
- Whether enemies evade, strafe, reposition, interrupt movement, or use another response to incoming attacks.
- Whether the response occurs on every hit, only after taking damage, or while the enemy is vulnerable.
- How enemy movement interacts with the existing knockback and vulnerability timers.
- Whether attack difficulty is adjusted through enemy speed, hitbox movement, attack timing, resistance, hit recovery, or a combination.
- How the change should remain fair for slower weapons and area attacks.

## Suggested Integration Areas

These are documentation pointers, not implementation instructions:

- Character selection and active-character state: `code/player.py` and `code/level.py`
- Ability input, cooldowns, and active effects: `code/player.py` and `code/timee.py`
- Enemy pushback, slowing, and targeting: `code/enemy.py` and `code/level.py`
- Temporary attacking copies: likely existing sprite/group patterns in `code/entity.py`, `code/enemy.py`, and `code/particles.py`
- Character animation assets: `graphics/player/`, `graphics/playerAnbu/`, and `graphics/playerFrog/`
- Ability visuals and sounds: `graphics/particles/` and `audio/`

Stage 1 uses `code/signature_abilities.py` for sprite-independent abilities, `code/player.py` for character state and input, `code/enemy.py` for temporary enemy effects, and `code/level.py` for integration callbacks. Stage 2 remains documentation-only and is not implemented.

## Open Design Decisions

Before implementation, define:

- Whether switching should be allowed during attack cooldowns, pause mode, or game over.
- Whether each character should have separate stats or share the current Player stats.
- Whether signature abilities should consume energy.
- Whether the current default ability durations and values need balancing.
Stage 2 complete: graph report finalized (communities 2-11 named, verified/inferred split, uncertainties added).
