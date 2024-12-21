import pygame
import random
import math

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


class Player:
    def __init__(self):
        self.image = pygame.image.load("../Art/player.png")
        self.x = 370
        self.y = 480
        self.change_x = 0

    def update(self):
        self.x += self.change_x
        self.x = max(0, min(SCREEN_WIDTH - 64, self.x))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def reset(self):
        self.x = 370
        self.y = 480
        self.change_x = 0

    def is_collision(self, ex, ey):
        return math.sqrt((math.pow(self.x - ex, 2)) + (math.pow(self.y - ey, 2))) < 27


class Bullet:
    def __init__(self):
        self.image = pygame.image.load("../Art/bullet.png")
        self.x = 0
        self.y = 480
        self.change_y = 10
        self.state = "ready"

    def fire(self, player_x):
        self.state = "fire"
        self.x = player_x
        self.y = 480

    def update(self):
        if self.state == "fire":
            self.y -= self.change_y
            if self.y <= 0:
                self.reset()

    def draw(self, screen):
        if self.state == "fire":
            screen.blit(self.image, (self.x + 16, self.y + 10))

    def reset(self):
        self.state = "ready"
        self.y = 480

    def is_collision(self, ex, ey):
        return math.sqrt((math.pow(self.x - ex, 2)) + (math.pow(self.y - ey, 2))) < 27


class EnemyManager:
    def __init__(self):
        self.rows = 5
        self.cols = 10
        self.initial_speed = 0.3
        self.speed_increment = 0.1
        self.current_speed = self.initial_speed
        self.direction = 1
        self.drop_rate = 8
        self.reset()

    def reset(self):
        self.x = [50 + col * 70 for row in range(self.rows) for col in range(self.cols)]
        self.y = [50 + row * 50 for row in range(self.rows) for col in range(self.cols)]
        self.change_x = [self.initial_speed * self.direction for _ in range(self.rows * self.cols)]
        self.active = [True] * (self.rows * self.cols)
        self.current_speed = self.initial_speed

    def update(self, bullet, player):
        active_enemy_count = 0
        reverse_direction = False

        for i in range(len(self.x)):
            if self.active[i]:
                active_enemy_count += 1
                self.x[i] += self.change_x[i] * self.direction

                if self.x[i] <= 0 or self.x[i] >= 736:
                    reverse_direction = True

                if bullet.is_collision(self.x[i], self.y[i]):
                    bullet.reset()
                    self.active[i] = False

                if player.is_collision(self.x[i], self.y[i]):
                    player.game_over = True

        if reverse_direction:
            self.direction *= -1
            for j in range(len(self.y)):
                self.y[j] += self.drop_rate

        if active_enemy_count < len(self.x):
            self.current_speed = self.initial_speed + (len(self.x) - active_enemy_count) * self.speed_increment
            for i in range(len(self.change_x)):
                self.change_x[i] = self.current_speed

    def draw(self, screen):
        for i in range(len(self.x)):
            if self.active[i]:
                screen.blit(pygame.image.load("../Art/enemy.png"), (self.x[i], self.y[i]))

    def all_inactive(self):
        return all(not active for active in self.active)


if __name__ == "__main__":
    game = Game()
    game.run()