# Path: src/game/functions/game_fuctions.py

from math import dist
from game.constants.constant import ColorConstants, GameConstants
from game.elimination_phase.elimination_functions import delete_piece
from game.functions.drawing_functions import draw_circle
from game.moving_phase.moving_functions_ai import move_piece_ai
from game.splash_phase.splash_functions import place_piece
from game.splash_phase.splash_functions_ai import place_piece_ai
from game.constants.array_constants import positions, adjacent_positions
from game.functions.evaluate_functions import find_complete_mills
from game.moving_phase.moving_functions import move_piece

player_1_aux = None
player_2_aux = None
possible_moves = []
piece_select = -1


def click_control(x, y, window, player_1, player_2, turn):
    global player_1_aux, player_2_aux
    player_1_aux = player_1
    player_2_aux = player_2

    return turn_control(x, y, window, turn)


def turn_control(x, y, window, turn):
    (player, oponent) = (
        (player_1_aux, player_2_aux) if turn == 1 else (player_2_aux, player_1_aux)
    )
    player_game_phase = player.game_phase
    if player_game_phase == GameConstants.SPLASH_MODE.value:
        return splash_mode(x, y, player, window, turn)
    if player_game_phase == GameConstants.MOVING_MODE.value:
        return moving_mode(x, y, player, window, turn)
    if player_game_phase == GameConstants.FLYING_MODE.value:
        return
    if player_game_phase == GameConstants.ELIMINATION_MODE.value:
        return elimination_mode(x, y, player, oponent, window, turn)


def splash_mode(x, y, player, window, turn):
    index = 0
    if x == -100 and y == -100:
        index = place_piece_ai(player_1_aux, player_2_aux)
    player_moved = place_piece(
        x if x != -100 else positions[index][0],
        y if y != -100 else positions[index][1],
        window,
        player,
    )
    if player_moved:
        is_mill = find_complete_mills(player, True, False)
        if is_mill == 1:
            print("Mill")
            player.change_phase(True)
            return
    return player_moved


def elimination_mode(x, y, player, oponent, window, turn):
    oponent = player_1_aux if turn == 2 else player_2_aux
    if delete_piece(x, y, oponent):
        player.change_phase(False)
        return True
    return False


def select_piece(x, y, player, window):
    global piece_select
    for circle in player.circles:
        pos_x = circle.x
        pos_y = circle.y
        distance = dist((x, y), (pos_x, pos_y))
        if distance < 10:
            piece_select = circle.index_origin
            show_possible_moves(piece_select, window)
            break


def show_possible_moves(index, window):
    global possible_moves
    if len(possible_moves) > 0:
        for possible_move in possible_moves:
            window.delete(possible_move)
        possible_moves.clear()
    for adjacent in adjacent_positions[index]:
        (x, y, state) = positions[adjacent]
        if state == 0:
            possible_moves.append(
                draw_circle(window, x, y, ColorConstants.POSIBLE_MOVE_COLOR)
            )


def moving_mode(x, y, player, window, turn):
    global possible_moves, piece_select
    if x == -100 and y == -100:
        (index, move) = move_piece_ai(player_1_aux, player_2_aux)
        x = positions[move][0]
        y = positions[move][1]
        piece_select = index
    else:
        select_piece(x, y, player, window)
    if piece_select != -1:
        player_moved = move_piece(x, y, player, piece_select)
        # print("Player moved: ", player_moved)
        if player_moved:
            is_mill = find_complete_mills(player, True, False)
            if is_mill == 1:
                print("Mill")
                player.change_phase(True)
                return
            piece_select = -1
            if len(possible_moves) > 0:
                for possible_move in possible_moves:
                    window.delete(possible_move)
                possible_moves.clear()
            return True
    return False


def print_board():
    for i in range(0, 24, 3):
        print(positions[i : i + 3])
    print()
