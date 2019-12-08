import sys
from util import *

data = sys.stdin.read().strip()

img = [int(c) for c in data]

w = 25
h = 6
cs = chunks(img, w*h)

for y in range(h):
    s = ""
    for x in range(w):
        for l in cs:
            p = l[y*w + x]
            if p == 0:
                s += " "
                break
            elif p == 1:
                s += "#"
                break
    print(s)
