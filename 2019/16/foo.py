import sys
from itertools import *

def rep(xs, n):
    return chain.from_iterable(repeat(x, n) for x in xs)

sig = [int(i) for i in sys.stdin.read().strip()]

pat = [0, 1, 0, -1]

for round in range(100):
    out = []
    for i in range(len(sig)):
        p = rep(pat, i+1)
        p = cycle(p)
        next(p)
        xx = 0
        for s, pp in zip(sig, p):
            xx += s * pp
        xx = abs(xx) % 10

        out.append(xx)
    sig = out

print("".join([str(i) for i in sig[:8]]))
