import sys
from intcode import *
from util import *

prog = parse(sys.stdin)
prog[0] = 2

bx = None
px = None

ic = Intcode(prog, lambda: sign(bx-px))

while True:
    x = ic.run()
    y = ic.run()
    t = ic.run()

    if x is None or y is None or t is None:
        break

    if x == -1 and y == 0:
        print(t) # score
    elif t == 3:
        px = x
    elif t == 4:
        bx = x
