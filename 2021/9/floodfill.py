import sys
from util import *

def parse(line):
    return list(map(int, line.strip()))

g = list(map(parse, sys.stdin))

def floodfill(grid, x, y):
    if grid[y][x] in (-1, 9):
        # already seen or a ridge
        return 0
    grid[y][x] = -1
    
    # recursively flood fill all neighbouring cells:
    return 1 + sum(floodfill(grid, xx, yy) for xx, yy in iter_orthogonal(x, y, g))

basins = sorted(floodfill(g, x, y) for x, y, _ in iter_grid(g))

print(product(x for x in basins[-3:]))
