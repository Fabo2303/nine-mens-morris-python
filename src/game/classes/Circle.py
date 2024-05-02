# Path: src/game/classes/Circle.py
import pygame


class Circle:
    def __init__(self, window, x, y, radius, index_origin, color="black"):
        self.window = window
        self.x = x
        self.y = y
        self.state = 1
        self.index_origin = index_origin
        self.number = 99999
        self.radius = radius
        self.color = color
        self.picture = None
        self.text = None
        self.rect = None

    def draw(self):
        rect = pygame.Rect(
            self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius
        )
        self.picture = pygame.draw.ellipse(self.window, self.color, rect, 0)
        self.text = pygame.font.Font("src/resources/font-atomic.ttf", 30).render(
            str(self.number),
            True,
            "white" if self.color == "black" else "black",
        )
        self.rect = self.text.get_rect(center=(self.x, self.y))
        self.window.blit(self.text, self.rect)

    def move(self, x, y, index_move):
        self.x, self.y = x, y
        self.state = 1
        self.index_origin = index_move
        if self.window is not None:
            self.draw()

    def change_color(self, color):
        self.color = color
        if self.window is not None:
            self.draw()

    def change_state(self):
        self.state = 1 if self.state == 0 else 0

    def change_number(self, number):
        self.number = number
        if self.window is not None:
            self.draw()

    def copy_data(self):
        return Circle(None, self.x, self.y, self.radius, self.index_origin, self.color)
