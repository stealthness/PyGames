from typing import Self

import pygame

class MenuConfig:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (200,0,0)


class MenuManager:

    
    def __init__(self, screen, timer_seconds=30):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 40)
        self.TIMER_SECONDS = timer_seconds
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        
        
    
    
    def show_end_level(self, score, level):
        """
        Draw the end-of-level screen and a Continue button.
        Returns the pygame.Rect of the Continue button so caller can detect clicks.
        """
        self.screen.fill((223, 237, 149))
        
        # Draw title and score using refactored helper
        MenuManager.create_text_at(self.screen,
                                   f"Next Level {level}",
                                   self.font,
                                   (0, 50),
                                   40)
        MenuManager.create_text_at(self.screen,
                                   f"Your current score is {score}",
                                   self.font,
                                   (0, -20),
                                   40)

        # Draw Continue button using refactored helper
        btn_rect = MenuManager.create_btn_at(self.screen,
                                             "Continue",
                                             self.font,
                                             (0, -100),
                                             22)
        return btn_rect
        
    def show_end_screen(self, score):
        self.screen.fill((133, 87, 50))
        end_text = f"game Over\n\nYour score iss {score}"
        end_surf = self.font.render(end_text, True, MenuConfig.RED)
        end_rect = end_surf.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(end_surf, end_rect)
        
        
    def _draw_text_with_shadow(self, text, pos, color=MenuConfig.WHITE, shadow_offset=(1, 2)):
        """Helper to draw text with shadow for readability. pos should be a pygame alignment tuple like midtop."""
        text_surf = self.font.render(text, True, color)
        text_rect = text_surf.get_rect(**{pos[0]: (pos[1][0], pos[1][1])})
        
        # Draw shadow
        shadow_surf = self.font.render(text, True, MenuConfig.BLACK)
        shadow_rect = shadow_surf.get_rect(**{pos[0]: (pos[1][0] + shadow_offset[0], pos[1][1] + shadow_offset[1])})
        self.screen.blit(shadow_surf, shadow_rect)
        
        # Draw text
        self.screen.blit(text_surf, text_rect)
        
    def draw_score(self, score):
        """Draw score in top-left with shadow."""
        self._draw_text_with_shadow(f"{score}", ("midtop", (20, 10)))
        
    def draw_timer(self, start_ticks):
        """Draw countdown timer at top-center with shadow. Returns remaining seconds."""
        elapsed_ms = pygame.time.get_ticks() - start_ticks
        remaining = max(0, self.TIMER_SECONDS - (elapsed_ms / 1000.0))
        timer_text = self.get_remaining_time_str_in_secs(remaining)
        self._draw_text_with_shadow(timer_text, ("midtop", (self.width // 2, 10)))
        return remaining
    
    def draw_deaths(self, deaths=0):
        """Draw score in top-left with shadow."""
        self._draw_text_with_shadow(f"deaths:{deaths}", ("midtop", (self.width -90, 10)))
    
    def show_start_menu(self):
        """
    Draw the end-of-level screen and a Continue button.
    Returns the pygame.Rect of the Continue button so caller can detect clicks.
    """
        self.screen.fill((223, 237, 149))
        # Draw two lines: title and score
        MenuManager.create_text_at(self.screen,
                                   f"Find the Sheep",
                                   self.font,
                                   (0, 120),
                                   50)


        MenuManager.create_text_at(self.screen,
                                   f"Your  job is to find all the lost sheep\nWatchout for sick sheep\nPress space to start",
                                   self.font,
                                   (0, 0),
                                   20)


        btn_rect = MenuManager.create_btn_at(self.screen,
                                             "continue",
                                             self.font,
                                             (0, -120),
                                             30)
        return btn_rect
    
    @staticmethod
    def get_remaining_time_str_in_secs(remaining) -> str:
        mins = int(remaining) // 60
        secs = int(remaining) % 60
        return f"{mins}:{secs:02d}"
    
    @staticmethod
    def create_text_at(screen,
                       text, 
                       font,
                       position: tuple,
                       font_size=20):
        """Draw text at screen center + offset. Position is (x_offset, y_offset)."""
        center_x = screen.get_rect().centerx
        center_y = screen.get_rect().centery
        text_font = pygame.font.SysFont("Arial", font_size)
        text_surf = text_font.render(text, True, MenuConfig.BLACK)
        text_rect = text_surf.get_rect(center=(center_x - position[0], center_y - position[1]))
        screen.blit(text_surf, text_rect)
        
    
    @staticmethod
    def create_btn_at(screen,
                      text,
                      font,
                      position,
                      font_size = 20
                      ):
        """Draw a button at screen center + offset. Returns button rect for click detection."""
        center_x = screen.get_rect().centerx
        center_y = screen.get_rect().centery
        
        # Draw button with size and position
        btn_w, btn_h = 220, 48
        btn_x = center_x - btn_w // 2
        btn_y = center_y - position[1]
        btn_rect = pygame.Rect(btn_x, btn_y, btn_w, btn_h)
        
        # button background
        pygame.draw.rect(screen, (30, 144, 255), btn_rect, border_radius=8)
        # button border
        pygame.draw.rect(screen, (0, 0, 0), btn_rect, width=2, border_radius=8)
        
        # button text
        btn_font = pygame.font.SysFont("Arial", font_size)
        btn_surf = btn_font.render(text, True, (0, 0, 0))
        btn_text_rect = btn_surf.get_rect(center=btn_rect.center)
        screen.blit(btn_surf, btn_text_rect)
        
        return btn_rect