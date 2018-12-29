import sys

def parse(line):
    return line.strip()

dirs = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0)
        }

pad = {
        (2, 0): 1,
        (1, 1): 2,
        (2, 1): 3,
        (3, 1): 4,
        (0, 2): 5,
        (1, 2): 6,
        (2, 2): 7,
        (3, 2): 8,
        (4, 2): 9,
        (1, 3): "A",
        (2, 3): "B",
        (3, 3): "C",
        (2, 4): "D",
        }

parsed = map(parse, sys.stdin)
x, y = 0, 2

code = ""
for ins in parsed:
    for c in ins:
        dx, dy = dirs[c]
        nx = x + dx
        ny = y + dy
        if (nx, ny) in pad:
            x = nx
            y = ny
    code += str((pad[(x, y)]))

print(code)
