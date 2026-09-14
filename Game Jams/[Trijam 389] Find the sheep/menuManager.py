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
        # Draw two lines: title and score
        title_text = f"Next Level {level}"
        score_text = f"Your current score is {score}"
        title_surf = self.font.render(title_text, True, MenuConfig.BLACK)
        score_surf = self.font.render(score_text, True, MenuConfig.BLACK)
        center_x = self.width // 2
        center_y = self.height // 2
        title_rect = title_surf.get_rect(center=(center_x, center_y - 24))
        score_rect = score_surf.get_rect(center=(center_x, center_y + 4))
        self.screen.blit(title_surf, title_rect)
        self.screen.blit(score_surf, score_rect)

        # Draw a Continue button below the text
        btn_w, btn_h = 220, 48
        btn_x = center_x - btn_w // 2
        btn_y = center_y + 48
        btn_rect = pygame.Rect(btn_x, btn_y, btn_w, btn_h)
        # button background
        pygame.draw.rect(self.screen, (30, 144, 255), btn_rect, border_radius=8)
        # button border
        pygame.draw.rect(self.screen, (0,0,0), btn_rect, width=2, border_radius=8)
        # button text
        btn_font = pygame.font.SysFont("Arial", 22)
        btn_surf = btn_font.render("Continue", True, (0,0,0))
        btn_text_rect = btn_surf.get_rect(center=btn_rect.center)
        self.screen.blit(btn_surf, btn_text_rect)

        return btn_rect
        
    def show_end_screen(self, score):
        self.screen.fill((133, 87, 50))
        end_text = f"game Over\n\nYour score iss {score}"
        end_surf = self.font.render(end_text, True, MenuConfig.RED)
        end_rect = end_surf.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(end_surf, end_rect)
        
        
    def draw_score(self, score):
        text_surf = self.font.render(f"{score}", True, MenuConfig.WHITE)
        text_rect = text_surf.get_rect(midtop=(20, 10))
        # optional shadow for readability
        shadow_surf = self.font.render(f"{score}", True, MenuConfig.BLACK)
        shadow_rect = shadow_surf.get_rect(midtop=(21, 12))
        self.screen.blit(shadow_surf, shadow_rect)
        self.screen.blit(text_surf, text_rect)
        
    def draw_timer(self, start_ticks):
        elapsed_ms = pygame.time.get_ticks() - start_ticks
        remaining = max(0, self.TIMER_SECONDS - (elapsed_ms / 1000.0))
        timer_text = self.get_remaining_time_str_in_secs(remaining)
        text_surf = self.font.render(timer_text, True, MenuConfig.WHITE)
        text_rect = text_surf.get_rect(midtop=(self.width // 2, 10))
        # optional shadow for readability
        shadow_surf = self.font.render(timer_text, True, MenuConfig.BLACK)
        shadow_rect = shadow_surf.get_rect(midtop=(self.width // 2 + 2, 12))
        self.screen.blit(shadow_surf, shadow_rect)
        self.screen.blit(text_surf, text_rect)
        return remaining
    
    def show_start_menu(self):
        """
    Draw the end-of-level screen and a Continue button.
    Returns the pygame.Rect of the Continue button so caller can detect clicks.
    """
        self.screen.fill((223, 237, 149))
        # Draw two lines: title and score
        title_text = f"Find the Sheep"
        descr_text = f"Your  job is to find all the lost sheep\nWatchout for sick sheep\nPress space to start"
        title_surf = self.font.render(title_text, True, MenuConfig.BLACK)
        score_surf = self.font.render(descr_text, True, MenuConfig.BLACK)
        center_x = self.width // 2
        center_y = self.height // 2
        title_rect = title_surf.get_rect(center=(center_x, center_y -200))
        score_rect = score_surf.get_rect(center=(center_x, center_y + 20))
        self.screen.blit(title_surf, title_rect)
        self.screen.blit(score_surf, score_rect)
        # 
        # Draw a Start button below the text
        btn_w, btn_h = 220, 48
        btn_x = center_x - btn_w // 2
        btn_y = center_y + 150
        btn_rect = pygame.Rect(btn_x, btn_y, btn_w, btn_h)
        # button background
        pygame.draw.rect(self.screen, (30, 144, 255), btn_rect, border_radius=8)
        # button border
        pygame.draw.rect(self.screen, (0,0,0), btn_rect, width=2, border_radius=8)
        # button text
        btn_font = pygame.font.SysFont("Arial", 22)
        btn_surf = btn_font.render("Start", True, (0,0,0))
        btn_text_rect = btn_surf.get_rect(center=btn_rect.center)
        self.screen.blit(btn_surf, btn_text_rect)   
        
        return btn_rect
    
    @staticmethod
    def get_remaining_time_str_in_secs(remaining) -> str:
        mins = int(remaining) // 60
        secs = int(remaining) % 60
        return f"{mins}:{secs:02d}"