import numpy as np

# grid = [[0]*8]*8
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
num_queens = 7


class SevenQueens():
    def __init__(self, g):
        self.grid = g
        self.num = 0

    def _is_safe_place(self, y0, x0):
        # horizontal:
        if any([self.grid[y0][x] for x in range(8)]):
            return False
        # vertical:
        if any([self.grid[y][x0] for y in range(8)]):
            return False

        # tlbr diagonal:
        k = x0 + y0
        if k > 7:
            if any([self.grid[y][x] for x, y in zip(range(k - 8 + 1, 8), range(8 - 1, k - 8, -1))]):
                return False
        else:
            if any([self.grid[y][x] for x, y in zip(range(0, k + 1), range(k, -1, -1))]):
                return False

        # bltr diagonal:
        k = y0 - x0
        if k < 0:
            if any([self.grid[y][x] for x, y in zip(range(-k, 8), range(0, 8 - k + 1))]):
                return False
        else:
            if any([self.grid[y][x] for x, y in zip(range(0, 8 - k), range(k, 8))]):
                return False

        return True


    def solve(self, num_queens):
        while self.num < num_queens:
            for y in range(8):
                for x in range(8):
                    if self._is_safe_place(y, x):
                        self.grid[y][x] = 1
                        self.num += 1
                        self.solve(num_queens)
                        self.grid[y][x] = 0
                        self.num -= 1
            return

        print(np.matrix(self.grid))
        input("more?")

    def solve_g(self, num_queens):
        while self.num < num_queens:
            for y in range(8):
                for x in range(8):
                    if self._is_safe_place(y, x):
                        self.grid[y][x] = 1
                        self.num += 1
                        self.solve_g(num_queens)
                        self.grid[y][x] = 0
                        self.num -= 1
            return

        yield self.grid




def main():
    global grid
    sq = SevenQueens(grid)
    # sq.solve(8)

    for grd in sq.solve_g(3):
        print(np.matrix(grd))



if __name__ == '__main__':
    main()
