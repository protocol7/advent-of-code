import sys
from operator import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

def eval(s):
    def eval_exp(c, op, val):
        if op is None:
            return int(c)
        else:
            return op(int(c), val)

    val = None
    op = None
    while True:
        c = next(s, None)
        if c is None:
            break
        elif c.isdigit():
            val = eval_exp(c, op, val)
        elif c == "*":
            op = mul
        elif c == "+":
            op = add
        elif c == "(":
            val = eval_exp(eval(s), op, val)
        elif c == ")":
            return val

    return val


print(sum(eval(iter(x)) for x in xs))