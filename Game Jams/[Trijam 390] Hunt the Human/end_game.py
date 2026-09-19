import asyncio

import pygame
from config import (
    BUTTON_HEIGHT,
    BUTTON_OK_COLOR,
    BUTTON_OK_HOVER_COLOR,
    BUTTON_OK_TEXT_COLOR,
    BUTTON_WIDTH,
    FPS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    end_game_background,
)

class EndGame:
    def __init__(self):
        self.end_game_background = end_game_background
        self.button_text = end_game_background
        self.button_rect = pygame.Rect(
            SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2,
            SCREEN_HEIGHT - 100,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
            )
        self.button_font = pygame.font.Font(None, 36)
        self.button_text = self.button_font.render("OK", True, BUTTON_OK_TEXT_COLOR)
        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)

    async def run(self, screen, clock):
        """
        Run the splash screen.
        :param screen: 
        :param clock: 
        :return: 
        """
        end_game_running = True
        while end_game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.handle_click():
                        splash_running = False
            self.draw(screen)
            clock.tick(FPS)
            await asyncio.sleep(0)
        return True

    def draw(self, screen):
        """Draw the end game with background and OK button."""
        screen.blit(self.end_game_background, (0, 0))
        pygame.draw.rect(screen, self.get_button_color(), self.button_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.button_rect, 2)
        self.button_text_rect.center = self.button_rect.center
        screen.blit(self.button_text, self.button_text_rect)
        pygame.display.flip()

    def get_button_color(self):
        """Return the button color based on hover state."""
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            return BUTTON_OK_HOVER_COLOR
        return BUTTON_OK_COLOR

    def handle_click(self):
        """
        Check if the OK button was clicked by the player. Returns True if clicked.
        Call this after each pygame event loop.
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            return True
        return False