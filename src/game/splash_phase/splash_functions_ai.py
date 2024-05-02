# Path: src/game/spash_phase/splash_functions_ai.py


from game.constants.array_constants import positions
from game.splash_phase.splash_functions_ai_easy import get_best_drop_move_easy
from game.splash_phase.splash_functions_ai_medium import get_best_drop_move_medium
from game.splash_phase.splash_functions_ai_hard import get_best_drop_move_hard
from game.constants.constant import GameDifficultyConstants


def place_piece_ai(player, opponent, game_difficulty):
    board = positions
    move = get_best_drop_move(board, player, opponent, game_difficulty)
    return move


def get_best_drop_move(board, player, opponent, game_difficulty):
    if game_difficulty == GameDifficultyConstants.EASY.value:
        return get_best_drop_move_easy(board)
    if game_difficulty == GameDifficultyConstants.MEDIUM.value:
        return get_best_drop_move_medium(board, player, opponent)
    if game_difficulty == GameDifficultyConstants.HARD.value:
        return get_best_drop_move_hard(board, player, opponent)
