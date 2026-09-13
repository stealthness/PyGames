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

# Font for timer display
pygame.font.init()
FONT = pygame.font.SysFont(None, 36)

TIMER_SECONDS = 30

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
        if (TEST_MODE):
            pass
    
        for sheep in flock:
            sheep.draw(screen)
        
        # Draw countdown timer at top center
        elapsed_ms = pygame.time.get_ticks() - start_ticks
        remaining = max(0, TIMER_SECONDS - (elapsed_ms / 1000.0))
        mins = int(remaining) // 60
        secs = int(remaining) % 60
        timer_text = f"{mins}:{secs:02d}"
        text_surf = FONT.render(timer_text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(midtop=(WIDTH // 2, 10))
        # optional shadow for readability
        shadow_surf = FONT.render(timer_text, True, (0, 0, 0))
        shadow_rect = shadow_surf.get_rect(midtop=(WIDTH // 2 + 2, 12))
        screen.blit(shadow_surf, shadow_rect)
        screen.blit(text_surf, text_rect)
        
        # If time's up, show final screen then quit
        if remaining <= 0:
            end_text = "Time's up!"
            end_surf = FONT.render(end_text, True, (255, 0, 0))
            end_rect = end_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(end_surf, end_rect)
            pygame.display.flip()
            await asyncio.sleep(2)
            running = False
            break

        # Display the new screen
        pygame.display.flip()
        
        await asyncio.sleep(0)

    pygame.quit()


# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())