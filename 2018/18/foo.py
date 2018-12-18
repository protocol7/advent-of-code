import sys

def adjecent(m, x, y):
    h = len(m)
    w = len(m[0])

    a = []
    for xx in range(-1, 2):
        for yy in range(-1, 2):
            sx = x+xx
            sy = y+yy
            if xx == 0 and yy == 0:
                pass
            elif sx <0 or sy <0 or sx >= w or sy >= h:
                pass
            else:
                a.append((x+xx, y+yy))
    return a

def count(m, a, target):
    return len(filter(lambda (ax, ay): m[ay][ax] == target, a))

def val(m):
    mm = "".join(m)
    yards = mm.count("#")
    threes = mm.count("|")
    return yards * threes

m = [l.strip() for l in sys.stdin]

for tick in range(10):
    nm = []
    for y, row in enumerate(m):
        nr = []
        for x, c in enumerate(row):
            a = adjecent(m, x, y)
            cur = m[y][x]
            if cur == ".":
                if count(m, a, "|") >= 3:
                    nr.append("|")
                else:
                    nr.append(".")
            elif cur == "|":
                if count(m, a, "#") >= 3:
                    nr.append("#")
                else:
                    nr.append("|")
            elif cur == "#":
                if count(m, a, "#") >= 1 and count(m, a, "|") >= 1:
                    nr.append("#")
                else:
                    nr.append(".")
        nm.append("".join(nr))
    m = nm

print(val(m))
