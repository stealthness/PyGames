import sys
import pygame


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('DaFluffyPotato Tutorial')
clock = pygame.time.Clock()
FPS = 60
BACKGROUND_COLOR = (200, 200, 250)

while True:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                pygame.init()

    pygame.display.flip()
    clock.tick(FPS)
