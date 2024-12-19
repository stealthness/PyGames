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
pygame.display.set_caption("Space Invaders")

# Load assets
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")

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

for row in range(rows):
    for col in range(cols):
        enemy_x.append(50 + col * 70)
        enemy_y.append(50 + row * 50)
        enemy_x_change.append(2)
        enemy_y_change.append(40)
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


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    return distance < 27


def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


# Game Loop
running = True
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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player Movement
    player_x += player_x_change
    player_x = max(0, min(SCREEN_WIDTH - 64, player_x))

    # Enemy Movement
    for i in range(len(enemy_x)):
        if enemy_active[i]:  # Only update active enemies
            enemy_x[i] += enemy_x_change[i]

            if enemy_x[i] <= 0 or enemy_x[i] >= 736:
                enemy_x_change[i] *= -1
                enemy_y[i] += enemy_y_change[i]

            # Collision
            if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
                bullet_y = 480
                bullet_state = "ready"
                score += 1
                enemy_active[i] = False  # Deactivate the enemy

            enemy(enemy_x[i], enemy_y[i], i)

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    player(player_x, player_y)
    show_score()

    pygame.display.update()
    clock.tick(60)
