import sys
from collections import defaultdict
from intcode import *

prog = parse(sys.stdin)
ic = Intcode(prog)

m = defaultdict(int)
x, y = 0, 0
d = (0, 1)
dirs = {
    (0, 1):  [(-1, 0), (1, 0)],
    (0, -1): [(1, 0), (-1, 0)],
    (-1, 0): [(0, -1), (0, 1)],
    (1, 0):  [(0, 1), (0, -1)]}

while True:
    ic.input.append(m[(x, y)])

    oc = ic.run()
    od = ic.run()
    if oc is None or od is None:
        break
    m[(x, y)] = oc
    d = dirs[d][od]
    x += d[0]
    y += d[1]

print(len(m))
