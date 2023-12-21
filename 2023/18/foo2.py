import sys
from util import Point, RIGHT, LEFT, DOWN, UP

def parse(line):
    _, _, c = line.strip().split()
    c = c[2:-1]

    a = int(c[5])
    b = int(c[:5], 16)

    return a, b


xs = list(map(parse, sys.stdin))

ds = {
    0: RIGHT,
    1: DOWN,
    2: LEFT,
    3: UP,
}

def shoelace(ps):
    area = 0
    for i in range(len(ps) - 1):
        x1 = ps[i].x
        y1 = ps[i].y
        x2 = ps[i + 1].x
        y2 = ps[i + 1].y

        area += x1 * y2 - x2 * y1
        
        # add the area covered by the polygon itself
        area += abs(x2 - x1)
        area += abs(y2 - y1)

    # why do I need the + 1 here?
    return area // 2 + 1


p = Point(0, 0)
ps = [p]
for d, l in xs:
    dx, dy = ds[d]

    p = Point(p.x + dx * l, p.y + dy * l)

    ps.append(p)

print(shoelace(ps))
