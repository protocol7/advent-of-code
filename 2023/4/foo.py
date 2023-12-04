import sys
from util import ints


def parse(line):
    l = line.strip()
    _, b = l.split(":")
    b, c = b.split("|")

    return set(ints(b)), set(ints(c))


xs = list(map(parse, sys.stdin))

print(sum(int(pow(2, len(b & c) - 1)) for b, c in xs))
