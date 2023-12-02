import sys
from util import *


def parse(line):
    _, b = line.split(":")

    return msplit(b, ";,")
    

xs = list(map(parse, sys.stdin))

# 12 red cubes, 13 green cubes, and 14 blue cubes

t = 0
for bs in xs:
    m = {"red": 0, "blue": 0, "green": 0}

    for a in bs:
        x, y = a.split()

        m[y] = max(m[y], int(x))

    t += prod(m.values())

print(t)
