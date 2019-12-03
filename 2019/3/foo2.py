import sys

dirs = dict(zip("RDUL", [(1, 0), (0, -1), (0, 1), (-1, 0)]))

def trace(w):
    w = w.strip().split(",")

    p = []
    x, y = 0, 0
    for r in w:
        dx, dy = dirs[r[0]]
        dist = int(r[1:])

        for i in range(dist):
            x += dx
            y += dy

            p.append((x, y))
    return p

def wire_dist(w1, w2, p):
    return w1.index(p) + w2.index(p) + 2

inp = list(sys.stdin)
w1 = trace(inp[0])
w2 = trace(inp[1])

crosses = set(w1).intersection(w2)
dists = map(lambda p: wire_dist(w1, w2, p), crosses)
print(min(dists))
