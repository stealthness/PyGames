import os

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60
BALL_SIZE = 15
LINE_WIDTH = 2
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
paddle1_speed = 5

# Paddle 2
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2_speed = 5

# Ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed = [4 * random.choice((1, -1)), 4 * random.choice((1, -1))]

# Score
score1 = 0
score2 = 0
font = pygame.font.Font("ObelusCompact.ttf", 72)

# Winning score
winning_score = 5

# Title Splash Screen
title_font = pygame.font.Font("ObelusCompact.ttf", 250)
title_text = title_font.render("Pong", True, WHITE)
title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT * 1 // 3))

# Main splash screen loop
splash_screen = True
screen.fill(BLACK)
screen.blit(title_text, title_rect)
pygame.display.flip()
pygame.time.wait(2000)





while splash_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            splash_screen = False
    clock.tick(FPS)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle1_speed
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += paddle1_speed
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= paddle2_speed
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += paddle2_speed

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Ball collisions with paddles
    if ball.colliderect(paddle1):
        ball_speed[0] = -ball_speed[0]
    elif ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]

    # Check if the ball goes out of bounds
    if ball.left <= 0:
        score2 += 1
        ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        if score2 == winning_score:
            win_message = font.render("Player 2 wins!", True, WHITE)
            screen.blit(win_message,
                        (WIDTH // 2 - win_message.get_width() // 2, HEIGHT // 2 - win_message.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(2000)  # Pause for 2 seconds
            win_message = font.render("Press R to Replay", True, WHITE)
            score1 = 0
            score2 = 0
            ball_speed = [0, 0]
        else:
            ball_speed = [4 * random.choice((1, -1)), 4 * random.choice((1, -1))]
    elif ball.right >= WIDTH:
        score1 += 1
        ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        if score1 == winning_score:
            win_message = font.render("Player 1 wins!", True, WHITE)
            screen.blit(win_message,
                        (WIDTH // 2 - win_message.get_width() // 2, HEIGHT // 2 - win_message.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(2000)  # Pause for 2 seconds
            win_message = font.render("Press R to Replay", True, WHITE)
            score1 = 0
            score2 = 0
            ball_speed = [0, 0]
        else:
            ball_speed = [4 * random.choice((1, -1)), 4 * random.choice((1, -1))]

    # Draw everything
    screen.fill(BLACK)

    # Draw dashed line down the middle
    for y in range(0, HEIGHT, 20):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - LINE_WIDTH // 2, y, LINE_WIDTH, 10))

    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw the score
    score_display = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - score_display.get_width() // 2, 10))

    # Check for replay
    if keys[pygame.K_r]:
        score1 = 0
        score2 = 0
        ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        ball_speed = [4 * random.choice((1, -1)), 4 * random.choice((1, -1))]

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)