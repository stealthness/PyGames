import pygame

from SimpleClickerGame.candy_cane import CandyCane

WHITE = (255, 255, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

class CandyCaneManager:
    def __init__(self, score):
        self.candy_list = []
        for _ in range(4):
            self.candy_list.append(CandyCane())
        self.score = score

    def increase_score(self, score, screen):
        self.score = self.score + 1

    def update_score(self, screen):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        text_rect = score_text.get_rect(center=( SCREEN_WIDTH // 2 - 10, SCREEN_HEIGHT - 100))
        screen.blit(score_text, text_rect)

    def update(self, screen, point):
        for candy in self.candy_list:
            if point is not None:
                print(f'point: {point}')
                if candy.point_collided(point):
                    self.increase_score(1, screen)
                    self.score += 1
                    self.update_score(screen)
                else:
                    pass
                    
                
            else:
                candy.update()
                candy.draw(screen)
