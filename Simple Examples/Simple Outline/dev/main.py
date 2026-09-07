'''
This code was partially constructed using chatgpt.
'''

import asyncio
import pygame


# --------------------------------------------------
# Configuration
# --------------------------------------------------

WIDTH = 960
HEIGHT = 540
FPS = 60

TITLE = "A Simple Pygame outline"


# --------------------------------------------------
# Initialization
# --------------------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()


# --------------------------------------------------
# Game State
# --------------------------------------------------

running = True

# Player create at the Centre with size of 50 pixels
player = pygame.Rect(
    WIDTH // 2 - 25,
    HEIGHT // 2 - 25,
    50,
    50,
    )

player_speed = 300  # pixels per second


# --------------------------------------------------
# Input
# --------------------------------------------------

def handle_events():
    global running

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


# --------------------------------------------------
# Update
# --------------------------------------------------

def update(dt):
    keys = pygame.key.get_pressed()

    movement = pygame.Vector2(0, 0)

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        movement.x -= 1

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        movement.x += 1

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        movement.y -= 1

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        movement.y += 1

    # Prevent diagonal movement from being faster
    if movement.length_squared() > 0:
        movement = movement.normalize()

    player.x += int(movement.x * player_speed * dt)
    player.y += int(movement.y * player_speed * dt)

    # Keep player inside the screen
    player.clamp_ip(screen.get_rect())


# --------------------------------------------------
# Drawing
# --------------------------------------------------

def draw():
    # Draw the background
    screen.fill((20, 20, 30))

    # Player
    pygame.draw.rect(
        screen,
        (80, 180, 255),
        player,
    )

    # Example outline
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        player,
        width=2,
    )

    # Display the new screen
    pygame.display.flip()


# --------------------------------------------------
# Async Game Loop
# --------------------------------------------------

async def main():
    global running

    while running:

        # -----------------------------
        # Events
        # -----------------------------
        handle_events()

        # -----------------------------
        # Delta time
        # -----------------------------
        dt = clock.tick(FPS) / 1000.0

        # -----------------------------
        # Game logic
        # -----------------------------
        update(dt)

        # -----------------------------
        # Rendering
        # -----------------------------
        draw()

        # -----------------------------
        # IMPORTANT FOR PYGBAG
        # -----------------------------
        # Give the browser event loop
        # control periodically.
        await asyncio.sleep(0)

    pygame.quit()


# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())