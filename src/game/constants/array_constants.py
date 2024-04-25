# Path: src/game/constants/array_constants.py

from game.constants.constant import FigureConstants, WindowConstants

BOARD_X = (WindowConstants.WIDTH.value - FigureConstants.BOARD_WIDTH.value) / 2
BOARD_Y = (WindowConstants.HEIGHT.value - FigureConstants.BOARD_HEIGHT.value) / 2

# Posiciones de las fichas
positions = (
    [(BOARD_X + 40 + 70 * i, BOARD_Y + 40, 0) for i in range(0, 7, 3)]
    + [(BOARD_X + 40 + 70 * i, BOARD_Y + 40 + 70, 0) for i in range(1, 7, 2)]
    + [(BOARD_X + 40 + 70 * i, BOARD_Y + 40 + 70 * 2, 0) for i in range(2, 5, 1)]
    + [(BOARD_X + 40 + 70 * i, BOARD_Y + 40 + 70 * 3, 0) for i in range(0, 7) if i != 3]
    + [(BOARD_X + 40 + 70 * i, BOARD_Y + 40 + 70 * 4, 0) for i in range(2, 5, 1)]
    + [(BOARD_X + 40 + 70 * i, BOARD_Y + 40 + 70 * 5, 0) for i in range(1, 7, 2)]
    + [(BOARD_X + 40 + 70 * i, BOARD_Y + 40 + 70 * 6, 0) for i in range(0, 7, 3)]
)

# Posiciones de las lineas
horizontal_lines = [
    ((BOARD_X + 40, BOARD_Y + 40), (BOARD_X + 40 + 70 * 6, BOARD_Y + 40)),
    (
        (BOARD_X + 40 + 70, BOARD_Y + 40 + 70),
        (BOARD_X + 40 + 70 * 5, BOARD_Y + 40 + 70),
    ),
    (
        (BOARD_X + 40 + 70 * 2, BOARD_Y + 40 + 70 * 2),
        (BOARD_X + 40 + 70 * 4, BOARD_Y + 40 + 70 * 2),
    ),
    (
        (BOARD_X + 40, BOARD_Y + 40 + 70 * 3),
        (BOARD_X + 40 + 70 * 2, BOARD_Y + 40 + 70 * 3),
    ),
    (
        (BOARD_X + 40 + 70 * 4, BOARD_Y + 40 + 70 * 3),
        (BOARD_X + 40 + 70 * 6, BOARD_Y + 40 + 70 * 3),
    ),
    (
        (BOARD_X + 40 + 70 * 2, BOARD_Y + 40 + 70 * 4),
        (BOARD_X + 40 + 70 * 4, BOARD_Y + 40 + 70 * 4),
    ),
    (
        (BOARD_X + 40 + 70, BOARD_Y + 40 + 70 * 5),
        (BOARD_X + 40 + 70 * 5, BOARD_Y + 40 + 70 * 5),
    ),
    (
        (BOARD_X + 40, BOARD_Y + 40 + 70 * 6),
        (BOARD_X + 40 + 70 * 6, BOARD_Y + 40 + 70 * 6),
    ),
]

vertical_lines = [
    ((BOARD_X + 40, BOARD_Y + 40), (BOARD_X + 40, BOARD_Y + 40 + 70 * 6)),
    (
        (BOARD_X + 40 + 70, BOARD_Y + 40 + 70),
        (BOARD_X + 40 + 70, BOARD_Y + 40 + 70 * 5),
    ),
    (
        (BOARD_X + 40 + 70 * 2, BOARD_Y + 40 + 70 * 2),
        (BOARD_X + 40 + 70 * 2, BOARD_Y + 40 + 70 * 4),
    ),
    (
        (BOARD_X + 40 + 70 * 3, BOARD_Y + 40),
        (BOARD_X + 40 + 70 * 3, BOARD_Y + 40 + 70 * 2),
    ),
    (
        (BOARD_X + 40 + 70 * 3, BOARD_Y + 40 + 70 * 4),
        (BOARD_X + 40 + 70 * 3, BOARD_Y + 40 + 70 * 6),
    ),
    (
        (BOARD_X + 40 + 70 * 4, BOARD_Y + 40 + 70 * 2),
        (BOARD_X + 40 + 70 * 4, BOARD_Y + 40 + 70 * 4),
    ),
    (
        (BOARD_X + 40 + 70 * 5, BOARD_Y + 40 + 70),
        (BOARD_X + 40 + 70 * 5, BOARD_Y + 40 + 70 * 5),
    ),
    (
        (BOARD_X + 40 + 70 * 6, BOARD_Y + 40),
        (BOARD_X + 40 + 70 * 6, BOARD_Y + 40 + 70 * 6),
    ),
]

mill_condition = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (9, 10, 11),
    (12, 13, 14),
    (15, 16, 17),
    (18, 19, 20),
    (21, 22, 23),
    (0, 9, 21),
    (3, 10, 18),
    (6, 11, 15),
    (1, 4, 7),
    (16, 19, 22),
    (8, 12, 17),
    (5, 13, 20),
    (2, 14, 23),
]

adjacent_positions = {
    0: (1, 9),
    1: (0, 2, 4),
    2: (1, 14),
    3: (4, 10),
    4: (1, 3, 5, 7),
    5: (4, 13),
    6: (7, 11),
    7: (4, 6, 8),
    8: (7, 12),
    9: (0, 10, 21),
    10: (3, 9, 11, 18),
    11: (6, 10, 15),
    12: (8, 13, 17),
    13: (5, 12, 14, 20),
    14: (2, 13, 23),
    15: (11, 16),
    16: (15, 17, 19),
    17: (12, 16),
    18: (10, 19),
    19: (16, 18, 20, 22),
    20: (13, 19),
    21: (9, 22),
    22: (19, 21, 23),
    23: (14, 22),
}
