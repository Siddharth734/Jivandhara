from settings import *
from timee import Timer

class Upgrade:
    def __init__(self, player):

        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_nr = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.max_values = list(player.max_stats.values())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        #0,1 refering x,y
        self.height = self.display_surface.get_size()[1] * 0.8
        self.width = self.display_surface.get_size()[0] // 6
        self.create_items()

        #selection system
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True
        self.selection_timer = Timer(300)

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.selection_timer:
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_nr - 1:
                self.selection_index += 1
                self.selection_timer.activate()
            elif keys[pygame.K_LEFT] and self.selection_index > 0:
                self.selection_index -= 1
                self.selection_timer.activate()
            
            if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                self.selection_timer.activate()
                self.item_list[self.selection_index].trigger(self.player)

    def create_items(self):
        self.item_list = []

        for item, index in enumerate(range(self.attribute_nr)):
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.attribute_nr
            left = (item * increment) + (increment - self.width) // 2

            top = self.display_surface.get_size()[1] * 0.15

            item = Item(left, top, self.width, self.height, index, self.font)
            self.item_list.append(item)

    def display(self):
        # Fill screen with a semi-transparent overlay
        overlay = pygame.Surface(self.display_surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))  # Black with transparency
        self.display_surface.blit(overlay, (0, 0))

        font = pygame.font.Font(UI_FONT, 40)
        pause_text = font.render("- - =_UPGRADE MENU_= - -", True, (240, 240, 240))
        text_rect = pause_text.get_rect(center=(WINDOW_WIDTH / 2, 45))
        self.display_surface.blit(pause_text, text_rect)

        self.input()
        self.selection_timer.update()

        for index, item in enumerate(self.item_list):
            name = self.attribute_names[index]
            value = self.player.get_value_by_index(index)
            max_value = self.max_values[index]
            cost = self.player.get_cost_by_index(index)

            item.display(self.display_surface, self.selection_index, name, value, max_value, cost)

class Item:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.FRect(l,t,w,h)
        self.index = index
        self.font = font

    def display_names(self, surface, name, cost, selected):
        title_color = TEXT_COLOR if selected else (120, 120, 120)
        cost_color = UI_BORDER_COLOUR_ACTIVE if selected else (100, 100, 100)

        title_surf = self.font.render(name, True, title_color)
        title_rect = title_surf.get_rect(midtop=self.rect.midtop + pygame.Vector2(0, 20))

        cost_surf = self.font.render(f"Cost: {int(cost)}", True, cost_color)
        cost_rect = cost_surf.get_rect(midbottom=self.rect.midbottom - pygame.Vector2(0, 20))

        surface.blit(title_surf, title_rect)
        surface.blit(cost_surf, cost_rect)

    def display_bar(self, surface, value, max_value, selected):

        top = self.rect.midtop + pygame.Vector2(0,60)
        bottom = self.rect.midbottom - pygame.Vector2(0,60)
        color = TEXT_COLOR if selected else (120, 120, 120)

        full_height = bottom[1] - top[1] 
        ratio = (value / max_value) * full_height
        value_rect = pygame.FRect(top[0] - 15, bottom[1] - ratio, 30, 30)

        pygame.draw.line(surface, color, top, bottom,5)
        pygame.draw.rect(surface, color, value_rect)

    def trigger(self, player):
        upgrade_attribute = list(player.stats.keys())[self.index]

        if player.exp >= player.upgrade_cost[upgrade_attribute] and player.stats[upgrade_attribute] < player.max_stats[upgrade_attribute]:
            player.exp -= player.upgrade_cost[upgrade_attribute]

            player.stats[upgrade_attribute] *= 1.2
            player.upgrade_cost[upgrade_attribute] *= 1.4

        if player.stats[upgrade_attribute] > player.max_stats[upgrade_attribute]:
            player.stats[upgrade_attribute] = player.max_stats[upgrade_attribute]

    def display(self, surface, selection_num, name, value, max_value, cost):
        bg_color = (45, 45, 45) if self.index == selection_num else UI_BG_COLOR
        pygame.draw.rect(surface, bg_color, self.rect, border_radius=10)

        self.display_names(surface, name, cost, self.index == selection_num)
        self.display_bar(surface, value, max_value, self.index == selection_num)
