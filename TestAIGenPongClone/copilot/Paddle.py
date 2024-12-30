import pygame

class Paddle:
    def __init__(self, x, y):
        self.image = pygame.Surface((10, 100))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(midleft=(x, y))
        self.speed = 0

    def update(self):
        self.rect.y += self.speed
        self.rect.y = max(0, min(500, self.rect.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_up(self):
        self.speed = -5

    def move_down(self):
        self.speed = 5

    def stop(self):
        self.speed = 0