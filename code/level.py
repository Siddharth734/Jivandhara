from settings import *
from debug import Debug
from support import *
from tile import Tile
from player import Player
from weapon import Weapon
from timee import Timer
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade
from gameover import GAMEOVER

class Level:
    def __init__(self):

        #gets display surface from anywhere in the code
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False
        self.delay = 0

        self.main_sound = pygame.mixer.Sound(join('audio','Theme.ogg')) 

        #sprite group setup
        self.visible_sprites = YSortCameraGroup(self.display_surface)
        self.obstacle_sprites = pygame.sprite.Group()

        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        self.create_map()

        self.time = 200 + weapons_data[self.player.weapon]['cooldown']
        self.kill_timer = Timer(self.time,func=self.killit)
        #self is refrenced to the level class thus self.kill failed as it should be refrenced to weapon class

        self.ui = UI()
        self.upgrade = Upgrade(self.player)
        self.gameover = GAMEOVER()

        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout(join('map','map_FloorBlocks.csv')),
            'grass': import_csv_layout(join('map','map_Grass.csv')),
            'object': import_csv_layout(join('map','map_Objects.csv')),
            'entities': import_csv_layout(join('map','map_Entities.csv'))
        }
        graphics = {
            'grass': import_folder('graphics','Grass'),
            'objects': import_folder('graphics','Objects')
        }

        for style, layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index,col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y), self.obstacle_sprites, 'invisible')
                        if style == 'grass':
                            random_glass_surf = graphics['grass'][randint(0,2)]
                            #choice(graphics['grass']) can also be used
                            Tile(
                                (x,y),
                                (self.visible_sprites, self.obstacle_sprites,self.attackable_sprites),
                                'grass', random_glass_surf)
                            
                        if style == 'object':
                            #col gives the index/tells specifically where to place the surface according to the tiled map
                            objects_surf = graphics['objects'][int(col)]
                            Tile((x,y), (self.visible_sprites, self.obstacle_sprites), 'objects', objects_surf)

                        if style == 'entities':
                            if col == '394':
                                self.player = Player(
                                    (x,y),
                                    self.visible_sprites, 
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.create_magic)
                            else:
                                if col == '390': monster_name = 'bamboo'
                                elif col == '391': monster_name = 'spirit'
                                elif col == '392': monster_name = 'raccoon'
                                else: monster_name = 'squid' 
                                Enemy(
                                    monster_name,
                                    (x,y),
                                    (self.visible_sprites,self.attackable_sprites),
                                    self.obstacle_sprites,
                                    self.damage_player,
                                    self.trigger_death_particles,
                                    self.add_exp)

    def create_attack(self):
        if not hasattr(self, 'weapon') or self.weapon is None or not self.weapon.alive():
            self.kill_timer.activate() 
            self.weapon = Weapon(self.player, (self.visible_sprites,self.attack_sprites))

    def create_magic(self,style,strength,cost):
        if style == 'heal':
            self.magic_player.heal(self.player, strength, cost, self.visible_sprites)
        if style == 'flame':
            self.magic_player.flame(self.player, strength, cost, (self.visible_sprites, self.attack_sprites))

    #if statement is used here to check if the group is not a none and a valid group
    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False,pygame.sprite.collide_mask)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            pos = target_sprite.rect.center
                            offset = pygame.Vector2(0,75)
                            for leaf in range(randint(3,6)):   
                                self.animation_player.create_grass_particles(pos - offset, self.visible_sprites)
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player,attack_sprite.sprite_type)#damaged by magic or by weapon

    def damage_player(self,amount,attack_type):
        if not self.player.vulnerability_timer:
            self.player.health -= amount
            self.player.vulnerability_timer.activate()
            self.animation_player.create_particles(attack_type, self.player.rect.center, self.visible_sprites)

    def killit(self):
        if not hasattr(self, 'weapon') or self.weapon.alive():
            self.weapon.kill()
            self.weapon = None

    def trigger_death_particles(self,pos,particle_type):
        self.animation_player.create_particles(particle_type, pos, self.visible_sprites)

    def add_exp(self, amount):
        self.player.exp += amount

    def toggle_menu(self):
        self.game_paused = not self.game_paused

    def run(self,dt):
        if self.player and self.player.health<= 1:
            if self.delay == 0:
                self.delay += 1
                pygame.time.delay(1000)
                self.main_sound.stop()
                self.main_sound = pygame.mixer.Sound(join('audio', 'rick.wav'))
                self.main_sound.play()
            self.gameover.display()
            self.gameover.update(dt)

        else:
            if self.game_paused:
                self.upgrade.display()
            else:
                self.kill_timer.update()
                self.visible_sprites.enemy_update(self.player)
                self.visible_sprites.update(dt)

            #weapon jerk
            if hasattr(self, 'weapon') and self.weapon:
                if self.weapon.direction == 'right' or self.weapon.direction == 'left':
                    self.weapon.rect.centerx += sin(pygame.time.get_ticks()) * randint(-1,2) * dt
                if self.weapon.direction == 'down' or self.weapon.direction == 'up':
                    self.weapon.rect.centery += sin(pygame.time.get_ticks()) * randint(-1,2) * dt

            self.visible_sprites.draw(self.player.rect.center)
            self.ui.display(self.player)
            self.player_attack_logic()

            if self.game_paused:
                self.upgrade.display()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, display_surface):
        super().__init__()
        self.display_surface = display_surface
        self.offset = pygame.Vector2()

        self.floor_surf = pygame.image.load(join('graphics','tilemap','ground.png')).convert()
        self.floor_rect = self.floor_surf.get_frect(topleft = (0,0))

    def draw(self, target_pos):
        self.offset.x = -target_pos[0] + WINDOW_WIDTH/2
        self.offset.y = -target_pos[1] + WINDOW_HEIGHT/2

        self.floor_offset = self.floor_rect.topleft + self.offset
        self.display_surface.blit(self.floor_surf,self.floor_offset)
        #self is a group that is not iterable, whereas 
        #self.sprites() is a list of sprites that group contains that is iterable
        for sprite in sorted(self.sprites(), key = lambda sp: sp.rect.centery):
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
            