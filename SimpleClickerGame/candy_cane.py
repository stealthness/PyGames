import random

import pygame
from pygame import Vector2


class CandyCane:
    def __init__(self, pos=Vector2(0, 0)):

        self.pos = self.get_random_start_position()
        self.image = pygame.image.load('Art/CandyCane.png')
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 32, 32)
        self.speed = 2
        self.active = True

    def set_active(self, active):
        self.active = active

    def update(self):
        if not self.active:
            self.reset_pos()
            return

        self.pos.y += self.speed
        self.rect.y = self.pos.y

        if self.pos.y > 500:
            self.reset_pos()
            
    def reset_pos(self):
        self.pos = self.get_random_start_position()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.active = True   
            

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.pos)

    def point_collided(self, point: Vector2):
        print(f'point_collided: {point}, self.pos: {self.pos}, type: {type(self)}, self.rect: {type(self.rect)}')
        if self.rect.collidepoint(point.x, point.y):
            self.active = False
            return True
        return False

    @staticmethod
    def get_random_start_position():
        rand_x = random.randint(0, 500)
        rand_y = random.randint(-250, -50)
        return Vector2(rand_x, rand_y)
