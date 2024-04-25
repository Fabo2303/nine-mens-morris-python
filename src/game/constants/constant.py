# Path: src/game/constants/window_constants.py

from enum import Enum


# Constantes para la ventana
class WindowConstants(Enum):
    WIDTH = 540
    HEIGHT = 540
    FPS = 60
    CAPTION = "Nine men's morris"


class MenuConstants(Enum):
    TITLE_WIDTH = 400
    TITLE_HEIGHT = 100
    TITLE_X = (WindowConstants.WIDTH.value - TITLE_WIDTH) / 2
    TITLE_Y = 50
    TITLE_TEXT_X = TITLE_X + 50
    TITLE_TEXT_Y = TITLE_Y + 10
    TITLE_SIZE = 50

    ESCALATED_SIZE = 30

    BUTTON_WIDTH = 300
    BUTTON_HEIGHT = 50
    BUTTON_X = (WindowConstants.WIDTH.value - BUTTON_WIDTH) / 2
    BUTTON_Y = (WindowConstants.HEIGHT.value - BUTTON_HEIGHT) / 2
    BUTTON_TEXT_X = BUTTON_X + 50
    BUTTON_TEXT_Y = BUTTON_Y + 10
    TEXT_SIZE = 30
    BUTTON_SPACING = 70


# Constantes para las figuras
class FigureConstants(Enum):
    BOARD_WIDTH = WindowConstants.WIDTH.value - 40
    BOARD_HEIGHT = WindowConstants.HEIGHT.value - 40
    CIRCLE_RADIUS = 10
    LINE_WIDTH = 4


# Constantes para colores
class ColorConstants(Enum):
    BACKGROUND_COLOR = "#705628"
    BOARD_COLOR = "#e4cb81"
    LINE_COLOR = "black"
    CIRCLE_COLOR = "black"
    POSIBLE_MOVE_COLOR = "green"
    PLAYER_1_COLOR = "white"
    PLAYER_2_COLOR = "black"
    MENU_COLOR = "#a2b3a3"
    TEXT_COLOR = "#333333"
    BUTTON_COLOR = "#4CAF50"


class GameModeConstants(Enum):
    PLAYER_VS_PLAYER = 1
    PLAYER_VS_AI = 2
    AI_VS_AI = 3


class GameDifficultyConstants(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class GamePhaseConstants(Enum):
    SPLASH_MODE = 1
    MOVING_MODE = 2
    FLYING_MODE = 3
    ELIMINATION_MODE = 4
    GAME_OVER = -1


# Constantes del juego
class GameConstants(Enum):
    TOKEN_AVAILABLE = 1
    TOKEN_BLOCK = 0
    SPLASH_MODE = 1
    MOVING_MODE = 2
    FLYING_MODE = 3
    ELIMINATION_MODE = 4
    GAME_OVER = -1
    PLAYER_VS_PLAYER = 1
    PLAYER_VS_AI = 2
