import sys
from util import *

xs = sys.stdin.read().strip()

kw = "power plant"
kw = kw.replace(" ", "")

kw = join(dict.fromkeys(kw))

from string import ascii_lowercase

ascii = join(sorted(set(ascii_lowercase) - set("j") - set(kw)))

grid = chunks(kw + ascii, 5)

def coords(s):
    for y, row in enumerate(grid):
        if s in row:
            return (row.index(s), y)

s = ""
for a, b in chunks(xs, 2):
    xa, ya = coords(a)
    xb, yb = coords(b)

    if ya == yb:
        # 1. If the two letters are in the same row, the new letters are the letters directly to the right of the input letters (wrapping around if necessary)
        s += grid[ya][xa-1] + grid[ya][xb-1]
    elif xa == xb:
        # 2. If the two letters are in the same column, the new letters are the letters directly below the input letters (wrapping as above)
        s += grid[ya-1][xa] + grid[yb-1][xa]
    else:
        # 3. If the letters are separated diagonally, they form the corners of a "box". The encrypted letters are the letters on the laterally 
        # opposite end of this box to the input (i.e. look to the far left or right of the input while staying within the box)
        s += grid[ya][xb]
        s += grid[yb][xa]

print(s)