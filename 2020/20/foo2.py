import sys
from util import *

xs = sys.stdin.read().split("\n\n")

trans = dict()
for x in xs:
    x = x.split()
    a = int(x[1][:-1])
    b = x[2:]

    trans[a] = transpositions(b)

def coll(x, col):
    return "".join([y[col] for y in x])

# finds candidates for top left corner, top edges and left edges
def find_corner_and_edges():
    corner = None
    top_edges = []
    left_edges = []
    for k, v in trans.items():
        # look for tiles that have no match in the top or left side
        for t in v:
            top = False
            left = False

            for kk, vv in trans.items():
                if k == kk:
                    continue

                for tt in vv:
                    if t[0] == tt[0]:
                        top = True
                        break
                    elif coll(t, 0) == tt[0]:
                        left = True
                        break

            tile = k, t
            if not top and not left:
                corner = tile
            elif not top:
                top_edges.append(tile)
            elif not left:
                left_edges.append(tile)

    return corner, top_edges, left_edges

# find a top left corner and top/left edges tiles
corner, top_edges, left_edges = find_corner_and_edges()

# build the first row
def build_first_row(corner, used):
    cid, c = corner
    used.add(cid)

    row = [c]

    # add top edges until we can't find any more. makes no assumption on the size of the picture
    while True:
        found = False
        cur = row[-1]

        for i, e in top_edges:
            if coll(cur, -1) == coll(e, 0) and i not in used:
                row.append(e)
                used.add(i)
                found = True
                break

        if not found:
            break
    return row

# set of used ids to make sure we don't use a tile twice
used = set()
first_row = build_first_row(corner, used)

# build remaining rows, using the first row as a seed
def build_picture(first_row, used):
    pict = [first_row]
    while True:  # for each row
        prev = pict[-1]
        row = []

        # find left most tile from left edges
        for i, t in left_edges:
            if t[0] == prev[0][-1] and i not in used:
                row.append(t)
                used.add(i)
                break

        # are we out of matching edge tiles?
        if not row:
            break

        # build the rest of the row
        for col in range(1, len(prev)):
            # now we have two edges to compared to, so we can look among all tiles
            for k, v in trans.items():
                for t in v:
                    if t[0] == prev[col][-1] and coll(t, 0) == coll(row[-1], -1) and k not in used:
                        row.append(t)
                        used.add(k)

        pict.append(row)

    return pict

pict = build_picture(first_row, used)

# the picture is stiched together, remove edges from each tile
def trim_tile(t):
    return [row[1:-1] for row in t[1:-1]]

pict = [[trim_tile(t) for t in row] for row in pict]

# merge tiles per row
np = []
for row in pict:
    for li in range(len(row[0])):
        np.append("".join(x[li] for x in row))
pict = np

# we now have the entire picture, look for monsters
monster = ["                  # ",
           "#    ##    ##    ###",
           " #  #  #  #  #  #   "]

def count_hashes(xs):
    return sum(x.count("#") for x in xs)

# compare rows with monsters
def find(rows):
    for row, mon in zip(rows, monster):
        for c, m in zip(row, mon):
            if m == "#" and c != "#":
                return False
    return True

ml = len(monster[0])
monsters = 0
for t in transpositions(pict):
    # look three rows at a time
    for rows in zip(t, t[1:], t[2:]):
        for ir in range(len(rows[0]) - ml):
            nr = [row[ir:ir+20] for row in rows]

            if find(nr):
                monsters += 1

print(count_hashes(pict) - monsters * count_hashes(monster))