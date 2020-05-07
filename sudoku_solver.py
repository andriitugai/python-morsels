import os
import numpy as np

g = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


class SudokuSolver():
    def __init__(self, grid):
        self.grid = grid

    def _is_possible(self, n, x, y):
        return \
            self._is_possible_horizontal(n, y) and \
            self._is_possible_vertical(n, x) and \
            self._is_possible_square(n, y, x)

    def _is_possible_horizontal(self, n, row):
        return n not in self.grid[row]

    def _is_possible_vertical(self, n, col):
        return n not in [self.grid[y][col] for y in range(9)]

    def _is_possible_square(self, n, row, col):
        row_range = range((row // 3) * 3, (row // 3) * 3 + 3)
        col_range = range((col // 3) * 3, (col // 3) * 3 + 3)
        return n not in [self.grid[y][x] for y in row_range for x in col_range]

    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for n in range(1, 10):
                        if self._is_possible(n, x, y):
                            self.grid[y][x] = n
                            self.solve()
                            self.grid[y][x] = 0
                    return
        print(np.matrix(self.grid))
        input("more?")

    def __str__(self):
        result = ""
        for row in self.grid:
            result += (str(row) + os.linesep)
        return result


def main():
    sudoku = SudokuSolver(g)
    sudoku.solve()


if __name__ == '__main__':
    main()
