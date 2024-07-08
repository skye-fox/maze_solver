"""This is the main module"""

import sys

from graphics import Window
from maze import Maze


def main():
    """Main function, entry point to program"""

    num_rows = 40
    num_cols = 40
    margin = 50
    screen_x = 1000
    screen_y = 1000
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()

    win.wait_for_close()


main()
