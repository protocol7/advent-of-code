import sys
from heapq import heappush, heappop
from collections import defaultdict
from util import *

g = sys.stdin.readlines()

# map, dict of (x, y) -> neighbours
M = defaultdict(list)

TYPES = "ABCD"

# positions of amphs
POS = {}
for x, y, c in iter_grid(g):
    def is_space(x):
        return x == "." or x in TYPES

    if is_space(c):
        for xx, yy in iter_orthogonal(x, y, g):
            cc = g[yy][xx]

            if is_space(cc):
                M[(x, y)].append((xx, yy))

    if c in TYPES:
        POS[(x, y)] = c

# set of positions in hallway
HALLWAY = set((x, y) for x, y in M if y == 1)

# set of positions in hallway where amphs can stop
STOPS = set((x, y) for x, y in HALLWAY if not (x, y+1) in M)

# dict of amph type -> final positions in order (going down)
ROOMS = defaultdict(list)
for c, x in zip(TYPES, (3, 5, 7, 9)):
    y = 2

    while (x, y) in M:
        ROOMS[c].append((x, y))
        y += 1

# we're done when we've reached this state
DONE = {x: k for k, v in ROOMS.items() for x in v}

COSTS = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}

# get position in room
# finds the deepest available position in a room for the amph, and check that there are no other amph types in the room
# return position, or None if the room is full or has amph of other type
def free_room_position(amph, current_positions):
    free = None
    for r in ROOMS[amph]:
        o = current_positions.get(r)

        if o is None:
            free = r
        elif amph != o:
            # other amph type in room, can't go here
            return None

    return free


# set of possible positions to go to and their costs
def valid_moves(amph, current_pos, current_positions):
    out = set()
    seen = set()

    q = [(current_pos, 0)]

    while q:
        p, c = q.pop()

        if p in seen:
            continue
        seen.add(p)

        if p in HALLWAY:
            if p in STOPS and current_pos not in HALLWAY:
                out.add((p, c))
        else:
            # in room, are we in the deepest free position, and are all other amphs of the same type?
            lowest = free_room_position(amph, current_positions)

            if lowest == p:
                # if a position in a final room is available, we can skip all other positions
                return [(p, c)]

        cc = c + COSTS[amph]
        for n in M[p]:
            # if the position free?
            if n not in current_positions:
                q.append((n, cc))

    return out


q = [(0, 0, POS)]
seen = set()

while q:
    total_cost, _, current_positions = heappop(q)

    cfp = frozenset(current_positions.items())
    if cfp in seen:
        continue
    seen.add(cfp)

    if current_positions == DONE:
        print(total_cost)
        break

    for current_pos, amph in current_positions.items():
        for pos, cost in valid_moves(amph, current_pos, current_positions):
            np = dict(current_positions)
            del np[current_pos]
            np[pos] = amph

            heappush(q, (total_cost + cost, id(np), np))
