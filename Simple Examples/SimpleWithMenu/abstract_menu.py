import asyncio
from abc import abstractmethod, ABC
import pygame

class AbstractMenu(ABC):
    """
    Handle the Menu screen
    """
    def __init__(self, screen):
        self.screen = screen


    async def run(self):
        """
        Run the menu screen loop. Handles events, updates, and drawing.
        Returns False if the user quits, True if OK button is clicked.
        """
        menu_running = True
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.handle_click():
                        menu_running = False
            self.update()
            self.draw()
            await asyncio.sleep(0)
        return True

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def handle_click(self):
        return True
