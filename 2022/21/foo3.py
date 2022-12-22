import sys
from util import *

# https://old.reddit.com/r/adventofcode/comments/zrdfb0/2022_day_21_part_3/

def parse(line):
    return line.strip().split()

xs = list(map(parse, sys.stdin))

d = {}
vals = {}
for x in xs:
    n = x[0].strip(":")

    c = x[1:]
    if len(c) == 3:
        d[n] = c
    else:
        vals[n] = int(c[0])

def foo(n, humn=None):
    if n == "humn" and humn is not None:
        return humn

    if n in vals:
        return vals[n]

    a, op, b = d[n]
    a = foo(a, humn)
    b = foo(b, humn)

    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    elif op == "-":
        return a - b

a, _, b = d["root"]

ans = []
for n in range(-10000, 10000):
    if foo(a, n) == foo(b, n):
        ans += [n]

print(product(ans))