import sys
from heapq import heappush, heappop

def parse(line):
    return line.strip()

def locations(m):
    locs = {}
    mm = []
    for y, row in enumerate(m):
        out = ""
        for x, c in enumerate(row):
            if c.isdigit():
                locs[(x, y)] = int(c)
                out += "."
            else:
                out += c
        mm.append(out)
    return mm, locs

def bfs(m, x, y, node, locs):
    seen = set()

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def n(m, x, y):
        out = []
        for dx, dy in dirs:
            xx = x + dx
            yy = y + dy
            if xx < 0 or yy < 0:
                continue
            if xx >= len(m[0]) or yy >= len(m):
                continue
            if m[yy][xx] == ".":
                out.append((xx, yy))
        return out

    def move(m, x, y, step):
        ns = n(m, x, y)
        for xx, yy in ns:
            if (xx, yy) in seen:
                continue
            seen.add((xx, yy))

            heappush(queue, (step + 1, xx, yy))

    queue = [(0, x, y)]
    pairs = []
    while queue:
        step, xx, yy = heappop(queue)
        if (xx, yy) in locs:
            pairs.append((node, locs[xx, yy], step))
        move(m, xx, yy, step)
    return pairs

def e(node, rem, dist, ret):
    if not rem:
        if ret:
            return e(node, ret, dist, [])
        else:
            return dist
    shortest = sys.maxint
    for r in rem:
        if (node, r) in pairs:
            rr = set(rem)
            rr.discard(r)

            shortest = min(shortest, e(r, rr, dist + pairs[(node, r)], ret))
    return shortest

m, locs = locations(map(parse, sys.stdin))

pairs = []
for (x, y), n in locs.iteritems():
    ll = dict(locs)
    del ll[(x, y)]

    pairs.extend(bfs(m, x, y, n, ll))

pairs = {(n1, n2):d for n1, n2, d in pairs}

rem = set(locs.values())
rem.discard(0)

# part 1
print(e(0, rem, 0, []))

# part 2
print(e(0, rem, 0, [0]))
