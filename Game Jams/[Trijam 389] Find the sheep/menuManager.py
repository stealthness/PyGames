import pygame


class MenuManager:
    
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 20)
        self.TIMER_SECONDS = 30
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
    
        
        
    def show_end_screen(self, score):
        self.screen.fill((0,0,0))
        end_text = "game Over"
        end_surf = self.font.render(end_text, True, (255, 0, 0))
        end_rect = end_surf.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(end_surf, end_rect)
        
        
    def draw_score(self, score):
        text_surf = self.font.render(f"{score}", True, (255, 255, 255))
        text_rect = text_surf.get_rect(midtop=(20, 10))
        # optional shadow for readability
        shadow_surf = self.font.render(f"{score}", True, (0, 0, 0))
        shadow_rect = shadow_surf.get_rect(midtop=(21, 12))
        self.screen.blit(shadow_surf, shadow_rect)
        self.screen.blit(text_surf, text_rect)
        
    def draw_timer(self, start_ticks):
        elapsed_ms = pygame.time.get_ticks() - start_ticks
        remaining = max(0, self.TIMER_SECONDS - (elapsed_ms / 1000.0))
        mins = int(remaining) // 60
        secs = int(remaining) % 60
        timer_text = f"{mins}:{secs:02d}"
        text_surf = self.font.render(timer_text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(midtop=(self.width // 2, 10))
        # optional shadow for readability
        shadow_surf = self.font.render(timer_text, True, (0, 0, 0))
        shadow_rect = shadow_surf.get_rect(midtop=(self.width // 2 + 2, 12))
        self.screen.blit(shadow_surf, shadow_rect)
        self.screen.blit(text_surf, text_rect)
        return remaining
    
    def show_start_menu(self):
        # add start screen with start button and exit application button
        pass