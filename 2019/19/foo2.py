import sys
from util import *
from intcode import *

prog = parse(sys.stdin)

def run(y):
    for x in range(1000, 0, -1):
        inp_iter = iter([x, y])
        ic = Intcode(prog, lambda: next(inp_iter))

        if ic.run():
            s = x
            break

    for x in range(1000):
        inp_iter = iter([x, y+99])
        ic = Intcode(prog, lambda: next(inp_iter))

        if ic.run():
            t = x
            break
    return t, s  - t

def check(y):
    x, l = run(y)
    return l >= 99

# this is a stupid solution, but works.
# binary search from y 900-1000 (found by some quick manual runs), where we
# search for a beam from x=1000 and backwards, and for c=0 and onwards at y+99
# until we can fit a 100x100 square in it.
_, y = binary_search(900, 1000, check)
x, _ = run(y)

print(x * 10000 + y)
