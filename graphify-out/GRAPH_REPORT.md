# Graph Report - PROJECT J  (2026-09-23)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 162 nodes · 329 edges · 12 communities (4 shown, 8 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 20 edges (avg confidence: 0.95)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `48633efb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10

## God Nodes (most connected - your core abstractions)
1. `Timer` - 39 edges
2. `Level` - 28 edges
3. `Enemy` - 26 edges
4. `Player` - 19 edges
5. `Entity` - 12 edges
6. `SignatureAbility` - 11 edges
7. `UI` - 11 edges
8. `Upgrade` - 9 edges
9. `AnimationPlayer` - 8 edges
10. `GAMEOVER` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Enemy` --uses--> `Timer`  [INFERRED]
  code/enemy.py → code/timee.py
- `Level` --uses--> `Timer`  [INFERRED]
  code/level.py → code/timee.py
- `Player` --uses--> `Timer`  [INFERRED]
  code/player.py → code/timee.py
- `AnbuClone` --uses--> `Timer`  [INFERRED]
  code/signature_abilities.py → code/timee.py
- `AnbuSignatureAbility` --uses--> `Timer`  [INFERRED]
  code/signature_abilities.py → code/timee.py


## Verified Enemy + Collision System Interaction (source-backed)
- Base movement / hitbox: `code/entity.py` L4 (Entity sprite), L13 (move), L25-33 (colliderect + push resolution).
- Enemy-specific separation: `code/enemy.py` L152 `separate_from_player()` uses rect overlap calc, pushes `hitbox.center`, syncs `rect`, and sets `self.direction`.
- Called in game loop: `enemy_update()` L264 calls `separate_from_player(player)` AFTER `actions(player)`.
- Pushback / knockback: `apply_pushback()` L221 sets `pushback_timer` (Timer/250) + `pushback_speed`; `knockback()` L240 inverts direction via `resistance` during `vulnerability_timer`; `update()` L255 selects `movement_speed = pushback_speed or contact_push_speed or (speed * speed_multiplier)`.
- Verified vs source (entity.py + enemy.py), not graph inference. Confirmed: Enemy uses Entity.move(), uses hitbox-based collision, integrates Timer/Timer for pushback/slows, and interacts with Player directly via rect/separate_from_player.
## Import Cycles
- None detected.

## Communities (12 total, 8 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.16
Nodes (10): Debug(), Entity, create_signature_ability(), Timer, math, os, os_path, pygame (+2 more)

### Community 1 - "Community 1"
Cohesion: 0.11
Nodes (6): AnbuClone, AnbuSignatureAbility, BefriendSignatureAbility, FrogSignatureAbility, PlayerSignatureAbility, SignatureAbility

### Community 2 - "Enemy core mechanics" (21 nodes, e.g. code_enemy_...)
Source-backed: enemy.py entities; verified collision/attack methods in code/enemy.py.
Note: bridged by Timer/Level; 26 reported edges unverified (no edges array; links=329).

### Community 3 - "Level / Game / Weapon" (20 nodes, e.g. code_level_level, code_main_game, code_weapon_weapon)
Source-backed: level.py, main game loop, weapon.
Note: cohesion 0.12; 11 inferred Level edges need verification.

### Community 4 - "Animation / Camera / Particles" (20 nodes, e.g. YSortCameraGroup, AnimationPlayer, ParticleEffect)
Source-backed: level/particle modules.
Note: overlaps Community 10 thin edges; not architecturally separate.

### Community 5 - "Player" (14 nodes, e.g. code_player_...)
Source-backed: player.py; verified sign-start/end mechanics.
Note: 2 inferred Player edges unverified.

### Community 6 - "Upgrade / progression" (11 nodes, e.g. code_upgrade_...)
Source-backed: upgrade/item modules.
Note: bridged by Level; high-centrality Upgrade node (9 edges in report, unverified).

### Community 7 - "UI / HUD" (9 nodes, e.g. code_ui_...)
Source-backed: ui.py; cross-bridged by Level.

### Community 8 - "Gameover / state" (5 nodes, e.g. code_gameover_...)
Source-backed: gameover state; thin; bridged by Level/ui.

### Community 9 - "Magic / MagicPlayer" (5 nodes, e.g. code_magic_magicplayer...)
Source-backed: magic modules.

### Community 10 - "Tile / map data" (3 nodes, e.g. code_tile_...)
Source-backed: tile/init; thin; edges to Community 4/Level unverified.

### Community 11 - "Test" (1 node: code_test)
Source-backed: test module; isolated; omitted from key relationships.

## Verified Relationships (from graph.json links, confidence=EXTRACTED / score=1.0)
- `code/enemy.py` L138: `code_enemy_enemy_actions` -> `code_enemy_enemy_attack_player` (`calls`)
- `code/entity.py`: `entity_collision` used by entity/init/move; verified by source inspection
- `code/level.py`: `Timer` / `Level` bridge used for stage/activation (link-present, source-backed; exact line not extracted in this pass)
- `code/player.py`: `signature_ability` start/end links verified by abilities module

## Inferred / Unverified Relationships (from node betweenness / community overlap; no direct link or source trace confirmed)
- Timer 10 edges to Enemy / Player / Level (inferred from cross-community betweenness; not traced to exact source lines)
- Level 11 edges (inferred; `links` present but not individually inspected for all 11)
- Enemy 2, Player 2 (inferred; based on reported edges, not all mapped to `links` entries)
- Upgrade 9 edges (high centrality; some links exist, full mapping not verified)
- Community 10 (Tile) -> Community 4 (Animation/Camera) edges (inter-community overlap, thin; unconfirmed)

### Uncertainties / Verification Gaps
- No `edges` array in graph.json; `links` count = 329 used as proxy, not verified.
- Inferred relationships: Timer 10, Level 11, Enemy 2, Player 2 — marked INFERRED in report; not confirmed by source traces (entity.py collision, enemy.py actions, timer usage in level/player).

## Knowledge Gaps
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.


### Thin Communities Named (<3 nodes, from graph + source mapping)
- Community 5: Audio / FX (particles, sounds � linked to Enemy trigger_death_particles / death_sound)
- Community 6: UI / HUD (UI node, GAMEOVER state � cross-bridged by Level)
- Community 7: Map / CSV import (import_csv_layout, import_folder, map data � bridged by Level)
- Community 8: Signature abilities sub-modules (PlayerSignatureAbility, etc. � Community 1 adjacent)
- Community 9: Upgrade / progression (Upgrade node � 9 edges, high centrality)
- Community 10: Animation / Camera (AnimationPlayer / YSortCameraGroup � already shown as Community 4 core, thin edges to 10)
- Community 2: Enemy core mechanics (Enemy, Weapon, Game � 26 edges, but thin node count isolated from base entities; bridged by Level/Timer)
- Note: 8 thin communities previously omitted; named here by mapping graph node labels to code folders.
## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Timer` connect `Community 0` to `Community 1`, `Community 2`, `Community 3`, `Community 4`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.350) - this node is a cross-community bridge._
- **Why does `Level` connect `Community 3` to `Community 0`, `Community 2`, `Community 4`, `Community 5`, `Community 6`, `Community 7`, `Community 8`, `Community 9`, `Community 10`?**
  _High betweenness centrality (0.251) - this node is a cross-community bridge._
- **Why does `Enemy` connect `Community 2` to `Community 0`, `Community 3`, `Community 4`?**
  _High betweenness centrality (0.184) - this node is a cross-community bridge._
- **Are the 10 inferred relationships involving `Timer` (e.g. with `Enemy` and `Entity`) actually correct?**
  _`Timer` has 10 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `Level` (e.g. with `Enemy` and `GAMEOVER`) actually correct?**
  _`Level` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Enemy` (e.g. with `Timer` and `Level`) actually correct?**
  _`Enemy` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Player` (e.g. with `Level` and `Timer`) actually correct?**
  _`Player` has 2 INFERRED edges - model-reasoned connections that need verification._