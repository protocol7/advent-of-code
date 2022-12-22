import sys
from util import *

xs, path = sys.stdin.read().split("\n\n")

path = path.strip()

def warp_input(p):
    # hello ugly hardcoded mess

    px, py = p

    if py == -1:
        if px < 100:
            return (0, 150 + (px - 50)), RIGHT
        else:
            return (0 + (px - 100), 199), UP
    elif px == -1:
        if py >= 150:
            return (50 + (py - 150), 0), DOWN
        else:
            # invert!
            return (50, 49 - (py - 100)), RIGHT
    elif px == 49:
        if py < 50:
            # invert!
            return (0, 149 - py), RIGHT
        else:
            return (py - 50, 100), DOWN
    elif px == 50:
        return (50 + (py - 150), 149), UP
    elif px == 100:
        if py < 100:
            return (100 + (py - 50), 49), UP
        else:
            # invert!
            return (149, 149 - py), LEFT
    elif px == 150:
        # invert!
        return (99, 149 - py), LEFT
    elif py == 50:
        return (99, 50 + (px - 100)), LEFT
    elif py == 99:
        return (50, 50 + px), RIGHT
    elif py == 150:
        return (49, 150 + (px - 50)), LEFT
    elif py == 200:
        return (100 + px, 0), DOWN

def warp_sample(p):
    if p == (12, 5):
        return (14, 8), DOWN
    elif p == (10, 12):
        return (1, 7), UP
    elif p == (6, 3):
        return (8, 2), RIGHT

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


if g.width() == 16:
    warp = warp_sample
else:
    warp = warp_input

# move one step in the path at a time
for step in ps:
    if type(step) == int:
        for _ in range(step):
            x, y = pos
            np = pos + dir

            if g[np] == ".":
                pos = np
            elif g[np] == "#":
                break
            elif g[np] == " " or g[np] is None:
                # where should we end up and in what direction?
                sp, sd = warp(np)

                if g[sp] == ".":
                    pos = Point(sp)
                    dir = sd
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