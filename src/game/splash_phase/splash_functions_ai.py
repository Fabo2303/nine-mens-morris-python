# Path: src/game/spash_phase/splash_functions_ai.py

import math
from game.classes.Circle import Circle
from game.constants.array_constants import positions
from game.functions.evaluate_functions import evaluate_drop_phase, find_complete_mills


def place_piece_ai(player_1, player_2):
    board = positions
    move = get_best_drop_move(board, player_1, player_2)
    return move


def get_best_drop_move(board, player_1, player_2):
    best_move = None
    best_eval = -math.inf
    for move in generate_drop_moves(board):
        # print("Move: ", move)
        new_board = board.copy()
        player_1_copy = player_1.copy_data()
        player_2_copy = player_2.copy_data()
        new_board[move] = (new_board[move][0], new_board[move][1], 2)
        create_circle_for_player(new_board, player_2_copy, move)
        # print_board(new_board)
        # print("Enter minimax drop phase:")
        eval = minimax_drop_phase(new_board, 2, False, player_1_copy, player_2_copy)
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move


def generate_drop_moves(board):
    drop_moves = []
    for index, (_, _, state) in enumerate(board):
        if state == 0:
            drop_moves.append(index)
    return drop_moves


def evaluate_phase(board, player_1_copy, player_2_copy):
    return evaluate_drop_phase(board, player_1_copy, player_2_copy)


def minimax_drop_phase(board, depth, maximizing_player, player_1_copy, player_2_copy):
    if (
        depth == 0
        or player_1_copy.tokens_to_place == 0
        or player_2_copy.tokens_to_place == 0
        or find_complete_mills(player_1_copy, True, True) == 1
        or find_complete_mills(player_2_copy, True, True) == 1
    ):
        evaluation = evaluate_phase(board, player_1_copy, player_2_copy)
        # print("Evaluation: ", evaluation)
        return evaluation

    # print("Depth: ", depth)
    if maximizing_player:
        max_eval = -math.inf
        for move in generate_drop_moves(board):
            new_board = board.copy()
            player_1_copy_copy = player_1_copy.copy_data()
            player_2_copy_copy = player_2_copy.copy_data()
            new_board[move] = (new_board[move][0], new_board[move][1], 2)
            create_circle_for_player(new_board, player_2_copy_copy, move)
            # print_board(new_board)
            # print("Enter minimax drop phase:")
            eval = minimax_drop_phase(
                new_board, depth - 1, False, player_1_copy_copy, player_2_copy_copy
            )
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in generate_drop_moves(board):
            new_board = board.copy()
            player_1_copy_copy = player_1_copy.copy_data()
            player_2_copy_copy = player_2_copy.copy_data()
            new_board[move] = (new_board[move][0], new_board[move][1], 1)
            create_circle_for_player(new_board, player_1_copy_copy, move)
            # # print_board(new_board)
            # print("Enter minimax drop phase:")
            eval = minimax_drop_phase(
                new_board, depth - 1, True, player_1_copy_copy, player_2_copy_copy
            )
            min_eval = min(min_eval, eval)
        return min_eval


def print_board(board):
    for i in range(0, 24, 3):
        print(board[i : i + 3])
    print()


def create_circle_for_player(board, player, index):
    player.add_circle(Circle(None, board[index][0], board[index][1], 20, index))
