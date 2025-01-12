#!/usr/bin/env python3

import sys
from collections import defaultdict
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from util import *

# https://github.com/elemel/call-of-the-fungeon

DIRS = [E, SE, S, SW, W, NW, N, NE]

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

def turn(wall, registers):
    assert wall != "#"

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

    # print(steps, p, WW[dir(registers)], np, nv, stack[:registers["s"]], dict(registers))

    npos = position(gs, np, level)

    if (np == start and level == start_level) or npos < 0:
        print(steps)
        break

    if nv.isdigit():
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
