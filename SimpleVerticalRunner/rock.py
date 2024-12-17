import random

import pygame

from SimpleVerticalRunner.objects import GameObject

class Rock(GameObject):
    '''
    This is a simple class that represents a rock in a game. The rock can move down the
    '''

    def __init__(self, x = 150, y = -50, dx = 0, dy = 3):
        super().__init__('rock', x, y)
        x = random.randint(0,300)
        self.width = 20
        self.color = (250, 100, 250)
        self.rect = pygame.Rect(x, y, self.width, self.width)
        self.speed = 10

    def update(self) -> bool:
        if self.rect.y > 600:
            self.active = False
            return False
        super().update()
        return True

    def move(self, dx, dy):
        super().move(0, self.dy)

    def draw(self, screen):
        if not self.active:
            return False
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            return True
