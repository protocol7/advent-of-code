import sys
from itertools import cycle, count
from util import *

xs = sys.stdin.read().strip()

rocks = [
    ["####"],

    [".#.",
     "###",
     ".#.",],

    ["..#",
     "..#",
     "###",],

    ["#",
     "#",
     "#",
     "#",],

    ["##",
     "##",]
]

# make the rock shapes into sets of points
d_rocks = []
for rock in rocks:
    h = len(rock)
    d = set()
    for y, row in enumerate(rock):
        for x, c in enumerate(row):
            if c == "#":
                # we're count y as increasing up, so need to invert the shape here
                d.add((x, h-y-1))

    d_rocks.append(d)

def size(rock):
    w, h = max_each(rock)

    return w + 1, h + 1

d = set()

maxy = -1 # floor is -1

jets = cycle(enumerate(xs))
rocks = cycle(enumerate(d_rocks))

seen = {}
for r in count(1):
    rocki, rock = next(rocks)

    w, h = size(rock)

    # can we move the rock to position x, y?
    def free(d, rock, x, y):
        for rx, ry in rock:
            xx = x + rx
            yy = y + ry

            if (xx, yy) in d:
                return False

        return True

    y = maxy + 4
    x = 2

    while True:
        jeti, jet  = next(jets)

        # move with the jet
        if jet == "<":
            if x > 0 and free(d, rock, x-1, y):
                x -= 1
        elif jet == ">":
            if x + w < 7 and free(d, rock, x+1, y):
                x += 1

        if y > 0 and free(d, rock, x, y-1):
            # move down
            y -= 1
        else:
            # rest

            # add the new rock to the occupied points, and bump the maxy (if needed)
            for rx, ry in rock:
                xx = x + rx
                yy = y + ry

                d.add((xx, yy))
                maxy = max(maxy, yy)

            def pattern(d, maxy):
                # get the occupied points some number rows below maxy
                p = set()
                for y in range(50):
                    for x in range(7):
                        if (x, maxy - y) in d:
                            p.add((x, y))

                return frozenset(p)

            if r == 2022:
                # height is max y + 1
                print(maxy + 1)
            elif r > 2022:
                # check if we seen this pattern before
                p = pattern(d, maxy)

                # state is where we are in the cycles of jets and rocks, and the points occupied in some rows below maxy
                k = (jeti, rocki, p)

                if k in seen:
                    last_r, last_maxy = seen[k]

                    delta_r = r - last_r

                    # how many repeats do we need to skip to get to the target rounds, given the size of the pattern?
                    skip_repeats = (1000000000000 - r) // delta_r

                    # what would the new round be?
                    nr = r + skip_repeats * delta_r

                    # try until we hit the target round
                    if nr == 1000000000000:
                        # what height does skipping gain us?
                        delta_maxy = maxy - last_maxy
                        nmaxy = maxy + skip_repeats * delta_maxy

                        print(nmaxy + 1)
                        sys.exit()

                seen[k] = (r, maxy)

            break