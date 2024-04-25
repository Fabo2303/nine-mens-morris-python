import pygame
from game.classes.Player import Player
from game.constants.constant import WindowConstants, ColorConstants, GameModeConstants
from game.functions.drawing_functions import draw_table, draw_menu_vs
from game.functions.game_functions import click_control

pygame.init()
screen = pygame.display.set_mode(
    (WindowConstants.WIDTH.value, WindowConstants.HEIGHT.value)
)
clock = pygame.time.Clock()
pygame.display.set_caption(WindowConstants.CAPTION.value)
pygame.mixer.music.load("src/resources/hongkong.mp3")
pygame.mixer.music.play(-1)
running = True

button_rects = draw_menu_vs(screen)
game_mode = 0
game_dificulty = 0
player_1 = Player(1)
player_2 = Player(2)
turn = 1
possible_moves = []
piece_select = -1
player_moved = False


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
                if len(button_rects) == 0:
                    player_moved = click_control(
                        x=mouse_pos[0],
                        y=mouse_pos[1],
                        window=screen,
                        player_1=player_1,
                        player_2=player_2,
                        turn=turn,
                    )
                else:
                    for button_value, button_rect in button_rects.items():
                        if button_rect.collidepoint(mouse_pos):
                            game_mode = button_value
                            button_rects.clear()
                            break
    screen.fill(ColorConstants.MENU_COLOR.value)
    if game_mode == 0:
        draw_menu_vs(screen)
    if (
        game_mode == GameModeConstants.PLAYER_VS_PLAYER.value
        or game_mode == GameModeConstants.PLAYER_VS_AI.value
        or game_mode == GameModeConstants.AI_VS_AI.value
    ):
        draw_table(screen)
    circles_player_1 = player_1.circles.copy()
    circles_player_2 = player_2.circles.copy()
    for circle in circles_player_1 + circles_player_2:
        circle.draw()
    if (game_mode == GameModeConstants.PLAYER_VS_AI.value and turn == 2) or (
        game_mode == GameModeConstants.AI_VS_AI.value
    ):
        player_moved = click_control(
            x=-100,
            y=-100,
            window=screen,
            player_1=player_1,
            player_2=player_2,
            turn=turn,
        )
    if player_moved:
        turn = change_turn(turn)
    pygame.display.flip()
    clock.tick(WindowConstants.FPS.value)

pygame.quit()
