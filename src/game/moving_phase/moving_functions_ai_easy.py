import random
from game.constants.array_constants import adjacent_positions


def get_best_move_easy(board, player):
    moves = generate_moves(board, player)
    all_possible_moves = [
        (circle_index, move)
        for circle_index, moves_list in moves.items()
        for move in moves_list
    ]
    circle_index, selected_move = random.choice(all_possible_moves)
    return circle_index, selected_move


def generate_moves(board, player):
    moves = {}
    for circle in player.circles:
        if circle.index_origin not in moves:
            moves[circle.index_origin] = []
        for adjacent in adjacent_positions[circle.index_origin]:
            (_, _, state) = board[adjacent]
            if state == 0:
                moves[circle.index_origin].append(adjacent)
    return moves
