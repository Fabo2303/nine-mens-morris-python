# Path: src/game/functions/evaluate_functions.py

from game.evaluate.evaluate_functions import (
    find_complete_mills,
    number_blocked_of_piece,
    number_of_pieces,
    number_of_two_pieces_configuration,
    number_of_three_pieces_configuration,
    winning_configuration,
    get_blocked_mill,
)
from game.constants.array_constants import mill_condition


def evaluate_drop_phase_medium(board, player, opponent, move):
    evaluation = 0
    blocked_mill = get_blocked_mill(player, opponent, move)
    if blocked_mill:
        evaluation += 200
    mill_formed = find_complete_mills(player)
    if len(mill_formed) > 0:
        evaluation += 300
    blocked_piece = number_blocked_of_piece(board, opponent)
    if blocked_piece > 0:
        evaluation += 50
    return evaluation


def evaluate_drop_phase(board, player, opponent):
    new_mill_1 = find_complete_mills(player, only_one=True, is_test=True)
    new_mill_2 = find_complete_mills(opponent, only_one=True, is_test=True)

    evaluation = (-new_mill_2 if new_mill_2 > new_mill_1 else new_mill_1) * 18
    # print("Evaluation - 1: ", evaluation)

    complete_mills_1 = find_complete_mills(player)
    complete_mills_2 = find_complete_mills(opponent)

    evaluation = evaluation + (len(complete_mills_1) - len(complete_mills_2)) * 26
    # print("Evaluation - 2: ", evaluation)

    blocked_piece_1 = number_blocked_of_piece(board, player)
    blocked_piece_2 = number_blocked_of_piece(board, opponent)

    evaluation = evaluation + (blocked_piece_2 - blocked_piece_1) * 1
    # print("Evaluation - 3: ", evaluation)

    pieces_1 = number_of_pieces(player)
    pieces_2 = number_of_pieces(opponent)

    evaluation = evaluation + (pieces_1 - pieces_2) * 6
    # print("Evaluation - 4: ", evaluation)

    two_pieces_configurations_1 = number_of_two_pieces_configuration(board, player)
    two_pieces_configurations_2 = number_of_two_pieces_configuration(board, opponent)

    evaluation = (
        evaluation + (two_pieces_configurations_1 - two_pieces_configurations_2) * 12
    )
    # print("Evaluation - 5: ", evaluation)

    three_pieces_configurations_1 = number_of_three_pieces_configuration(board, player)
    three_pieces_configurations_2 = number_of_three_pieces_configuration(
        board, opponent
    )

    evaluation = (
        evaluation + (three_pieces_configurations_1 - three_pieces_configurations_2) * 7
    )
    # print("Evaluation - 6: ", evaluation)

    return evaluation


def evaluate_move_phase(board, player, opponent):
    new_mill_1 = find_complete_mills(player, only_one=True, is_test=True)
    new_mill_2 = find_complete_mills(opponent, only_one=True, is_test=True)

    evaluation = (-new_mill_2 if new_mill_2 > new_mill_1 else new_mill_1) * 14
    # print("Evaluation - 1: ", evaluation)

    complete_mills_1 = find_complete_mills(player)
    complete_mills_2 = find_complete_mills(opponent)

    evaluation = evaluation + (len(complete_mills_1) - len(complete_mills_2)) * 43
    # print("Evaluation - 2: ", evaluation)

    blocked_piece_1 = number_blocked_of_piece(board, player)
    blocked_piece_2 = number_blocked_of_piece(board, opponent)

    evaluation = evaluation + (blocked_piece_2 - blocked_piece_1) * 10
    # print("Evaluation - 3: ", evaluation)

    pieces_1 = number_of_pieces(player)
    pieces_2 = number_of_pieces(opponent)

    evaluation = evaluation + (pieces_1 - pieces_2) * 8
    # print("Evaluation - 4: ", evaluation)
    two_pieces_configurations_1 = number_of_two_pieces_configuration(board, player)
    two_pieces_configurations_2 = number_of_two_pieces_configuration(board, opponent)

    evaluation = (
        evaluation + (two_pieces_configurations_1 - two_pieces_configurations_2) * 7
    )

    # double morris 42
    # winning configuration 1086
    winning = winning_configuration(opponent) - winning_configuration(player)
    evaluation = evaluation + winning * 1086

    return evaluation


def evaluate_elimination_phase(board, player, opponent):
    evaluation = 0
    return evaluation
