import sys

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

inss = [x.strip() for x in sys.stdin.read().split(",")]
dir = 0
x, y = 0, 0
visited = set()

for ins in inss:
    if ins[0] == "R":
        dir += 1
    else:
        dir -= 1
    dir = dir % 4
    dx, dy = dirs[dir]
    l = int(ins[1:])

    nx = x + dx * l
    ny = y + dy * l

    sx = dx
    if sx == 0:
        sx = 1

    sy = dy
    if sy == 0:
        sy = 1

    for vx in range(x + dx, nx + sx, sx):
        for vy in range(y + dy, ny + sy, sy):
            if (vx, vy) in visited:
                print(abs(vx) + abs(vy))
                sys.exit()
            visited.add((vx, vy))

    x = nx
    y = ny
