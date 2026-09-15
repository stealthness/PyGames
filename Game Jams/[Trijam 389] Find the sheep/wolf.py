from operator import ifloordiv

import pygame


class Wolf:
    """
    This class represents a wolf on the screen. it starts from just outside the left or right of the screen and will move
    across horizontally and kill any sheep it touches
    """
    def __init__(self, pos = (-300, 200), wolf_image_path=None):
        self.is_toggled_on = False
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
        if self.is_toggled_on:
            screen.blit(self.wolf_image, (self.pos[0], self.pos[1]))
            
    def update(self):
        """
        Moves the wolf to the next position
        :return: 
        """
        if self.is_toggled_on:
            self.pos[0] += self.direction * self.speed
            
            
        