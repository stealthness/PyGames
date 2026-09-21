import pygame

from abstract_menu import AbstractMenu
from config import DEBUG_MODE, end_game_background

class EndGame(AbstractMenu):
    
    
    def draw(self):
        self.screen.blit(end_game_background, (0, 0))
        pygame.display.flip()

    def update(self):
        pass

    def __init__(self, screen):
        super().__init__(screen)
        
    async def run(self):
        if DEBUG_MODE:
            print("End Game")
        return await super().run()