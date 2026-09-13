import os
import pygame

BASE_DIR = os.path.dirname(__file__)

class Sheep:
    def __init__(self, position, image_path=None):
        self.pos = position
        self.isFound = False
        self.color = (240, 255, 255)
        # Resolve image path relative to this script
        if image_path is None:
            image_path = os.path.join(BASE_DIR, "Art", "sheep.png")
        if os.path.exists(image_path):
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect(topleft=self.pos)
        else:
            # fallback: simple surface
            self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.ellipse(self.image, self.color, self.image.get_rect())
            pygame.draw.ellipse(self.image, (0,0,0), self.image.get_rect(), width=2)
            self.rect = self.image.get_rect(topleft=self.pos)

    def draw(self, screen):
        if self.isFound:
            return
        screen.blit(self.image, self.rect)

    def handle_click(self, pos):
        if not self.isFound and self.rect.collidepoint(pos):
            self.isFound = True
            return True
        return False
