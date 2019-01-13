import sys
from blist import blist

step = int(sys.argv[1])

buf = blist()
pos = 0

for i in range(50000000):
    pos += 1
    buf.insert(pos, i)
    pos = (pos + step) % len(buf)

print(buf[buf.index(0) + 1])
