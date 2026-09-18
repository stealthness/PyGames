import pygame

from config import game_background
from hunan import Human


class Game:
    """
    This is the main game class.
    the game is a vertical runner game.
    
    """
    
    def __init__(self, screen):
        self.screen = screen
        self.background = game_background
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
        pass
    
    def draw(self):
        """
        The function will draw all the game objects connect to the game class
        :return: 
        """
        self.screen.blit(self.background, (0, 0))
        for game_object in self.game_objects:
            game_object.draw(self.screen)
        pygame.display.flip()