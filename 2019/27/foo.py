import sys
from copy import deepcopy

# On a English peg solitaire, your input, what's the maximum number of pegs you
# can heve left after playing?
#
#   ooo  
#   ooo  
# ooooooo
# ooo-ooo
# ooooooo
#   ooo  
#   ooo  

def parse(line):
    return list(line.strip("\n"))

m = tuple(map(parse, sys.stdin))

def pp(m):
    for line in m:
        print("".join(line))
    print("")

w = len(m[0])
h = len(m)

adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def moves(m):
    ms = []
    for y, line in enumerate(m):
        for x, c in enumerate(line):
            if c == ".":
                for ax, ay in adjacent:
                    x1 = x + ax
                    y1 = y + ay
                    x2 = x + 2*ax
                    y2 = y + 2*ay
                    if x2 < 0 or y2 < 0 or x2 >= w or y2 >= h:
                        continue

                    c1 = m[y1][x1]
                    c2 = m[y2][x2]

                    if c1 == "o" and c2 == "o":
                        ms.append((x2, y2, x1, y1, x, y))
    return ms

def trans(m):
    ms = [tuple(m)]

    # 90
    mm = []
    for x in range(w-1, -1, -1):
        line = []
        for y in range(h):
            line.append(m[y][x])
        mm.append(line)
    ms.append(tuple(mm))

    # 180
    mm = []
    for y in range(h-1, -1, -1):
        line = m[y][::-1]
        mm.append(line)
    ms.append(tuple(mm))

    # 270
    mm = []
    for x in range(w):
        line = []
        for y in range(h-1, -1, -1):
            line.append(m[y][x])
        mm.append(line)
    ms.append(tuple(mm))

    return ms

def deeptuple(m):
    return tuple([tuple(l) for l in m])

def pegs(m):
    p = 0
    for line in m:
        p += line.count("o")
    return p

def run(m):
    q = [[m]]
    seen = set()
    while q:
        ms = q.pop(0)
        m = ms[-1]
        movs = moves(m)
        if not movs:
            return ms
            break

        for mov in moves(m):
            x2, y2, x1, y1, x, y = mov
            mm = deepcopy(m)

            mm[y2][x2] = "."
            mm[y1][x1] = "."
            mm[y][x] = "o"

            new = True
            for t in trans(mm):
                t = deeptuple(t)
                if t in seen:
                    new = False
                    break
            if new:
                q.append(ms + [mm])
            seen.add(deeptuple(mm))

ms = run(m)
for mm in ms:

    pp(mm)

print(pegs(ms[-1]))
