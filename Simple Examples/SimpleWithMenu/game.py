import asyncio

import math
import pygame
from config import DEBUG_MODE

class Game:
    """
    Handle the game logic
    """
    def __init__(self, screen):
        self.screen = screen
        self.frame_tick = 0


    async def run(self):
        """
        Run the game loop. Handles events, updates, and drawing.
        Returns False if the user quits, True if the game is completed.
        """
        if DEBUG_MODE:
            print("running Game")
        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True
            self.update()
            self.draw()
            #clock.tick(FPS)
            await asyncio.sleep(0)
        return True

    def update(self):
        self.frame_tick += 1

    def draw(self):
        variation =  int(50 * math.sin(self.frame_tick/1000))
        self.screen.fill((50 + variation, 20, 30))
        pygame.display.flip()

    def handle_click(self):
        return True