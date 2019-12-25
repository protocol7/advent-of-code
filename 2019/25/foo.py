import sys
from intcode import *

# #-S-*-*
#       |
#       *-*-* !
#       | |   |
#       ! !---*
#         |   |
# !-* W-K-X   *-P
#   |     |
#   C-----!

# For weight check, bring:
# - spool of cat6
# - hypercube
# - weather machine
# - tambourine

inp = []
inp_iter = iter(inp)

prog = parse(open("input.txt"))
ic = Intcode(prog, lambda: next(inp_iter))

story = ""

while True:
    o = ic.run()

    if o is None:
        break

    story += chr(o)
    sys.stdout.write(chr(o))
    sys.stdout.flush()

    if story.endswith("Command?\n"):
        # wait for input
        ii = raw_input()
        for c in ii:
            inp.append(ord(c))
        inp.append(10)
