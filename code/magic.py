from settings import *

class MagicPlayer:
    def __init__(self,animation_player):
        self.animation_player = animation_player
        self.sounds = {
            'heal': pygame.mixer.Sound(join('audio','heal.wav')),
            'flame': pygame.mixer.Sound(join('audio','fire.wav'))
        }

    def heal(self, player, strength, cost, groups):
        if player.energy >= cost and player.health < player.stats['health']:
            self.sounds['heal'].play()
            player.health += strength 
            player.energy -= cost
            if player.health > player.stats['health']: 
                player.health = player.stats['health']
            self.animation_player.create_particles('heal', player.rect.center + pygame.Vector2(0,-30), groups)
            self.animation_player.create_particles('aura', player.rect.center, groups)

    def flame(self, player, strength, cost, groups):
        if player.energy >= cost:
            self.sounds['flame'].play()
            player.energy -= cost

            player_direction = player.state.split('_')[0]
            if player_direction == 'right': direction = pygame.Vector2(1,0)
            elif player_direction == 'left': direction = pygame.Vector2(-1,0)
            elif player_direction == 'down': direction = pygame.Vector2(0,1)
            else: direction = pygame.Vector2(0,-1)
            
            for i in range(1,6): #starting with 1 cuz 64 se multiply karke tile_size bhi fix karna hai
                if direction.x:
                    x_offset = direction.x * i * TILESIZE
                    x = player.rect.centerx + x_offset + randint(-TILESIZE//3, TILESIZE//3)
                    y = player.rect.centery + randint(-TILESIZE//3, TILESIZE//3)
                    self.animation_player.create_particles('flame', (x,y), groups)
                if direction.y:
                    y_offset = direction.y * i * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE//3, TILESIZE//3)
                    y = player.rect.centery + y_offset + randint(-TILESIZE//3, TILESIZE//3)
                    self.animation_player.create_particles('flame', (x,y), groups)