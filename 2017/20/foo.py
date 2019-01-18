import sys
import re

def parse(line):
    return [int(i) for i in re.findall("-?\d+", line)]

def man_dist(x, y, z):
    return abs(x) + abs(y) + abs(z)

ps = map(parse, sys.stdin)
X, Y, Z, VX, VY, VZ, AX, AY, AZ = range(9)


for _ in range(1000):
    for p in ps:
        x, y, z, vx, vy, vz, ax, ay, az = p

        p[VX] += p[AX]
        p[VY] += p[AY]
        p[VZ] += p[AZ]
        p[X] += p[VX]
        p[Y] += p[VY]
        p[Z] += p[VZ]

min_md = sys.maxint
min_p = None
for i, p in enumerate(ps):
    md = man_dist(p[X], p[Y], p[Z])

    if md < min_md:
        min_md = md
        min_p = i

print(min_p)
