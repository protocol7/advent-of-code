import sys
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))


dir = {
    ">": RIGHT,
    "<": LEFT,
    "^": UP,
    "v": DOWN,
}

ps = set()
winds = list()

g = Grid(xs)
for p, v in g.points():
    if v == "." or v in dir:
        ps.add(p)
    if v in dir:
        winds.append((v, p))

w = len(xs[0])
h = len(xs)

for x, v in enumerate(xs[0]):
    if v == ".":
        start = Point(x, 0)

for x, v in enumerate(xs[h-1]):
    if v == ".":
        end = Point(x, h-1)

def move_winds(winds):
    nw = []
    for wind in winds:
        d, p = wind

        np = p + dir[d]

        if np not in ps:
            if d == ">":
                np = (1, p.y)
            elif d == "<":
                np = (w-2, p.y)
            elif d == "^":
                np = (p.x, h-2)
            elif d == "v":
                np = (p.x, 1)

        nw.append((d, Point(np)))

    return nw

turn = 0
for s, g in ((start, end), (end, start), (start, end)):
    pp = {s}

    while True:
        ws = set(w for _, w in winds)

        npp = set()
        for p in pp:
            if p not in ws:
                npp.add(p)

            for d in ORTHOGONAL:
                np = p + d
                if np not in ws and np in ps:
                    npp.add(np)

        pp = npp

        if g in pp:
            break

        turn += 1
        winds = move_winds(winds)

    print(turn)
