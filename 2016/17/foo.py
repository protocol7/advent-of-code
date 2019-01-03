import sys
import hashlib
from heapq import heappush, heappop

def hash(inp, path):
    return hashlib.md5(inp + path).hexdigest()[:4]

def open(inp, path):
    h = [int(i, 16) for i in hash(inp, path)]
    return [d for d, i in zip("UDLR", h) if i > 0xa]

def move(inp, x, y, path):
    o = open(inp, path)
    for p in o:
        dx, dy = dirs[p]
        xx = x + dx
        yy = y + dy
        if xx < 0 or yy < 0:
            continue
        if xx > 3 or yy > 3:
            continue
        heappush(queue, (len(path), xx, yy, path + p))

dirs = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0)
        }

tx, ty = 3, 3

inp = sys.argv[1]

queue = []
heappush(queue, (0, 0, 0, ""))

while queue:
    _, x, y, path = heappop(queue)
    if x == tx and y == ty:
        print(path)
        break

    move(inp, x, y, path)

# part 2
queue = []
heappush(queue, (0, 0, 0, ""))

longest = 0
while queue:
    _, x, y, path = heappop(queue)
    if x == tx and y == ty:
        longest = max(longest, len(path))
        continue

    move(inp, x, y, path)

print(longest)
