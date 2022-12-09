import sys

def parse(line):
    return list(map(int, line.strip()))

xs = list(map(parse, sys.stdin))

w = len(xs[0])
h = len(xs)

ss = []
for y, row in enumerate(xs):
    for x, c in enumerate(row):
        # right
        r = 0
        for xx in range(x+1, w):
            cc = xs[y][xx]

            r += 1
            if cc >= c:
                break

        # left
        l = 0
        for xx in range(x-1, -1, -1):
            cc = xs[y][xx]

            l += 1
            if cc >= c:
                break

        # down
        d = 0
        for yy in range(y+1, h):
            cc = xs[yy][x]

            d += 1
            if cc >= c:
                break

        # up
        u = 0
        for yy in range(y-1, -1, -1):
            cc = xs[yy][x]

            u += 1
            if cc >= c:
                break

        ss.append(r * l * d * u)

print(max(ss))