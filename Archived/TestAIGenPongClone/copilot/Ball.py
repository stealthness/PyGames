import pygame
import random

class Ball:
    def __init__(self):
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(400, 300))
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.center = (400, 300)
        self.speed_x *= random.choice([-1, 1])
        self.speed_y *= random.choice([-1, 1])