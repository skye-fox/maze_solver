"""This is the module for the graphics"""

# pylint: disable=too-few-public-methods

from tkinter import BOTH, Canvas, Tk


class Window:
    """Class for managing the the TK inter window"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="black", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__win_run = False

    def redraw(self):
        """Method for redrawing the contents of the window"""

        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="8b5cf6"):
        """Method for drawing a line to the canvas in the window"""

        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        """Method that continuously redraws the contents of the window until it is closed"""

        self.__win_run = True
        while self.__win_run:
            self.redraw()
        print("Window closed...")

    def close(self):
        """Method for closing the program when the user closes the window"""

        self.__win_run = False


class Point:
    """Class to create a point with x, y coordinates. Used by the Line class"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    """Class to create a line between two points.
    Takes two points as input and draws a line on the canvas when it's draw method is called
    """

    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2

    def draw(self, canvas, fill_color):
        """Method for drawing a line on the canvas between the two given points"""

        canvas.create_line(
            self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, fill=fill_color, width=2
        )
