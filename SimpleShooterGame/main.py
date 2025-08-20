import pygame
from pygame import Vector2

from SimpleShooterGame.enemy_class import Solder

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Shooter Game')

'''
This class represents the game scene, which contains all the game objects.
It manages the enemies and updates their states.
'''
class Scene:
    def __init__(self):
        self.enemies = []

    '''
    Adds an enemy to the scene.
    :param enemy: An instance of Solder or any other enemy class.
    '''
    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    '''
    Updates the scene by drawing all items in scene.
    '''
    def update(self):
        for enemy in self.enemies:
            enemy.draw(screen)

'''
Initializes the game scene with player and enemy instances.
'''
def init(scene):

    player = Solder(100, 100, 2)
    enemy = Solder(200, 100, 2, image='Art/misc/simplePlayer.png')
    scene.add_enemy(player)
    scene.add_enemy(enemy)

'''
The main game loop that handles events, updates the scene, 
and draws everything on the screen.
'''
def run():
    is_running = True
    scene = Scene()
    init(scene)

    _dir = Vector2(0, 0)

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    is_running = False
                if event.key == pygame.K_a:
                    _dir.x = -1
                if event.key == pygame.K_d:
                    _dir.x = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    _dir.x = 0
                if event.key == pygame.K_d:
                    _dir.x = 0

        draw_background()

        scene.enemies[0].move(_dir)

        for enemy in scene.enemies:
            enemy.draw(screen)

        pygame.display.flip()
        pygame.display.update()
        pygame.time.Clock().tick(60)

'''
Draws the background of the game screen.
'''
def draw_background():
    screen.fill((255, 255, 255))


if __name__ == '__main__':
    run()
    pygame.quit()
    exit(0)