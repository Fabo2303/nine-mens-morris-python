import math
from game.classes.Player import Player
from game.constants.array_constants import positions
from game.functions.evaluate_functions import evaluate_drop_phase


def delete_piece_ai(player_1, player_2):
    board = positions
    move = get_best_elimination_move(board, player_1, player_2)
    return move


def get_best_elimination_move(board, player_1, player_2):
    best_move = None
    best_eval = -math.inf
    for move in generate_elimination_moves(board, player_1, player_2):
        new_board = board.copy()
        player_1_copy = player_1.copy_data(True)
        player_2_copy = player_2.copy_data(True)
        generate_delete_in_board(new_board, player_1_copy, move)
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move


def generate_delete_in_board(board, player: Player, move):
    board[move] = (board[move][0], board[move][1], 0)
    player.remove_circle(move)


def generate_elimination_moves(board, player_1, player_2):
    elimination_moves = []
    for circle in player_2.circles:
        elimination_moves.append(circle.index_origin)
    return elimination_moves
