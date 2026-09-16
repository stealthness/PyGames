from random import randint

import pygame


class Sheep:
    def __init__(self, position, image, sick_image, dead_image, blaa_sounds=None):
        self.pos = position
        self.isFound = False
        self.color = (240, 255, 255)
        self.image = image
        self.sick_image = sick_image
        self.dead_image = dead_image
        self.rect = self.image.get_rect(topleft=self.pos)
        self.isSick = False
        self.blaa_sounds = blaa_sounds
        self.isDead = False
        
    def make_sick(self):
        if self.isFound or self.isDead:
            return
        self.isSick = True
        
    def die(self):
        if self.isFound or self.isDead:
            return
        self.isDead = True
        self.isSick = False
    
    def is_active(self):
        return not self.isFound and not self.isDead
 
    def draw(self, screen) -> None:
        """
        This method draws a sheep to the screen. If a sheep is found, then no sheep is drawn. If sheep is sick the sick sheep image is drawn
        :param screen: 
        :return: None
        """
        if self.isFound:
            return
        
        if self.isDead:
            screen.blit(self.dead_image, self.get_rect())
            return
        
        if self.isSick:
            screen.blit(self.sick_image, self.get_rect())
        else:
            screen.blit(self.image, self.get_rect())

    def handle_click(self, pos)-> int:
        if self.isDead:
            return 0
        
        if not self.isFound and self.rect.collidepoint(pos):
            self.isFound = True
            if not self.blaa_sounds is None:
                i = randint(0, len(self.blaa_sounds) - 1)
                pygame.mixer.Sound(self.blaa_sounds[i]).play()
            return 1
        return 0

    def is_eaton(self):
        self.die()
        
    def get_rect(self):
        return self.rect
