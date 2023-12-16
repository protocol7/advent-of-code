import sys
from util import ints

def parse(line):
    return sum(ints(line))

xs = set(map(parse, sys.stdin))
ys = set(range(100, 500))

print(next(iter(ys - xs)))
