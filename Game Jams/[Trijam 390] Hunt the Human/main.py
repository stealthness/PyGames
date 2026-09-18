import asyncio

import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game, GameStatus

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                                 
game_status = GameStatus.Splash

async def main():
    global game_status
    # Start with Splash
    if game_status == GameStatus.Splash:
        game_status = GameStatus.Menu
    
    # Start Menu
    
    if game_status == GameStatus.Menu:
        game_status = GameStatus.Game
    
    # Start Game
    if game_status == GameStatus.Game:
        
        game = Game(screen)
        running = True
        while running:
            running = game.run()
            await asyncio.sleep(0)

        game_status = GameStatus.EndGame
        
    if game_status == GameStatus.EndGame:
        game = GameStatus.Menu

# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())