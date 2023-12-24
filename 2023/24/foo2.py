import sys
from util import ints
from z3 import Int, Ints, Solver


def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

s = Solver()

rx, ry, rz, rdx, rdy, rdz = Ints("rx ry rz rdx rdy rdz")

for i, ((x0, y0, z0, dx0, dy0, dz0)) in enumerate(xs):
	t = Int("t" + str(i))
	s.add(rx + rdx * t == x0 + dx0 * t)
	s.add(ry + rdy * t == y0 + dy0 * t)
	s.add(rz + rdz * t == z0 + dz0 * t)

s.check()

m = s.model()

print(m[rx].as_long() + m[ry].as_long() + m[rz].as_long())
