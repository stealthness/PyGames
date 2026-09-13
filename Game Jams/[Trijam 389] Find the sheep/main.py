import asyncio
import os
from random import randrange

import pygame

from menuManager import MenuManager
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

# Font for timer display
pygame.font.init()
FONT = pygame.font.SysFont(None, 36)

TIMER_SECONDS = 30

active_boxes = []
flock = []

menuManager = MenuManager(screen)
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
        pos = get_random_sheep_pos()
        flock.append(Sheep(pos))
        
def get_random_sheep_pos():
    while True:
        pos = randrange(WIDTH), randrange(HEIGHT)
        if 400 < pos[0] < 500 and 100 < pos[1] < 300:
            continue
        else:
            return pos
        
        
async def main():
    global running
    
    GAME_OVER = False
            
    print(f" flock {len(flock)}")
    
    init_game()
    
    # start countdown timer
    start_ticks = pygame.time.get_ticks()

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
        if TEST_MODE:
            pass
    
        for sheep in flock:
            sheep.draw(screen)
        
        if GAME_OVER:
            continue
        
        # Draw countdown timer at top center
        remaining = menuManager.draw_timer(start_ticks)
        
        # If time's up, show final screen then quit
        if remaining <= 0:
            GAME_OVER = True
            menuManager.show_end_screen(2)
            pygame.display.flip()
            await asyncio.sleep(2)

        # Display the new screen
        pygame.display.flip()
        
        await asyncio.sleep(0)

    pygame.quit()


# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())