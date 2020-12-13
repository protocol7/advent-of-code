import sys
from util import *

def parse(line):
    return line[0], int(line[1:])

xs = list(map(parse, sys.stdin))

x, y = 0, 0
dx, dy = 10, -1

for a, b in xs:
    if a == "W":
        dx -= b
    elif a == "E":
        dx += b
    elif a == "N":
        dy -= b
    elif a == "S":
        dy += b
    elif a == "F":
        x += b * dx
        y += b * dy
    elif a in "LR":
        if a == "R":
            b = abs(b-360)

        if b == 90:
            dx, dy = dy, -dx
        elif b == 180:
            dx, dy = -dx, -dy
        elif b == 270:
            dx, dy = -dy, dx

print(manhattan(x, y))