# Path: src/game/classes/Player.py

from game.constants.constant import GamePhaseConstants


class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.tokens_to_place = 9
        self.tokens_on_board = 0
        self.circles = []
        self.game_phase = 1

    def change_phase(self, elimination=False):
        if elimination:
            self.game_phase = GamePhaseConstants.ELIMINATION_MODE.value
            return
        if self.tokens_to_place > 0:
            self.game_phase = GamePhaseConstants.SPLASH_MODE.value
            return
        elif self.tokens_on_board > 3:
            self.game_phase = GamePhaseConstants.MOVING_MODE.value
            return
        elif self.tokens_on_board == 3:
            self.game_phase = GamePhaseConstants.FLYING_MODE.value
            return
        self.game_phase = GamePhaseConstants.GAME_OVER.value

    def add_circle(self, circle):
        if self.tokens_to_place == 0:
            return
        self.assign_number_to_circle(circle)
        self.circles.append(circle)
        self.tokens_to_place -= 1
        self.tokens_on_board += 1
        if self.tokens_to_place == 0:
            self.change_phase()

    def move_circle(self, index, index_move, x, y):
        for circle in self.circles:
            if circle.index_origin == index:
                circle.move(x, y, index_move)
                return

    def remove_circle(self, index):
        for circle_index, circle in enumerate(self.circles):
            if circle.index_origin == index:
                self.circles.pop(circle_index)
                self.tokens_on_board -= 1
                return

    def assign_number_to_circle(self, circle):
        option = self.tokens_to_place % 3
        if option == 0:
            circle.change_number(1)
            return
        if option == 2:
            circle.change_number(2)
            return
        circle.change_number(3)

    def copy_data(self, trap=False):
        player = Player(self.player_number)
        player.tokens_to_place = self.tokens_to_place
        player.tokens_on_board = self.tokens_on_board
        player.game_phase = self.game_phase
        if trap:
            player.circles = self.circles.copy()
        else:
            for circle in self.circles:
                player.circles.append(circle.copy_data())
        return player

    def check_lose(self):
        tokens = [0, 0, 0]
        for circle in self.circles:
            tokens[circle.number - 1] += 1
        if self.tokens_to_place == 0:
            for token in tokens:
                if token == 0:
                    return True
        return False

    def print_circles(self):
        for circle in self.circles:
            print(circle.number, circle.x, circle.y, circle.index_origin)
