import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

d = set()
for y, row in enumerate(xs):
    for x, c in enumerate(row):
        if c == "#":
            d.add((x, y))

dirs = [(N, NW, NE), (S, SE, SW), (W, NW, SW), (E, NE, SE)]

gg = Grid(d)

for r in count():

    nps = {}
    cc = Counter()
    for p in gg:
        def occupied(g, p, neighbours):
            for _, nv in g.neighbours(p, neighbours):
                if nv:
                    return True

            return False

        # During the first half of each round, each Elf considers the eight positions adjacent to themself. 
        # If no other Elves are in one of those eight positions, the Elf does not do anything during this round. 
        if not occupied(gg, p, ADJACENT):
            nps[p] = p
            cc[p] += 1
            continue

        # Otherwise, the Elf looks in each of four directions in the following order and proposes moving one 
        # step in the first valid direction:

        # If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
        # If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
        # If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
        # If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.
        moved = False
        for dir in dirs:
            if not occupied(gg, p, dir):
                np = p + dir[0]

                nps[p] = np
                cc[np] += 1
                moved = True
                break
        
        if not moved:
            nps[p] = p
            cc[p] += 1

    # After each Elf has had a chance to propose a move, the second half of the round can begin. 
    # Simultaneously, each Elf moves to their proposed destination tile if they were the only Elf 
    # to propose moving to that position. If two or more Elves propose moving to the same position, none of those Elves move.
    nd = set()
    for p in gg:
        np = nps[p]
        if cc[np] == 1:
            nd.add(np)
        else:
            nd.add(p)

    nd = Grid(nd)

    # Finally, at the end of the round, the first direction the Elves considered is moved to the end of the list of directions. 
    # For example, during the second round, the Elves would try proposing a move to the south first, then west, then east, then north. 
    # On the third round, the Elves would first consider west, then east, then north, then south.
    dirs = dirs[1:] + dirs[0:1]

    if gg.d.keys() == nd.d.keys():
        print(r+1)
        break

    gg = nd

    if r == 9:
        minx, miny = gg.min()
        maxx, maxy = gg.max()

        c = 0
        for x in range(minx, maxx+1):
            for y in range(miny, maxy+1):
                if (x, y) not in gg:
                    c += 1

        print(c)
