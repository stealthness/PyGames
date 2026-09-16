import asyncio
import pygame


class StartMenu:
    """Handles the start menu display and input."""

    def __init__(self, screen, menu_manager):
        self.screen = screen
        self.menu_manager = menu_manager

    async def handle_game_over_events(self, button_rect) -> str:
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

    def run_start_menu(self, image) -> str:
        """Show start menu and return next game status."""
        self.screen.blit(image, (0, 0))
        continue_rect = self.menu_manager.show_start_menu(image)
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
