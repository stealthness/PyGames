import asyncio
import os
from random import randrange, randint

import pygame

from game import Game
from menuManager import MenuManager
from musicManager import MusicManager   
from sheep import Sheep
from path_utils import get_base_dir

# --------------------------------------------------
# Configuration
# --------------------------------------------------

WIDTH = 960  # Window width
# Load the background image (path relative to this script)
BASE_DIR : str = get_base_dir(False)
background_path = os.path.join(BASE_DIR, "Art", "background.png")
background = pygame.image.load(background_path)
music_path = os.path.join(BASE_DIR, "Hidden", "geoffharvey-farmyard-fun-374610.ogg")
HEIGHT = 540
FPS = 60
TEST_MODE = True
TITLE = "Find the Sheep"


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

TIMER_SECONDS = 4

active_boxes = []
flock = []


menuManager = MenuManager(screen, timer_seconds=TIMER_SECONDS)
musicManager = MusicManager(music_path)
# --------------------------------------------------
# Game State
# --------------------------------------------------

running = True

# --------------------------------------------------
# Async Game Loop
# --------------------------------------------------


def init_game(level: int):
    musicManager.play_music()
    flock.clear()
    # create sheep
    for i in range(level * 3 + 2):
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
    score = 0
    player_lost_sheep_strike = 0
    game_status = "menu"

    NEXT_SICK_SHEEP_DELAY = randint(800, 2500)
    start_ticks = pygame.time.get_ticks()
    next_sick_timer = start_ticks + NEXT_SICK_SHEEP_DELAY
    game = Game(screen,background, flock, music_path)


    while running:

        if game_status == "menu":
            game_status = StartMenu.run_start_menu()
            screen.fill((0, 0, 200))
            continue_rect = menuManager.show_start_menu()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                    if event.key == pygame.K_SPACE:
                        game_status = "init_game"
                        break
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if continue_rect.collidepoint(event.pos):
                            print('clicked')
                            game_status = "init_game"
                        break
            
            continue
            
        if game_status == "init_game":
            level = 1
            score = 0
            player_lost_sheep_strike = 0
            NEXT_SICK_SHEEP_DELAY = randint(800, 2500)
            game_status = "start_game"
            # Draw the background
            if background is None:
                screen.fill((0, 0, 0))
            else:
                screen.blit(background, (0, 0))
            pygame.display.flip()
            continue
            
        if game_status == "start_game":
            game_status = game.run()

        if game_status == "game_over":
            print("Game Over")
            menuManager.show_end_screen(score)            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                    if event.key == pygame.K_SPACE:
                        game_status = "menu_game"
                        break

        # Display the new screen
        pygame.display.flip()
        print(game_status)
        await asyncio.sleep(0)

    pygame.quit()


async def reset_score(is_game_over: bool, level: int, player_lost_sheep_strike: int, score: int):
    level = 1
    score = 0
    player_lost_sheep_strike = 0
    is_game_over = False



class StartMenu:
    
    @staticmethod
    def run_start_menu() -> str:
        return "menu"



# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())