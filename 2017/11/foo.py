import sys

# Using code cooridnates as described here
# https://www.redblobgames.com/grids/hexagons/

def parse(line):
    return line.strip().split(",")

def man_dist(x, y, z):
    return (abs(x) + abs(y) + abs(z)) / 2

steps = parse(sys.stdin.read())

dirs = {
        "se": [1, -1, 0],
        "sw": [-1, 0, 1],
        "ne": [1, 0, -1],
        "nw": [-1, 1, 0],
        "n": [0, 1, -1],
        "s": [0, -1, 1]
        }

x, y, z = 0, 0, 0

max_dist = -sys.maxint

for s in steps:
    dx, dy, dz = dirs[s]
    x += dx
    y += dy
    z += dz

    max_dist = max(max_dist, man_dist(x, y, z))

print(man_dist(x, y, z))

# part 2
print(max_dist)
