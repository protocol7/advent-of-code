#!/usr/bin/env python3

import sys
from util import *

# https://github.com/elemel/fungeon-call
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
#
# ...

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

WW = {
    N: "N",
    NE: "NE",
    E: "E",
    SE: "SE",
    S: "S",
    SW: "SW",
    W: "W",
    NW: "NW",
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

stack = []
p = start
level = start_level
steps = 0
while True:
    steps += 1

    np = p + dir

    if np == start and level == start_level:
        if stack:
            print(stack.pop())
        else:
            print(steps)
        break

    nv = gs[level][np]

    # print(p, WW[dir], np, nv, stack)

    if nv.isdigit():
        stack.append(int(nv))

        p = np
    elif nv in "+-*/%;&|^\\":
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
        elif nv == ";":
            # swap the numbers on top of the stack
            stack.append(b)
            stack.append(a)
        elif nv == "&":
            stack.append(a & b)
        elif nv == "|":
            stack.append(a | b)
        elif nv == "^":
            stack.append(a ^ b)
        elif nv == "\\":
            # signed -> unsigned
            a = a & 0xFFFFFFFF

            # b is the number of bits to rotate, constrained to 0 <= b < 32
            b = b % 32

            # rotate left
            ans = ((a << b) | (a >> (32 - b))) & 0xFFFFFFFF
            # unsigned -> signed
            ans = (ans ^ 0x80000000) - 0x80000000

            stack.append(ans)

        p = np
    elif nv in ":,~":
        a = stack.pop()

        if nv == ":":
            stack.append(a)
            stack.append(a)
        elif nv == ",":
            # discard the number on top of the stack
            pass
        elif nv == "~":
            # swap the numbers on top of the stack
            stack.append(~a)

        p = np
    elif nv == "=":
        # Whenever you step onto a = tile, you pop a number b from the stack,
        # then pop another number a from the stack, and finally turn based on
        # how the numbers compare. You turn 90 degrees left if a < b, or 90
        # degrees right if a > b. If the numbers are equal, your direction
        # remains the same as before.

        b = stack.pop()
        a = stack.pop()

        if a < b:
            dir = turn("[", dir)
        elif a > b:
            dir = turn("]", dir)

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
