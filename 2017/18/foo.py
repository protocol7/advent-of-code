import sys
from collections import defaultdict

def parse(line):
    return line.split()

def v(x):
    if x.isdigit() or x[0] == "-":
        return int(x)
    else:
        return reg[x]

prog = map(parse, sys.stdin)
reg = defaultdict(int)

pos = 0
sound = None

while pos >= 0 and pos < len(prog):
    ins = prog[pos]
    o = ins[0]

    if o == "set":
        x = ins[1]
        y = v(ins[2])
        reg[x] = y
    elif o == "add":
        x = ins[1]
        y = v(ins[2])
        reg[x] += y
    elif o == "mul":
        x = ins[1]
        y = v(ins[2])
        reg[x] *= y
    elif o == "mod":
        x = ins[1]
        y = v(ins[2])
        reg[x] %= y
    elif o == "snd":
        sound = v(ins[1])
    elif o == "rcv":
        x = v(ins[1])
        if x != 0:
            print(sound)
            break
    elif o == "jgz":
        x = v(ins[1])
        y = v(ins[2])
        if x > 0:
            pos += y - 1

    pos += 1
