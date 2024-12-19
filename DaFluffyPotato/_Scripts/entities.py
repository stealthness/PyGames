import pygame
from pygame import Vector2

class PhysicsEntity:
    def __init__(self, game, e_type, pos: Vector2, size, img):
        self.game = game
        self.type = e_type
        self.pos = pos
        self.size = size
        self.active = True
        self.velocity = Vector2(0, 0)
        self.image = pygame.image.load('data\\Art\\entities\\player\\idle\\00.png').convert_alpha()
        self.image = img
        
    def update(self):
        if not self.active:
            return
        frame_movement = self.pos + self.velocity * self.game.dt
        self.pos = frame_movement
        
    def render(self, surface):
        surface.blit(self.image, self.pos)
        