import pygame


SCREEN_WIDTH = 960
SCREEN_HEIGHT = 600
ART_SCALE = 4

FPS = 60

# Background movement tuning.
BACKGROUND_SCROLL_SPEED = 1
BACKGROUND_RECYCLE_THRESHOLD = 100

# Human tuning values.
HUMAN_BOTTOM_OFFSET = 60
HUMAN_GRAVITY = 0.2
HUMAN_JUMP_VELOCITY = -10
HUMAN_MAX_FALL_SPEED = 6
HUMAN_START_LIVES = 3
HUMAN_INVULNERABILITY_FRAMES = 45
HUMAN_HITBOX_INSET_X = 12
HUMAN_HITBOX_INSET_Y = 8
HUMAN_WALK_FRAME_COUNT = 11
HUMAN_WALK_FRAME_TICKS = 6

# Human controls (rebindable key groups).
HUMAN_KEYS_JUMP = (pygame.K_SPACE, pygame.K_w)
HUMAN_KEYS_HIDE = (pygame.K_s, pygame.K_DOWN)
HUMAN_KEYS_CLIMB = (pygame.K_UP,)
HUMAN_KEYS_MOVE_LEFT = (pygame.K_a, pygame.K_LEFT)
HUMAN_KEYS_MOVE_RIGHT = (pygame.K_d, pygame.K_RIGHT)

game_background = pygame.image.load('Hidden/Art/Backgrounds/game_background.png')
GAME_BACKGROUNDS = [game_background, game_background, game_background]

_human_walk_frames_unscaled = [
	pygame.image.load(f'Hidden/Art/Human/deserted_islander{index}.png')
	for index in range(1, HUMAN_WALK_FRAME_COUNT + 1)
]
human_walk_frames = [
	pygame.transform.scale(
		frame,
		(frame.get_width() * ART_SCALE, frame.get_height() * ART_SCALE),
	)
	for frame in _human_walk_frames_unscaled
]
human_default_image = human_walk_frames[0]
