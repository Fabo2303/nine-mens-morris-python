# Path: src/game/moving_phase/moving_functions_ai.py

import math
from game.constants.array_constants import positions, adjacent_positions
from game.functions.evaluate_functions import evaluate_move_phase, find_complete_mills


def move_piece_ai(player_1, player_2):
    board = positions
    (index, move) = get_best_move(board, player_1, player_2)
    return index, move


def get_best_move(board, player_1, player_2):
    best_move = None
    best_eval = -math.inf
    moves = generate_moves(board, player_2)
    for index in moves:
        for move in moves[index]:
            new_board = board.copy()
            # print_board(new_board)
            player_1_copy = player_1.copy_data()
            player_2_copy = player_2.copy_data()
            generate_move_in_board(new_board, player_2_copy, index, move)
            # print_board(new_board)
            eval = minimax_move_phase(new_board, 3, False, player_1_copy, player_2_copy)
            if eval > best_eval:
                best_eval = eval
                best_move = (index, move)
    # print("Best move: ", best_move)
    return best_move


def generate_move_in_board(board, player, index, move):
    board[index] = (board[index][0], board[index][1], 0)
    player.move_circle(index, move, board[move][0], board[move][1])
    board[move] = (board[move][0], board[move][1], player.player_number)


def generate_moves(board, player):
    moves = {}
    for circle in player.circles:
        if circle.index_origin not in moves:
            moves[circle.index_origin] = []
        for adjacent in adjacent_positions[circle.index_origin]:
            (_, _, state) = board[adjacent]
            if state == 0:
                moves[circle.index_origin].append(adjacent)
    # print("Moves: ", moves)
    return moves


def minimax_move_phase(board, depth, maximizing_player, player_1_copy, player_2_copy):
    if (
        depth == 0
        or find_complete_mills(player_1_copy, True, True) == 1
        or find_complete_mills(player_2_copy, True, True) == 1
    ):
        evaluation = evaluate_move_phase(board, player_1_copy, player_2_copy)
        # print("Evaluation: ", evaluation)
        return evaluation

    # print("Depth: ", depth)
    if maximizing_player:
        max_eval = -math.inf
        moves = generate_moves(board, player_2_copy)
        for index in moves:
            for move in moves[index]:
                new_board = board.copy()
                # print_board(new_board)
                player_1_copy_copy = player_1_copy.copy_data()
                player_2_copy_copy = player_2_copy.copy_data()
                generate_move_in_board(new_board, player_2_copy_copy, index, move)
                # print_board(new_board)
                eval = minimax_move_phase(
                    new_board, depth - 1, False, player_1_copy_copy, player_2_copy_copy
                )
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        moves = generate_moves(board, player_1_copy)
        for index in moves:
            for move in moves[index]:
                new_board = board.copy()
                # print_board(new_board)
                player_1_copy_copy = player_1_copy.copy_data()
                player_2_copy_copy = player_2_copy.copy_data()
                generate_move_in_board(new_board, player_1_copy_copy, index, move)
                # print_board(new_board)
                eval = minimax_move_phase(
                    new_board, depth - 1, True, player_1_copy_copy, player_2_copy_copy
                )
                min_eval = min(min_eval, eval)
        return min_eval


def print_board(board):
    for i in range(0, 24, 3):
        print(board[i : i + 3])
    print()
