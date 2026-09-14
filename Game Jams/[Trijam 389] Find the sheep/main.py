import asyncio
import os
from random import randrange, randint

import pygame
from pygame.examples.music_drop_fade import music_file_list

from menuManager import MenuManager
from musicManager import MusicManager   
from sheep import Sheep

# --------------------------------------------------
# Configuration
# --------------------------------------------------

WIDTH = 960  # Window width
# Load the background image (path relative to this script)
BASE_DIR : str = os.path.dirname(__file__)
#BASE_DIR : str = "" # pygbag
background_path = os.path.join(BASE_DIR, "Art", "background.png")
background = pygame.image.load(background_path)
music_path = os.path.join(BASE_DIR, "Hidden", "geoffharvey-farmyard-fun-374610.mp3")
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
musicManager = MusicManager(music_path)
# --------------------------------------------------
# Game State
# --------------------------------------------------

running = True

# --------------------------------------------------
# Async Game Loop
# --------------------------------------------------

def init_game(level):
    musicManager.play_music()
    flock.clear()
    # create sheep
    for i in range((level -1) * 3 + 5):
        pos = get_random_sheep_pos()
        flock.append(Sheep(pos, blaa_sounds=["Hidden/blaa1.ogg", "Hidden/blaa2.ogg", "Hidden/blaa3.ogg"]))
        
def get_random_sheep_pos():
    while True:
        pos = randrange((WIDTH - 40)), randrange((HEIGHT-40))
        if 400 < pos[0] < 500 and 100 < pos[1] < 300:
            continue
        else:
            return pos
        
        
async def main():
    global running
    level = 1
    GAME_OVER = False
    NEXT_SICK_SHEEP_DELAY = 2000
    
    init_game(level)
    score = 0
    
    # start countdown timer
    start_ticks = pygame.time.get_ticks()
    next_sick_timer = start_ticks + NEXT_SICK_SHEEP_DELAY

    while running:

        # Draw the background
        screen.blit(background, (0, 0))
        
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for sheep in flock:
                    score += sheep.handle_click(pos)

        
        menuManager.draw_score(score)
        
        if TEST_MODE:
            pass
    
        if pygame.time.get_ticks() - start_ticks > next_sick_timer:
            next_sick_timer = pygame.time.get_ticks() +  NEXT_SICK_SHEEP_DELAY
            flock[randint(0, len(flock) - 1)].make_sick()
    
    
        for sheep in flock:
            sheep.draw(screen)
        
        
        
        # Check if all sheep are found
        all_found = all(sheep.isFound for sheep in flock)
        if all_found and not GAME_OVER:
            # Draw end level screen and get continue button rect
            continue_rect = menuManager.show_end_level(score, level)
            musicManager.stop_music()
            pygame.display.flip()

            # Wait up to 3 seconds, but allow player to click Continue to skip the wait
            clicked = False
            wait_start = pygame.time.get_ticks()
            timeout_ms = 8000
            while not clicked and (pygame.time.get_ticks() - wait_start) < timeout_ms and running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            break
                        else:
                            # any key press also continues
                            clicked = True
                            break
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if continue_rect.collidepoint(event.pos):
                            clicked = True
                            break

                # keep showing the screen
                pygame.display.flip()
                await asyncio.sleep(0.05)

            # Advance to next level
            if not running:
                break
            level += 1
            init_game(level)
            start_ticks = pygame.time.get_ticks()
            next_sick_timer = start_ticks + NEXT_SICK_SHEEP_DELAY
            continue
        
        # Draw countdown timer at top center
        remaining = menuManager.draw_timer(start_ticks)
        
        # If time's up, show final screen then quit
        if remaining <= 0:
            GAME_OVER = True
            menuManager.show_end_screen(score)
            musicManager.stop_music()
            pygame.display.flip()
            await asyncio.sleep(10)

        # Display the new screen
        pygame.display.flip()
        
        await asyncio.sleep(0)

    pygame.quit()


# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())