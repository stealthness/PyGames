import math

import pygame


class Bullet:
    def __init__(self):
        self.image = pygame.image.load("../Art/bullet.png")
        self.x = 0
        self.y = 480
        self.change_y = 10
        self.state = "ready"

    def fire(self, player_x):
        self.state = "fire"
        self.x = player_x
        self.y = 480

    def update(self):
        if self.state == "fire":
            self.y -= self.change_y
            if self.y <= 0:
                self.reset()

    def draw(self, screen):
        if self.state == "fire":
            screen.blit(self.image, (self.x + 16, self.y + 10))

    def reset(self):
        self.state = "ready"
        self.y = 480

    def is_collision(self, ex, ey):
        return math.sqrt((math.pow(self.x - ex, 2)) + (math.pow(self.y - ey, 2))) < 27
