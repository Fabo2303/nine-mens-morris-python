import math
from game.classes.Circle import Circle
from game.evaluate.evaluate_phases import evaluate_drop_phase


def get_best_drop_move_medium(board, player, opponent):
    best_move = None
    best_eval = -math.inf
    for move in generate_drop_moves(board):
        new_board = board.copy()
        player_copy = player.copy_data(True)
        opponent_copy = opponent.copy_data(True)
        new_board[move] = (
            new_board[move][0],
            new_board[move][1],
            player_copy.player_number,
        )
        create_circle_for_player(new_board, player_copy, move)
        eval = minimax_drop_phase(new_board, player_copy, opponent_copy)
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


def minimax_drop_phase(board, player_copy, opponent_copy):
    evaluation = evaluate_drop_phase(board, player_copy, opponent_copy)
    return evaluation


def print_board(board):
    for i in range(0, 24, 3):
        print(board[i : i + 3])
    print()


def create_circle_for_player(board, player, index):
    player.add_circle(Circle(None, board[index][0], board[index][1], 20, index))
