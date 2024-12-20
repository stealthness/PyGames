import pygame
from pygame import Vector2


class PhysicsEntity:

    def __init__(self, game, e_type, pos: Vector2, size, img, gravity=10.0):
        self.TERMINAL_VELOCITY = 5.0
        self.game = game
        self.type = e_type
        self.pos = pos
        self.size = size
        self.active = True
        self.velocity : Vector2 = Vector2(0.0, 0.0)
        self.image = pygame.image.load('data\\Art\\entities\\player\\idle\\00.png').convert_alpha()
        self.image = img
        self.gravity = gravity
        self.speed = 5.0

    def update(self, tilemap):
        if not self.active:
            return  
        if self.gravity > 0:
            self.velocity = Vector2(self.velocity.x,
                                    self.velocity.y + min(self.TERMINAL_VELOCITY, float(self.gravity * self.game.dt)))
        frame_movement = None
        check_collision = True
        
        while check_collision:
            frame_movement = self.pos + self.game.unit * self.velocity * self.game.dt
            check_collision = False
            for tile_rec in tilemap.physics_rects_around(frame_movement):
                if self.rect().colliderect(tile_rec):
                    print('checking...')
                    check_collision = True
                    if self.velocity.y > 0:
                        frame_movement.y = tile_rec.top
                        self.velocity.y = 0
                        break
                    elif self.velocity.y < 0:
                        frame_movement.y = tile_rec.bottom
                        self.velocity.y = 0
                        break
                    if self.velocity.x > 0:
                        frame_movement.x = tile_rec.right
                        self.velocity.x = 0
                        break
                    elif self.velocity.x < 0:
                        frame_movement.x = tile_rec.left
                        self.velocity.x = 0
                        break

        self.pos = frame_movement
        
    def move(self, new_dir):
        self.velocity = Vector2(new_dir.x * self.speed, self.velocity.y)
        
    def rect(self):
        return pygame.Rect(self.pos, self.size)

    def render(self, surface):
        surface.blit(self.image, self.pos)
