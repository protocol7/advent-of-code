#!/usr/bin/env python3

import sys
from collections import deque

blocks = sys.stdin.read().strip()

disk = []
file = True
id = 0
index = 0
none_index = deque()
for b in blocks:
    b = int(b)

    if file:
        disk.extend([id] * b)
        file = False
        id += 1
    else:
        disk.extend([None] * b)
        file = True

        for j in range(b):
            none_index.append(index + j)

    index += b

# compact
while None in disk:
    d = disk.pop()
    if d is None:
        continue
    i = none_index.popleft()
    disk[i] = d

t = 0
for i, d in enumerate(disk):
    t += i * d

print(t)
