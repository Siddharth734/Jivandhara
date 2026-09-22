# Pygame Patterns

## Sprite Construction

Existing example: `Tile`, `Player`, `Enemy`, `Weapon`, and `ParticleEffect` call `super().__init__(groups)`, assign an image, and assign a Pygame rect/hitbox.

Reuse when creating world or effect objects. Keep group membership explicit at construction time.

## Group Responsibilities

Existing example: `Level` maintains separate visible, obstacle, attack, and attackable groups. Reuse the appropriate group rather than scanning every sprite for every behavior.

## Camera Drawing

Existing example: `YSortCameraGroup.draw(target_pos)` computes an offset, draws the floor, sorts sprites by `rect.centery`, and blits each sprite with the offset.

## Frame Effects

Existing example: `AnimationPlayer` loads frame lists and `ParticleEffect` kills itself after the final frame. Reuse this for finite visual effects.
