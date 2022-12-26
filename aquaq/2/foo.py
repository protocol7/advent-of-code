import sys
from collections import *
from itertools import *
from util import *

xs = ints(sys.stdin.read())

print(xs)

i = 0

while i < len(xs):
    n = xs[i]

    try:
        last = max([j for j, v in enumerate(xs) if v == n])

        if last != i:
            xs = xs[:i] + xs[last:]

    except ValueError:
        pass

    i += 1

print(sum(xs))



