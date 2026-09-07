import random

import pygame

from SimpleVerticalRunner.objects import GameObject

class Rock(GameObject):
    """
    This is a simple class that represents a rock in a game. The rock can move down the
    """

    def __init__(self, x = 50, y = 50, dx = 0, dy = 3, is_random = True):
        super().__init__('rock', x, y)
        if is_random:
            self.x = random.randint(0,300)
        self.width = 20
        self.color = (250, 100, 250)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.width)
        self.speed = 10

    def update(self) -> bool:
        """
        Updates the rock's position. If the rock goes off the screen,
        it is marked as inactive.
        :return: True if the rock is still active, False otherwise.
        """
        if self.rect.y > 600:
            self.active = False
            return False
        super().update()
        return True

    def move(self, dx, dy):
        super().move(0, 1)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        """
        Draws the rock on the given screen.
        If the rock is not active, it does nothing.
        :param screen:
        :return: true if the rock was drawn, False if it was not active.
        """
        if not self.active:
            return False
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            return True
