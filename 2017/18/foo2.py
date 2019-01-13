import sys
from collections import defaultdict

def parse(line):
    return line.split()


prog = map(parse, sys.stdin)

def run(pid, inq, outq):
    reg = defaultdict(int)
    reg["p"] = pid

    def v(x):
        if x.isdigit() or x[0] == "-":
            return int(x)
        else:
            return reg[x]

    pos = 0
    sent = 0

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
            x = v(ins[1])
            outq.append(x)
            sent += 1
            yield "snd"
        elif o == "rcv":
            if inq:
                x = ins[1]
                reg[x] = inq.pop(0)
            else:
                yield "wait"
                continue
        elif o == "jgz":
            x = v(ins[1])
            y = v(ins[2])
            if x > 0:
                pos += y - 1

        pos += 1

p0q = []
p1q = []

p0 = run(0, p1q, p0q)
p1 = run(1, p0q, p1q)

p0send = 0
p1send = 0

while True:
    y0, y1 = None, None
    try:
        if p0:
            y0 = next(p0)
    except StopIteration:
        p0 = None
    try:
        if p1:
            y1 = next(p1)
    except StopIteration:
        p1 = None


    if y1 == "snd":
        p1send += 1

    print(y0, y1, len(p0q), len(p1q), p1send)

    if (p0 is None or y0 == "wait") and (p1 is None or y1 == "wait"):
        break

print(p1send)

# 127 too low
