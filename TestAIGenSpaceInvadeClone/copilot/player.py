import math

import pygame

SCREEN_WIDTH = 800
class Player:
    def __init__(self):
        self.image = pygame.image.load("../Art/player.png")
        self.x = 370
        self.y = 480
        self.change_x = 0

    def update(self):
        self.x += self.change_x
        self.x = max(0, min(SCREEN_WIDTH - 64, self.x))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def reset(self):
        self.x = 370
        self.y = 480
        self.change_x = 0

    def is_collision(self, ex, ey):
        return math.sqrt((math.pow(self.x - ex, 2)) + (math.pow(self.y - ey, 2))) < 27
