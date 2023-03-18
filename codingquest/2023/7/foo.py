import sys
from util import *

xs = sys.stdin.readlines()

fs = list(map(tuple, chunks(ints(xs[1]), 2)))
ms = xs[3].strip()

d = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}

s = [(0, 0)]

p = 0
for m in ms:
    dx, dy = d[m]

    x, y = s[-1]

    x += dx
    y += dy

    if (x, y) in s:
        break
    if x < 0 or y < 0 or x >= 20 or y >= 20:
        break

    s.append((x, y))

    p += 1

    # eating fruit?
    if (x, y) == fs[0]:
        p += 100
        fs.pop(0)
    else:
        s.pop(0)

print(p)