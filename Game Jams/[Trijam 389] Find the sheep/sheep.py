import os
from random import randint
from path_utils import get_base_dir

import pygame


class Sheep:
    def __init__(self, position, image_path=None, sick_image_path=None, blaa_sounds=None):
        self.pos = position
        self.isFound = False
        self.color = (240, 255, 255)
        self.load_image(image_path, sick_image_path)
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
        if self.isFound or self.isDead:
            return
        
        if self.isSick:
            screen.blit(self.sick_image, self.rect)
        else:
            screen.blit(self.image, self.rect)

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

    def load_image(self, image_path, sick_image_path):
        # Resolve image path relative to this script
        if image_path is None:
            random_sheep = randint(1, 3)
            # prefer actual asset names (capitalization matches files)
            BASE_DIR = get_base_dir()
            # image and sick image use different files in the Art folder
            image_path = os.path.join(BASE_DIR, "Art", f"Sheep{random_sheep}.png")
            sick_image_path = os.path.join(BASE_DIR, "Art", f"SickSheep{random_sheep}.png")
        # If both files exist, load them. If sick image missing, fall back to a tinted copy
        if os.path.exists(image_path):
            self.image = pygame.image.load(image_path).convert_alpha()
        else:
            self.image = None

        if sick_image_path and os.path.exists(sick_image_path):
            self.sick_image = pygame.image.load(sick_image_path).convert_alpha()
        else:
            # if no explicit sick image, try to create one by tinting the normal image
            if self.image is not None:
                # create a green-tinted copy for sick appearance
                self.sick_image = self.image.copy()
                tint = pygame.Surface(self.sick_image.get_size(), pygame.SRCALPHA)
                tint.fill((0, 160, 0, 90))  # semi-transparent green overlay
                self.sick_image.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)
            else:
                self.sick_image = None

        # If image(s) not available, create a simple fallback surface
        if self.image is None:
            self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.ellipse(self.image, self.color, self.image.get_rect())
            pygame.draw.ellipse(self.image, (0, 0, 0), self.image.get_rect(), width=2)

        # Ensure we always have a rect to position the sprite
        self.rect = self.image.get_rect(topleft=self.pos)
