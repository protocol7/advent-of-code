import sys
from util import *

xx = list(map(int, sys.stdin))

for part, multiplier in ((1, 1), (10, 811589153)):
    xs = CircularList([(n * multiplier, i) for i, n in enumerate(xx)])

    for _ in range(part):
        for move in range(len(xs)):
            # find the next to move
            i = [oi for _, oi in xs].index(move)

            xs.move_by(i, xs[i][0])

    i = [n for n, _ in xs].index(0)

    s = 0
    for y in (1000, 2000, 3000):
        s += xs[y + i][0]
    print(s)
