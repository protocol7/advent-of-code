import sys
from collections import *
import itertools
from itertools import *
from util import *

def parse(s):
    s = list(s.split("\n"))

    out = []

    for x in s[1:]:
        out.append(tuple(ints(x)))

    return tuple(out)


def build_transformation_matrix(scanner_a, scanner_b):
    
    # what absolute distances between beacons are the same for the two scanner (rotated by all combinations of x, y z dimensions)
    intersection = set(scanner_a.keys()).intersection(set(scanner_b.keys()))

    # each absolute distance map to a pair of beacons for each scanner (a, b), here we reduce this to a unique match for each beacon in a to a beacon in b

    # beacon from a -> candidates of beacons from b for which this might match
    u = {}


    for i in intersection:
        a_pair = scanner_a[i]
        b_pair = set(scanner_b[i])

        for a_beacon in a_pair:
            if not a_beacon in u:
                # a can map to each ot the two in b
                u[a_beacon] = b_pair
            else:
                # a can only map to the intersection of known candidates, and the beacons in this b pair
                u[a_beacon] = u[a_beacon].intersection(b_pair)

    # u will now be dict of pairs of a -> b

    # we only count those with 12 or more matching beacons
    if len(u) < 12:
        return None

    # check that we arrived at unique pairs
    for v in u.values():
        assert len(v) == 1

    # u contains pairs of beacons that are the same, but in different coordinate systems
    u = {k: list(v)[0] for k, v in u.items()}

    # calculate transformation matrix

    # translate in all possible directions (rotated and flipped)
    p = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1)]
    TRANS = list(itertools.product(p, p))

    # find a rotation and flip that gives the same translation for all 12 pairs of beacons
    m = defaultdict(set)

    for k, v in u.items():
        for (a, da), (b, db) in TRANS:
            delta = v[a] * da - k[b] * db

            m[(a, da, b, db)].add(delta)

    # pick the transformations that led to a unique solution
    m = {k:list(v)[0] for k, v in m.items() if len(v) == 1}  # TODO do I want k[1] == 1?

    # trans is a transformation matrix from one beacon to another
    return m


# transform beacon b using transformation matrix m
def transform(b, m):
    for k, v in m.items():
        sa, da, sb, db = k

        # only transform in one direction
        if db == 1:
            translated = (b[sa] - v*da) * da

            if sb == 0:
                x = translated
            elif sb == 1:
                y = translated
            elif sb == 2:
                z = translated

    return x, y, z

xs = sys.stdin.read().strip().split("\n\n")

# scanners with their beacons
xs = [parse(s) for s in xs]

# produce abs distances for all permutations for each scanner
ds = []
for x in xs:
    # for each scanner

    # absolute distances -> pair of the original beacons
    d = {}

    # for each combination of beacons for this scanner
    for a, b in combinations(x, 2):
        # absolute distances between the beacons
        # absolute to remove having to care about the axis directions
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        dz = abs(a[2] - b[2])

        # add in all possible permutations of x, y z
        for x, y, z in permutations([dx, dy, dz], 3):
            d[(x, y, z)] = tuple([a, b])

    ds.append(d)

g = defaultdict(set)
matrices = {}

# for all pairs of scanners, see if we can generate a transformation matrix for b -> a
for a, b in permutations(range(len(xs)), 2):
    m = build_transformation_matrix(ds[a], ds[b])

    if m:
        # there a transformation b -> a
        g[b].add(a)

        matrices[(b, a)] = m

# scanner 0 is the reference frame, add all it's beacons
all_beacons = set(xs[0])

# skip scanner 0
for scanner in range(1, len(xs)):
    # find a path to scanner 0
    p = bfs(g, scanner, lambda x: x == 0)

    # start with the scanner and transform step by step until we're in scanner 0's reference frame
    beacons = xs[scanner]

    for a, b in zip(p, p[1:]):

        m = matrices[(a, b)]

        # transform all beacons
        beacons = [transform(b, m) for b in beacons]

    # we're now in scanner 0's reference frame, add beacons
    all_beacons.update(beacons)

# part 1, how many unique beacons are there?
print(len(all_beacons))


# scanner 0 is the reference frame
scanners = [[0, 0, 0]]

# transform each scanner
for scanner in range(1, len(xs)):
    p = bfs(g, scanner, lambda x: x == 0)

    # start at the reference frame and tramsform backwards per this scanner
    x = [0, 0, 0]

    for a, b in zip(p, p[1:]):
        m = matrices[(a, b)]
        x = transform(x, m)

    scanners.append(x)

# part 2, what's the max manhattan distance between scanner?
print(max(abs(bx-ax) + abs(by-ay) + abs(bz-az) for (ax, ay, az), (bx, by, bz) in combinations(scanners, 2)))