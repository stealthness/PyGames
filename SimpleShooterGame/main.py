import pygame

from SimpleShooterGame.enemy_class import Solder

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Shooter Game')

player = Solder(100, 100, 2)

enemy = Solder(200, 100, 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    screen.blit(player.image, player.rect)
    screen.blit(enemy.image, enemy.rect)

    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(60)

if __name__ == '__main__':
    pass