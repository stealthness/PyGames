import pygame
from pygame import Vector2

from .entities import PhysicsEntity


class Player(PhysicsEntity):

    def __init__(self, game, e_type, pos: Vector2, size):
        img = pygame.image.load('data\\Art\\entities\\player\\idle\\00.png').convert_alpha()
        super().__init__(game, e_type, pos, size, img)
