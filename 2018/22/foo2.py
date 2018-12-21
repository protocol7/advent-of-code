import sys
from collections import defaultdict
from heapq import heappush, heappop

depth = int(sys.argv[1])
tx, ty = int(sys.argv[2]), int(sys.argv[3])
types = ".=|"

maxx = tx + 900
maxy = ty + 20

m = {}
el = {}
for y in range(maxy):
    for x in range(maxx):
        if x == tx and y == ty:
            geo = 0
        elif x == 0 and y == 0:
            geo = 0
        elif x == 0:
            geo = y * 48271
        elif y == 0:
            geo = x * 16807
        else:
            geo = el[(x-1, y)] * el[(x, y-1)]

        ero = (geo + depth) % 20183
        el[(x, y)] = ero
        m[(x, y)] = types[ero % 3]

costs = defaultdict(lambda: sys.maxint)
h = [(0, 0, 0, "t")]

allowed = {
        ".": ("t", "c"),
        "=": ("n", "c"),
        "|": ("t", "n")
        }

while h:
    c, x, y, tool = heappop(h)

    if costs[(x, y, tool)] <= c:
        # more expensive, no need to continue
        continue

    costs[(x, y, tool)] = c
    if x == tx and y == ty and tool == "t":
        # done
        print(c)
        break

    # try moving
    for sx, sy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        xx = x + sx
        yy = y + sy
        if xx >= 0 and yy >= 0 and tool in allowed[m[(xx, yy)]]:
            heappush(h, (c + 1, xx, yy, tool))

    # try switching tool
    for new_tool in allowed[m[(x, y)]]:
        if new_tool != tool:
            heappush(h, (c + 7, x, y, new_tool))
