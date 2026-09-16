import os

import pygame

from core.path_utils import get_base_dir


class HayBale:
    def __init__(self, position, image_path=None):
        self.pos = position
        self.image = self.load_image(image_path)
        self.rect = self.image.get_rect(topleft=self.pos)

    def load_image(self, image_path):
        if image_path is None:
            base_dir = get_base_dir()
            image_path = os.path.join(base_dir, "Art", "HayBale1.png")
        return pygame.image.load(image_path).convert_alpha()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
