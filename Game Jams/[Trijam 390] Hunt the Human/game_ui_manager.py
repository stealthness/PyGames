import pygame

from config import HUMAN_START_LIVES, SCREEN_WIDTH, ui_heart_active_image, ui_heart_inactive_image


class GameUIManager:
    """
    
    """
    
    def __init__(self):
        self.score = 0
        self.lives = HUMAN_START_LIVES
        self.max_lives = HUMAN_START_LIVES

        self.top_band_height = 70
        self.top_band_rect = pygame.Rect(0, 0, SCREEN_WIDTH, self.top_band_height)

        self.life_box_size = ui_heart_active_image.get_width()
        self.life_box_padding = 10
        self.life_box_x = 12
        self.life_box_y = (self.top_band_height - self.life_box_size) // 2
        self.active_heart_image = ui_heart_active_image
        self.inactive_heart_image = ui_heart_inactive_image
    
    
    def update_score(self, score):
        """
        This function will update the score of the game
        :param score: 
        :return: 
        """
        self.score = score
    
    def update_health(self, lives):
        """
        This function will update the health of the game
        :param lives: 
        :return: 
        """
        self.lives = max(0, min(lives, self.max_lives))

    def draw(self, screen):
        """Draw the top HUD band and life placeholders."""

        for index in range(self.max_lives):
            x_position = self.life_box_x + index * (self.life_box_size + self.life_box_padding)
            life_position = (x_position, self.life_box_y)
            if index < self.lives:
                screen.blit(self.active_heart_image, life_position)
            else:
                screen.blit(self.inactive_heart_image, life_position)
