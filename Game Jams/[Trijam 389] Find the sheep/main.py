import asyncio
import pygame

from core.game import Game
from managers.menuManager import MenuManager
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
                game_status = await StartMenu.handle_game_over_events(game.game_over_button_rect)
                if game_status == "quit":
                    running = False
            continue
    
    pygame.quit()




class StartMenu:
    """Handles the start menu display and input."""

    @staticmethod
    async def handle_game_over_events(button_rect) -> str:
        """Wait for input on the game-over screen and return the next state."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "quit"
                    if event.key == pygame.K_SPACE:
                        return "menu"
                if event.type == pygame.MOUSEBUTTONDOWN and button_rect is not None:
                    if button_rect.collidepoint(event.pos):
                        return "menu"
            pygame.display.flip()
            await asyncio.sleep(0.05)
    
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
