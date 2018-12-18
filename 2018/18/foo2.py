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
                a.append((sx, sy))
    return a

def count(m, a, target):
    return len(filter(lambda (ax, ay): m[ay][ax] == target, a))

m = [l.strip() for l in sys.stdin]

for tick in range(500):
    nm = []
    yards = 0
    threes = 0
    for y, row in enumerate(m):
        nr = []
        for x, c in enumerate(row):
            a = adjecent(m, x, y)
            if c == ".":
                if count(m, a, "|") >= 3:
                    nr.append("|")
                    threes += 1
                else:
                    nr.append(".")
            elif c == "|":
                if count(m, a, "#") >= 3:
                    nr.append("#")
                    yards += 1
                else:
                    nr.append("|")
                    threes += 1
            elif c == "#":
                if count(m, a, "#") >= 1 and count(m, a, "|") >= 1:
                    nr.append("#")
                    yards += 1
                else:
                    nr.append(".")
        nm.append("".join(nr))
    m = nm
    print("%s\t%s" % (tick+1, yards * threes))

# https://docs.google.com/spreadsheets/d/1QdiNDy6kkdnNmK4Q4qzP70aXHT-HNweKN_z7gH7g0bo/edit
