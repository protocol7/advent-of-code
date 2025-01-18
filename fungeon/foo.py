#!/usr/bin/env python3

import sys
from collections import defaultdict
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from util import *

# https://github.com/elemel/call-of-the-fungeon

DIRS = [E, SE, S, SW, W, NW, N, NE]

WALLS = {
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

def turn(wall, registers):
    w = WALLS[wall]
    registers["r"] = registers["r"] + w

def dir(registers):
    return DIRS[registers["r"] % 8]

def parse(line):
    return line.strip()

registers = defaultdict(int)
stack = [0] * 10000

def push(x):
    stack[registers["s"]] =  x
    registers["s"] += 1

def pop():
    registers["s"] -= 1
    return stack[registers["s"]]

def position(gs, p, level):
    pos = 0

    for i in range(level):
        mx, my = gs[i].max()
        size = (mx + 1) * (my + 1)
        pos += size

    mx, _ = gs[level].max()

    return pos + p.x + p.y * (mx + 1)

def from_position(gs, pos):
    for level, g in enumerate(gs):
        mx, my = gs[level].max()
        size = (mx + 1) * (my + 1)

        if pos > size:
            pos -= size
        else:
            break

    mx, _ = gs[level].max()

    y = pos // (mx + 1)
    x = pos % (mx + 1)

    return Point(x, y), level

xss = sys.stdin.read().strip().split("\n\n")

xss = [list(map(parse, xs.split("\n"))) for xs in xss]

gs = [Grid(xs) for xs in xss]
start_level = 0

start = gs[start_level].points_by_value()["<"][0]
gs[start_level].d[start] = "."

p = start
level = start_level
steps = 0
while True:
    steps += 1

    np = p + dir(registers)
    nv = gs[level][np]


    npos = position(gs, np, level)

    if (np == start and level == start_level) or npos < 0:
        print()
        print(steps)
        break

    if nv == "$":
        # Whenever you step onto a mimic tile, pop a number from the stack.
        # Act as if you stepped onto a tile with that number as extended ASCII code.
        # For a wall tile, move backward to the tile before the mimic tile, then turn
        # as specified by the wall tile. This counts as a single step.
        nv = chr(pop())

        if nv in WALLS:
            np = p
            npos = position(gs, np, level)

    # print(steps, p, WW[dir(registers)], np, nv, stack[:registers["s"]], dict(registers))

    if nv == "'":
        # This dungeon contains stash tiles (marked ' on the map), mimic tiles (marked $), and passage tiles (marked ").
        # Whenever you step onto a stash tile, move forward to the next tile immediately, then push the extended
        # ASCII code (0 through 255) of that tile onto the stack. This counts as a single step, and lets you
        # stand on any tile, including wall tiles.
        np = np + dir(registers)
        nv = gs[level][np]
        npos = position(gs, np, level)

        push(ord(nv))

        p = np
    elif nv == '"':
        # Whenever you step onto a passage tile, search for the next passage tile in your facing direction.
        # If you find one, push your position onto the stack, then move to the other passage tile, and finally
        # push your position onto the stack again. This counts as a single step, and lets you pass through any
        # tile, including wall tiles.
        nnp = np + dir(registers)
        while gs[level][nnp] != '"':
            nnp = nnp + dir(registers)

        if nnp:
            push(npos)
            np = nnp
            npos = position(gs, np, level)
            push(npos)

        p = np

    elif nv == "?":
        # This dungeon contains reader tiles (marked ? on the map) and writer tiles (marked !).

        # Whenever you step onto a reader tile, pop a number a from the stack. Find the tile at position a, t
        # hen get the extended ASCII code of that tile as another number b. Finally, push b onto the stack.

        # Whenever you step onto a writer tile, pop two numbers from the stack: first b, then a.
        # Find the tile at position a, then set the extended ASCII code of that tile to b % 256.

        a = pop()

        apoint, alevel = from_position(gs, a)
        b = ord(gs[alevel][apoint])

        push(b)

        p = np
    elif nv == "!":
        b = pop()
        a = pop()

        if a == -2:
            #print(b)
            print(chr(b % 256), end="")
        else:
            apoint, alevel = from_position(gs, a)
            gs[alevel].d[apoint] = chr(b % 256)

        p = np
    elif nv.isdigit():
        push(int(nv))

        p = np
    elif nv in "pP_":
        if nv == "p":
            # get your position as a number, then push that number onto the stack
            push(npos)
        elif nv == "P":
            # pop a number from the stack, then set your position to that number
            np, level = from_position(gs, pop())
        else:
            # pop a number b from the stack, then get your position as another number a, then push a onto the stack, and finally set your position to b
            b = pop()
            a = npos
            push(a)
            np, level = from_position(gs, b)

        p = np
    elif nv in "sS":
        if nv == "s":
            # get the stack size as a number, then push that number onto the stack
            push(registers["s"])
        else:
            # pop a number from the stack, then set the stack size to that number
            # stack starts at the end of the list
            registers["s"] = pop()

        p = np
    elif nv in ascii_letters:
        if nv in ascii_lowercase:
            push(registers[nv])
        else:
            registers[nv.lower()] = pop()

        p = np
    elif nv in "+-*/%;&|^\\":
        b = pop()
        a = pop()

        if nv == "+":
            push(a + b)
        elif nv == "-":
            push(a - b)
        elif nv == "*":
            push(a * b)
        elif nv == "/":
            push(a // b)
        elif nv == "%":
            push(a % b)
        elif nv == ";":
            # swap the numbers on top of the stack
            push(b)
            push(a)
        elif nv == "&":
            push(a & b)
        elif nv == "|":
            push(a | b)
        elif nv == "^":
            push(a ^ b)
        elif nv == "\\":
            # signed -> unsigned
            a = a & 0xFFFFFFFF

            # b is the number of bits to rotate, constrained to 0 <= b < 32
            b = b % 32

            # rotate left
            ans = ((a << b) | (a >> (32 - b))) & 0xFFFFFFFF
            # unsigned -> signed
            ans = (ans ^ 0x80000000) - 0x80000000

            push(ans)

        p = np
    elif nv in ":,~":
        a = pop()

        if nv == ":":
            push(a)
            push(a)
        elif nv == ",":
            # discard the number on top of the stack
            pass
        elif nv == "~":
            # invert the number on top of the stack
            push(~a)

        p = np
    elif nv == "=":
        # Whenever you step onto a = tile, you pop a number b from the stack,
        # then pop another number a from the stack, and finally turn based on
        # how the numbers compare. You turn 90 degrees left if a < b, or 90
        # degrees right if a > b. If the numbers are equal, your direction
        # remains the same as before.

        b = pop()
        a = pop()

        if a < b:
            turn("[", registers)
        elif a > b:
            turn("]", registers)

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
        turn(nv, registers)
