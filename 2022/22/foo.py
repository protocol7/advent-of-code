import sys
from util import *

xs, path = sys.stdin.read().split("\n\n")

path = path.strip()

# parse path
ps = []
last = ""
for c in path:
    if c.isdigit():
        last += c
    else:
        if last:
            ps.append(int(last))
            last = ""
        ps.append(c)

if last:
    ps.append(int(last))

g = Grid(xs.split("\n"))

# find starting point
for pos, v in g:
    if c == ".":
        break

# start facing right
dir = RIGHT

# move one step in the path at a time
for step in ps:
    if type(step) == int:
        for _ in range(step):
            np = pos + dir

            if g[np] == ".":
                pos = np
            elif g[np] == "#":
                break
            elif g[np] is None or g[np] == " ":
                # wrap
                px, py = pos
                if dir == RIGHT:
                    sp = Point(0, py)
                elif dir == LEFT:
                    sp = Point(g.width(), py)
                elif dir == DOWN:
                    sp = Point(px, 0)
                elif dir == UP:
                    sp = Point(px, g.height())

                while g[sp] is None or g[sp] == " ":
                    sp += dir

                if g[sp] == ".":
                    pos = sp
                elif g[sp] == "#":
                    break

    elif step == "L":
        dir = turn_left(dir)
    elif step == "R":
        dir = turn_right(dir)

# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
f = {
    RIGHT: 0,
    LEFT: 2,
    UP: 3,
    DOWN: 1,
}

px, py = pos

# The final password is the sum of 1000 times the row, 4 times the column, and the facing.

print(1000 * (py+1) + 4 * (px+1) + f[dir])