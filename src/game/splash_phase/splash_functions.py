# Path: src/game/spash_phase/splash_functions.py

import pygame
from game.constants.constant import ColorConstants
from game.constants.array_constants import positions
from game.functions.drawing_functions import draw_token
from math import dist


def place_piece(x, y, window, player):
    """
    Place a piece on the board
    :param x: x coordinate
    :param y: y coordinate
    :param canvas: canvas to draw the piece
    :param player: player who is placing the piece
    :return: None
    """
    for index, (pos_x, pos_y, state) in enumerate(positions):
        if state != 0:
            continue

        distance = dist((x, y), (pos_x, pos_y))
        if distance < 10:
            token_color = (
                ColorConstants.PLAYER_1_COLOR.value
                if player.player_number == 1
                else ColorConstants.PLAYER_2_COLOR.value
            )
            token = draw_token(
                window=window,
                x=pos_x,
                y=pos_y,
                color=token_color,
                index_origin=index,
            )
            player.add_circle(token)
            positions[index] = (pos_x, pos_y, player.player_number)
            return True
    return False
