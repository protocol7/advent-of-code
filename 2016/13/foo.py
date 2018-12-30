import sys
from heapq import heappush, heappop

def wall(x, y):
    v = x*x + 3*x + 2*x*y + y + y*y
    v += fav
    b = "{0:b}".format(v)
    return b.count("1") % 2 != 0

def s(x, y, step):
    for dx, dy in dirs:
        sx = x + dx
        sy = y + dy

        if sx < 0 or sy < 0:
            continue

        if wall(sx, sy):
            continue

        if (sx, sy) in seen:
            continue
        seen.add((sx, sy))

        heappush(queue, (step + 1, sx, sy))


fav, tx, ty = 1362, 31, 39

dirs = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)]

seen = set([(1, 1)])

queue = []
heappush(queue, (0, 1, 1))

while queue:
    step, x, y = heappop(queue)
    if x == tx and y == ty:
        print(step)
        break
    s(x, y, step)


# part 2
seen = set([(1, 1)])
heappush(queue, (0, 1, 1))
while queue:
    step, x, y= heappop(queue)
    if step < 50:
        s(x, y, step)
print(len(seen))
