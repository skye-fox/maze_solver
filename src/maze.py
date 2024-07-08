"""Module for managing the maze"""

# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments

import random
import time

from cell import Cell


class Maze:
    """Class to create the maze"""

    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for _ in range(self._num_cols):
            col = []
            for _ in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(len(self._cells)):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []

            # if top cell hasn't been visited
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # if bottom cell hasn't been visited
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            # if left cell hasn't been visited
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # if right cell hasn't been visited
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            direction = random.choice(to_visit)

            if direction[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            if direction[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if direction[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if direction[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        """Method to try and solve the maze"""
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self._num_cols - 1][self._num_rows - 1]:
            return True
        if (
            j < self._num_rows - 1
            and not self._cells[i][j + 1].visited
            and not self._cells[i][j + 1].has_top_wall
            and not self._cells[i][j].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            is_true = self._solve_r(i, j + 1)
            if is_true:
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        if (
            i < self._num_cols - 1
            and not self._cells[i + 1][j].visited
            and not self._cells[i + 1][j].has_left_wall
            and not self._cells[i][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            is_true = self._solve_r(i + 1, j)
            if is_true:
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        if (
            j > 0
            and not self._cells[i][j - 1].visited
            and not self._cells[i][j - 1].has_bottom_wall
            and not self._cells[i][j].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            is_true = self._solve_r(i, j - 1)
            if is_true:
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        if (
            i > 0
            and not self._cells[i - 1][j].visited
            and not self._cells[i - 1][j].has_right_wall
            and not self._cells[i][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            is_true = self._solve_r(i - 1, j)
            if is_true:
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        return False
