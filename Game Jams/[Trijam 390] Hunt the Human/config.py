import pygame


SCREEN_WIDTH = 960
SCREEN_HEIGHT = 600
ART_SCALE = 4

FPS = 60

game_background = pygame.image.load('Hidden/Art/Backgrounds/game_background.png')

_human_base_image = pygame.image.load('Hidden/Art/Human/deserted_islander1.png')
human_default_image = pygame.transform.scale(
	_human_base_image,
	(_human_base_image.get_width() * ART_SCALE, _human_base_image.get_height() * ART_SCALE),
)
