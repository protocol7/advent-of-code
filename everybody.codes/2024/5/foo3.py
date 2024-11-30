#!/usr/bin/env python3

import sys
from collections import Counter
from itertools import count
from util import *


def parse(line):
    return ints(line.strip())


xs = list(map(parse, sys.stdin))

xs = transpose(xs)

boards = set()

ma = 0
for r in count():
    if r % 1000 == 0 and r > 1000:
        pass

    c = r % len(xs)
    n = xs[c].pop(0)

    col = xs[(c + 1) % len(xs)]

    pos = (n - 1) % (len(col) * 2)
    pos = min(pos, len(col)) - max(pos - len(col), 0)

    col.insert(pos, n)

    shout = int("".join(map(str, [col[0] for col in xs])))

    board = tuple(tuple(col) for col in xs)
    if board in boards:
        break
    boards.add(board)

    ma = max(ma, shout)

print(ma)
