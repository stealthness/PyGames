import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60
BALL_SIZE = 15
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Paddle 1
paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Paddle 2
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed = [4 * random.choice((1, -1)), 4 * random.choice((1, -1))]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= 5
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += 5
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= 5
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += 5

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Ball collisions with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]

    # Check if the ball goes out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        ball_speed = [4 * random.choice((1, -1)), 4 * random.choice((1, -1))]

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)