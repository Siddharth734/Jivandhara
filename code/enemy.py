from settings import *
from entity import Entity

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.sprite_type = 'enemy'

        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = self.frames[self.status][self.frame_index]
        # self.image = pygame.Surface((64,64))

        self.rect = self.image.get_frect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstacle_sprites = obstacle_sprites

        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.notice_radius = monster_info['notice_radius']
        self.attack_radius = monster_info['attack_radius']
        self.attack_type = monster_info['attack_type']

    def import_graphics(self, name):
        self.frames = {'idle':[],'move':[],'attack':[]}

        for state in self.frames.keys():
            for folder_path,sub_folder,file_names in walk(join('graphics','monsters',name,state)):
                if file_names:
                    for file_name in file_names:
                        full_path = join(folder_path,file_name)
                        frame = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(frame)

    def get_player_distance_direction(self, player):
        V_enemy = pygame.Vector2(self.rect.center)
        V_player = pygame.Vector2(player.rect.center) 
        distance = (V_player - V_enemy).magnitude()
        direction = (V_player - V_enemy).normalize() if distance else pygame.Vector2()

        return(distance,direction)

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius:
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def update(self,dt):
        self.move(self.speed,dt)

    def enemy_update(self, player):
        self.get_status(player)