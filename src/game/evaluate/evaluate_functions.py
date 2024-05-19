from game.classes.Circle import Circle
from game.constants.array_constants import mill_condition, adjacent_positions


def is_token_active(circle):
    return circle.state != 0


def get_circle_by_index(index, player) -> Circle:
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


def get_indexes_probably_form_mill(player):
    indexes = set()
    for mill in mill_condition:
        (a, b, c) = mill
        indexes_mill = 0
        found_indexes = set()
        circle_a = get_circle_by_index(a, player)
        circle_b = get_circle_by_index(b, player)
        circle_c = get_circle_by_index(c, player)
        pottential_mill_1 = pottential_mill(circle_a, circle_b)
        pottential_mill_2 = pottential_mill(circle_b, circle_c)
        if pottential_mill_1:
            indexes_mill += 1
            found_indexes.add(a)
            found_indexes.add(b)
        if pottential_mill_2:
            indexes_mill += 1
            found_indexes.add(b)
            found_indexes.add(c)
        if indexes_mill >= 1:
            indexes.update(found_indexes)
    return list(indexes)


def pottential_mill(circle_1, circle_2):
    if circle_1 is None or circle_2 is None:
        return False
    return (
        (circle_1.number == 1 and circle_2.number == 2)
        or (circle_1.number == 2 and circle_2.number == 1)
        or (circle_1.number == 3 and circle_2.number == 2)
        or (circle_1.number == 2 and circle_2.number == 3)
    )
