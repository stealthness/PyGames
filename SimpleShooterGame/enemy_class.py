import pygame



class Solder(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Art/simplePlayer.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image = pygame.transform.scale(self.image, (int(self.rect.width * scale), int(self.rect.height * scale)))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
