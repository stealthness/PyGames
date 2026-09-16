import asyncio
import pygame

from core.game import Game
from managers.menuManager import MenuManager
from managers.startMenu import StartMenu
from core.image_store import ImageStore
from core.path_utils import get_base_dir
from core.config import WIDTH, HEIGHT, FPS, TITLE, TIMER_SECONDS

# --------------------------------------------------
# Configuration & Initialization
# --------------------------------------------------

BASE_DIR = get_base_dir(False)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
images = ImageStore(BASE_DIR)
backgrounds = images.get_backgrounds()
music_path = images.music_path

# Global game state
menuManager = MenuManager(screen, timer_seconds=TIMER_SECONDS)
startMenu = StartMenu(screen, menuManager)

# --------------------------------------------------
# Async Game Loop
# --------------------------------------------------


async def main():
    """Main async game loop."""
    game_status = "menu"
    game = Game(screen, images, music_path)
    running = True
    
    while running:
        # Menu state
        if game_status == "menu":
            game_status = startMenu.run_start_menu(backgrounds[3])
            if game_status == "quit":
                running = False
            await asyncio.sleep(0)
            continue
        
        # Initialize new game
        if game_status == "init_game":
            game.score = 0
            game.strikes = 0
            game.level = 1
            game.game_init(1)
            game_status = "start_game"
            continue
        
        # Main gameplay loop
        if game_status == "start_game":
            game_status = await game.run()
            if game_status == "quit":
                running = False
            elif game_status == "game_over":
                game_status = await startMenu.handle_game_over_events(game.game_over_button_rect)
                if game_status == "quit":
                    running = False
            continue
    
    pygame.quit()



# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())
