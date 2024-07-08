"""Module for defining cells in the Window"""

# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes

from graphics import Line, Point


class Cell:
    """A class to define cells within the Window object"""

    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        """Method for drawing cells to the window
        Takes coordinates for the top left corner & bottom right corner"""

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            if self._win is not None:
                self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")
        else:
            if self._win is not None:
                self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
        if self.has_right_wall:
            if self._win is not None:
                self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
        else:
            if self._win is not None:
                self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        if self.has_top_wall:
            if self._win is not None:
                self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")
        else:
            if self._win is not None:
                self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
        if self.has_bottom_wall:
            if self._win is not None:
                self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")
        else:
            if self._win is not None:
                self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")

    def draw_move(self, to_cell, undo=False):
        """Method to draw a line from the center of the cell it's called on to
        the center of the cell it is passed"""

        x1_c = (self._x1 + self._x2) // 2
        y1_c = (self._y1 + self._y2) // 2

        x2_c = (to_cell._x1 + to_cell._x2) // 2
        y2_c = (to_cell._y1 + to_cell._y2) // 2

        fill_color = "#8b5cf6"
        if undo:
            fill_color = "red"

        if self._win is not None:
            self._win.draw_line(Line(Point(x1_c, y1_c), Point(x2_c, y2_c)), fill_color)
