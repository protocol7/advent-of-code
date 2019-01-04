import sys
from heapq import heappush, heappop

def p(size):
    return int(size.strip("T"))

def parse(line):
    l = line.split()
    n = l[0]
    n = n.split("-")
    x = int(n[1].strip("x"))
    y = int(n[2].strip("y"))
    u = p(l[2])
    a = p(l[3])
    return x, y, u, a

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def n(m, x, y, disk1):
    out = []
    for dx, dy in dirs:
        xx = x + dx
        yy = y + dy
        if xx < 0 or yy < 0:
            continue
        if xx >= len(m[0]) or yy >= len(m):
            continue

        disk2 = m[yy][xx]
        if disk1[0] > 0 and disk2[1] >= disk1[0]:
            out.append((xx, yy, disk2))
    return out

def c(m):
    return [row[:] for row in m]

seen = set()
def move(m, step):
    for y, row in enumerate(m):
        for x, d in enumerate(row):
            for nx, ny, nd in n(m, x, y, d):
                nm = c(m)
                # moved from, now empty
                nm[y][x] = (0, d[0] + d[1], False)
                # moved to
                nm[ny][nx] = (nd[0] + d[0], nd[1] - d[0], d[2] or nd[2])

                ss = str(nm)
                if ss in seen:
                    continue
                seen.add(ss)

                heappush(queue, (step + 1, nm))

def pp(m):
    for row in m:
        out = ""
        for u, a, t in row:
            if t:
                out += "G"
            elif u == 0:
                out += "_"
            elif u > 100:
                out += "#"
            else:
                out += "."
        print(out)

print("This is too slow for the real input")

disks = map(parse, list(sys.stdin)[2:])

m = []
for y in range(disks[-1][1] + 1):
    row = []
    for x in range(disks[-1][0] + 1):
        row.append(None)
    m.append(row)

for x, y, u, a in disks:
    target = x == len(m[0]) - 1 and y == 0
    m[y][x] = (u, a, target)


queue = [(0, m)]

pp(m)

while queue:
    step, mm = heappop(queue)

    if mm[0][0][2]:
        # done!
        print("done", step)
        break

    move(mm, step)
