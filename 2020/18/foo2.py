import sys
from operator import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

def eval_exp(vals):
    for cop, op in zip("+*", [add, mul]):
        while cop in vals:
            i = vals.index(cop)
            vv = op(vals[i - 1], vals[i + 1])
            vals = vals[0:i-1] + [vv] + vals[i+2:]

    return vals[0]

def eval(s):
    vals = []

    while True:
        c = next(s, None)
        if c is None:
            break
        elif c.isdigit():
            vals.append(int(c))
        elif c in "*+":
            vals.append(c)
        elif c == "(":
            vals.append(eval(s))
        elif c == ")":
            return eval_exp(vals)

    return eval_exp(vals)


print(sum(eval(iter(x)) for x in xs))