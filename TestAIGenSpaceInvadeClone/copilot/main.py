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

# Create Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("(Copilot) Space Invaders")

# Load assets
player_img = pygame.image.load("../Art/player.png")
enemy_img = pygame.image.load("../Art/enemy.png")
bullet_img = pygame.image.load("../Art/bullet.png")

# Game Variables
player_x = 370
player_y = 480
player_x_change = 0

rows = 5
cols = 10
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_active = []  # Track if enemies are active

initial_speed = 0.3  # Start slower
speed_increment = 0.1
current_speed = initial_speed

enemy_direction = 1  # Shared direction for all enemies
enemy_drop_rate = 8  # Variable to adjust drop-down amount

for row in range(rows):
    for col in range(cols):
        enemy_x.append(50 + col * 70)
        enemy_y.append(50 + row * 50)
        enemy_x_change.append(initial_speed * enemy_direction)
        enemy_y_change.append(enemy_drop_rate)
        enemy_active.append(True)

bullet_x = 0
bullet_y = 480
bullet_y_change = 10
bullet_state = "ready"

score = 0
font = pygame.font.Font(None, 36)

# Clock for controlling FPS
clock = pygame.time.Clock()

# Functions
def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(obj1_x, obj1_y, obj2_x, obj2_y, distance_threshold):
    distance = math.sqrt((math.pow(obj1_x - obj2_x, 2)) + (math.pow(obj1_y - obj2_y, 2)))
    return distance < distance_threshold

def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def show_game_over():
    game_over_text = font.render("Game Over! Press R to Restart", True, RED)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 20))

# Game Loop
running = True
game_over = False
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
            if event.key == pygame.K_r and game_over:
                # Restart the game
                game_over = False
                score = 0
                player_x = 370
                player_y = 480
                bullet_y = 480
                bullet_state = "ready"
                enemy_x = [50 + col * 70 for row in range(rows) for col in range(cols)]
                enemy_y = [50 + row * 50 for row in range(rows) for col in range(cols)]
                enemy_active = [True] * (rows * cols)
                current_speed = initial_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    if not game_over:
        # Player Movement
        player_x += player_x_change
        player_x = max(0, min(SCREEN_WIDTH - 64, player_x))

        # Enemy Movement
        active_enemy_count = 0
        reverse_direction = False

        for i in range(len(enemy_x)):
            if enemy_active[i]:  # Only update active enemies
                active_enemy_count += 1
                enemy_x[i] += enemy_x_change[i] * enemy_direction

                if enemy_x[i] <= 0 or enemy_x[i] >= 736:
                    reverse_direction = True

                # Collision with bullet
                if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y, 27):
                    bullet_y = 480
                    bullet_state = "ready"
                    score += 1
                    enemy_active[i] = False  # Deactivate the enemy

                # Collision with player
                if is_collision(enemy_x[i], enemy_y[i], player_x, player_y, 27):
                    game_over = True

                enemy(enemy_x[i], enemy_y[i], i)

        if reverse_direction:
            enemy_direction *= -1
            for j in range(len(enemy_y)):
                enemy_y[j] += enemy_drop_rate  # Use adjustable drop rate

        # Increase speed as enemies are killed
        if active_enemy_count < len(enemy_x):
            current_speed = initial_speed + (len(enemy_x) - active_enemy_count) * speed_increment
            for i in range(len(enemy_x_change)):
                enemy_x_change[i] = current_speed

        # Bullet Movement
        if bullet_state == "fire":
            fire_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change

        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"

        player(player_x, player_y)
        show_score()
    else:
        show_game_over()

    pygame.display.update()
    clock.tick(60)

pygame.quit()