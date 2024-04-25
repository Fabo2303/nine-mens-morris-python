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

    def move(self, x, y):
        """
        Moves the circle to the specified coordinates.

        Args:
            x (int): The x-coordinate of the new position.
            y (int): The y-coordinate of the new position.

        Returns:
            None
        """
        self.x = x
        self.y = y
        if self.window is not None:
            self.draw()

    def change_color(self, color):
        """
        Changes the color of the circle.

        Args:
            color (str): The new color of the circle.

        Returns:
            None
        """
        self.color = color
        if self.window is not None:
            self.draw()

    def change_state(self):
        """
        Changes the state of the circle.

        If the current state is 0, it changes it to 1.
        If the current state is 1, it changes it to 0.

        Returns:
            None
        """
        self.state = 1 if self.state == 0 else 0

    def change_number(self, number):
        """
        Changes the number of the circle.

        Args:
            number (int): The new number of the circle.

        Returns:
            None
        """
        self.number = number
        if self.window is not None:
            self.draw()

    def copy_data(self):
        """
        Returns a copy of the circle.

        Returns:
            Circle: A copy of the circle.
        """
        return Circle(None, self.x, self.y, self.radius, self.index_origin, self.color)
