import pygame
import sys
from playerClass import Player
# Intialise pygame
pygame.init()

# setting some costants
WINDOW_WIDTH = 300 
WINSOW_HEIGHT = 600

PLAYER_WIDTH = 20
player = Player(WINDOW_WIDTH // 2, WINSOW_HEIGHT - PLAYER_WIDTH)

# Create the game window

screen = pygame.display.set_mode((WINDOW_WIDTH, WINSOW_HEIGHT))
pygame.display.set_caption("Simple Vertical Runner")

# set the game clock fram rate
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



while isRunning:
    
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            isRunning = False
            
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player.move(-5)
            
        if keys[pygame.K_d]:
            player.move(5)
            
        if keys[pygame.K_q]:
            isRunning = False
            
    # move the player
    screen.fill(DARK_BLUE)
    player.draw(screen)
    
    # Update the display
    pygame.display.flip()
            
    clock.tick(60)
    

sys.exit()


