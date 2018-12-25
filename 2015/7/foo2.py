import sys
from collections import defaultdict
from itertools import chain, imap

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def parse(line):
    line = line.strip()
    exp, assigned = line.split(" -> ")
    exp = exp.split()
    return assigned, exp

def isvalue(e):
    return e.isdigit()

def wrap(x):
    if x < 0:
        return 65536 + x
    else:
        return x

cache = {}
def ev(e):
    global cache
    if isvalue(e):
        return int(e)
    if e in cache:
        return cache[e]
    exp = parsed[e]
    if len(exp) == 1:
        res = ev(exp[0])
    elif len(exp) == 2:
        op, x = exp
        x = ev(x)
        if op == "NOT":
            res = wrap(~x)
    elif len(exp) == 3:
        x, op, y = exp
        x = ev(x)
        y = ev(y)
        if op == "AND":
            res = x & y
        elif op == "OR":
            res = x | y
        elif op == "RSHIFT":
            res = x >> y
        elif op == "LSHIFT":
            res = x << y

    cache[e] = res
    return res

parsed = {assigned:exp for assigned, exp in map(parse, sys.stdin)}
a = ev("a")
cache.clear()
cache["b"] = a
print(ev("a"))
