"""This is the module for the graphics"""

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

    def wait_for_close(self):
        """Method that continuously redraws the contents of the window until it is closed"""

        self.__win_run = True
        while self.__win_run:
            self.redraw()
        print("Window closed...")

    def close(self):
        """Method for closing the program when the user closes the window"""

        self.__win_run = False
