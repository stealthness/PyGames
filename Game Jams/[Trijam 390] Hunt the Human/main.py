import asyncio

import pygame

from config import FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game, GameStatus
from splash import Splash
from end_game import EndGame


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
                                 
game_status = GameStatus.Splash

async def main():
    global game_status

    while True:
        # Start with Splash
        if game_status == GameStatus.Splash:
            splash = Splash()
            splash_ok = await splash.run(screen, clock)
            if splash_ok:
                game_status = GameStatus.Menu
                continue
            return

        # Start Menu
        if game_status == GameStatus.Menu:
            game_status = GameStatus.Game
            continue

        # Start Game
        if game_status == GameStatus.Game:
            game = Game(screen)
            running = True
            while running:
                dt_ms = clock.tick(FPS)
                running = game.run(dt_ms)
                await asyncio.sleep(0)

            if game.quit_requested:
                return

            game_status = GameStatus.EndGame
            continue

        if game_status == GameStatus.EndGame:
            end_game = EndGame()
            end_game_ok = await end_game.run(screen, clock)
            if end_game_ok:
                game_status = GameStatus.Splash
                continue
            return
            

# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())