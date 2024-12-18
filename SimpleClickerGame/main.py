import sys

import pygame

from SimpleClickerGame.candy_cane_manager import CandyCaneManager

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (200, 200, 255)

pygame.init()
pygame.display.set_caption("Clicker Game")
screen = pygame.display.set_mode((500, 500))


def run():
    
    candy_cane_manager = CandyCaneManager()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        candy_cane_manager.update()
        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()
        pygame.display.update()


if __name__ == "__main__":
    run()
    pygame.quit()
    sys.exit()
