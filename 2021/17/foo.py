import sys
from util import *

x1, x2, y1, y2 = ints(sys.stdin.read())

# find dx candidates
dx_cand = set()
for idx in range(1, 200):
    x = 0
    dx = idx

    while dx:
        x += dx
        dx -= sign(dx)

        if x1 <= x <= x2:
            dx_cand.add(idx)

# find dy candidates
dy_cand = set()
for idy in range(-200, 200):
    y = 0
    dy = idy

    while y >= y1:
        y += dy

        if y1 <= y <= y2:
            dy_cand.add(idy)

        dy -= 1

my = -1
c = 0

# find valid combinations of dx and dy
for idx in dx_cand:
    for idy in dy_cand:
        dx = idx
        dy = idy
        x = 0
        y = 0

        mmy = -1

        while True:
            x += dx
            y += dy

            mmy = max(mmy, y)

            if x1 <= x <= x2 and y1 <= y <= y2:
                c += 1

                my = max(my, mmy)

                break
            elif y < y1:
                break

            dx -= sign(dx)
            dy -= 1

print(my)
print(c)