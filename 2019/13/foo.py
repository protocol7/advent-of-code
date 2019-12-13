import sys
from intcode import *

prog = parse(sys.stdin)
ic = Intcode(prog, [])

ts = 0

while True:
    x = ic.run()
    y = ic.run()
    t = ic.run()

    if x is None or y is None or t is None:
        break

    if t == 2:
        ts += 1

print(ts)
