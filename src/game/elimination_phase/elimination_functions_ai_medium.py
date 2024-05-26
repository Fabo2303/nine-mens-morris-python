import random
from game.classes.Player import Player
from game.evaluate.evaluate_functions import get_indexes_probably_form_mill


def get_best_eliminate_move_medium(board, player, opponent):
    move = random.choice(get_piece_with_least_count(opponent))
    return move


def get_piece_with_least_count(opponent: Player):
    opponent_circles = opponent.circles
    count = [0, 0, 0]
    for circle in opponent_circles:
        count[circle.number - 1] += 1
    min_count = min(count)
    if min_count == 3:
        eliminate_moves = get_indexes_probably_form_mill(opponent)
        return eliminate_moves
    for circle in opponent_circles:
        if count[circle.number - 1] == min_count:
            return [circle.index_origin]
