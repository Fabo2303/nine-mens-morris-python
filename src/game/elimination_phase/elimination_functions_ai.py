from game.constants.array_constants import positions
from game.elimination_phase.elimination_functions_ai_easy import (
    get_best_eliminate_move_easy,
)
from game.elimination_phase.elimination_functions_ai_medium import (
    get_best_eliminate_move_medium,
)
from game.elimination_phase.elimination_functions_ai_hard import (
    get_best_eliminate_move_hard,
)
from game.constants.constant import GameDifficultyConstants


def delete_piece_ai(player, opponent, game_difficulty):
    board = positions
    move = get_best_elimination_move(board, player, opponent, game_difficulty)
    return move


def get_best_elimination_move(board, player, opponent, game_difficulty):
    if game_difficulty == GameDifficultyConstants.EASY.value:
        return get_best_eliminate_move_easy(opponent)
    if game_difficulty == GameDifficultyConstants.MEDIUM.value:
        return get_best_eliminate_move_medium(board, player, opponent)
    if game_difficulty == GameDifficultyConstants.HARD.value:
        return get_best_eliminate_move_medium(board, player, opponent)
