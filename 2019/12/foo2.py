import sys
from itertools import *
from util import *

def parse(line):
    return ints(line) + [0]*3

m = map(parse, sys.stdin)
moons = dict(enumerate(m))

combs = list(combinations(moons.keys(), 2))

def state(moons):
    xyz = [[], [], []]
    for m in moons.values():
        for i in range(3):
            xyz[i].append(m[i])
            xyz[i].append(m[i+3])
    return [tuple(l) for l in xyz]

# initial state
xi, yi, zi = state(moons)

# round at which each dimension was found
xf = 0
yf = 0
zf = 0

rounds = 0
while True:
    # update velocities
    for a, b in combs:
        m1 = moons[a]
        m2 = moons[b]
        for i in range(3):
            # x, y, z
            x = sign(m1[i] - m2[i])
            m1[i+3] -= x
            m2[i+3] += x

    # update positions
    for m in moons.values():
        for i in range(3):
            m[i] += m[i+3]

    rounds += 1

    # check if any dimension has rotated
    x, y, z = state(moons)

    if x == xi and not xf:
        xf = rounds
    if y == yi and not yf:
        yf = rounds
    if z == zi and not zf:
        zf = rounds

    if xf and yf and zf:
        break


print(lcm(xf, yf, zf))
