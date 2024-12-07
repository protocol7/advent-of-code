#!/usr/bin/env python3

import sys
from util import Grid, UP, turn_right

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

start = g.points_by_value()["^"][0]
g.d[start] = "."

def is_loop(grid, p, dir):
    seen = set([(p, dir)])
    while True:
        np = p + dir
        nv = grid[np]

        if nv == "#":
            dir = turn_right(dir)
        elif nv is None:
            return False
        elif nv == ".":
            k = (np, dir)
            if k in seen:
                return True
            seen.add(k)
            p = np


def walk(grid, p, dir):
    path = [(p, dir)]
    tested = set()
    obstacles = 0

    while True:
        np = p + dir
        nv = grid[np]

        if nv == "#":
            dir = turn_right(dir)
        elif nv is None:
            return path, obstacles
        elif nv == ".":
            if np not in tested:
                # what if np was an obstacle?
                g.d[np] = "#"
                obstacles += is_loop(g, p, dir)
                g.d[np] = "."

                tested.add(np)

            path.append((np, dir))
            p = np

path, obstacles = walk(g, start, UP)

print(obstacles)
