import sys
from util import ints, chunks
from z3 import Solver, Real, sat

def parse(line):
    return chunks(ints(line.strip()), 3)

xs = list(map(parse, sys.stdin))

if len(xs) == 5:
    # sample
    ta = 7
    tb = 27
else:
    ta = 200000000000000
    tb = 400000000000000

tt = 0
for i, ((x0, y0, z0), (dx0, dy0, dz0)) in enumerate(xs):
    for j, ((x1, y1, z1), (dx1, dy1, dz1)) in enumerate(xs):
        if i >= j:
            continue

        s = Solver()

        t0 = Real("t0")
        t1 = Real("t1")

        ex0 = x0 + dx0 * t0
        ey0 = y0 + dy0 * t0

        ex1 = x1 + dx1 * t1
        ey1 = y1 + dy1 * t1

        # must be in the future
        s.add(t0 >= 0)
        s.add(t1 >= 0)

        # must intersect
        s.add(ex0 == ex1)
        s.add(ey0 == ey1)

        # must intersect within the boundary
        s.add(ex0 >= ta, ex0 <= tb)
        s.add(ey0 >= ta, ey0 <= tb)

        s.add(ex1 >= ta, ex1 <= tb)
        s.add(ey1 >= ta, ey1 <= tb)

        tt += s.check() == sat

        if s.check() == sat:
            print((x0, y0, z0), (dx0, dy0, dz0), (x1, y1, z1), (dx1, dy1, dz1))

print(tt)
