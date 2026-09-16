import asyncio
import os
import pygame

from game import Game
from menuManager import MenuManager
from path_utils import get_base_dir
from config import WIDTH, HEIGHT, FPS, TITLE, TIMER_SECONDS

# --------------------------------------------------
# Configuration & Initialization
# --------------------------------------------------

BASE_DIR = get_base_dir(False)
background_path = os.path.join(BASE_DIR, "Art", "background.png")
menu_background_path = os.path.join(BASE_DIR, "Art", "menu_background.png")
game_over_background_path = os.path.join(BASE_DIR, "Art", "game_over_background.png")
next_level_background_path = os.path.join(BASE_DIR, "Art", "next_level_background.png")
music_path = os.path.join(BASE_DIR, "Hidden", "geoffharvey-farmyard-fun-374610.ogg")
background_paths = [background_path, next_level_background_path, game_over_background_path, menu_background_path]
backgrounds = []

for path in background_paths:
    try:
        backgrounds.append(pygame.image.load(path))
    except (FileNotFoundError, pygame.error):
        print(f"Warning: Could not load background from {path}")


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Global game state
flock = []
pack = []
menuManager = MenuManager(screen, timer_seconds=TIMER_SECONDS)

# --------------------------------------------------
# Async Game Loop
# --------------------------------------------------


async def main():
    """Main async game loop."""
    game_status = "menu"
    game = Game(screen, backgrounds, flock, pack, music_path)
    running = True
    
    while running:
        # Menu state
        if game_status == "menu":
            game_status = StartMenu.run_start_menu(backgrounds[3])
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
                # Wait for user input before returning to menu
                wait_screen = True
                while wait_screen:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            wait_screen = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                wait_screen = False
                            elif event.key == pygame.K_SPACE:
                                game_status = "menu"
                                wait_screen = False
                    pygame.display.flip()
                    await asyncio.sleep(0.05)
            continue
    
    pygame.quit()




class StartMenu:
    """Handles the start menu display and input."""
    
    @staticmethod
    def run_start_menu(image) -> str:
        """Show start menu and return next game status."""
        screen.blit(image, (0, 0))
        continue_rect = menuManager.show_start_menu(image)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"
                if event.key == pygame.K_SPACE:
                    return "init_game"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if continue_rect.collidepoint(event.pos):
                    return "init_game"
        
        return "menu"



# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())