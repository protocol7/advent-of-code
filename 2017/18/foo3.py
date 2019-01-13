import sys
from collections import defaultdict

def parse(line):
    return line.split()

prog = map(parse, sys.stdin)

def v(reg, q):
    if q.isdigit() or q[0] == "-":
        return int(q)
    else:
        return reg[q]

class Program():

    def __init__(self, pid, inq, outq):
        self.pos = 0
        self.inq = inq
        self.outq = outq
        self.reg = defaultdict(int)
        self.reg["p"] = pid
        self.sent = 0


    def tick(self):
        if self.pos < 0 or self.pos >= len(prog):
            return True

        i = prog[self.pos]
        o = i[0]
        x = i[1]
        if len(i) > 2:
            y = v(self.reg, i[2])

        if o == "set":
            self.reg[x] = y
        elif o == "add":
            self.reg[x] += y
        elif o == "mul":
            self.reg[x] *= y
        elif o == "mod":
            self.reg[x] %= y
        elif o == "snd":
            self.outq.append(v(self.reg, x))
            self.sent += 1
        elif o == "rcv":
            if self.inq:
                self.reg[x] = self.inq.pop(0)
            else:
                return True
        elif o == "jgz":
            x = v(self.reg, x)
            if x > 0:
                self.pos += y - 1

        self.pos += 1

p0q = []
p1q = []

p0 = Program(0, p1q, p0q)
p1 = Program(1, p0q, p1q)

while True:
    y0 = p0.tick()
    y1 = p1.tick()

    if y0 and y1:
        break

print(p1.sent)
