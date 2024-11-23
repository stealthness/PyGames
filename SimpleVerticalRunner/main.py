import pygame
import sys
from playerClass import Player
from objects import Rock
from rockManager import RockManager

# Initialise pygame
pygame.init()

# setting some constants
WINDOW_WIDTH = 300 
WINDOW_HEIGHT = 600

PLAYER_WIDTH = 20
player = Player()
rock1 = Rock(dy=5)
rock1.dy = 5
RockManager = RockManager()

# Create the game window

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Simple Vertical Runner")

# set the game clock frame rate
FPS = 15
clock = pygame.time.Clock()

score = 0 
lives = 3
playerSpeed = 5
WHITE = (255,255,255)
RED = (255, 0 , 0)
BLACK = (0, 0, 0 )
DARK_BLUE = (0, 0, 55)

## MAIN GAME Loop

isRunning = True
isGameOver = False


while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            isRunning = False


        keys = pygame.key.get_pressed()
        if not isGameOver and keys[pygame.K_a]:
            player.move(-5)

        if not isGameOver and keys[pygame.K_d]:
            player.move(5)

        if keys[pygame.K_q]:
            isRunning = False

    if isGameOver:
        clock.tick(FPS)
        continue


    # move the player
    screen.fill(DARK_BLUE)
    player.draw(screen)
    if not rock1.update():
        rock1 = Rock()
    rock1.draw(screen)
    RockManager.update()
    # Update the display

    # check for collision
    if player.check_collision(rock1):
        lives -= 1
        if lives == 0:
            isGameOver = True
            rock1.active = False
        else:
            rock1 = Rock()

    pygame.display.flip()

    clock.tick(FPS)


sys.exit()


