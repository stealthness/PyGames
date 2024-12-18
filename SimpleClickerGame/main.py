import sys

import pygame
from pygame import Vector2

from SimpleClickerGame.candy_cane_manager import CandyCaneManager





def run():
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 800
    BACKGROUND_COLOR = (200, 200, 255)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Clicker Game")
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    candy_cane_manager = CandyCaneManager()
    pos = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                SCREEN_WIDTH = event.w
                SCREEN_HEIGHT = event.h
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
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
    pygame.init()
    run()
    pygame.quit()
    sys.exit()
