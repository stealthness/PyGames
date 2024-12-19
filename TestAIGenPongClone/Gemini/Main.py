import pygame

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

# Initial positions
player_pos = height // 2 - paddle_height // 2
opponent_pos = height // 2 - paddle_height // 2
ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2

# Ball speed
ball_speed_x, ball_speed_y = 3, 3

# Game speed control
game_speed = 60  # Frames per second

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Cap the frame rate
    clock.tick(game_speed)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos > 0:
        player_pos -= 5
    if keys[pygame.K_s] and player_pos < height - paddle_height:
        player_pos += 5

    # Opponent AI (simple)
    if ball_y > opponent_pos + paddle_height // 2:
        opponent_pos += 5
    if ball_y < opponent_pos + paddle_height // 2:
        opponent_pos -= 5

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (ball_x <= paddle_width and ball_y >= player_pos and ball_y <= player_pos + paddle_height) or (
            ball_x >= width - paddle_width - ball_size and ball_y >= opponent_pos and ball_y <= opponent_pos + paddle_height):
        ball_speed_x *= -1

    # Game over (simplified)
    if ball_x < 0 or ball_x > width:
        ball_x, ball_y = width // 2 - ball_size // 2, height // 2 - ball_size // 2

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, white, (0, player_pos, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (width - paddle_width, opponent_pos, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))
    pygame.display.flip()

# Quit Pygame
pygame.quit()