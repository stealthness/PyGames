# Game Configuration
WIDTH = 960
HEIGHT = 540
FPS = 60
TITLE = "Find the Sheep"

# Game Parameters
TIMER_SECONDS = 4
MAX_STRIKES = 3
STARTING_SHEEP_COUNT = 5
DIFFICULTY_SCALING = 3  # sheep per level

# Timers (milliseconds)
SICK_SHEEP_DELAY_MIN = 800
SICK_SHEEP_DELAY_MAX = 2500
LEVEL_TRANSITION_TIMEOUT = 8000

# Menu Exclusion Zone (where sheep don't spawn)
MENU_EXCLUSION_ZONE = ((400, 500), (100, 300))

# TEST_MODE
TEST_MODE = False
