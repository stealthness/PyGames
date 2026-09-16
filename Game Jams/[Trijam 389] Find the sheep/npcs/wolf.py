from random import randint
import pygame
from core.config import (
    START_WOLF_SPEED,
    NORMAL_WOLF_SPEED,
)

class Wolf:
    """
    This class represents a wolf on the screen. it starts from just outside the left or right of the screen and will move
    across horizontally and kill any sheep it touches
    """
    def __init__(self, pos = (-300, 200), wolf_image=None):
        self.is_active = False
        self.hit_points = 3
        self.pos = pos
        self.wolf_image = wolf_image
        if pos[0] > 0:
            self.direction = 1
        else:
            self.direction = -1
        self.speed = NORMAL_WOLF_SPEED
        self.slow_speed = START_WOLF_SPEED
        self.set_edge_limits()
        
        
    def draw(self, screen):
        """
        Draws the wold on the screen
        :param screen: 
        :return: 
        """
        if self.is_active:
            wolf_image = pygame.transform.flip(self.wolf_image, self.direction < 0, False)
            screen.blit(wolf_image, (int(self.pos[0]), int(self.pos[1])))
            
    def update(self):
        """
        Moves the wolf to the next position
        :return: 
        """
        if self.is_active:
             if self.pos[0] >= self.right_limit:
                self.direction = -1
                self.pos = (self.pos[0], randint(100, 500))
             elif self.pos[0] <= self.left_limit:
                self.direction = 1
                self.pos = (self.pos[0], randint(100, 500))
             movement_speed = self.speed
             if self.direction > 0 and self.pos[0] < 40:
                 movement_speed = self.slow_speed
             elif self.direction < 0 and self.pos[0] > (self.screen_width - 40):
                 movement_speed = self.slow_speed

             self.pos = (self.direction * movement_speed + self.pos[0], self.pos[1])
        
    def check_sheep_collision(self, flock) -> int:
        
              
        if not self.is_active:
            return 0

        eaton_count = 0
        
        wolf_rect = self.wolf_image.get_rect(topleft=(int(self.pos[0]), int(self.pos[1])))
        for sheep in flock:
            if sheep.is_active() and wolf_rect.colliderect(sheep.get_rect()):
                sheep.is_eaton()
                eaton_count += 1
        return eaton_count
                
            
                
    def activate(self, position):
        self.is_active = True
        self.pos = position

    def set_edge_limits(self):
        surface = pygame.display.get_surface()
        screen_width = surface.get_width() if surface else 1000
        self.screen_width = screen_width
        wolf_width = self.wolf_image.get_width()
        self.right_limit = screen_width + wolf_width * 2
        self.left_limit = -wolf_width * 2
    
        
