import sys
from intcode import *

prog = parse(sys.stdin)
ic = Intcode(prog, [])

m = dict()
s = ""
x, y = 0, 0

# get maze by running the program which outputs #, ., newlines and the robot
# direction in ascii
while True:
    o = ic.run()

    if o is None:
        break
    elif o == 10:
        y += 1
        x = 0
        print(s)
        s = ""
    else:
        m[(x, y)] = chr(o)
        x += 1
        s += chr(o)

# find intersections by simply checking each cell, and if it's a # (path) check
# if it has paths in it's orthogonal directions
def inters(m):
    adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    inter = []
    for y in range(60):
        for x in range(60):
            c = m.get((x, y), ".")
            if c == "#":
                adj = True
                for ax, ay in adjacent:
                    a = m.get((x + ax, y + ay), ".")
                    if a != "#":
                        adj = False
                        break

                if adj:
                    inter.append((x, y))
    return inter

# sum up the product of all intersections
def ap(inter):
    a = 0
    for x, y in inter:
        a += x * y
    return a

print(ap(inters(m)))
