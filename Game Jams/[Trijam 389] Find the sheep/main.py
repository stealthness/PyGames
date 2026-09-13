import asyncio
import pygame


# --------------------------------------------------
# Configuration
# --------------------------------------------------

WIDTH = 960# Load the background image
background = pygame.image.load("Art/background.png")
HEIGHT = 540
FPS = 60
TEST_MODE = True

TITLE = "A Simple Pygame outline"


# --------------------------------------------------
# Initialization
# --------------------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

active_boxes = []

# --------------------------------------------------
# Game State
# --------------------------------------------------

running = True

# --------------------------------------------------
# Async Game Loop
# --------------------------------------------------

async def main():
    global running

    while running:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False        
        
        
        # Draw the background
        screen.blit(background, (0, 0))
        if (TEST_MODE):
            pass
        
        # Display the new screen
        pygame.display.flip()
        
        await asyncio.sleep(0)

    pygame.quit()


# --------------------------------------------------
# Entry Point
# --------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())