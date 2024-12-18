import sys

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (200, 200, 255)

pygame.init()
pygame.display.set_caption("Clicker Game")
screen = pygame.display.set_mode((500, 500))


def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()
        pygame.display.update()


if __name__ == "__main__":
    run()
    pygame.quit()
    sys.exit()
