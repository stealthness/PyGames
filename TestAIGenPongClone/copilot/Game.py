import pygame

from TestAIGenPongClone.copilot.Ball import Ball
from TestAIGenPongClone.copilot.Paddle import Paddle


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("(Copilot) Pong")
        self.clock = pygame.time.Clock()
        self.running = True
        self.ball = Ball()
        self.player_paddle = Paddle(50, 300)
        self.opponent_paddle = Paddle(750, 300)
        self.player_score = 0
        self.opponent_score = 0
        self.font = pygame.font.Font(None, 36)

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
                if event.key == pygame.K_UP:
                    self.player_paddle.move_up()
                if event.key == pygame.K_DOWN:
                    self.player_paddle.move_down()
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    self.player_paddle.stop()

    def update(self):
        self.ball.update()
        self.player_paddle.update()
        self.opponent_paddle.update()

        # Ball collision with paddles
        if self.ball.rect.colliderect(self.player_paddle.rect) or self.ball.rect.colliderect(self.opponent_paddle.rect):
            self.ball.speed_x *= -1

        # Ball out of bounds
        if self.ball.rect.left <= 0:
            self.opponent_score += 1
            self.ball.reset()
        if self.ball.rect.right >= 800:
            self.player_score += 1
            self.ball.reset()

        # Opponent AI
        if self.opponent_paddle.rect.centery < self.ball.rect.centery:
            self.opponent_paddle.move_down()
        else:
            self.opponent_paddle.move_up()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.ball.draw(self.screen)
        self.player_paddle.draw(self.screen)
        self.opponent_paddle.draw(self.screen)
        self.show_score()
        pygame.display.update()

    def show_score(self):
        player_score_text = self.font.render(f"Player: {self.player_score}", True, (255, 255, 255))
        opponent_score_text = self.font.render(f"Opponent: {self.opponent_score}", True, (255, 255, 255))
        self.screen.blit(player_score_text, (20, 20))
        self.screen.blit(opponent_score_text, (600, 20))

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()