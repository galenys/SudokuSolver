import numpy as np

grid = np.array([
    [0, 2, 0, 6, 5, 8, 0, 0, 9],
    [7, 0, 0, 0, 0, 1, 5, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 7, 0, 0, 2, 3, 4, 5],
    [0, 9, 0, 0, 1, 0, 0, 0, 6],
    [0, 0, 5, 0, 0, 7, 0, 9, 1],
    [0, 7, 0, 0, 0, 0, 9, 1, 0],
    [9, 0, 0, 3, 0, 0, 0, 0, 0],
    [6, 0, 0, 1, 0, 0, 0, 0, 0]
])

def possible(x, y, n, grid):
    for i in range(9):
        if grid[y][i] == n:
            return False
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(x, y, n, grid):
                        grid[y][x] = n
                        solve(grid)
                        grid[y][x] = 0
                return
    print(grid)
    input("Find more solutions?")