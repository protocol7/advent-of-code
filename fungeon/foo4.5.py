#!/usr/bin/env python3

import sys
from util import *

# https://spotify.slack.com/archives/C2RUDPD63/p1735238455771449
#
# You have entered a dungeon. You are still standing at the bottom of the staircase where you entered
# (marked < on the map), facing north (up on the map). Before leaving the dungeon, you are compelled
# to explore it.
#
# You can walk on the floor tiles (marked . on the map). You always walk forward if you can, without
# turning. Walking to the next tile takes one tick of dungeon time.
# Whenever you are about to walk into a wall (marked [, #, or ] on the map), you instead stay where
# you are and turn. You turn 90 degrees left in front of [ walls, 180 degrees around in front of # walls,
# and 90 degrees right in front of ] walls. Staying and turning also takes one tick. If you still face a
# wall after turning, that is handled during the next tick.
#
# You start counting ticks immediately, including any time spent turning before leaving the staircase.
# After how many ticks do you return to the staircase?
#
# In this dungeon, there are additional wall types for turning diagonally (marked {, (, ), and } on the
# map). While facing a diagonal direction, the tile in front of you is the next tile in the diagonal
# direction. As before, you always walk forward if you can. You turn 135 degrees left in front of {
# walls, 45 degrees left in front of ( walls, 45 degrees right in front of ) walls, and 135 degrees
# right in front of } walls.

DIRS = [N, NE, E, SE, S, SW, W, NW]

WALLS = {
    "#": 4,
    "[": -2,
    "]": 2,
    "(": -1,
    ")": 1,
    "{": -3,
    "}": 3,
}

def turn(wall, dir):
    w = WALLS[wall]
    return DIRS[(DIRS.index(dir) + w) % 8]

def parse(line):
    return line.strip()

xss = sys.stdin.read().strip().split("\n\n")

xss = [list(map(parse, xs.split("\n"))) for xs in xss]

gs = [Grid(xs) for xs in xss]
start_level = 0

start = gs[start_level].points_by_value()["<"][0]
gs[start_level].d[start] = "."
dir = N

DS = "0123456789+-*/%"

def run(gs, start, dir, level):
    stack = []
    p = start
    level = start_level
    while True:
        np = p + dir

        if np == start and level == start_level:
            return stack.pop()

        nv = gs[level][np]

        if nv in DS:
            if nv.isdigit():
                stack.append(int(nv))
            else:
                b = stack.pop()
                a = stack.pop()

                if nv == "+":
                    stack.append(a + b)
                elif nv == "-":
                    stack.append(a - b)
                elif nv == "*":
                    stack.append(a * b)
                elif nv == "/":
                    stack.append(a // b)
                elif nv == "%":
                    stack.append(a % b)

            p = np
        elif nv == ".":
            p = np
        elif nv == ">":
            p = np
            level += 1
        elif nv == "<":
            p = np
            level -= 1
        else:
            dir = turn(nv, dir)

OPS = "+-*/%"

for i in range(len(gs)):
    for op in OPS:
        ps = gs[i].points_by_value()[op]

        for p in ps:
            for other_op in OPS:
                if other_op == op:
                    continue

                gs[i].d[p] = other_op

                try:
                    ff = run(gs, start, dir, start_level)

                    if ff % 2025 == 0:
                        print("2025!", i, p, op, other_op, ff)
                except ZeroDivisionError:
                    pass

                gs[i].d[p] = op
