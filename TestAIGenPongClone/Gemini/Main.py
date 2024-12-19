import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 700, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle dimensions
paddle_width, paddle_height = 10, 100

# Ball dimensions
ball_size = 20

# Game speed control
game_speed = 60  # Frames per second

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Font for title screen
font = pygame.font.Font(None, 36)

# Create game objects
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = paddle_width
        self.height = paddle_height

    def draw(self):
        pygame.draw.rect(screen, white, (self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self):
        self.x = width // 2 - ball_size // 2
        self.y = height // 2 - ball_size // 2
        self.speed_x = random.choice([-3, 3])
        self.speed_y = random.choice([-3, 3])
        self.size = ball_size

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Wall collisions
        if self.y <= 0 or self.y >= height - self.size:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.ellipse(screen, white, (self.x, self.y, self.size, self.size))

# Create game objects
player = Paddle(0, height // 2 - paddle_height // 2)
opponent = Paddle(width - paddle_width, height // 2 - paddle_height // 2)
ball = Ball()

# Title screen
def show_title_screen():
    screen.fill(black)
    title_text = font.render("Pong", True, white)
    title_rect = title_text.get_rect(center=(width // 2, height // 4))
    screen.blit(title_text, title_rect)

    start_text = font.render("Press any key to start", True, white)
    start_rect = start_text.get_rect(center=(width // 2, height // 2))
    screen.blit(start_text, start_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    return

# Game loop
show_title_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player.y > 0:
        player.y -= 5
    if keys[pygame.K_s] and player.y < height - player.height:
        player.y += 5

    # Opponent AI (simple)
    if ball.y > opponent.y + opponent.height // 2:
        opponent.y += 5
    if ball.y < opponent.y + opponent.height // 2:
        opponent.y -= 5

    # Ball movement and collisions
    ball.update()

    # Paddle collisions
    if (ball.x <= player.x + player.width and ball.y >= player.y and ball.y <= player.y + player.height) or (
            ball.x >= opponent.x - ball.size and ball.y >= opponent.y and ball.y <= opponent.y + opponent.height):
        ball.speed_x *= -1

    # Game over (simplified)
    if ball.x < 0 or ball.x > width:
        ball.x = width // 2 - ball.size // 2
        ball.y = height // 2 - ball.size // 2
        ball.speed_x = random.choice([-3, 3])  # Randomize direction on reset

    # Draw everything
    screen.fill(black)
    player.draw()
    opponent.draw()
    ball.draw()
    pygame.draw.line(screen, white, (width // 2, 0), (width // 2, height))  # Center line
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(game_speed)