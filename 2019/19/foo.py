import sys
from intcode import *

prog = parse(sys.stdin)

# just count how many 1's we got in a 50x50 map
c = 0
for x in range(50):
    for y in range(50):
        inp = iter([x, y])
        ic = Intcode(prog, lambda: next(inp))

        c += ic.run()

print(c)
