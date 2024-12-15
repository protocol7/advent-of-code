#!/usr/bin/env python3

import sys
from util import Grid, LEFT, RIGHT, UP, DOWN

def parse(line):
    return line.strip()

a, b = sys.stdin.read().strip().split("\n\n")

# expand
a = a.split("\n")

na = []
for line in a:
    nline = ""
    for c in line:
        if c == "#":
            nline += "##"
        elif c == "O":
            nline += "[]"
        elif c == ".":
            nline += ".."
        elif c == "@":
            nline += "@."
        else:
            nline += c
    na.append(nline)

g = Grid(na)

moves = b.replace("\n", "")

start = g.points_by_value()["@"][0]
g.d[start] = "."

dirs = {
    "<": LEFT,
    "^": UP,
    ">": RIGHT,
    "v": DOWN,
}

def box(g, p):
    v = g[p]
    if v == "[":
        return (p, "["), (p+RIGHT, "]")
    else:
        return (p+LEFT, "["), (p, "]")

def try_move(g, p, dir):
    np = p + dir
    bs = list(box(g, np))

    gg = Grid(dict(g.d))
    while True:
        for b, _ in bs:
            gg.d[b] = "."

        # try to move, these would be the new positions and values
        nbs = [(b + dir, x) for b, x in bs]

        if any(gg[b] == "#" for b, _ in nbs):
            # something in the way, give up
            return []
        elif all(gg[b] == "." for b, _ in nbs):
            # all free, move
            out = {}
            # reset old positions
            for b, _ in bs:
                out[b] = "."
            # and move
            for b, v in nbs:
                out[b] = v

            return list(out.items())
        else:
            # there must be some boxes in the way, add those boxes and try again
            new_boxes = set()
            for b, _ in nbs:
                if gg[b] in "[]":
                    new_boxes.update(box(g, b))

            bs.extend(new_boxes)

p = start
for d in moves:
    dir = dirs[d]

    np = p + dir
    nv = g[np]

    if nv == "#":
        continue
    elif nv == ".":
        p = np
    elif nv in "[]":
        r = try_move(g, p, dir)

        if r:
            for rp, rv in r:
                g.d[rp] = rv
            p = np

t = 0
for b in g.points_by_value()["["]:
    x, y = b
    t += y * 100 + x

print(t)
