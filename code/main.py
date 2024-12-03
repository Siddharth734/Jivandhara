import sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption('Jivandhara')
        self.clock = pygame.time.Clock()
        self.running = True

        self.level = Level()

        main_sound = pygame.mixer.Sound(join('audio','Theme.ogg'))
        # main_sound.set_volume(0.7)
        main_sound.play(-1)

    def run(self):
        dt = self.clock.tick(FPS) / 1000
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.level.toggle_menu()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()

            self.screen.fill(WATER_COLOR)
            self.level.run(dt)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
