import sys
from util import *

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

print(int(foo("root")))

a, _, b = d["root"]

def check(n):
    return 

s = binary_search(-sys.maxsize, sys.maxsize, lambda n: foo(a, n) > foo(b, n))

if s is None:
    s = binary_search(-sys.maxsize, sys.maxsize, lambda n: foo(a, n) < foo(b, n))

s, _ = s
assert foo(a, s) == foo(b, s)

print(s)

with open("out.csv", "w") as f:
    for n in range(s - 1000000, s + 1000000, 1000):
        f.write("%s\t%s\n" % (n, foo(a, n) - foo(b, - n)))