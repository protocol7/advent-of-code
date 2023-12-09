import sys
from util import ints


def parse(line):
    return sum(ints(line.strip()))


xs = list(map(parse, sys.stdin))

for a, b in zip(xs, xs[1:]):
    if a > b:
        print(a)
        break
