from operator import ifloordiv
from random import random, randint
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
        self.set_edge_limits()
        
        
    def draw(self, screen):
        """
        Draws the wold on the screen
        :param screen: 
        :return: 
        """
        if self.is_active:
            wolf_image = pygame.transform.flip(self.wolf_image, self.direction < 0, False)
            screen.blit(wolf_image, (self.pos[0], self.pos[1]))
            
    def update(self):
        """
        Moves the wolf to the next position
        :return: 
        """
        if self.is_active:
             if self.pos[0] >= self.right_limit:
                self.direction = -1
                self.pos = (self.pos[0], randint(100, 500))
             elif self.pos[0] <= self.left_limit:
                self.direction = 1
                self.pos = (self.pos[0], randint(100, 500))

             self.pos = (self.direction * self.speed + self.pos[0], self.pos[1])
        
    def check_sheep_collision(self, flock):
        for sheep in flock.sheep:
            if self.wolf_image.get_rect().colliderect(sheep.get_rect()):
                sheep.is_eaton()
            
                
    def activate(self, position):
        self.is_active = True
        self.pos = position

    def set_edge_limits(self):
        surface = pygame.display.get_surface()
        screen_width = surface.get_width() if surface else 1000
        wolf_width = self.wolf_image.get_width()
        self.right_limit = screen_width + wolf_width * 2
        self.left_limit = -wolf_width * 2
    
        
