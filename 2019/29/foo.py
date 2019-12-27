import sys
from collections import *
from util import *
from intcode import *


asm = """
    inp a
    add 0 3 c3
    add 0 5 c5
    add 0 15 c15
lb1:add b 1 b

    # check if equal to 15 counter
    eq b c15 d
    jif d lb3
    out -15
    add 15 c15 c15
    add 3 c3 c3
    add 5 c5 c5
    jit d lb5

    # check if equal to 3 counter
lb3:eq b c3 d
    jif d lb4
    out -3
    add 3 c3 c3
    jit d lb5

    # check if equal to 5 counter
lb4:eq b c5 d
    jif d lb2
    out -5
    add 5 c5 c5
    jit d lb5

    # print digit if not fizz or buzz
lb2:out b

lb5:eq a b d
    jif d lb1
    ext
"""


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
        }

ll = 0
labels = dict()
for i in asm.split("\n"):
    i = i.split("#")[0].strip()
    if i:
        if ":" in i:
            label, i = i.split(":")
            labels[label] = ll
        i = i.split(" ")[0]
        ll += lens[i]

def next_mem():
    global ll
    x = ll
    ll += 1
    return x

regs = defaultdict(next_mem)

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
        elif o == "ext":
            op = "99"
        else:
            assert False
        prog += ([int(op)] + out)


print(prog)
print(labels)
print(dict(regs))

ic = Intcode(prog, lambda: 100)

while True:
    o = ic.run()

    if o is None:
        print("done")
        break

    print(o)
