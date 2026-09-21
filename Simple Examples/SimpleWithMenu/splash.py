import asyncio
import pygame
from config import DEBUG_MODE, splash_background

class Splash:
    """
    Handle the Menu screen
    """
    def __init__(self, screen):
        self.screen = screen


    async def run(self):
        """
        Run the splash screen loop. Handles events, updates, and drawing.
        Returns False if the user quits, True if OK button is clicked.
        """
        if DEBUG_MODE:
            print("running Menu")
        splash_running = True
        while splash_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.handle_click():
                        splash_running = False
            self.update()
            self.draw()
            #clock.tick(FPS)
            await asyncio.sleep(0)
        return True

    def update(self):
        pass

    def draw(self):
        self.screen.blit(splash_background, (0, 0))
        pygame.display.flip()

    def handle_click(self):
        return True

