import sys

def parse(line):
    return line.strip()

def val(m, x, y):
    v = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            xx = x + dx
            yy = y + dy
            if dx == 0 and dy == 0:
                continue
            elif xx < 0 or yy < 0:
                continue
            elif yy == len(m) or xx == len(m[0]):
                continue
            elif m[yy][xx] == "#":
                v += 1
    return v

def t(m):
    res = []
    for y, row in enumerate(m):
        r = ""
        for x, c in enumerate(row):
            v = val(m, x, y)
            if c == "#":
                if v == 2 or v == 3:
                    r += "#"
                else:
                    r += "."
            elif c == ".":
                if v == 3:
                    r += "#"
                else:
                    r += "."
            else:
                assert False
        res.append(r)
    return res

m = map(parse, sys.stdin)
rounds = int(sys.argv[1])

for _ in range(rounds):
    m = t(m)

count = 0
for row in m:
    for c in row:
        if c == "#":
            count += 1
print(count)
