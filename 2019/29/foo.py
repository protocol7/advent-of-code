import sys
from collections import *
from util import *
from intcode import *

# Day 27: Implement FizzBuzz in Intcode to run on your ASCII capable computer.
# Your program should take one input, a number between 1 and 999. Your program
# should output the numbers from 1 to your input as ASCII, each number on a
# line. For multiples of 3, instead output Fizz, for multiples of 5 instead
# output Buzz.  For mutliples of both 3 and 5, instead output FizzBuzz. For
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

asm = ""
for i in range(50, -1, -1):
    asm += "    var b%s %s\n" % (i, 1<<i)


asm += """
    inp start
    inp end

    add start end end

    var bstart b50

    add start 0 i

lb0:add i 0 p

    # check if divisibe by 3
    add 0 0 mod
    add bstart -1 tmp

    # keep state of relative base
    mul tmp -1 trb
    rb tmp
l31:rb 1
    add trb -1 trb
    add &0 0 bit

    mul mod 2 mod
    lt p bit xx
    jit xx l32
    add mod 1 mod
    mul bit -1 nbit
    add p nbit p

l32:lt mod 3 xx
    jit xx l33
    add mod -3 mod

l33:eq bit 1 bitc
    jif bitc l31

    eq mod 0 tmp
    jif tmp lb1
    out -3
    jit 1 lb2

lb1:out i

lb2:add i 1 i
    eq i end tmp
    rb trb
    jif tmp lb0

    ext
"""

print(asm)

inp = iter(map(int, sys.argv[1:]))



lens = {
    "add": 4,
    "mul": 4,
    "inp": 2,
    "out": 2,
    "jit": 3,
    "jif": 3,
    "lt": 4,
    "eq": 4,
    "ext": 1,
    "rb": 2,
        }

ll = 0
labels = dict()
vars = OrderedDict()
for i in asm.split("\n"):
    i = i.split("#")[0].strip()
    if i:
        if ":" in i:
            label, i = i.split(":")
            labels[label] = ll
        i = i.split(" ")
        o = i[0]
        if o == "var":
            vars[i[1]] = i[2]
        else:
            ll += lens[o]

def next_mem():
    global ll
    x = ll
    ll += 1
    return x

regs = defaultdict(next_mem)

# make sure vars are stored first
for v in vars.keys():
    _ = regs[v]

prog = []
for i in asm.split("\n"):
    i = i.split("#")[0].strip()
    if i:
        if ":" in i:
            label, i = i.split(":")

        i = i.split(" ")
        o = i[0]
        i = i[1:]
        out = []
        if o == "add" or o == "mul":
            if o == "add":
                op = "01"
            else:
                op = "02"
            for x in i:
                if isint(x):
                    op = "1" + op
                    out.append(int(x))
                elif x[0] == "&":
                    op = "2" + op
                    out.append(int(x[1:]))
                else:
                    op = "0" + op
                    out.append(regs[x])
        elif o == "inp":
            op = "03"
            out.append(regs[i[0]])
        elif o == "out":
            op = "04"
            x = i[0]
            if isint(x):
                op = "1" + op
                out.append(int(x))
            elif x[0] == "&":
                op = "2" + op
                out.append(int(x[1:]))
            else:
                op = "0" + op
                out.append(regs[x])
        elif o == "jit" or o == "jif":
            if o == "jit":
                op = "05"
            else:
                op = "06"

            x = i[0]
            if isint(x):
                op = "1" + op
                out.append(int(x))
            else:
                op = "0" + op
                out.append(regs[x])

            op = "1" + op
            out.append(labels[i[1]])
        elif o == "lt" or o == "eq":
            if o == "lt":
                op = "07"
            else:
                op = "08"
            for x in i:
                if isint(x):
                    op = "1" + op
                    out.append(int(x))
                else:
                    op = "0" + op
                    out.append(regs[x])
        elif o == "rb":
            op = "09"
            x = i[0]
            if isint(x):
                op = "1" + op
                out.append(int(x))
            else:
                op = "0" + op
                out.append(regs[x])
        elif o == "ext":
            op = "99"
        elif o == "var":
            continue
        else:
            assert False
        prog += ([int(op)] + out)

for value in vars.values():
    if isint(value):
        prog.append(int(value))
    else:
        prog.append(regs[value])


print(",".join([str(i) for i in prog]))
print(len(prog))
print(labels)
print(dict(regs))
print(vars)

ic = Intcode(prog, lambda: next(inp))

while True:
    o = ic.run()

    if o is None:
        print("done")
        break

    #sys.stdout.write(chr(o))
    print(o)
    sys.stdout.flush()
