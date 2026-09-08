import asyncio
import pygame
from game_class import Game

# --------------------------------------------------
# Configuration
# --------------------------------------------------

WIDTH = 270
HEIGHT = 480
FPS = 60

TITLE = "A Simple Mouse Clicker Game"

   


# --------------------------------------------------
# Initialization
# --------------------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()


# --------------------------------------------------
# Async Game Loop
# --------------------------------------------------

async def main():
    running = True
    
    game = Game(screen)

    while running:

        # -----------------------------
        # Delta time
        # -----------------------------
        dt = clock.tick(FPS) / 1000.0

        # -----------------------------
        # Game logic
        # -----------------------------
        running = game.update(dt)


        # -----------------------------
        # IMPORTANT FOR PYGBAG
        # -----------------------------
        # Give the browser event loop
        # control periodically.
        await asyncio.sleep(0)

    pygame.quit()

    

# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())