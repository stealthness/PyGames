import sys

import pygame
from pygame import Vector2

from _Scripts.entities import PhysicsEntity


class Game:
    def __init__(self):
        pygame.init()
        self.BACKGROUND_Color = (200, 200, 250)
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('DaFluffyPotato Tutorial')
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.dt = 1
        self.img = pygame.image.load('data/Art/clouds/cloud_1.png').convert_alpha()
        self.movement = [False, False, False, False]
        self.img_pos = [100, 100]
        self.collision_area = pygame.Rect(200, 200, 80, 80)
        self.player = PhysicsEntity(self, 'player', (100, 100), (32, 32))
        self.entities = [self.player]

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
                        
                        
                      
            self.screen.fill(self.BACKGROUND_Color)
            # r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            r = pygame.Rect(*self.player.pos, *self.player.size)
            
            if r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (255, 200, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (255, 255, 255), self.collision_area)

            vel = Vector2(self.movement[1] - self.movement[0],  self.movement[3] - self.movement[2])
            self.player.velocity = vel
            
            for entity in self.entities:
                entity.update()
                entity.render(self.screen)
        
            self.screen.blit(self.img, self.img_pos)
            self.screen.blit(self.img, (200, 200))
            pygame.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
