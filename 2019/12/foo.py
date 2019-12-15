import sys
from itertools import *
from util import *

def parse(line):
    return ints(line) + [0]*3

m = map(parse, sys.stdin)
d = dict(enumerate(m))

combs = list(combinations(d.keys(), 2))

for i in range(1000):
    # update velocities
    for a, b in combs:
        m1 = d[a]
        m2 = d[b]
        for i in range(3):
            # x, y, z
            g = sign(m1[i] - m2[i])
            m1[i+3] -= g
            m2[i+3] += g

    # update positions
    for m in d.values():
        for i in range(3):
            m[i] += m[i+3]

    # calculate energies
    t = 0
    for m in d.values():
        p = 0
        k = 0
        for i in range(3):
            p += abs(m[i])
            k += abs(m[i+3])
        t += p * k

# after all the rounds
print(t)
