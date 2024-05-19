import math
from game.constants.array_constants import adjacent_positions
from game.evaluate.evaluate_phases import evaluate_move_phase, find_complete_mills


def get_best_move_hard(board, player, opponent):
    best_move = None
    best_eval = -math.inf
    moves = generate_moves(board, player)
    for index in moves:
        for move in moves[index]:
            new_board = board.copy()
            player_copy = player.copy_data()
            opponent_copy = opponent.copy_data()
            generate_move_in_board(new_board, player_copy, index, move)
            eval = minimax_move_phase(new_board, 2, False, player_copy, opponent_copy)
            if eval > best_eval:
                best_eval = eval
                best_move = (index, move)
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
    return moves


def minimax_move_phase(board, depth, maximizing_player, player_copy, opponent_copy):
    if (
        depth == 0
        or find_complete_mills(player_copy, True, True) == 1
        or find_complete_mills(opponent_copy, True, True) == 1
    ):
        evaluation = evaluate_move_phase(board, player_copy, opponent_copy)
        return evaluation

    if maximizing_player:
        max_eval = -math.inf
        moves = generate_moves(board, player_copy)
        for index in moves:
            for move in moves[index]:
                new_board = board.copy()
                player_copy_copy = player_copy.copy_data()
                opponent_copy_copy = opponent_copy.copy_data()
                generate_move_in_board(new_board, player_copy_copy, index, move)
                eval = minimax_move_phase(
                    new_board, depth - 1, False, player_copy_copy, opponent_copy_copy
                )
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        moves = generate_moves(board, opponent_copy)
        for index in moves:
            for move in moves[index]:
                new_board = board.copy()
                player_copy_copy = player_copy.copy_data()
                opponent_copy_copy = opponent_copy.copy_data()
                generate_move_in_board(new_board, opponent_copy_copy, index, move)
                eval = minimax_move_phase(
                    new_board, depth - 1, True, player_copy_copy, opponent_copy_copy
                )
                min_eval = min(min_eval, eval)
        return min_eval


def print_board(board):
    for i in range(0, 24, 3):
        print(board[i : i + 3])
    print()
