import sys

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

inss = [x.strip() for x in sys.stdin.read().split(",")]
dir = 0
x, y = 0, 0

for ins in inss:
    if ins[0] == "R":
        dir += 1
    else:
        dir -= 1
    dir = dir % 4
    dx, dy = dirs[dir]
    l = int(ins[1:])
    x += dx * l
    y += dy * l

print(abs(x) + abs(y))
