import math

from game.classes.Player import Player
from game.evaluate.evaluate_phases import evaluate_elimination_phase
from game.constants.constant import GamePhaseConstants
from game.splash_phase.splash_functions_ai_hard import minimax_drop_phase
from game.moving_phase.moving_functions_ai_hard import minimax_move_phase


def get_best_eliminate_move_hard(board, player, opponent):
    best_move = None
    best_eval = -math.inf
    for move in generate_eliminate_moves(opponent):
        new_board = board.copy()
        player_copy: Player = player.copy_data(True)
        opponent_copy = opponent.copy_data(True)
        new_board[move] = (new_board[move][0], new_board[move][1], 0)
        player_copy.remove_circle(move)
        eval = minimax_elimination_phase(
            new_board, 3, False, player_copy, opponent_copy
        )
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move


def generate_eliminate_moves(opponent):
    eliminate_moves = []
    for circle in opponent.circles:
        eliminate_moves.append(circle.index_origin)
    return eliminate_moves


def minimax_elimination_phase(
    board, depth, maximizing_player, player_copy, opponent_copy
):
    if depth == 0 or opponent_copy.tokens_on_board == 0:
        evaluation = evaluate_elimination_phase(board, player_copy, opponent_copy)
        return evaluation

    if maximizing_player:
        max_eval = -math.inf
        new_board = board.copy()
        player_copy_copy = player_copy.copy_data(True)
        opponent_copy_copy = opponent_copy.copy_data(True)
        eval = 0
        if player_copy_copy.game_phase == GamePhaseConstants.SPLASH_MODE.value:
            eval = minimax_drop_phase(
                new_board, depth - 1, False, player_copy_copy, opponent_copy_copy
            )
        if player_copy_copy.game_phase == GamePhaseConstants.MOVING_MODE.value:
            eval = minimax_move_phase(
                new_board, depth - 1, False, player_copy_copy, opponent_copy_copy
            )
        max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        new_board = board.copy()
        player_copy_copy = player_copy.copy_data(True)
        opponent_copy_copy = opponent_copy.copy_data(True)
        eval = 0
        if opponent_copy_copy.game_phase == GamePhaseConstants.SPLASH_MODE.value:
            eval = minimax_drop_phase(
                new_board, depth - 1, False, player_copy_copy, opponent_copy_copy
            )
        if opponent_copy_copy.game_phase == GamePhaseConstants.MOVING_MODE.value:
            eval = minimax_move_phase(
                new_board, depth - 1, False, player_copy_copy, opponent_copy_copy
            )
        min_eval = min(min_eval, eval)
        return min_eval
