import pygame
import asyncio

from config import (
    BUTTON_HEIGHT,
    BUTTON_OK_COLOR,
    BUTTON_OK_HOVER_COLOR,
    BUTTON_OK_TEXT_COLOR,
    BUTTON_WIDTH,
    FPS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    splash_background,
)

class Splash:
    """
    This class is splash screen that will run only once at the start.
    It displays the HuntTheHuman-GameMenuBackground.png background.
    It shows a button with 'OK' on it that returns True when clicked.
    """

    def __init__(self):
        self.background = splash_background
        self.button_rect = pygame.Rect(
            SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2,
            SCREEN_HEIGHT - 100,
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
        )
        self.button_font = pygame.font.Font(None, 36)
        self.button_text = self.button_font.render("OK", True, BUTTON_OK_TEXT_COLOR)
        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)

    def handle_click(self):
        """
        Check if the OK button was clicked by the player. Returns True if clicked.
        Call this after each pygame event loop.
        """
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            return True
        return False

    def get_button_color(self):
        """Return the button color based on hover state."""
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            return BUTTON_OK_HOVER_COLOR
        return BUTTON_OK_COLOR

    def draw(self, screen):
        """Draw the splash screen with background and OK button."""
        screen.blit(self.background, (0, 0))
        pygame.draw.rect(screen, self.get_button_color(), self.button_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.button_rect, 2)
        self.button_text_rect.center = self.button_rect.center
        screen.blit(self.button_text, self.button_text_rect)
        pygame.display.flip()

    def update(self):
        """Update splash screen state per frame."""
        pass

    async def run(self, screen, clock):
        """
        Run the splash screen loop. Handles events, updates, and drawing.
        Returns False if the user quits, True if OK button is clicked.
        """
        splash_running = True
        while splash_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.handle_click():
                        splash_running = False
            self.update()
            self.draw(screen)
            clock.tick(FPS)
            await asyncio.sleep(0)
        return True

