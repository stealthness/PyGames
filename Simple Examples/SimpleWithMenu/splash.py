import asyncio
import pygame
from _testcapi import awaitType

from abstract_menu import AbstractMenu
from config import DEBUG_MODE, splash_background

class Splash (AbstractMenu):
    """
    Handle the Splash screen at the beginning of the game
    """

    def __init__(self, screen):
        AbstractMenu.__init__(self, screen)


    async def run(self):
        """
        Run the splash screen loop. Handles events, updates, and drawing.
        Returns False if the user quits, True if OK button is clicked.
        """
        if DEBUG_MODE:
            print("running Splash")
        return await super().run()

    def update(self):
        pass

    def draw(self):
        self.screen.blit(splash_background, (0, 0))
        pygame.display.flip()



