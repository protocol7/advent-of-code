import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

cs = dict()
for y, row in enumerate(xs):
    for x, v in enumerate(row):
        cs[(x, y, 0, 0)] = (v == "#")

def coord(cs, x, y, z, w):
    return cs.get((x, y, z, w))

def around(cs, x, y, z, w):
    c = 0
    for dw in [-1, 0, 1]:
        for dz in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                        continue

                    if coord(cs, x+dx, y+dy, z+dz, w+dw):
                        c += 1

    return c

sx = len(xs[0]) + 1
sy = len(xs) + 1
sz = 2
sw = 2

for cyc in range(6):
    nd = dict()
    for w in range(-sw, sw):
        for z in range(-sz, sz):
            for y in range(-sy, sy):
                for x in range(-sx, sx):
                    cur = coord(cs, x, y, z, w)
                    aa = around(cs, x, y, z, w)

                    nv = False
                    if cur and (aa == 2 or aa == 3):
                        nv = True
                    elif not cur and aa == 3:
                        nv = True

                    nd[(x, y, z, w)] = nv
    cs = nd

    sw += 1
    sz += 1
    sy += 1
    sx += 1

print(sum(cs.values()))