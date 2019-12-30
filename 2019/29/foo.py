import sys
from intcode import *
from intasm import *

# implement "fast division" - read positive integers a and b from input and
# output a/b (truncated). program should be "fast"; max ~1000 executed
# instructions for any 64-bit a and b values.

asm = """
    inp p
    inp q

    add 1 0 i

    rb 10000

lb7:add i 0 &0
    rb -1
    mul i 2 i
    lt p i tmp
    jif tmp lb7

    # div = 0
    # mod = 0

    # divide
lb1:rb 1
    add &0 0 bit

    mul mod 2 mod

    lt p bit xx
    jit xx lb2
    add mod 1 mod
    mul bit -1 nbit
    add p nbit p

lb2:lt mod q xx
    jit xx lb3
    mul q -1 nq
    add mod nq mod
    add div bit div

lb3:eq bit 1 bitc
    jif bitc lb1

    out div

    ext
"""

prog = intasm(asm)

print(",".join([str(i) for i in prog]))
print("program length: %s" % len(prog))
print("")

inp = iter(map(int, sys.argv[1:]))
ic = Intcode(prog, lambda: next(inp))

while True:
    o = ic.run()

    if o is None:
        break

    print(o)
