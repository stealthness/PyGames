import pygame
from pygame import Vector2


class PhysicsEntity:

    def __init__(self, game, e_type, pos: Vector2, size, img, gravity=1):
        self.TERMNAL_VELOCITY = 5
        self.game = game
        self.type = e_type
        self.pos = pos
        self.size = size
        self.active = True
        self.velocity = Vector2(0, 0)
        self.image = pygame.image.load('data\\Art\\entities\\player\\idle\\00.png').convert_alpha()
        self.image = img
        self.gravity = gravity

    def update(self, tilemap):
        if not self.active:
            return
        
        if self.gravity > 0:
            self.velocity.y += min(self.TERMNAL_VELOCITY, self.velocity.y + self.gravity * (self.game.dt))
            
        frame_movement = self.pos + self.velocity * self.game.dt
        entity_rect = self.rect()
        has_collided = False
        for tile_rec in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(tile_rec):
                has_collided = True
                print('collision')
                # if frame_movement.x < 0:
                #     entity_rect.left = tile_rec.right
                #     self.velocity.x = 0
                # if frame_movement.x > 0:
                #     entity_rect.right = tile_rec.left 
                #     self.velocity.x = 0
                if frame_movement.y < 0:
                    self.velocity.y = 0
                    frame_movement.y = self.pos.y
                if frame_movement.y > 0:
                    self.velocity.y = 0
                    frame_movement.y = self.pos.y

        if not has_collided:
            self.pos = frame_movement
        else:
            self.pos = frame_movement
        
    def rect(self):
        return pygame.Rect(self.pos, self.size)

    def render(self, surface):
        surface.blit(self.image, self.pos)
