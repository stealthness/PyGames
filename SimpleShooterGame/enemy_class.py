from ctypes.macholib.dylib import dylib_info

import pygame



class Solder(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed = 2):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Art/Carol.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * scale), int(self.rect.height * scale)))
        self.speed = speed
        self.dir = pygame.Vector2(0, 0)
        self.is_flip_x = True

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.is_flip_x, False), self.rect)


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
