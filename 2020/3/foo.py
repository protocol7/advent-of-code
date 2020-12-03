import sys
from util import *

lines = list(map(lambda l: l.strip(), sys.stdin))

def run(right, down):
    x = 0
    cnt = 0
    for y in range(0, len(lines), down):
        if lines[y][x % len(lines[0])] == "#":
            cnt += 1
        x += right
    return cnt

print(run(3, 1))

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
print(product([run(*s) for s in slopes]))