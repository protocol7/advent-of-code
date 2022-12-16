import sys
from collections import *
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

if xs[0] == [2, 18, -2, 15]:
    width = 20
    row = 10
else:
    width = 4000000
    row = 2000000
    print("this takes a while...")

check = Interval(0, width)

intervals = defaultdict(Intervals)
row_bxs = set()
for sx, sy , bx, by in xs:
    if by == row:
        row_bxs.add(bx)

    m = manhattan(sx, sy, bx, by)

    miny = max(sy - m, 0)
    maxy = min(sy + m, width)

    for yy in range(miny, maxy):
        dx = m - abs(yy - sy)
        s = Interval(sx - dx, sx + dx)

        if s:
            intervals[yy].add(s)

# part 1
ps = set()
for interval in intervals[row]:
    for x in interval:
        ps.add(x)

print(len(ps - row_bxs))

# part 2
# find row with more than one interval, there's only one
row, iss = item(filter(lambda item: len(item[1]) > 1, intervals.items()))

# take the first span
print((iss[0].end + 1) * 4000000 + row)
