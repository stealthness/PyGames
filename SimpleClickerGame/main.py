import sys

import pygame
from pygame import Vector2

from SimpleClickerGame.candy_cane_manager import CandyCaneManager

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (200, 200, 255)

pygame.init()
pygame.display.set_caption("Clicker Game")
screen = pygame.display.set_mode((500, 500))


def run():
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    candy_cane_manager = CandyCaneManager()
    pos = None
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
                pos = Vector2(event.pos[0], event.pos[1])
                print(pos)

        screen.fill(BACKGROUND_COLOR)    
        candy_cane_manager.update(screen, pos)
        pygame.display.flip()
        clock.tick(60)
        pos = None


if __name__ == "__main__":
    run()
    pygame.quit()
    sys.exit()
