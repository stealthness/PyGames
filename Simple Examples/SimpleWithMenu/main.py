import asyncio
from enum import Enum

import pygame

from endgame import EndGame
from splash import Splash
from menu import Menu
from game import Game
from config import WIDTH, HEIGHT, FPS, TITLE, DEBUG_MODE


# --------------------------------------------------
# GameStatus
# --------------------------------------------------

class GameStatus(Enum):
    """
    Represents the different states of the game.
    """
    Splash = 0,
    Menu = 1,
    Running = 2,
    Finished = 3,
    
# --------------------------------------------------
# Initialization
# --------------------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()


# --------------------------------------------------
# Game State
# --------------------------------------------------

running = True
game_status = GameStatus.Splash
# --------------------------------------------------
# Async Game Loop
# --------------------------------------------------

async def main():
    global running
    global game_status
    
    while running:
        # Start with Splash
        if game_status == GameStatus.Splash:
            splash = Splash(screen)
            splash_ok = await splash.run()
            if splash_ok:
                game_status = GameStatus.Menu
                continue
            return   
        
        if game_status == GameStatus.Menu:
            menu = Menu(screen)
            menu_ok = await menu.run()
            if menu_ok:
                game_status = GameStatus.Running
                continue
            return

        if game_status == GameStatus.Running:
            game = Game(screen)
            game_ok = await game.run()
            if game_ok:
                game_status = GameStatus.Finished
                continue
            return

            
        if game_status == GameStatus.Finished:
            end_game = EndGame(screen)
            end_game_ok = await end_game.run()
            if end_game_ok:
                game_status = GameStatus.Menu
                continue
            return
        
        await asyncio.sleep(0)

    pygame.quit()




# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())