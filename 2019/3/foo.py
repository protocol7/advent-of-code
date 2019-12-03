import sys

dirs = dict(zip("RDUL", [(1, 0), (0, -1), (0, 1), (-1, 0)]))

def trace(w):
    w = w.strip().split(",")

    p = set()
    x, y = 0, 0
    for r in w:
        dx, dy = dirs[r[0]]
        dist = int(r[1:])

        for i in range(dist):
            x += dx
            y += dy

            p.add((x, y))
    return p

def man(p):
    x, y = p
    return abs(x) + abs(y)

inp = list(sys.stdin)
w1 = trace(inp[0])
w2 = trace(inp[1])

dists = map(man, w1.intersection(w2))
print(min(dists))
