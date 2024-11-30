#!/usr/bin/env python3

import sys
from collections import Counter
from itertools import count
from util import *


def parse(line):
    return ints(line.strip())


xs = list(map(parse, sys.stdin))

xs = transpose(xs)

counter = Counter()

def get_count(counter):
    return counter.most_common(1)[0][1]

check_every = False
for r in count():
    if r % 1000 == 0 and r > 1000:
        # checking the count turns out to be the most expensive, so first we only check roughly
        if get_count(counter) > 2020:
            check_every = True

    c = r % len(xs)
    n = xs[c].pop(0)

    col = xs[(c + 1) % len(xs)]

    pos = (n - 1) % (len(col) * 2)
    pos = min(pos, len(col)) - max(pos - len(col), 0)

    col.insert(pos, n)

    shout = int("".join(map(str, [col[0] for col in xs])))

    counter[shout] += 1

    if check_every and get_count(counter) == 2024:
        print((r+1) * counter.most_common(1)[0][0])
        break
