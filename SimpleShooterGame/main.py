import pygame
from pygame import Vector2

from SimpleShooterGame.enemy_class import Solder

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Shooter Game')

class Scene:
    def __init__(self):
        self.enemies = []

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def update(self):
        for enemy in self.enemies:
            enemy.draw(screen)


def init(scene):

    player = Solder(100, 100, 2)
    enemy = Solder(200, 100, 2)
    scene.add_enemy(player)
    scene.add_enemy(enemy)

def run():
    is_running = True
    scene = Scene()
    init(scene)

    dir = Vector2(0, 0)

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    is_running = False
                if event.key == pygame.K_a:
                    dir.x = -1
                if event.key == pygame.K_d:
                    dir.x = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    dir.x = 0
                if event.key == pygame.K_d:
                    dir.x = 0

        screen.fill((255, 255, 255))

        scene.enemies[0].move(dir)

        for enemy in scene.enemies:
            enemy.draw(screen)

        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == '__main__':
    run()
    pygame.quit()
    exit(0)