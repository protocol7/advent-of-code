import sys
sys.setrecursionlimit(15000)

from util import *

def parse(line):
    return tuple(ints(line))

xs = set(map(parse, sys.stdin))

ORTHOGONAL_3D = [(0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1)]

c = 0
for x, y, z in xs:
    for dx, dy, dz in ORTHOGONAL_3D:
        c += (x+dx, y+dy, z+dz) not in xs

print(c)

sx, sy, sz = [s - 2 for s in min_each(xs)]
ex, ey, ez = [s + 2 for s in max_each(xs)]

def flood_fill(dd, x ,y, z):
    # check that we are in the grid
    if x < sx or x >= ex or y < sy or y >= ey or z < sz or z >= ez:
        return

    k = (x, y, z)
    # check if we are on the boundary
    if k in xs:
        return

    # check if we are already filled
    if k in dd:
        return

    # fill
    dd.add(k)

    # attempt to fill the neighboring positions
    for dx, dy, dz in ORTHOGONAL_3D:
        flood_fill(dd, x + dx, y + dy, z + dz)

dd = set()

flood_fill(dd, sx, sy, sz)

c = 0
for x, y, z in xs:
    for dx, dy, dz in ORTHOGONAL_3D:
        c += (x+dx, y+dy, z+dz) in dd

print(c)
