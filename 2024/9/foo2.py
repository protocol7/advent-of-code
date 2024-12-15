#!/usr/bin/env python3

import sys

blocks = sys.stdin.read().strip()

file = True
id = 0
files = {} # id -> [index, size]
frees = {} # index -> size
index = 0

for b in blocks:
    b = int(b)

    if file:
        files[id] = [index, b]
        file = False
        id += 1
    else:
        frees[index] = b
        file = True

    index += b

# compact
for id in range(id-1, 0, -1):
    index, size = files[id]

    free_indexes = sorted(frees.keys())

    for j in free_indexes:
        free_size = frees[j]

        if free_size >= size and j < index:
            # move
            files[id] = [j, size]
            new_free_index = j + size
            del frees[j]
            frees[new_free_index] = free_size - size

            break

files_in_order = {}
for id, (index, size) in files.items():
    files_in_order[index] = (id, size)

files_by_index = sorted(files_in_order.keys())

t = 0
for index in files_by_index:
    id, size = files_in_order[index]
    for j in range(size):
        t += (index + j) * id

print(t)
