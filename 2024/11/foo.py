#!/usr/bin/env python3

import sys
from collections import Counter
from util import ints

stones = ints(sys.stdin.read())

def blink(stone):
    if stone == 0:
        return [1]

    f = str(stone)
    if len(f) % 2 == 0:
        mid = len(f) // 2
        return int(f[:mid]), int(f[mid:])
    else:
        return [stone * 2024]

def run(counts, rounds):
    for r in range(rounds):
        nc = Counter()
        for s, count in counts.items():
            ns = blink(s)
            for n in ns:
                nc[n] += count

        counts = nc

    return sum(counts.values())

for rounds in (25, 75):
    print(run(Counter(stones), rounds))
