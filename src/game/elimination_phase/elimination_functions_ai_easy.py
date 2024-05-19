import random

from game.classes.Player import Player


def get_best_eliminate_move_easy(opponent):
    move = random.choice(generate_eliminate_moves(opponent))
    return move


def generate_eliminate_moves(opponent):
    eliminate_moves = []
    for circle in opponent.circles:
        eliminate_moves.append(circle.index_origin)
    return eliminate_moves
