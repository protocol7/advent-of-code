import sys

def parse(line):
    return line.split()

def pp(grid):
    for row in grid:
        print("".join(row))

def rotate(l, by):
    b = len(l) - by
    return l[b:] + l[:b]

parsed = map(parse, sys.stdin)

width = 50
height = 6

grid = [["." for _ in range(width)] for _ in range(height)]

for ins in parsed:
    o = ins[0]
    if o == "rect":
        w, h = [int(i) for i in ins[1].split("x")]
        for x in range(w):
            for y in range(h):
                grid[y][x] = "#"
    else:
        t = ins[1]
        i = int(ins[2].split("=")[1])
        by = int(ins[-1])
        if t == "column":
            col = rotate([row[i] for row in grid], by)
            for y, c in enumerate(col):
                grid[y][i] = c
        else:
            grid[i] = rotate(grid[i], by)

count = 0
for row in grid:
    count += sum([1 for c in row if c == "#"])
print(count)

pp(grid)
