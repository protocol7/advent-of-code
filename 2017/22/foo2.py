import sys

def parse(line):
    return line.strip()

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
def turn(d, right):
    x = dirs.index(d)
    if right:
        x += 1
    else:
        x -= 1
    x %= len(dirs)
    return dirs[x]

def tick(m, x, y, d):
    node = m.get((x, y), ".")
    if node == "#":
        d = turn(d, True)
    elif node == ".":
        d = turn(d, False)
    elif node == "F":
        d = (-d[0], -d[1])

    infection = 0
    if node == "#":
        m[(x, y)] = "F"
    elif node == "F":
        m[(x, y)] = "."
    elif node == ".":
        m[(x, y)] = "W"
    elif node == "W":
        m[(x, y)] = "#"
        infection = 1

    dx, dy = d
    return (x+dx, y+dy, d, infection)

parsed = list(map(parse, sys.stdin))

m = {}
for y, row in enumerate(parsed):
    for x, c in enumerate(row):
        m[(x, y)] = c

x = len(parsed[0]) / 2
y = len(parsed) / 2

d = dirs[0]

infections = 0
for burst in range(10000000):
    x, y, d, inf = tick(m, x, y, d)
    infections += inf

print(infections)
