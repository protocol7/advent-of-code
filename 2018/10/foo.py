import sys
import re
from itertools import count

def parse(line):
    return [int(i) for i in re.findall("-?\d+", line)]

def move(pp):
    x, y, vx, vy = pp
    return (x+vx, y+vy, vx, vy)

def bound(p):
    minx = min([x for x, _, _, _ in p])
    maxx = max([x for x, _, _, _ in p])
    miny = min([x for _, x, _, _ in p])
    maxy = max([x for _, x, _, _ in p])
    return (minx, maxx, miny, maxy)

msg = list(map(parse, sys.stdin))

best = sys.maxsize
best_msg = None

for sec in count():
    msg = list(map(move, msg))

    minx, maxx, miny, maxy = bound(msg)
    area = (maxx - minx) * (maxy - miny)

    if area < best:
        best = area
        best_msg = msg
    else:
        # bounced, we're done
        break

minx, maxx, miny, maxy = bound(best_msg)
msg = [[" "] * (maxx-minx+1) for _ in range(0, maxy-miny+1)]

for x, y, _, _ in best_msg:
    msg[y - miny][x - minx] = "*"

for row in msg:
   print("".join(row))

print(sec)
