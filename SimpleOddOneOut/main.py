import pygame
from pygame import Color

pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.Color(0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left key pressed")
            if event.key == pygame.K_RIGHT:
                print("Right key pressed")
            if event.key == pygame.K_UP:
                print("Up key pressed")
            if event.key == pygame.K_DOWN:
                print("Down key pressed")
            if event.key == pygame.K_SPACE:
                background = (255, 255, 255)

    screen.fill(background)

    pygame.display.flip()

