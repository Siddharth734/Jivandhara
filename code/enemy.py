from settings import *
from entity import Entity
from timee import Timer

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

        self.attack_timer = Timer(400)

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

        if self.status == "attack" and self.frame_index < len(self.frames["attack"]) - 1:
            return

        if distance <= self.attack_radius and not self.attack_timer:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    #attacks, follows, and stops following according to the radius detection
    def actions(self,player):
        if self.status == 'attack':
            print('attack')
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.Vector2()

    def animate(self,dt):
        animation = self.frames[self.status]
        self.frame_index += self.animation_speed * dt

        if self.frame_index >= len(animation) and self.status == "attack":
            self.frame_index = 0
        self.image = animation[int(self.frame_index) % len(self.frames[self.status])]
        self.rect = self.image.get_frect(center = self.hitbox.center)

        if self.status == "attack" and not self.attack_timer:
            self.attack_timer.activate()

    # def animate(self, dt):
    #     self.frame_index += self.animation_speed * dt

    #     # Get the current animation frames
    #     animation_frames = self.frames[self.status]

    #     # If the attack animation finishes, allow a transition
    #     if self.status == "attack" and self.frame_index >= len(animation_frames):
    #         self.frame_index = 0  # Reset the animation
    #         if not self.attack_timer.active:  # Only transition when the timer is inactive
    #             self.status = "idle"

    #     # Update the current image
    #     self.image = animation_frames[int(self.frame_index) % len(animation_frames)]
        
    #     # Align the rect with the updated image
    #     self.rect = self.image.get_rect(center=self.hitbox.center)

    #     # Ensure the attack timer activates if the status is 'attack'
    #     if self.status == "attack" and not self.attack_timer.active:
    #         self.attack_timer.activate()


    def update(self,dt):
        self.attack_timer.update()
        self.move(self.speed,dt)
        self.animate(dt)

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)