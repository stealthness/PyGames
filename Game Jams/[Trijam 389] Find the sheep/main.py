import asyncio
import os
from random import randrange

import pygame

from sheep import Sheep

# --------------------------------------------------
# Configuration
# --------------------------------------------------

WIDTH = 960  # Window width
# Load the background image (path relative to this script)
BASE_DIR : str = os.path.dirname(__file__)
background_path = os.path.join(BASE_DIR, "Art", "background.png")
background = pygame.image.load(background_path)
HEIGHT = 540
FPS = 60
TEST_MODE = True

TITLE = "A Simple Pygame outline"


# --------------------------------------------------
# Initialization
# --------------------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

active_boxes = []
flock = []
# --------------------------------------------------
# Game State
# --------------------------------------------------

running = True

# --------------------------------------------------
# Async Game Loop
# --------------------------------------------------

def init_game():
    # create sheep
    for i in range(5):
        pos = (randrange(900), randrange(500))
        flock.append(Sheep(pos))
        
        
async def main():
    global running
    

            
    print(f" flock {len(flock)}")
    
    init_game()

    while running:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for sheep in flock:
                    sheep.handle_click(pos)
        
        
        # Draw the background
        screen.blit(background, (0, 0))
        if (TEST_MODE):
            pass
    
        for sheep in flock:
            sheep.draw(screen)
        
        # Display the new screen
        pygame.display.flip()
        
        await asyncio.sleep(0)

    pygame.quit()


# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())