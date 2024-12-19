import sys

import pygame


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('DaFluffyPotato Tutorial')


while True:
    screen.fill((200, 200, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()