import sys
from util import *

def parse(line):
    a, b = line.strip().split()
    b = int(b)
    return a, b

xs = list(map(parse, sys.stdin))

s = []
for _ in range(10):
    s.append([0, 0])

dirs = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}

seen = set()
for a, b in xs:
    for _ in range(b):
        mx, my = dirs[a]
        s[0][0] += mx
        s[0][1] += my

        for i in range(1, 10):
            dx = s[i-1][0] - s[i][0]
            dy = s[i-1][1] - s[i][1]

            if abs(dx) > 1 or abs(dy) > 1:
                s[i][0] += sign(dx)
                s[i][1] += sign(dy)

        seen.add((s[-1][0], s[-1][1]))

print(len(seen))
