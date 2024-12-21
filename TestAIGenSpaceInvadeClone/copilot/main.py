import pygame

from TestAIGenSpaceInvadeClone.copilot.bullet import Bullet
from TestAIGenSpaceInvadeClone.copilot.enemy_manager import EnemyManager
from TestAIGenSpaceInvadeClone.copilot.player import Player

# Initialize Pygame
pygame.init()

# Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("(Copilot) Space Invaders")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.running = True
        self.game_over = False
        self.score = 0
        self.player = Player()
        self.bullet = Bullet()
        self.enemies = EnemyManager()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.change_x = -5
                if event.key == pygame.K_RIGHT:
                    self.player.change_x = 5
                if event.key == pygame.K_SPACE and self.bullet.state == "ready":
                    self.bullet.fire(self.player.x)
                if event.key == pygame.K_r and self.game_over:
                    self.reset_game()
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    self.player.change_x = 0

    def update(self):
        if not self.game_over:
            self.player.update()
            self.bullet.update()
            self.enemies.update(self.bullet, self.player)
            self.check_collisions()
            if self.enemies.all_inactive():
                self.enemies.reset()
        else:
            self.show_game_over()

    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        self.bullet.draw(self.screen)
        self.enemies.draw(self.screen)
        self.show_score()
        pygame.display.update()

    def check_collisions(self):
        for i, (ex, ey, active) in enumerate(zip(self.enemies.x, self.enemies.y, self.enemies.active)):
            if active and self.bullet.is_collision(ex, ey):
                self.bullet.reset()
                self.score += 1
                self.enemies.active[i] = False
            if active and self.player.is_collision(ex, ey):
                self.game_over = True

    def show_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        text_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        self.screen.blit(score_text, text_rect)

    def show_game_over(self):
        game_over_text = self.font.render("Game Over! Press R to Restart", True, RED)
        self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 20))

    def reset_game(self):
        self.game_over = False
        self.score = 0
        self.player.reset()
        self.bullet.reset()
        self.enemies.reset()


if __name__ == "__main__":
    game = Game()
    game.run()