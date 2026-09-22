from settings import *
from math import pi
from timee import Timer
from entity import Entity


class SignatureAbility:
    cooldown_duration = 30000

    def __init__(self, player, get_enemies, visible_sprites):
        self.player = player
        self.get_enemies = get_enemies
        self.visible_sprites = visible_sprites
        self.cooldown = Timer(self.cooldown_duration)
        self.active_timer = Timer(1)

    @property
    def active(self):
        return bool(self.active_timer)

    def activate(self):
        if self.cooldown or self.active:
            return False
        self.cooldown.activate()
        return True

    def update(self):
        self.cooldown.update()
        self.active_timer.update()

    def cancel(self):
        self.active_timer.deactivate()


class PlayerSignatureAbility(SignatureAbility):
    cooldown_duration = 30000
    radius = 220
    pushback_strength = 8
    slow_duration = 5000

    def activate(self):
        if not super().activate():
            return False

        player_position = pygame.Vector2(self.player.rect.center)
        for enemy in self.get_enemies():
            enemy_position = pygame.Vector2(enemy.rect.center)
            offset = enemy_position - player_position
            if offset.length() <= self.radius:
                direction = offset.normalize() if offset else pygame.Vector2(1, 0)
                enemy.apply_pushback(direction, self.pushback_strength)
                enemy.apply_slow(self.slow_duration, 0.5)
        return True


class AnbuClone(Entity):
    def __init__(self, player, get_enemies, groups, image, lifetime=8000):
        super().__init__(groups)
        self.sprite_type = 'ally'
        self.player = player
        self.get_enemies = get_enemies
        self.image = image
        self.rect = self.image.get_frect(center=player.rect.center)
        self.hitbox = self.rect.inflate(-4, -4)
        self.attack_timer = Timer(800)
        self.lifetime = Timer(lifetime, func=self.kill)
        self.speed = 4
        self.damage = 3
        self.obstacle_sprites = player.obstacle_sprites

    def nearest_enemy(self):
        enemies = [enemy for enemy in self.get_enemies() if enemy.alive()]
        clone_position = pygame.Vector2(self.rect.center)
        return min(enemies, key=lambda enemy: clone_position.distance_to(enemy.rect.center), default=None)

    def update(self, dt):
        self.lifetime.update()
        self.attack_timer.update()
        if not self.alive() or self.player.character_name != 'playerAnbu':
            self.kill()
            return

        target = self.nearest_enemy()
        if target is None:
            self.direction = pygame.Vector2()
            return

        target_offset = pygame.Vector2(target.rect.center) - pygame.Vector2(self.rect.center)
        if target_offset.length() <= 42:
            self.direction = pygame.Vector2()
            if not self.attack_timer:
                target.apply_signature_damage(self.damage)
                self.attack_timer.activate()
        else:
            self.direction = target_offset.normalize()
            self.move(self.speed, dt)


class AnbuSignatureAbility(SignatureAbility):
    cooldown_duration = 30000
    clone_count = 4
    duration = 8000

    def __init__(self, player, get_enemies, visible_sprites):
        super().__init__(player, get_enemies, visible_sprites)
        self.clones = []

    def cancel(self):
        super().cancel()
        for clone in self.clones:
            clone.kill()
        self.clones.clear()

    def activate(self):
        if not super().activate():
            return False

        self.active_timer = Timer(self.duration)
        clone_image = pygame.transform.grayscale(self.player.image.copy())
        clone_size = (max(1, clone_image.get_width() // 2), max(1, clone_image.get_height() // 2))
        clone_image = pygame.transform.smoothscale(clone_image, clone_size)
        for index in range(self.clone_count):
            angle = index * (2 * pi / self.clone_count)
            clone = AnbuClone(self.player, self.get_enemies, self.visible_sprites, clone_image.copy(), self.duration)
            clone.rect.center = self.player.rect.center + pygame.Vector2(48, 0).rotate(-angle)
            clone.hitbox.center = clone.rect.center
            self.clones.append(clone)
        return True


class FrogSignatureAbility(SignatureAbility):
    cooldown_duration = 30000
    duration = 10000

    def cancel(self):
        if self.active:
            self.player.end_frog_signature()
        super().cancel()

    def activate(self):
        if not super().activate():
            return False

        self.active_timer = Timer(self.duration, func=self.finish)
        self.player.begin_frog_signature(self.duration)
        return True

    def finish(self):
        self.player.end_frog_signature()


def create_signature_ability(character, player, get_enemies, visible_sprites):
    abilities = {
        'player': PlayerSignatureAbility,
        'playerAnbu': AnbuSignatureAbility,
        'playerFrog': FrogSignatureAbility,
    }
    return abilities[character](player, get_enemies, visible_sprites)