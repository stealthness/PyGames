import asyncio
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

async def main():
    
    game = Game(screen)
    running = True
    while running:
        running = game.run()
        await asyncio.sleep(0)



# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())