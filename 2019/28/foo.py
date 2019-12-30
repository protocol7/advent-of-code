import sys
from intcode import *
from intasm import *

# Day 27: Implement FizzBuzz in Intcode to run on your ASCII capable computer.
# Your program should take one input, a number between 1 and 999. Your program
# should output the numbers from 1 to your input as ASCII, each number on a
# line. For multiples of 3, instead output Fizz, for multiples of 5 instead
# output Buzz.  For multiples of both 3 and 5, instead output FizzBuzz. For
# example, with the input 7, your program should output (in ASCII):
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7

# Part 2: Your first input is the starting number of your sequence, your second
# input is still the length of the sequence (1-999)

asm = """
    var c3 3
    var c5 5

    inp a

    # increment counter
lb1:add b1 1 b1
    eq b1 10 tmp
    jif tmp lb6
    add 0 0 b1
    add b10 1 b10
    eq b10 10 tmp
    jif tmp lb6
    add 0 0 b10
    add b100 1 b100

lb6:mul b100 100 b
    mul b10 10 tmp
    add tmp b b
    add b1 b b

    # check if equal to 3 counter
lb3:eq b c3 d3
    jif d3 lb4
    out 70
    out 105
    out 122
    out 122
    add 3 c3 c3

    # check if equal to 5 counter
lb4:eq b c5 d5
    jif d5 lb2
    out 66
    out 117
    out 122
    out 122
    add 5 c5 c5

lb2:jit d3 lb5
    jit d5 lb5

    # print digit if not fizz or buzz
    jif b100 ot1
    add b100 48 tmp
    out tmp
    jit 1 ot3
ot1:jif b10 ot2
ot3:add b10 48 tmp
    out tmp
ot2:add b1 48 tmp
    out tmp

lb5:out 10
    eq a b tmp
    jif tmp lb1
    ext
"""

inp = iter(map(int, sys.argv[1:]))

prog = intasm(asm)

print(",".join([str(i) for i in prog]))
print("program length: %s" % len(prog))
print("")

ic = Intcode(prog, lambda: next(inp))

while True:
    o = ic.run()

    if o is None:
        break

    sys.stdout.write(chr(o))
    sys.stdout.flush()
