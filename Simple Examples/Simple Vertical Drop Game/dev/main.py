import asyncio

import pygame
from player_class import Player


# --------------------------------------------------
# Configuration
# --------------------------------------------------

WIDTH = 960
HEIGHT = 540
FPS = 60
TITLE = "My Pygame Game"


# --------------------------------------------------
# Player
# --------------------------------------------------




# --------------------------------------------------
# Game
# --------------------------------------------------

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(
            WIDTH // 2 - 25,
            HEIGHT // 2 - 25,
            )

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self, dt):
        self.player.update(
            dt,
            self.screen.get_rect(),
        )

    def draw(self):
        self.screen.fill((20, 20, 30))

        self.player.draw(self.screen)

        pygame.display.flip()

    async def run(self):
        while self.running:

            self.handle_events()

            # Convert milliseconds to seconds.
            dt = self.clock.tick(FPS) / 1000.0

            self.update(dt)
            self.draw()

            # Yield to the browser/event loop.
            await asyncio.sleep(0)

        pygame.quit()


# --------------------------------------------------
# Entry Point
# --------------------------------------------------

async def main():
    game = Game()
    await game.run()


if __name__ == "__main__":
    asyncio.run(main())