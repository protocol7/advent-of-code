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
        (0, 0): 1,
        (1, 0): 2,
        (2, 0): 3,
        (0, 1): 4,
        (1, 1): 5,
        (2, 1): 6,
        (0, 2): 7,
        (1, 2): 8,
        (2, 2): 9,
        }

parsed = map(parse, sys.stdin)
x, y = 1, 1

code = ""
for ins in parsed:
    for c in ins:
        dx, dy = dirs[c]
        x += dx
        y += dy
        x = min(max(0, x), 2)
        y = min(max(0, y), 2)
    code += str((pad[(x, y)]))

print(code)
