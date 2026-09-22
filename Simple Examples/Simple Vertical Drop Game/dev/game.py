import asyncio

import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, FPS
from player_class import Player

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(
            SCREEN_WIDTH // 2 - 25,
            SCREEN_HEIGHT // 2 - 25,
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

