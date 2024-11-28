from settings import *

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

        self.health_bar_rect = pygame.FRect(10,7,HEALTH_BAR_WIDTH,BAR_HEIGHT)
        self.energy_bar_rect = pygame.FRect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)

        #weapon['graphic'] passes arguments in join as a tuple thus, the tuple is unpacked 
        self.weapon_graphics = []
        for weapon in weapons_data.values():
            path = join(*weapon['graphic'])
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        self.magic_graphics = []
        for magic in magic_data.values():
            path = join(*magic['graphic'])
            magic = pygame.image.load(path).convert_alpha()
            self.magic_graphics.append(magic)

    def show_bar(self,current,max_amount,bg_rect,color):
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect,0,5)

        health_ratio = current / max_amount
        current_rect = bg_rect.copy()
        current_rect.width = bg_rect.width * health_ratio

        if current > 0: pygame.draw.rect(self.display_surface,color,current_rect,0,5)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOUR,bg_rect,3,5)

    #str(int(exp)) first converting exp to integer to avoid large float values then converting it into a string
    def show_exp(self,exp):
        text_surf = self.font.render(str(int(exp)),False,TEXT_COLOR)
        text_rect = text_surf.get_frect(center = (self.display_surface.get_width() - 50, self.display_surface.get_height() - 30))

        pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20),0,5)
        self.display_surface.blit(text_surf,text_rect)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOUR,text_rect.inflate(20,20),3,5)

    def selection_box(self, left, top, switch_timer=False):
        bg_rect = pygame.FRect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)

        if not switch_timer:
            pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
        else:
            pygame.draw.rect(self.display_surface,UI_BORDER_COLOUR_ACTIVE,bg_rect)

        pygame.draw.rect(self.display_surface,UI_BORDER_COLOUR,bg_rect,3)

        # pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
        # if not switch_timer: 
        #     pygame.draw.rect(self.display_surface,UI_BORDER_COLOUR,bg_rect,3)
        # else : 
        #     pygame.draw.rect(self.display_surface,UI_BORDER_COLOUR_ACTIVE,bg_rect,3)

        return bg_rect

    def weapon_overlay(self, weapon_index, weapon_switch_timer):
        bg_rect = self.selection_box(10,630,weapon_switch_timer)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_frect(center = bg_rect.center)

        self.display_surface.blit(weapon_surf,weapon_rect)

    def magic_overlay(self, magic_index, magic_switch):
        bg_rect = self.selection_box(80,635,magic_switch)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_frect(center = bg_rect.center)

        self.display_surface.blit(magic_surf,magic_rect)

    def display(self,player):
        self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)
        self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,ENERGY_COLOR)

        self.show_exp(player.exp)

        self.weapon_overlay(player.weapon_index,player.weapon_switch_timer)
        self.magic_overlay(player.magic_index, player.magic_switch)