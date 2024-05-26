# Path: src/game/functions/game_fuctions.py

from math import dist
from game.constants.constant import GamePhaseConstants
from game.elimination_phase.elimination_functions_ai import delete_piece_ai
from game.elimination_phase.elimination_functions import delete_piece
from game.moving_phase.moving_functions_ai import move_piece_ai
from game.splash_phase.splash_functions import place_piece
from game.splash_phase.splash_functions_ai import place_piece_ai
from game.constants.array_constants import positions, adjacent_positions
from game.evaluate.evaluate_phases import find_complete_mills
from game.moving_phase.moving_functions import move_piece

player_aux = None
opponent_aux = None
possible_moves_aux = []
piece_select = -1
game_difficulty_aux = 0


def click_control(x, y, window, player, opponent, possible_moves, game_difficulty=0):
    global player_aux, opponent_aux, possible_moves_aux, game_difficulty_aux
    player_aux = player
    opponent_aux = opponent
    possible_moves_aux = possible_moves
    game_difficulty_aux = game_difficulty
    return turn_control(x, y, window)


def turn_control(x, y, window):
    player_game_phase = player_aux.game_phase
    if player_game_phase == GamePhaseConstants.SPLASH_MODE.value:
        return splash_mode(x, y, player_aux, window)
    if player_game_phase == GamePhaseConstants.MOVING_MODE.value:
        return moving_mode(x, y, player_aux)
    if player_game_phase == GamePhaseConstants.FLYING_MODE.value:
        return
    if player_game_phase == GamePhaseConstants.ELIMINATION_MODE.value:
        return elimination_mode(x, y, player_aux, opponent_aux)


def splash_mode(x, y, player, window):
    index = 0
    if x == -100 and y == -100:
        index = place_piece_ai(player_aux, opponent_aux, game_difficulty_aux)
    player_moved = place_piece(
        x if x != -100 else positions[index][0],
        y if y != -100 else positions[index][1],
        window,
        player,
    )
    if player_moved:
        is_mill = find_complete_mills(player, True, False)
        if is_mill == 1:
            player.change_phase(True)
            return
    return player_moved


def elimination_mode(x, y, player, oponent):
    index = 0
    if x == -100 and y == -100:
        index = delete_piece_ai(player_aux, opponent_aux, game_difficulty_aux)
    player_moved = delete_piece(
        x if x != -100 else positions[index][0],
        y if y != -100 else positions[index][1],
        oponent,
    )
    if player_moved:
        player.change_phase(False)
        return True
    return False


def select_piece(x, y, player):
    global piece_select
    for circle in player.circles:
        pos_x = circle.x
        pos_y = circle.y
        distance = dist((x, y), (pos_x, pos_y))
        if distance < 15:
            piece_select = circle.index_origin
            show_possible_moves(piece_select)
            break


def show_possible_moves(index):
    global possible_moves_aux
    if len(possible_moves_aux) > 0:
        possible_moves_aux.clear()
    for adjacent in adjacent_positions[index]:
        (x, y, state) = positions[adjacent]
        if state == 0:
            possible_moves_aux.append((x, y))


def moving_mode(x, y, player):
    global possible_moves_aux, piece_select
    if x == -100 and y == -100:
        (index, move) = move_piece_ai(player_aux, opponent_aux, game_difficulty_aux)
        x = positions[move][0]
        y = positions[move][1]
        piece_select = index
    else:
        select_piece(x, y, player)
    if piece_select != -1:
        player_moved = move_piece(x, y, player, piece_select)
        if player_moved:
            is_mill = find_complete_mills(player, True, False)
            if len(possible_moves_aux) > 0:
                possible_moves_aux.clear()
            if is_mill == 1:
                player.change_phase(True)
                return
            piece_select = -1
            return True
    return False


def print_board():
    for i in range(0, 24, 3):
        print(positions[i : i + 3])
    print()
