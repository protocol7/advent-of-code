import sys
from fractions import gcd

def parse(line):
    return line.strip()

parsed = map(parse, sys.stdin)

m = set()
for y, line in enumerate(parsed):
    for x, c in enumerate(line):
        if c == "#":
            m.add((x, y))

ss = []
for x, y in m:
    seen = set()
    for xx, yy in m:
        if x == xx and y == yy:
            continue
        dx = xx - x
        dy = yy - y
        g = abs(gcd(dx, dy))
        dx /= g
        dy /= g

        seen.add((dx, dy))

    ss.append(len(seen))

print(max(ss))
