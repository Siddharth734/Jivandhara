from settings import *
from timee import Timer

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__(groups)
        self.direction = player.state.split('_')[0]

        full_path = join('graphics','weapons',f"{player.weapon}",f"{self.direction}.png")
        self.image = pygame.image.load(full_path).convert_alpha()

        if self.direction == 'right':
            self.rect = self.image.get_frect(midleft = player.rect.midright + pygame.Vector2(0,16))
        elif self.direction == 'left':
            self.rect = self.image.get_frect(midright = player.rect.midleft + pygame.Vector2(0,16))
        elif self.direction == 'down':
            self.rect = self.image.get_frect(midtop = player.rect.midbottom + pygame.Vector2(-10,0))
        else:
            self.rect = self.image.get_frect(midbottom = player.rect.midtop + pygame.Vector2(-10,0))
            


