import random
from game.evaluate.evaluate_functions import get_indexes_probably_form_mill


def get_best_eliminate_move_medium(board, player, opponent):
    move = random.choice(generate_eliminate_moves(opponent))
    return move


def generate_eliminate_moves(opponent):
    eliminate_moves = get_indexes_probably_form_mill(opponent)
    return eliminate_moves
