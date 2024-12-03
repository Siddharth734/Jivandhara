from settings import *
from entity import Entity
from timee import Timer

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites, damage_player, trigger_death_particles, add_exp):
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

        self.attack_timer = Timer(500)
        self.damage_player = damage_player
        self.trigger_death_particles = trigger_death_particles
        self.add_exp = add_exp

        self.attack_sound = pygame.mixer.Sound(join(*monster_info['attack_sound']))
        self.death_sound = pygame.mixer.Sound(join('audio','death.wav'))
        self.hit_sound = pygame.mixer.Sound(join('audio','hit.wav'))
        self.death_sound.set_volume(uniform(0.1,0.2))
        self.hit_sound.set_volume(uniform(0.1,0.2))
        self.attack_sound.set_volume(uniform(0.1,0.3))

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
        enemyVector = pygame.Vector2(self.rect.center)
        playerVector = pygame.Vector2(player.rect.center) 
        distance = (playerVector - enemyVector).magnitude() 
        direction = (playerVector - enemyVector).normalize() if distance else pygame.Vector2()

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
            self.damage_player(self.attack_damage, self.attack_type)
            self.attack_sound.play()
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

        if self.monster_name != 'spirit':
            if self.vulnerability_timer:
                alpha = self.wave_value()
                self.image.set_alpha(alpha)
            else:
                self.image.set_alpha(255)

        else: self.image.set_alpha(100)

    def get_damage(self,player,attack_type):
        if not self.vulnerability_timer:
            self.hit_sound.play()
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
            else:
                self.health -= player.get_full_magic_damage()
            self.vulnerability_timer.activate()

    def check_death(self):
        if self.health <= 0:
            self.kill()
            self.trigger_death_particles(self.rect.center, self.monster_name)
            self.add_exp(self.exp)
            self.death_sound.play()

    def knockback(self):
        if self.vulnerability_timer:
            self.direction *= -self.resistance

    def update(self,dt):
        self.attack_timer.update()
        self.vulnerability_timer.update()
        self.knockback()
        self.move(self.speed,dt)
        self.animate(dt)
        self.check_death()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)
        player.vulnerability_timer.update()
