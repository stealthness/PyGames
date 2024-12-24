import pygame


class Ball:
    pass


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("(Copilot) Pong")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.score = 0

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
