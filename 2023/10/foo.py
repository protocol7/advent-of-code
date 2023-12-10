import sys
from util import Grid, Point, DOWN, LEFT, RIGHT, UP

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

s = g.points_by_value()["S"][0]

DS = {
    (RIGHT, "J"): UP,
    (RIGHT, "7"): DOWN,
    (RIGHT, "-"): RIGHT,

    (LEFT, "L"): UP,
    (LEFT, "F"): DOWN,
    (LEFT, "-"): LEFT,

    (DOWN, "L"): RIGHT,
    (DOWN, "J"): LEFT,
    (DOWN, "|"): DOWN,

    (UP, "F"): RIGHT,
    (UP, "7"): LEFT,
    (UP, "|"): UP,
}

# check all possible replacments for S
for c in "-|FJ7L":
    # if S was hiding c, what directions would the pipe go in?
    dirs = [b for (_, a), b in DS.items() if a == c]

    # does the neighbours match those?
    if all(DS.get((d, g[s + d])) for d in dirs):
        # pick one of the directions to start with, either will work
        S = dirs[0]
        # replace S in the grid with the correct pipe
        g.d[s] = c
        break

d = S
# move one step so the `while` below doesn't match immediatelly
p = Point(s) + d

path = set([p])
while p != s:
    d = DS[(d, g[p])]

    p += d
    path.add(p)

# part 1
print(len(path) // 2)

# part 2
# https://www.tutorialspoint.com/computer_graphics/images/scan_line_algorithm.jpg
s = 0
for row in g.rows():
    inpoly = False

    for p, c in row:
        if p in path and c in "|LJ":
            inpoly = not inpoly

        if p not in path and inpoly:
            s += 1

print(s)
