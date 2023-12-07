import sys
from util import ints, binary_search


def parse(line):
    return ints(line.strip())


xs = list(map(parse, sys.stdin))

a = int("".join(str(x) for x in xs[0]))
b = int("".join(str(x) for x in xs[1]))

def d(i):
    return i * (a - i)

# guess that halfway is a winner
_, f = binary_search(0, a // 2, lambda i: d(i) > b)
_, g = binary_search(a // 2, a, lambda i: d(i) < b)

print(g - f)
