import pygame

class Player:
    
    
    def __init__(self, x = 100, y = 100):
        self.WIDTH = 20
        self.color = (200, 0, 0)
        self.rect = pygame.Rect(x, y, self.WIDTH, self.WIDTH)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
    def move(self, amount):
        self.rect.x += amount
        