from operator import ifloordiv
from turtledemo.paint import switchupdown
from typing import Self

import pygame





class Wolf:
    """
    This class represents a wolf on the screen. it starts from just outside the left or right of the screen and will move
    across horizontally and kill any sheep it touches
    """
    def __init__(self, pos = (-300, 200), wolf_image_path=None):
        self.is_active = False
        self.hit_points = 3
        self.pos = pos
        self.wolf_image = pygame.image.load(wolf_image_path)
        if pos[0] > 0:
            self.direction = 1
        else:
            self.direction = -1
        self.speed = 1
        
    def draw(self, screen):
        """
        Draws the wold on the screen
        :param screen: 
        :return: 
        """
        if self.is_active:
            
            
            screen.blit(self.wolf_image, (self.pos[0], self.pos[1]))
            
    def update(self):
        """
        Moves the wolf to the next position
        :return: 
        """
        if self.is_active:
            self.pos = (self.direction * self.speed + self.pos[0], self.pos[1])
            
    def activate(self, position):
        self.is_active = True
        self.pos = position
    
        