import pygame


SCREEN_WIDTH = 960
SCREEN_HEIGHT = 600
ART_SCALE = 4

FPS = 60
# Debug and test mode settings.
TEST_MODE_DEFAULT = False
TEST_MODE_TOGGLE_KEY = pygame.K_F1
TEST_MODE_HITBOX_COLOR = (255, 0, 0)
TEST_MODE_HITBOX_WIDTH = 2

MUSIC_VOLUME = 0.5
MUSIC_TOGGLE_KEY = pygame.K_m
MUSIC_PATH = "Hidden/Sound/331music-comedy-cinematic-cartoon-603031.ogg"

# Background movement tuning.
BACKGROUND_SCROLL_SPEED = 1
BACKGROUND_RECYCLE_THRESHOLD = 100

# Human tuning values.
HUMAN_BOTTOM_OFFSET = 60
HUMAN_GRAVITY = 0.2
HUMAN_JUMP_VELOCITY = -10
HUMAN_MAX_FALL_SPEED = 6
HUMAN_START_LIVES = 3
HUMAN_INVULNERABILITY_MS = 2000
HUMAN_HITBOX_INSET_X = 12
HUMAN_HITBOX_INSET_Y = 8
HUMAN_HITBOX_WIDTH_SCALE = 0.5
HUMAN_WALK_FRAME_COUNT = 11
HUMAN_WALK_FRAME_MS = 100
HUMAN_PLATFORM_LAND_TOLERANCE = 10

# Human controls (rebindable key groups).
HUMAN_KEYS_JUMP = (pygame.K_SPACE, pygame.K_w)
HUMAN_KEYS_HIDE = (pygame.K_s, pygame.K_DOWN)
HUMAN_KEYS_CLIMB = (pygame.K_UP,)
HUMAN_KEYS_MOVE_LEFT = (pygame.K_a, pygame.K_LEFT)
HUMAN_KEYS_MOVE_RIGHT = (pygame.K_d, pygame.K_RIGHT)

# Fox tuning values.
FOX_BOTTOM_OFFSET = 60
FOX_START_X = SCREEN_WIDTH + 220
FOX_SPEED = 4
FOX_MAX_SPEED = 8
FOX_HITBOX_INSET_X = 15
FOX_HITBOX_INSET_Y = 10
FOX_SPAWN_INTERVAL_START_MS = 5000
FOX_SPAWN_INTERVAL_MIN_MS = 3000
FOX_SPAWN_INTERVAL_DECREASE_MS = 50
FOX_SPAWN_INTERVAL_VARIATION_MS = 150
FOX_RIDING_FRAME_COUNT = 4
FOX_RIDING_FRAME_MS = 120

game_background = pygame.image.load('Hidden/Art/Backgrounds/game_background_2.png')
game_background2 = pygame.image.load('Hidden/Art/Backgrounds/game_background_3.png')
game_background3 = pygame.image.load('Hidden/Art/Backgrounds/game_background_4.png')
GAME_BACKGROUNDS = [game_background, game_background2, game_background3]

# Menu and splash backgrounds.
splash_background = pygame.image.load('Hidden/Art/Backgrounds/HuntTheHuman-GameMenuBackgroundv2.png')
end_game_background = pygame.image.load('Hidden/Art/Backgrounds/HuntTheHuman-EndGameBackground.png')

# UI tuning.
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 50
BUTTON_PLAY_COLOR = (150, 0, 0)
BUTTON_PLAY_HOVER_COLOR = (250, 0, 0)
BUTTON_PLAY_TEXT_COLOR = (255,255,255)
BUTTON_END_COLOR = (150, 0, 0)
BUTTON_END_HOVER_COLOR = (250, 0, 0)
BUTTON_END_TEXT_COLOR = (255,255,255)

_ui_active_heart_base = pygame.image.load('Hidden/Art/Fluff/Heart1.png')
_ui_inactive_heart_base = pygame.image.load('Hidden/Art/Fluff/Heart4.png')
ui_heart_active_image = pygame.transform.scale(
	_ui_active_heart_base,
	(_ui_active_heart_base.get_width() * ART_SCALE//2, _ui_active_heart_base.get_height() * ART_SCALE //2),
)
ui_heart_inactive_image = pygame.transform.scale(
	_ui_inactive_heart_base,
	(_ui_inactive_heart_base.get_width() * ART_SCALE//2, _ui_inactive_heart_base.get_height() * ART_SCALE//2),
)

# Wall tuning values.
WALL_COLOR = (139, 69, 19)
WALL_SPAWN_INTERVAL_MS = 8000
WALL_SPAWN_INTERVAL_MIN_MS = 3000
WALL_SPAWN_INTERVAL_DECREASE_MS = 50
WALL_SPAWN_INTERVAL_VARIATION_MS = 500

WALL_SPAWN_X = SCREEN_WIDTH + 50
WALL_VERTICAL_OFFSET = 50

_wall_base_image = pygame.image.load('Hidden/Art/Fluff/wall.png')
wall_image = pygame.transform.scale(
	_wall_base_image,
	(_wall_base_image.get_width() * ART_SCALE, _wall_base_image.get_height() * ART_SCALE),
)
WALL_WIDTH = wall_image.get_width()
WALL_HEIGHT = wall_image.get_height()

_human_walk_frames_unscaled = [
	pygame.image.load(f'Hidden/Art/Human/deserted_islander_running{index}.png')
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

_fox_riding_frames_unscaled = [
	pygame.image.load(f'Hidden/Art/FoxOnHorse/fox_riding{index}.png')
	for index in range(1, FOX_RIDING_FRAME_COUNT + 1)
]


_fox_image= pygame.image.load('Hidden/Art/FoxOnHorse/Fox.png')
fox_image = pygame.transform.scale(
	_fox_image,
	(_fox_image.get_width() * ART_SCALE, _fox_image.get_height() * ART_SCALE),
)

# fox_riding_frames = [fox_image, fox_image, fox_image, fox_image]
fox_riding_frames = [
	pygame.transform.scale(
		frame,
		(frame.get_width() * ART_SCALE, frame.get_height() * ART_SCALE),
	)
	for frame in _fox_riding_frames_unscaled
]