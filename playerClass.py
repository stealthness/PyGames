import pygame

class Player:
    
    
    def __init__(self):
        self.WIDTH = 20
        self.color = (20, 155, 20)
        self.rect = pygame.Rect(0,0, WIDTH, WIDTH)
        
    def draw(self, screen)
        pygame.draw.rect(screen, self.color, self.rect)
        