import sys

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Clicker Game")
    screen = pygame.display.set_mode((500, 500))
    run()
    pygame.quit()
    sys.exit()
