from settings import *
from debug import Debug
from support import *
from tile import Tile
from player import Player
from weapon import Weapon
from timee import Timer
from ui import UI
from enemy import Enemy

from random import randint,choice

class Level:
    def __init__(self):

        #gets display surface from anywhere in the code
        self.display_surface = pygame.display.get_surface()

        #sprite group setup
        self.visible_sprites = YSortCameraGroup(self.display_surface)
        self.obstacle_sprites = pygame.sprite.Group()

        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        self.create_map()

        self.time = 500 + weapons_data[self.player.weapon]['cooldown']
        self.kill_timer = Timer(self.time,func=self.killit)
        #self is refrenced to the level class thus self.kill failed as it should be refrenced to weapon class

        self.ui = UI()
    
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
                                    self.damage_player)

    def create_attack(self):
        if not hasattr(self, 'weapon') or self.weapon is None or not self.weapon.alive():
            self.kill_timer.activate() 
            self.weapon = Weapon(self.player, (self.visible_sprites,self.attack_sprites))

    def create_magic(self,style,strength,cost):
        print(style)
        print(strength)
        print(cost)

    #if statement is used here to check if the group is not a none and a valid group
    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False,pygame.sprite.collide_mask)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player,attack_sprite.sprite_type)#damaged by magic or by weapon

    def damage_player(self,amount,attack_type):
        if not self.player.vulnerability_timer:
            self.player.health -= amount
            self.player.vulnerability_timer.activate()

    def killit(self):
        if not hasattr(self, 'weapon') or self.weapon.alive():
            self.weapon.kill()
            self.weapon = None

    def run(self,dt):
        #weapon jerk
        if hasattr(self, 'weapon') and self.weapon:
            if self.weapon.direction == 'right' or self.weapon.direction == 'left':
                self.weapon.rect.centerx += sin(pygame.time.get_ticks()) * randint(-1,2) * dt
            if self.weapon.direction == 'down' or self.weapon.direction == 'up':
                self.weapon.rect.centery += sin(pygame.time.get_ticks()) * randint(-1,2) * dt

        self.kill_timer.update()
        self.visible_sprites.draw(self.player.rect.center)
        self.visible_sprites.enemy_update(self.player)
        self.visible_sprites.update(dt)
        self.player_attack_logic()
        self.ui.display(self.player)

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
            