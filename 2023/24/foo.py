import sys
from util import ints, sign, Line


def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

if len(xs) == 5:
    # sample
    ta = 7
    tb = 27
else:
    ta = 200000000000000
    tb = 400000000000000

tt = 0
for i, (x0, y0, _, dx0, dy0, _) in enumerate(xs):
    for x1, y1, _, dx1, dy1, _ in xs[i:]:

        l1 = Line.from_point_and_delta((x0, y0), dx0, dy0)
        l2 = Line.from_point_and_delta((x1, y1), dx1, dy1)

        p = l1.intersection(l2)

        if p is None:
            # not intersecting
            continue
        else:
            if p.x < ta or p.x > tb or p.y < ta or p.y > tb:
                # outside test area
                continue
            elif sign(p.x - x0) == sign(dx0) and sign(p.y - y0) == sign(dy0) and sign(p.x - x1) == sign(dx1) and sign(p.y - y1) == sign(dy1):
                # ok
                tt += 1

print(tt)
