import sys

import pygame

class Game:
    """
    Main game class
    """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Shooter")
        self.clock = pygame.time.Clock()
        self.running = True
        self.keys = [False, False, False, False]

    def run(self):
        self.running = True
        while self.running:
            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.keys[0] = True
                if event.key == pygame.K_RIGHT:
                    self.keys[1] = True
                if event.key == pygame.K_UP:
                    self.keys[2] = True
                if event.key == pygame.K_DOWN:
                    self.keys[3] = True

if __name__ == "__main__":
    game = Game()
    game.run()
    sys.exit()