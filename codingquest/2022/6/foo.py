import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip().split()

xs = list(map(parse, sys.stdin))

r = defaultdict(int)

ip = 0

def ts(x):
    if isint(x):
        return int(x)
    else:
        assert "A" <= x <= "L", x
        return x

cmp = False
while True:
    o = xs[ip]

    print(ip, o)

    op = o[0]

    if op == "ADD":
        t, s = ts(o[1]), ts(o[2])

        if type(s) == int:
            r[t] += s
        else:
            r[t] += r[s]
    elif op == "MOD":
        t, s = ts(o[1]), ts(o[2])

        if type(s) == int:
            r[t] %= s
        else:
            r[t] %= r[s]
    elif op == "DIV":
        t, s = ts(o[1]), ts(o[2])

        if type(s) == int:
            r[t] //= s
        else:
            r[t] //= r[s]
    elif op == "MOV":
        t, s = ts(o[1]), ts(o[2])

        if type(s) == int:
            r[t] = s
        else:
            r[t] = r[s]
    elif op == "CEQ":
        t, s = ts(o[1]), ts(o[2])

        t = t if type(t) == int else r[t]
        s = s if type(s) == int else r[s]

        cmp = t == s
    elif op == "CGE":
        t, s = ts(o[1]), ts(o[2])

        t = t if type(t) == int else r[t]
        s = s if type(s) == int else r[s]

        cmp = t >= s
    elif op == "JMP":
        s = ts(o[1])

        s = s if type(s) == int else r[s]

        ip += s - 1
    elif op == "JIF":
        if cmp:
            s = ts(o[1])

            s = s if type(s) == int else r[s]

            ip += s - 1
    elif op == "OUT":
        s = ts(o[1])

        s = s if type(s) == int else r[s]

        print(s)
    elif op == "END":
        break
    else:
        assert False

    ip += 1



