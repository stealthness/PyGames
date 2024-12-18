import pygame


class CandyCane:
    def __init__(self):
        self.pos = pygame.Vector2(0,0)
        self.image = pygame.image.load('candy_cane.png')
        self.rect = pygame.Rect(0,0)


class CandyCaneManager:
    def __init__(self):
        candy_cane = CandyCane()
        self.candy_list = []

    def update(self):
        pass
