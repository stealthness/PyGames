import pygame


class HayBale:
    def __init__(self, position, image):
        self.pos = position
        self.image = image
        self.rect = self.image.get_rect(topleft=self.pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
