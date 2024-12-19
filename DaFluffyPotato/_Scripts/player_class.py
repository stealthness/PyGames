import pygame
from pygame import Vector2

from . import utils
from .entities import PhysicsEntity


class Player(PhysicsEntity):

    def __init__(self, game, e_type, pos: Vector2, size):
        # img = utils.load_img('player\\idle\\00.png')
        img = utils.load_img('entities//player.png')
        super().__init__(game, e_type, pos, size, img)