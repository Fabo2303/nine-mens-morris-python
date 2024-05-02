# Path: src/game/moving_phase/moving_functions_ai.py

from game.constants.array_constants import positions
from game.moving_phase.moving_functions_ai_easy import get_best_move_easy
from game.moving_phase.moving_functions_ai_medium import get_best_move_medium
from game.moving_phase.moving_functions_ai_hard import get_best_move_hard
from game.constants.constant import GameDifficultyConstants


def move_piece_ai(player, opponent, game_difficulty):
    board = positions
    (index, move) = get_best_move(board, player, opponent, game_difficulty)
    return index, move


def get_best_move(board, player, opponent, game_difficulty):
    if game_difficulty == GameDifficultyConstants.EASY.value:
        return get_best_move_easy(board, player)
    if game_difficulty == GameDifficultyConstants.MEDIUM.value:
        return get_best_move_medium(board, player, opponent)
    if game_difficulty == GameDifficultyConstants.HARD.value:
        return get_best_move_hard(board, player, opponent)
