import random


def get_best_drop_move_easy(board):
    return random.choice(generate_drop_moves(board))


def generate_drop_moves(board):
    drop_moves = []
    for index, (_, _, state) in enumerate(board):
        if state == 0:
            drop_moves.append(index)
    return drop_moves
