
import pygame

from SimpleShooterGame.animator_class import Animator


class Solder(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed = 2, image = 'Art/carol/Carol-Idle.png'):
        pygame.sprite.Sprite.__init__(self)
        self.animator = Animator('Art/carol/carol_idle_', 0.2, frame_count=4, frame_times=[3, 0.2, 0.2, 0.2])
        self.scale = scale
        self.default_image = self.animator.get_image_at(0)
        self.rect = self.default_image.get_rect()
        self.default_image = pygame.transform.scale(self.default_image,(int(self.rect.width * self.scale), int(self.rect.height * self.scale)))
        self.rect.topleft = (x, y)
        self.image = self.speed = speed
        self.dir = pygame.Vector2(0, 0)
        self.is_flip_x = True

    def draw(self, screen):
        if self.animator.check_frame_time():
            self.image = self.animator.get_image()
            self.image = pygame.transform.scale(self.image, (int(self.rect.width * self.scale), int(self.rect.height * self.scale)))
        if isinstance(self.image, pygame.surface.Surface):
            screen.blit(pygame.transform.flip(self.image, self.is_flip_x, False), self.rect)

        else:
            screen.blit(pygame.transform.flip(self.default_image, self.is_flip_x, False), self.rect)

    def move(self, dir):
        dx = dir.x * self.speed
        dy = dir.y * self.speed
        self.dir = dir

        if dx < 0:
            self.is_flip_x = True
        if dx > 0:
            self.is_flip_x = False

        self.rect.x += dx
        self.rect.y += dy
