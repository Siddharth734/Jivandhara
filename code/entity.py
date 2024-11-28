from settings import *
from timee import Timer

class Entity(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.05
        self.direction = pygame.Vector2()

        self.vulnerability_timer = Timer(1000)

    def move(self, speed, dt):
        self.direction = self.direction.normalize() if self.direction else self.direction
        
        self.hitbox.x += self.direction.x * speed * dt
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed * dt
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x >= 0: self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < WINDOW_WIDTH: self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y >= 0: self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.x < WINDOW_HEIGHT: self.hitbox.top = sprite.hitbox.bottom

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        return 255 if value >= 0 else 0