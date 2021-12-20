import sys

a, b = sys.stdin.read().strip().split("\n\n")

a = [x == "#" for x in a]

d = {}
for y, row in enumerate(b.split()):
    for x, c in enumerate(row):
        d[(x, y)] = c == "#"

def run(d, runs):
    d = dict(d)

    for r in range(runs):
        sx, sy = min(d.keys())
        ex, ey = max(d.keys())

        nd = {}        
        for x in range(sx-1, ex+2):
            for y in range(sy-1, ey+2):
                s = ""
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        # default depends on row, will not work with sample
                        s += str(int(d.get((x + dx, y + dy), r % 2 != 0)))

                nd[(x, y)] = a[int(s, 2)]

        d = nd

    return d

print(sum(run(d, 2).values()))
print(sum(run(d, 50).values()))