import sys

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.BACKGROUND_Color = (200, 200, 250)
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('DaFluffyPotato Tutorial')
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.img = pygame.image.load('data/Art/clouds/cloud_1.png')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        pygame.init()
            self.screen.fill(self.BACKGROUND_Color)
            self.screen.blit(self.img, (100, 100))
            pygame.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
