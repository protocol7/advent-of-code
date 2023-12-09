import sys
from util import ints
from functools import reduce

xs = list(map(ints, sys.stdin))

def foo(x):
    # create a stack of lists from each delta
    s = [x]
    while any(s[-1]):
        s.append([b - a for a, b in zip(s[-1], s[-1][1:])])

    # now extrapolate backwards through the stack
    return reduce(lambda e, g: e + g[-1], s[::-1], 0)

print(sum(foo(x) for x in xs))
print(sum(foo(x[::-1]) for x in xs))
