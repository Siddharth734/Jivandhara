from settings import *
from timee import Timer
from entity import Entity

class   Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_attack, create_magic):
        super().__init__(groups)
        self.image = pygame.image.load(join('graphics','playerAnbu','down','down0.png')).convert_alpha()
        self.rect = self.image.get_frect(topleft = pos)
        self.hitbox = self.rect.inflate(-6,HITBOX_OFFSET['player'])

        self.import_player_assets()
        self.state = 'down'

        self.obstacle_sprites = obstacle_sprites

        self.create_attack = create_attack
        self.weapon_index = 0
        self.weapon = list(weapons_data.keys())[self.weapon_index]
        self.weapon_switch_timer = Timer(200)

        self.attack_cooldown = Timer(200 + weapons_data[self.weapon]['cooldown'])

        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.magic_switch = Timer(200)

        self.stats = {'health': 100,'energy': 60,'attack': 10,'magic': 4,'speed': 2}
        self.max_stats = {'health': 300,'energy': 180,'attack': 20,'magic': 10,'speed': 7}
        self.upgrade_cost = {'health': 50,'energy': 50,'attack': 50,'magic': 50,'speed': 50}
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.exp = 200
        self.speed = self.stats['speed']

        self.weapon_attack_sound = pygame.mixer.Sound(join('audio','sword.wav'))
        self.weapon_attack_sound.set_volume(uniform(0.1,0.4))

    def import_player_assets(self):
        self.frames = {
            'up': [],'down': [],'left': [],'right': [],
            'up_idle': [],'down_idle': [],'left_idle': [],'right_idle': [],
            'up_attack': [],'down_attack': [],'left_attack': [],'right_attack': []
            }

        for state in self.frames.keys():
            for folder_path,sub_folders,file_names in walk(join('graphics','playerAnbu',state)):
                if file_names:
                    for file_name in file_names:
                        full_path = join(folder_path, file_name)
                        frame = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(frame)

    def input(self):
        if not self.attack_cooldown.active:
            Keys = pygame.key.get_pressed()
            self.direction.x = (int(Keys[pygame.K_RIGHT]) or int(Keys[pygame.K_d])) - (int(Keys[pygame.K_LEFT]) or int(Keys[pygame.K_a]))
            self.direction.y = (int(Keys[pygame.K_DOWN]) or int(Keys[pygame.K_s])) - (int(Keys[pygame.K_UP]) or int(Keys[pygame.K_w]))

            recent_keys = pygame.key.get_just_pressed()
            if recent_keys [pygame.K_SPACE]:
                self.attack_cooldown.activate()
                self.create_attack()
                self.weapon_attack_sound.play()

            if recent_keys[pygame.K_LCTRL]: 
                self.attack_cooldown.activate()
                style = self.magic
                strength = magic_data[self.magic]['strength'] + self.stats['magic']
                cost = magic_data[self.magic]['cost']
                self.create_magic(style, strength, cost)

            if recent_keys[pygame.K_TAB] and not self.weapon_switch_timer:
                self.weapon_switch_timer.activate()
                self.weapon_index += 1
                self.weapon_index *= 0 if self.weapon_index > len(list(weapons_data.keys()))-1 else 1
                self.weapon = list(weapons_data.keys())[self.weapon_index]

            if recent_keys[pygame.K_q]  and not self.magic_switch:
                self.magic_switch.activate()
                self.magic_index += 1
                self.magic_index *= 0 if self.magic_index > len(list(magic_data.keys()))-1 else 1
                self.magic = list(magic_data.keys())[self.magic_index]

    def animate(self, dt):
        # Update movement state based on direction
        if not self.attack_cooldown:
            if self.direction.x != 0:
                self.state = 'right' if self.direction.x > 0 else 'left'
            if self.direction.y != 0:
                self.state = 'down' if self.direction.y > 0 else 'up'
        
        # Handle attack animation state
        if self.attack_cooldown.active:
            # Lock movement during attack
            self.direction.x, self.direction.y = 0, 0
            if '_attack' not in self.state:
                self.state = self.state + '_attack'
        else:
            self.state = self.state.replace('_attack', '')
        
        self.frame_index %= len(self.frames[self.state])  # Loop within frame bounds

        self.frame_index += self.animation_speed * dt
        self.frame_index *= 0 if not self.direction.x and not self.direction.y else 1
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]# Update current image
        self.rect = self.image.get_frect(center = self.hitbox.center)

        if self.vulnerability_timer:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def get_full_weapon_damage(self):
        base_damage = self.stats['attack']
        weapon_damage = weapons_data[self.weapon]['damage']
        return base_damage + weapon_damage
    
    def get_full_magic_damage(self):
        base_damage = self.stats['magic']
        spell_damage = magic_data[self.magic]['strength']
        return base_damage + spell_damage

    def get_value_by_index(self, index):
        return list(self.stats.values())[index]

    def get_cost_by_index(self, index):
        return list(self.upgrade_cost.values())[index]

    def energy_recovery(self,dt):
        if self.energy < self.stats['energy']:
            self.energy += 0.009 * self.stats['magic'] * dt 
        else:
            self.energy = self.stats['energy']

    def update(self, dt):
        self.attack_cooldown.update()
        self.weapon_switch_timer.update()
        self.magic_switch.update()
        self.input() 
        self.move(self.stats['speed'], dt)
        self.animate(dt)
        self.energy_recovery(dt)