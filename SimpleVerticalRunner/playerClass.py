import pygame
import random
"""
This is a simple class that represents a player in a game. The player can move left and right
"""
class Player:
    
    def __init__(self, x = 150, y = 550, random_x = False):
        if random_x:
            x = random.randint(0, 300)
        self.WIDTH = 20
        self.color = (200, 0, 0)
        self.rect = pygame.Rect(x, y, self.WIDTH, self.WIDTH)
        self.active = True



    def draw(self, screen):
        """
        This method draws the player on the scree.........n
        :param screen: screen to draw the player on
        :return: True if the player is active, False otherwise
        """
        if (not self.active):
            return False
        pygame.draw.rect(screen, self.color, self.rect)
        
    def move(self, amount):
        if (not self.active):
            return False
        self.rect.x += amount

    def check_collision(self, rock):
        """
        This method checks if the player has collided with a rock
        :param rock: the rock to check collision with
        :return: True if the player has collided with the rock, False otherwise
        """
        if not self.active:
            return False
        if not rock.active:
            return False
        return self.rect.colliderect(rock.rect)
        
class Rock:
    
    def __init__(self):
        x = random.randint(0,300)
        y = -20
        self.width = 20
        self.color = (250, 250, 250)
        self.rect = pygame.Rect(x, y, self.width, self.width)
        self.speed = 10
        self.active = True
        
    def update(self):
        if not self.active:
            return False
        elif self.rect.y > 600:
            self.active = False
        else:
            self.move(self.speed)
            return True
            
    def move(self, amount):
        if not self.active:
            return False
        else:
            self.rect.y += amount
            return True
        
    def draw(self, screen):
        if not self.active:
            return False
        else:
            pygame.draw.rect(screen, self.color, self.rect)
            return True
            
            
