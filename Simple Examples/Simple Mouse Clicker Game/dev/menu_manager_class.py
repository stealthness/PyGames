from enum import Enum

import pygame

class MenuAction (Enum):
    PlayAction = "Play"
    QuitAction = "Quit"


class MenuManager:
    """
    Manages the main menu display and button interactions.
    """

    def __init__(self, screen):
        """
        Initialize the menu.

        Args:
            screen: The Pygame display surface.
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Fonts
        self.title_font = pygame.font.Font(None, 72)
        self.description_font = pygame.font.Font(None, 32)
        self.button_font = pygame.font.Font(None, 40)

        # Text
        self.title = "My Game"
        self.description = "Press Play to start the game."

        # Buttons
        button_width = 200
        button_height = 60

        center_x = self.screen_rect.centerx - button_width // 2

        self.play_button = pygame.Rect(
            center_x,
            300,
            button_width,
            button_height,
        )

        self.quit_button = pygame.Rect(
            center_x,
            380,
            button_width,
            button_height,
        )

    def handle_event(self):
        """
        Handle menu button clicks.

        Returns:
            str | None: "play", "quit", or None.
        """
        for event in pygame.event.get():
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.play_button.collidepoint(event.pos):
                    return MenuAction.PlayAction

                if self.quit_button.collidepoint(event.pos):
                    return MenuAction.QuitAction

        return None

    def draw_button(self, rect, text):
        """
        Draw a menu button.
        """
        mouse_pos = pygame.mouse.get_pos()

        # Change appearance when hovering.
        if rect.collidepoint(mouse_pos):
            color = (100, 100, 180)
        else:
            color = (60, 60, 120)

        pygame.draw.rect(
            self.screen,
            color,
            rect,
            border_radius=8,
        )

        # Button outline
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            rect,
            width=2,
            border_radius=8,
        )

        text_surface = self.button_font.render(
            text,
            True,
            (255, 255, 255),
        )

        text_rect = text_surface.get_rect(
            center=rect.center
        )

        self.screen.blit(
            text_surface,
            text_rect,
        )

    def draw(self):
        """
        Draw the complete menu.
        """

        # Title
        title_surface = self.title_font.render(
            self.title,
            True,
            (255, 255, 255),
        )

        title_rect = title_surface.get_rect(
            center=(self.screen_rect.centerx, 100)
        )

        self.screen.blit(
            title_surface,
            title_rect,
        )

        # Description
        description_surface = self.description_font.render(
            self.description,
            True,
            (200, 200, 200),
        )

        description_rect = description_surface.get_rect(
            center=(self.screen_rect.centerx, 180)
        )

        self.screen.blit(
            description_surface,
            description_rect,
        )

        # Buttons
        self.draw_button(
            self.play_button,
            "Play",
        )

        self.draw_button(
            self.quit_button,
            "Quit",
        )