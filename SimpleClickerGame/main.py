import sys

import pygame
from pygame import Vector2

from SimpleClickerGame.candy_cane_manager import CandyCaneManager


class Game:
    def __init__(self):
        self.DISPLAY_WIDTH = 300
        self.DISPLAY_HEIGHT = 600
        self.SCREEN_SCALE = 1
        self.BACKGROUND_COLOR = (200, 200, 255)
        self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        screen_size = (self.DISPLAY_WIDTH * self.SCREEN_SCALE, self.DISPLAY_HEIGHT * self.SCREEN_SCALE)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Clicker Game")
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.score = 0
        self.candy_cane_manager = CandyCaneManager(self.score)
        self.pos = None

    def show_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_rect = score_text.get_rect(center=(self.DISPLAY_WIDTH // 2, 100))
        self.display.blit(score_text, text_rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = Vector2(event.pos[0], event.pos[1])

            self.display.fill(self.BACKGROUND_COLOR)
            self.candy_cane_manager.update(self.display, self.pos)
            self.show_score()
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.flip()
            self.clock.tick(60)
            self.pos = None


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()