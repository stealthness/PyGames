import pygame


SCREEN_WIDTH = 960
SCREEN_HEIGHT = 600
ART_SCALE = 4

FPS = 60

# Human tuning values.
HUMAN_BOTTOM_OFFSET = 50
HUMAN_GRAVITY = 0.8
HUMAN_JUMP_VELOCITY = -14
HUMAN_MAX_FALL_SPEED = 16
HUMAN_START_LIVES = 3
HUMAN_INVULNERABILITY_FRAMES = 45
HUMAN_HITBOX_INSET_X = 12
HUMAN_HITBOX_INSET_Y = 8

game_background = pygame.image.load('Hidden/Art/Backgrounds/game_background.png')

_human_base_image = pygame.image.load('Hidden/Art/Human/deserted_islander1.png')
human_default_image = pygame.transform.scale(
	_human_base_image,
	(_human_base_image.get_width() * ART_SCALE, _human_base_image.get_height() * ART_SCALE),
)
