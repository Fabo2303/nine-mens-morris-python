import pygame
from game.classes.Player import Player
from game.constants.constant import WindowConstants, ColorConstants, GameModeConstants
from game.functions.drawing_functions import draw_table, draw_menu_vs, draw_pieces
from game.functions.game_functions import click_control
import time

pygame.init()
screen = pygame.display.set_mode(
    (WindowConstants.WIDTH.value, WindowConstants.HEIGHT.value)
)
clock = pygame.time.Clock()

pygame.display.set_icon(pygame.image.load("src/resources/icon.png"))
pygame.display.set_caption(WindowConstants.CAPTION.value)
# pygame.mixer.music.load("src/resources/hongkong.mp3")
# pygame.mixer.music.play(-1)
running = True

list_modes = draw_menu_vs(screen)
list_difficulty = []
game_mode = 0
game_dificulty = 0
player_1 = Player(1)
player_2 = Player(2)
turn = 1
possible_moves = []
player_moved = False


def detect_click_button(button_list):
    for button_value, button_rect in button_list.items():
        if button_rect.collidepoint(mouse_pos):
            return button_value
    return 0


def draw_piece_players():
    circles_player_1 = player_1.circles.copy()
    circles_player_2 = player_2.circles.copy()
    for circle in circles_player_1 + circles_player_2:
        circle.draw()
    if len(possible_moves) > 0:
        draw_pieces(screen, possible_moves, ColorConstants.POSIBLE_MOVE_COLOR.value)


def draw_context():
    if game_mode == 0:
        draw_menu_vs(screen)
    if game_mode == GameModeConstants.PLAYER_VS_AI.value:
        draw_menu_vs(screen, 1)
    if (
        game_mode == GameModeConstants.PLAYER_VS_PLAYER.value
        or (game_mode == GameModeConstants.PLAYER_VS_AI.value and game_dificulty != 0)
        or game_mode == GameModeConstants.AI_VS_AI.value
    ):
        draw_table(screen)


def change_turn(turn):
    if turn == 1:
        return 2
    return 1


while running:
    player_moved = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if len(list_modes) == 0:
                    if len(list_difficulty) == 0:
                        player_moved = click_control(
                            x=mouse_pos[0],
                            y=mouse_pos[1],
                            window=screen,
                            player=player_1 if turn == 1 else player_2,
                            opponent=player_2 if turn == 1 else player_1,
                            turn=turn,
                            possible_moves=possible_moves,
                        )
                    else:
                        game_dificulty = detect_click_button(list_difficulty)
                        list_difficulty.clear()
                else:
                    game_mode = detect_click_button(list_modes)
                    if game_mode == GameModeConstants.PLAYER_VS_AI.value:
                        list_difficulty = draw_menu_vs(screen, 1)
                    list_modes.clear()
    screen.fill(ColorConstants.MENU_COLOR.value)
    draw_context()
    draw_piece_players()
    if (game_mode == GameModeConstants.PLAYER_VS_AI.value and turn == 2) or (
        game_mode == GameModeConstants.AI_VS_AI.value
    ):
        player_moved = click_control(
            x=-100,
            y=-100,
            window=screen,
            player=player_1 if turn == 1 else player_2,
            opponent=player_2 if turn == 1 else player_1,
            turn=turn,
            possible_moves=possible_moves,
        )
        # time.sleep(1)
    if player_moved:
        turn = change_turn(turn)
    pygame.display.flip()
    clock.tick(WindowConstants.FPS.value)

pygame.quit()
