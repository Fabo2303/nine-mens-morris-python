# Path: src/game/elimination_phase/elimination_functions.py
from game.classes.Player import Player
from game.constants.array_constants import positions
from math import dist


def delete_piece(x, y, oponent: Player):
    """
    Delete a piece from the board
    :param x: x coordinate
    :param y: y coordinate
    :param oponent: player who is deleting the piece
    :return: None
    """
    for index, (pos_x, pos_y, state) in enumerate(positions):
        if state != oponent.player_number:
            continue
        distance = dist((x, y), (pos_x, pos_y))
        if distance < 15:
            oponent.remove_circle(index)
            positions[index] = (pos_x, pos_y, 0)
            return True
    return False
