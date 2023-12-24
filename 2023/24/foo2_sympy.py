import sys
from util import ints, chunks
from sympy import symbols, solve, Eq


def parse(line):
    return chunks(ints(line.strip()), 3)

xs = list(map(parse, sys.stdin))

rx, ry, rz, rdx, rdy, rdz = symbols("rx ry rz rdx rdy rdz")

equations = []
times = []
for i, ((x0, y0, z0), (dx0, dy0, dz0)) in enumerate(xs[:3]):
	t = symbols("t" + str(i))

	times.append(t)

	equations.append(Eq(rx + rdx * t, x0 + dx0 * t))
	equations.append(Eq(ry + rdy * t, y0 + dy0 * t))
	equations.append(Eq(rz + rdz * t, z0 + dz0 * t))

r = solve(equations, rx, ry, rz, rdx, rdy, rdz, *times, dict=True)[0]

print(r[rx] + r[ry] + r[rz])
