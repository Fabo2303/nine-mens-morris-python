# Path: src/game/moving_phase/moving_functions.py

from math import dist
from game.constants.array_constants import adjacent_positions, positions


def move_piece(x, y, player, index):
    """
    Move a piece on the board
    :param x: x coordinate
    :param y: y coordinate
    :param player: player who is moving the piece
    :param index: index of the piece to move
    :return: None
    """
    for adjacent in adjacent_positions[index]:
        (pos_x, pos_y, state) = positions[adjacent]
        distance = dist((x, y), (pos_x, pos_y))
        if distance < 10 and state == 0:
            positions[index] = (positions[index][0], positions[index][1], 0)
            player.move_circle(index, adjacent, pos_x, pos_y)
            positions[adjacent] = (pos_x, pos_y, player.player_number)
            return True
    return False
