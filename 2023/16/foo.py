import sys
from collections import deque
from util import Grid, Point, UP, DOWN, LEFT, RIGHT

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

def foo(s):
    ps = deque([s])

    seen = set()

    while ps:
        p, d = ps.pop()

        c = g[p]
        if c is None:
            continue

        k = (p, d)
        if k in seen:
            continue
        seen.add(k)

        if c == ".":
            ps.appendleft((p + d, d))
        elif c == "-":
            if d in (RIGHT, LEFT):
                ps.appendleft((p + d, d))
            else:
                # split
                ps.appendleft((p + RIGHT, RIGHT))
                ps.appendleft((p + LEFT, LEFT))
        elif c == "|":
            if d in (UP, DOWN):
                ps.appendleft((p + d, d))
            else:
                # split
                ps.appendleft((p + UP, UP))
                ps.appendleft((p + DOWN, DOWN))
        elif c == "\\":
            nd = (d[1], d[0])
            ps.appendleft((p + nd, nd))
        elif c == "/":
            nd = (-d[1], -d[0])
            ps.appendleft((p + nd, nd))

    return len(set(p for p, _ in seen))

# part 1
print(foo((Point(0, 0), RIGHT)))

# part 2
w = len(xs[0])
h = len(xs)

print(max(map(foo, 
    [(Point(0, y), RIGHT) for y in range(h)] + 
    [(Point(w - 1, y), LEFT) for y in range(h)] +
    [(Point(x, 0), DOWN) for x in range(w)] +
    [(Point(x, h - 1), UP) for x in range(w)]
)))
