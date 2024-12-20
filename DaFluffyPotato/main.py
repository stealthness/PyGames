import sys

import pygame
from pygame import Vector2

from DaFluffyPotato._Scripts import utils
from DaFluffyPotato._Scripts.tilemap import Tilemap
from _Scripts.player_class import Player


class Game:
    def __init__(self):
        pygame.init()
        self.BACKGROUND_Color = (200, 200, 250)
        self.DISPLAY_WIDTH = 320
        self.DISPLAY_HEIGHT = 240
        self.SCREEN_SCALE = 4
        self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.screen = pygame.display.set_mode((self.DISPLAY_WIDTH * self.SCREEN_SCALE,
                                               self.DISPLAY_HEIGHT * self.SCREEN_SCALE))
        pygame.display.set_caption('DaFluffyPotato Tutorial')
        self.clock = pygame.time.Clock()
        self.unit = 16
        self.FPS = 60
        self.dt = 1 / self.FPS
        self.movement = [False, False, False, False]
        self.img_pos = [100, 100]
        self.collision_area = pygame.Rect(200, 200, 80, 80)
        self.player = Player(self, 'player', Vector2(100, 100), (32, 32))
        self.assets = {
            'decor': utils.load_images('tiles\\decor'),
            'grass': utils.load_images('tiles\\grass'),
            'stone': utils.load_images('tiles\\stone'),
            
            
        }
        self.entities = [self.player]
        self.tilemap = Tilemap(self, 16)
        print(self.tilemap)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        pygame.init()
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[3] = False

            self.display.fill(self.BACKGROUND_Color)
            r = pygame.Rect(*self.player.pos, *self.player.size)

            if r.colliderect(self.collision_area):
                pygame.draw.rect(self.display, (255, 200, 255), self.collision_area)
            else:
                pygame.draw.rect(self.display, (255, 255, 255), self.collision_area)

            dir = Vector2(float(self.movement[1] - self.movement[0]), float(self.movement[3] - self.movement[2]))
            self.player.move(dir)

            if len(self.tilemap.tiles_around(self.player.pos)) > 0:
                print(self.tilemap.physics_rects_around(self.player.pos))

            for entity in self.entities:
                entity.update(self.tilemap)
                entity.render(self.display)
            self.tilemap.render(self.display)
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
