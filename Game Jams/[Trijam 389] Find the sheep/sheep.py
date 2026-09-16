import os
from random import randint
from typing import Self

from path_utils import get_base_dir

import pygame


class Sheep:
    def __init__(self, position, image_path=None, sick_image_path=None, blaa_sounds=None, dead_image_path=None):
        self.pos = position
        self.isFound = False
        self.color = (240, 255, 255)
        self.load_image(image_path, sick_image_path, dead_image_path)
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

    def load_image(self, image_path, sick_image_path, dead_image_path):
        # Resolve image paths relative to this script when not explicitly provided
        if image_path is None or sick_image_path is None:
            random_sheep = randint(1, 3)
            base_dir = get_base_dir()
            if image_path is None:
                image_path = os.path.join(base_dir, "Art", f"Sheep{random_sheep}.png")
            if sick_image_path is None:
                sick_image_path = os.path.join(base_dir, "Art", f"SickSheep{random_sheep}.png")
        if dead_image_path is None:
            base_dir = get_base_dir()
            dead_image_path = os.path.join(base_dir, "Art", "SheepDead1.png")

        self.image = pygame.image.load(image_path).convert_alpha()
        self.sick_image = pygame.image.load(sick_image_path).convert_alpha()
        self.dead_image = pygame.image.load(dead_image_path).convert_alpha()

        # Ensure we always have a rect to position the sprite
        self.rect = self.image.get_rect(topleft=self.pos)
