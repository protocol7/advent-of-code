import sys
from collections import defaultdict

inp = sys.stdin.read().strip()

x, y = 0, 0
houses = defaultdict(int)
houses[(x, y)] += 1

for c in inp:
    if c == "^":
        y -= 1
    elif c == "v":
        y += 1
    elif c == "<":
        x -= 1
    elif c == ">":
        x += 1

    houses[(x, y)] += 1

print(len(houses))
