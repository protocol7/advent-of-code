import sys
import re

def parse(line):
    x1, y1, x2, y2 = [int(x) for x in re.findall("\d+", line)]
    if line.startswith("toggle"):
        cmd = "toggle"
    elif line.startswith("turn off"):
        cmd = "off"
    elif line.startswith("turn on"):
        cmd = "on"
    return cmd, x1, y1, x2, y2


parsed = map(parse, sys.stdin)

grid = [[0 for x in range(1000)] for y in range(1000)]

for cmd, x1, y1, x2, y2 in parsed:
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if cmd == "on":
                grid[y][x] += 1
            elif cmd == "off":
                grid[y][x] = max(0, grid[y][x] - 1)
            elif cmd == "toggle":
                grid[y][x] += 2

c = 0
for row in grid:
    for x in row:
        c += x
print(c)

