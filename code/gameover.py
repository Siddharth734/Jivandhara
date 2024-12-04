from settings import *
from timee import Timer

class GAMEOVER:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

    def display(self):
        # Fill screen with a semi-transparent overlay
        overlay = pygame.Surface(self.display_surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0))  # Black with transparency
        self.display_surface.blit(overlay, (0, 0))

    def make(self,font,text,text_rect):
        self.display_surface.blit(text, text_rect)

    def update(self, dt):
        font = pygame.font.Font(UI_FONT, 75)
        text = font.render("GAME OVER", True, (240, 240, 240))
        text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        text_rect.centerx += sin(pygame.time.get_ticks()) * randint(-1,2) * dt
        text_rect.centery += sin(pygame.time.get_ticks()) * randint(-1,2) * dt

        self.make(font,text,text_rect)