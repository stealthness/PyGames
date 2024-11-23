import random
import pygame

class GameObject:

    def __init__(self, name, x = 0, y = 0, dx = 0, dy = 0):
        self.name = name
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.active = True
        self.debugMode = True
        self.init_x = x
        self.init_y = y
        self.init_dx = dx
        self.init_dy = dy

    def __str__(self):
        return f'{self.name}, isActive:{self.active} at {self.x},{self.y}, with speed dx:{self.dx}, dy:{self.dy}'

    def update(self) -> bool:
        if self.debugMode:
            print(f'GO update:{self}')
        if not self.active:
            print(f'{self.name} not active: {self.active}')
            return False
        self.move(self.dx, self.dy)
        return True

    def move(self, dx, dy):
        if self.debugMode:
            print(f'GO move: {self}, dx:{dx}, dy:{dy}')
        if self.active:
            self.x += dx
            self.y += dy

    def reset(self):
        self.x = self.init_x
        self.y = self.init_y
        self.dx = self.init_dx
        self.dy = self.init_dy

class Rock(GameObject):

    def __init__(self, x = 150, y = -50, dx = 0, dy = 3):
        super().__init__('rock', x, y)
        x = random.randint(0,300)
        self.width = 20
        self.color = (250, 250, 250)
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
