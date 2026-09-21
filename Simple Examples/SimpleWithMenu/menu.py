import pygame

from abstract_menu import AbstractMenu
from config import DEBUG_MODE, menu_background

class Menu (AbstractMenu):
    """
    Handle the Menu Screen
    """
    def __init__(self, screen):
        super().__init__(screen)

    async def run(self):
        """
        Run the menu screen loop. Handles events, updates, and drawing.
        Returns False if the user quits, True if OK button is clicked.
        """
        if DEBUG_MODE:
            print("running menu")
        return await super().run()

    def update(self):
        pass

    def draw(self):
        self.screen.blit(menu_background, (0, 0))
        pygame.display.flip()
