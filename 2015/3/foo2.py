import sys
from collections import defaultdict
from itertools import cycle

inp = sys.stdin.read().strip()

santa = [0, 0]
robo = [0, 0]
houses = defaultdict(int)
houses[(0, 0)] += 2

turns = cycle([santa, robo])
for c in inp:
    turn = next(turns)
    x, y = turn
    if c == "^":
        y -= 1
    elif c == "v":
        y += 1
    elif c == "<":
        x -= 1
    elif c == ">":
        x += 1
    turn[0] = x
    turn[1] = y

    houses[(x, y)] += 1

print(len(houses))
