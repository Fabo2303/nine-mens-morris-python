# Path: src/game/functions/evaluate_functions.py

from game.constants.array_constants import mill_condition, adjacent_positions


def is_token_active(circle):
    return circle.state != 0


def get_circle_by_index(index, player):
    for token in player.circles:
        if token.index_origin == index:
            return token
    return None


def is_scaled(circle_1, circle_2, circle_3):
    return (
        (circle_1.number == 1 and circle_3.number == 3)
        or (circle_1.number == 3 and circle_3.number == 1)
    ) and circle_2.number == 2


def block_token(circle):
    circle.state = 0


def is_scaled_mill(mill, player, only_one=False, is_test=False):
    index_1 = mill[0]
    index_2 = mill[1]
    index_3 = mill[2]
    cirle_1 = get_circle_by_index(index_1, player)
    cirle_2 = get_circle_by_index(index_2, player)
    cirle_3 = get_circle_by_index(index_3, player)

    if cirle_1 is None or cirle_2 is None or cirle_3 is None:
        return False

    if (
        (
            is_token_active(cirle_1)
            or is_token_active(cirle_2)
            or is_token_active(cirle_3)
        )
        or not only_one
    ) and is_scaled(cirle_1, cirle_2, cirle_3):
        if is_test or not only_one:
            return True
        block_token(cirle_1)
        block_token(cirle_2)
        block_token(cirle_3)
        return True
    return False


def find_complete_mills(player, only_one=False, is_test=False):
    complete_mills = []
    for mill in mill_condition:
        if is_scaled_mill(mill, player, only_one, is_test):
            if only_one:
                return 1
            complete_mills.append(mill)
    if not only_one:
        return complete_mills
    return 0


def number_blocked_of_piece(board, player):
    adjacent_blocked = 0
    for token in player.circles:
        indicator_block = 0
        index = token.index_origin
        adjacents = adjacent_positions[index]
        for adjacent in adjacents:
            if board[adjacent][2] != player.player_number and board[adjacent][2] != 0:
                indicator_block += 1
        if indicator_block == len(adjacents):
            adjacent_blocked += 1
    return adjacent_blocked


def number_of_pieces(player):
    return len(player.circles)


def number_of_two_pieces_configuration(board, player):
    two_pieces_configurations = set()
    for token in player.circles:
        index = token.index_origin
        for position in adjacent_positions[index]:
            if board[position][2] == player.player_number:
                two_pieces_configurations.add(
                    (index, position) if index < position else (position, index)
                )
    return len(two_pieces_configurations)


def number_of_three_pieces_configuration(board, player):
    possible_index_configurations = [0, 2, 3, 5, 6, 8, 15, 17, 18, 19, 20, 21, 23]
    number_of_three_pieces_configurations = 0
    for token in player.circles:
        index = token.index_origin
        if index in possible_index_configurations:
            adjacent_index_1 = adjacent_positions[index][0]
            adjacent_index_2 = adjacent_positions[index][1]
            if (
                board[adjacent_index_1][2] == player.player_number
                and board[adjacent_index_2][2] == player.player_number
            ):
                number_of_three_pieces_configurations += 1
    return number_of_three_pieces_configurations


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

    evaluation = evaluation + (pieces_1 - pieces_2) * 9
    # print("Evaluation - 4: ", evaluation)

    two_pieces_configurations_1 = number_of_two_pieces_configuration(board, player)
    two_pieces_configurations_2 = number_of_two_pieces_configuration(board, opponent)

    evaluation = (
        evaluation + (two_pieces_configurations_1 - two_pieces_configurations_2) * 10
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

    evaluation = evaluation + (pieces_1 - pieces_2) * 11
    # print("Evaluation - 4: ", evaluation)

    return evaluation


def evaluate_delete_phase(board, player, opponent):
    evaluation = 0
    return evaluation
