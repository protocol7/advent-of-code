import sys

sys.setrecursionlimit(10000)

class Node():
    def __init__(self, parent):
        self.parent = parent
        self.c = {}

def rev(d):
    if d == "N":
        return "S"
    elif d == "S":
        return "N"
    elif d == "E":
        return "W"
    elif d == "W":
        return "E"

def w(rr, start):
    node = start
    while rr:
        c = rr.pop(0)
        if c == "(":
            w(rr, node)
        elif c ==")":
            return
        elif c == "|":
            node = start
        else:
            if node.c.get(c):
                node = node.c[c]
            elif node.parent and node.parent.c.get(rev(c)) == node:
                node = node.parent
            else:
                n = Node(node)
                node.c[c] = n
                node = n

def pp(node):
    size = 1000
    grid = []
    for y in range(size):
        grid.append([" " for x in range(size)])
    p(node, grid, size//2, size//2)

    # find bound
    minx, miny, maxx, maxy = sys.maxint, sys.maxint, 0, 0
    for y, row in enumerate(grid):
        mi, ma = sys.maxint, 0
        for x, c in enumerate(row):
            if c != " ":
                mi = min(mi, x)
                ma = max(ma, x)
        minx = min(minx, mi)
        maxx = max(maxx, ma)
        if ma != 0:
            miny = min(miny, y)
            maxy = max(maxy, y)

    for y in range(miny-1, maxy+2):
        row = ""
        for x in range(minx-1, maxx+2):
            if x == size//2 and y == size//2:
                row += "X"
            else:
                c = grid[y][x]
                if c == " ":
                    row += "#"
                else:
                    row += c
        print(row)

def p(node, g, x, y):
    g[y][x] = "."
    for d in ["E", "W", "N", "S"]:
        if node.c.get(d):
            if d == "N":
                g[y-1][x] = "-"
                p(node.c[d], g, x, y-2)
            elif d == "S":
                g[y+1][x] = "-"
                p(node.c[d], g, x, y+2)
            elif d == "E":
                g[y][x+1] = "|"
                p(node.c[d], g, x+2, y)
            elif d == "W":
                g[y][x-1] = "|"
                p(node.c[d], g, x-2, y)

def l(node, doors, max_doors, rooms):
    max_doors = max(max_doors, doors)
    for child in node.c.itervalues():
        md, rooms = l(child, doors + 1, max_doors, rooms)
        max_doors = max(max_doors, md)

    if doors >= 1000:
        rooms += 1
    return max_doors, rooms

inp = sys.stdin.read().strip().strip("^").strip("$")

root = Node(None)

w(list(inp), root)

pp(root)

max_doors, rooms = l(root, 0, 0, 0)
print(max_doors, rooms)
