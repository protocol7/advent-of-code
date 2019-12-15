import sys
from intcode import *

prog = parse(sys.stdin)

# part 1
ic = Intcode(prog, lambda: 1)
print(ic.run())

# part 2
ic = Intcode(prog, lambda: 2)
print(ic.run())
