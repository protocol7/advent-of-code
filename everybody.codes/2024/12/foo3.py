#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *
from dataclasses import dataclass

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

segments = [(Point(0, 1), 1), (Point(0, 2), 2), (Point(0, 3), 3)]

a = segments[0][0]
ms = [Point(a.x + x, a.y + y) for x, y in xs]

@dataclass
class Projectile:
    x: int
    y: int
    phase2: int
    value: int

best = defaultdict(lambda: sys.maxsize)
ps = []

out = 0
for time in count(1):
    if not ms:
        break

    # projectiles that have already passed all meteors can be ignored
    max_x = max(m.x for m in ms)

    # move projectiles
    nps = []
    for p in ps:
        if p.phase2:
            p.x += 1
            p.phase2 -= 1
            if p.x <= max_x:
                nps.append(p)
        else:
            p.x += 1
            p.y -= 1
            if p.y > 0 and p.x <= max_x:
                nps.append(p)

    ps = nps

    # send new projectiles
    # rather than sending all projectiles with all powers at once, we can send power p at time t
    # since this with lower powers will already have passed the relevant points in phase 1 already
    # since we send them at time t, they have also passes phase 1, so we can just start them at phase 2
    for segment, n in segments:
        ps.append(Projectile(segment.x + time, segment.y + time, time, n * time))

    # set the current best value at each projectile position
    for p in ps:
        k = (p.x, p.y)
        best[k] = min(best[k], p.value)

    # move meteors
    nms = []
    for m in ms:
        m.x -= 1
        m.y -= 1

        v = best[(m.x, m.y)]
        if v != sys.maxsize:
            out += v
        else:
            nms.append(m)

    ms = nms

print(out)
