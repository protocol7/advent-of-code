import sys
from itertools import *
from util import *

def parse(line):
    return ints(line) + [0]*3

m = map(parse, sys.stdin)
d = dict(enumerate(m))

combs = list(combinations(d.keys(), 2))

def sign(i):
    if i > 0:
        return 1
    elif i < 0:
        return -1
    else:
        return 0

xs = set()
ys = set()
zs = set()
xf = 0
yf = 0
zf = 0

rounds = 0
while True:
    for a, b in combs:
        m1 = d[a]
        m2 = d[b]
        for i in range(3):
            # x, y, z
            x = sign(m1[i] - m2[i])
            m1[i+3] -= x
            m2[i+3] += x

    for m in d.values():
        for i in range(3):
            m[i] += m[i+3]

    x = []
    y = []
    z = []
    for i in range(len(d)):
        m = d[i]
        x.append(m[0])
        x.append(m[0+3])
        y.append(m[1])
        y.append(m[1+3])
        z.append(m[2])
        z.append(m[2+3])

    x = tuple(x)
    y = tuple(y)
    z = tuple(z)
    if x in xs and not xf:
        xf = rounds
    if y in ys and not yf:
        yf = rounds
    if z in zs and not zf:
        zf = rounds

    if xf and yf and zf:
        break
    xs.add(x)
    ys.add(y)
    zs.add(z)

    rounds += 1

print(lcm(zf, lcm(xf, yf)))
