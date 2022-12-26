import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = sys.stdin.read().strip()

room = ["  ##",
        " ####",
        "######",
        "######",
        " ####",
        "  ##"]

d = set()
for y, row in enumerate(room):
    for x, c in enumerate(row):
        if c == "#":
            d.add((x, y))

x, y = 2, 0

dir = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}

ps = []
for m in xs:
    dx, dy = dir[m]

    nx = x + dx
    ny = y + dy

    if (nx, ny) in d:
        x = nx
        y = ny

    ps.extend((x, y))

print(sum(ps))