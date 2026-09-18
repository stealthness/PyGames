from enum import Enum

import pygame

from background_controller import BackgroundController
from hunan import Human


class Game:
    """
    This is the main game class.
    the game is a vertical runner game.
    
    """
    
    def __init__(self, screen):
        self.screen = screen
        self.background_controller = BackgroundController()
        self.human = Human()
        self.game_objects = [self.human]
        
        
    def run(self):
        # Run one frame and report whether the game should continue.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        self.update()
        self.draw()
        return True
        
        
    def update(self):
        """
        this function update all game objects connect to the game class
        :return: 
        """
        self.background_controller.update()
        for game_object in self.game_objects:
            game_object.update()
    
    def draw(self):
        """
        The function will draw all the game objects connect to the game class
        :return: 
        """
        self.background_controller.draw(self.screen)
        for game_object in self.game_objects:
            game_object.draw(self.screen)
        pygame.display.flip()
        
class GameStatus(Enum):
    
    Splash = 0,
    Menu = 1,
    Game = 2,
    EndGame = 3,