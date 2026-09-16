from enum import Enum


class GameStatus(str, Enum):
    MENU = "menu"
    INIT_GAME = "init_game"
    PLAYING = "playing"
    GAME_OVER = "game_over"
    QUIT = "quit"
