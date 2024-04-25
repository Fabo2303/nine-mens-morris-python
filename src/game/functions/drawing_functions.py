# Path: src/game/constants/drawing_functions.py

import pygame
from game.classes.Circle import Circle
from game.constants.constant import (
    ColorConstants,
    FigureConstants,
    WindowConstants,
    GameModeConstants,
    MenuConstants,
)
from game.constants.array_constants import positions, horizontal_lines, vertical_lines
import pygame
import math


def draw_square(window, x, y, width, height, color):
    pygame.draw.rect(window, color, (x, y, width, height))


def draw_circle(window, x, y, color):
    pygame.draw.circle(window, color, (x, y), FigureConstants.CIRCLE_RADIUS.value)


def draw_pieces(window, positions, color):
    for pos in positions:
        draw_circle(window, pos[0], pos[1], color)


def draw_lines(window, lines, color):
    for line in lines:
        pygame.draw.line(
            window, color, line[0], line[1], FigureConstants.LINE_WIDTH.value
        )


def draw_table(window):
    BOARD_X = (WindowConstants.WIDTH.value - FigureConstants.BOARD_WIDTH.value) / 2
    BOARD_Y = (WindowConstants.HEIGHT.value - FigureConstants.BOARD_HEIGHT.value) / 2
    draw_square(
        window,
        0,
        0,
        WindowConstants.WIDTH.value,
        WindowConstants.HEIGHT.value,
        ColorConstants.BACKGROUND_COLOR.value,
    )
    draw_square(
        window,
        BOARD_X,
        BOARD_Y,
        FigureConstants.BOARD_WIDTH.value,
        FigureConstants.BOARD_HEIGHT.value,
        ColorConstants.BOARD_COLOR.value,
    )
    draw_pieces(window, positions, ColorConstants.CIRCLE_COLOR.value)
    draw_lines(window, horizontal_lines, ColorConstants.LINE_COLOR.value)
    draw_lines(window, vertical_lines, ColorConstants.LINE_COLOR.value)


def draw_text(text, x, y, width, height, size, text_color, angle=0):
    font = pygame.font.Font("src/resources/font-atomic.ttf", size)
    text_surface = font.render(text, True, text_color)
    text_surface = pygame.transform.rotate(text_surface, angle)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width / 2, y + height / 2)
    return (text_surface, text_rect)


def draw_button(window, text, x, y, width, height, color, text_color, font_size):
    (text_surface, text_rect) = draw_text(
        text, x, y, width, height, font_size, text_color
    )
    rect = pygame.draw.rect(window, color, (x, y, width, height), border_radius=30)
    window.blit(text_surface, text_rect)
    return rect


def draw_title(window, text, x, y, width, height, text_color, font_size):
    (text_surface, text_rect) = draw_text(
        text, x, y, width, height, font_size, text_color
    )
    window.blit(text_surface, text_rect)


def draw_escalated(window, text, x, y, width, height, text_color, font_size, angle):
    (text_surface, text_rect) = draw_text(
        text, x, y, width, height, font_size, text_color, angle
    )
    window.blit(text_surface, text_rect)


def draw_menu_vs(window):
    draw_title(
        window,
        WindowConstants.CAPTION.value.lower(),
        MenuConstants.TITLE_X.value,
        MenuConstants.TITLE_Y.value,
        MenuConstants.TITLE_WIDTH.value,
        MenuConstants.TITLE_HEIGHT.value,
        ColorConstants.TEXT_COLOR.value,
        MenuConstants.TITLE_SIZE.value,
    )
    draw_escalated(
        window,
        "scaled",
        MenuConstants.TITLE_X.value + 200,
        MenuConstants.TITLE_Y.value + 50,
        MenuConstants.TITLE_WIDTH.value,
        MenuConstants.TITLE_HEIGHT.value,
        ColorConstants.TEXT_COLOR.value,
        MenuConstants.ESCALATED_SIZE.value,
        30,
    )
    button_rects = {}
    button_rects[1] = draw_button(
        window,
        GameModeConstants.PLAYER_VS_PLAYER.name.lower(),
        MenuConstants.BUTTON_X.value,
        MenuConstants.BUTTON_Y.value,
        MenuConstants.BUTTON_WIDTH.value,
        MenuConstants.BUTTON_HEIGHT.value,
        ColorConstants.BUTTON_COLOR.value,
        ColorConstants.TEXT_COLOR.value,
        MenuConstants.TEXT_SIZE.value,
    )
    button_rects[2] = draw_button(
        window,
        GameModeConstants.PLAYER_VS_AI.name.lower(),
        MenuConstants.BUTTON_X.value,
        MenuConstants.BUTTON_Y.value + MenuConstants.BUTTON_SPACING.value,
        MenuConstants.BUTTON_WIDTH.value,
        MenuConstants.BUTTON_HEIGHT.value,
        ColorConstants.BUTTON_COLOR.value,
        ColorConstants.TEXT_COLOR.value,
        MenuConstants.TEXT_SIZE.value,
    )

    button_rects[3] = draw_button(
        window,
        GameModeConstants.AI_VS_AI.name.lower(),
        MenuConstants.BUTTON_X.value,
        MenuConstants.BUTTON_Y.value + MenuConstants.BUTTON_SPACING.value * 2,
        MenuConstants.BUTTON_WIDTH.value,
        MenuConstants.BUTTON_HEIGHT.value,
        ColorConstants.BUTTON_COLOR.value,
        ColorConstants.TEXT_COLOR.value,
        MenuConstants.TEXT_SIZE.value,
    )

    return button_rects


def draw_token(window, x, y, color, index_origin):
    token = Circle(
        window, x, y, FigureConstants.CIRCLE_RADIUS.value * 2, index_origin, color
    )
    return token


def delete_token(canvas, token_id):
    for id in token_id:
        canvas.delete(id)
