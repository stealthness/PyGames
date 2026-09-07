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
        self.velocity: Vector2 = Vector2(0.0, 0.0)
        self.image = pygame.image.load('data\\Art\\entities\\player\\idle\\00.png').convert_alpha()
        self.image = img
        self.gravity = gravity
        self.speed = 5.0

    def update(self, tilemap):
        if not self.active:
            return None

        old_pos = self.pos
        if self.gravity > 0:
            self.velocity = Vector2(self.velocity.x,
                                    self.velocity.y + min(self.TERMINAL_VELOCITY, float(self.gravity * self.game.dt)))
        frame_movement = None
        check_collision = True

        while check_collision:
            frame_movement = self.pos + self.game.unit * self.velocity * self.game.dt
            check_collision = False
            
            for tile_rec in tilemap.physics_rects_around(frame_movement):
                pygame.draw.rect(self.game.display, (0, 255, 0), tile_rec, 1)
                if self.rect().colliderect(tile_rec):
                    print('checking...')
                    if self.velocity.y > 0:
                        old_pos = Vector2(old_pos.x, old_pos.y + 16)
                        self.velocity.y = 0
                        break
                    elif self.velocity.y < 0:
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
                    frame_movement = Vector2(0, 0)

        print(f'frame_movement: {frame_movement}')
        self.pos = frame_movement

    def move(self, new_dir):
        self.velocity = Vector2(new_dir.x * self.speed, self.velocity.y)

    def rect(self):
        int_pos = (int(self.pos.x // 1), int(self.pos.y // 1))
        return pygame.Rect(int_pos, self.size)

    def render(self, surface):
        int_pos = (int(self.pos.x // 1), int(self.pos.y // 1))
        pygame.draw.rect(surface, (255, 0, 0), self.rect(), 1)
        surface.blit(self.image, int_pos)
