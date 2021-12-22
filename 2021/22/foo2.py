import sys
from util import *
from functools import cache

def parse(line):
    state = line.startswith("on")
    x1, x2, y1, y2, z1, z2 = ints(line.strip())

    return state, ((x1, x2), (y1, y2), (z1, z2))

def vol(cube):
    (x1, x2), (y1, y2), (z1, z2) = cube
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 +1)

def intersection_1d(r1, r2):
    a1, a2 = r1
    b1, b2 = r2

    s = max(a1, b1)
    e = min(a2, b2)

    if s > e:
        # don't intersect
        return None
    else:
        return s, e

def intersection_3d(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2

    xi = intersection_1d(x1, x2)
    yi = intersection_1d(y1, y2)
    zi = intersection_1d(z1, z2)

    if xi is None or yi is None or zi is None:
        # don't intersect
        return None
    else:
        return (xi, yi, zi)

@cache
def contributes(cube, removals):
    v = vol(cube)

    for i, (_, cube2) in enumerate(removals):
        cc = intersection_3d(cube, cube2)

        if cc is not None:
            v -= contributes(cc, removals[i+1:])

    return v

xs = tuple(map(parse, sys.stdin))

c = 0
for i, f in enumerate(xs):
    state, cube = f

    # ignore off cuboids
    if state:
        c += contributes(cube, xs[i+1:])

print(c)