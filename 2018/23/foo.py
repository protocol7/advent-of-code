import sys
import re

def parse(line):
    return [int(i) for i in re.findall("-?\d+", line)]

def man_dist(x1, y1, z1, x2, y2, z2):
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)

bots = map(parse, sys.stdin)

bots = sorted(bots, key=lambda p: p[3])

lx, ly, lz, lr = bots[-1]

count = 0
for x, y, z, r in bots:
    if man_dist(x, y, z, lx, ly, lz) <= lr:
        count += 1
print(count)
