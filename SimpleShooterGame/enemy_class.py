import pygame



class Solder(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Art/simplePlayer.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * scale), int(self.rect.height * scale)))
        self.speed = 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, dir):
        self.rect.x += dir.x * self.speed
        self.rect.y += dir.y * self.speed
