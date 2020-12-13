import sys
from util import *

def parse(line):
    return line[0], int(line[1:])

xs = list(map(parse, sys.stdin))

x, y = 0, 0
dx, dy = 1, 0

for a, b in xs:
    if a == "W":
        x -= b
    elif a == "E":
        x += b
    elif a == "N":
        y -= b
    elif a == "S":
        y += b
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