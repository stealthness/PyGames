import os
from random import randint

import pygame


class Sheep:
    def __init__(self, position, image_path=None, sick_image_path=None):
        self.pos = position
        self.isFound = False
        self.color = (240, 255, 255)
        self.load_image(image_path, sick_image_path)
        self.isSick = False
        
    
    def isActive(self):
        return not self.isFound

    def draw(self, screen):
        if self.isFound:
            return
        
        if self.isSick:
            screen.blit(self.sick_image, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def handle_click(self, pos)-> int:
        if not self.isFound and self.rect.collidepoint(pos):
            self.isFound = True
            return 1
        return 0

    def load_image(self, image_path, sick_image_path):
        # Resolve image path relative to this script
        if image_path is None:
            random_sheep = randint(1,3)
            print(f"sheep{random_sheep}.png")

            BASE_DIR = os.path.dirname(__file__) # windows
            #BASE_DIR = "" #pygbag
            image_path = os.path.join(BASE_DIR, "Art", f"sheep{random_sheep}.png")
            sick_image_path = os.path.join(BASE_DIR, "Art", f"sheep{random_sheep}.png")
        if os.path.exists(image_path) and os.path.exists(sick_image_path):
            self.image = pygame.image.load(image_path).convert_alpha()
            self.sick_image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect(topleft=self.pos)
        else:
            # fallback: simple surface
            self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.ellipse(self.image, self.color, self.image.get_rect())
            pygame.draw.ellipse(self.image, (0,0,0), self.image.get_rect(), width=2)
            self.rect = self.image.get_rect(topleft=self.pos)