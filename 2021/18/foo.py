import sys
from itertools import *
from util import *
import re
from functools import reduce as _reduce

def parse(line):
    return line.strip()

def explode(x):
    d = 0

    for i, c in enumerate(x):
        d += c == "["
        d -= c == "]"

        if d == 5:
            e = x.index("]", i)

            al, ar = ints(x[i:e+1])

            def add_pre(m):
                return m.group(1) + str(int(m.group(2)) + al) + m.group(3)

            def add_suf(m):
                return m.group(1) + str(int(m.group(2)) + ar)

            pre = re.sub(r"(.*?)(\d+)([^\d]*)$", add_pre, x[0:i])
            suf = re.sub(r"^(.*?)(\d+)", add_suf, x[e+1:])

            return "%s0%s" % (pre, suf)

    return x

def split(x):
    def spl(x):
        return "[%s,%s]" % (x // 2, (x+1) // 2)

    return re.sub("\d\d+", lambda m:  spl(int(m.group())), x, count=1)
            
def reduce(x):
    while True:
        old_x = x
        x = explode(x)

        if old_x != x:
            continue

        x = split(x)

        if old_x == x:
            return x

def add(a, b):
    return "[%s,%s]" % (a, b)

def magnitude(s):
    while True:
        def h(m):
            a, b = ints(m.group(1))
            return str(a*3 + b*2)

        ns = re.sub(r"\[(\d+,\d+)\]", h, s)

        if s == ns:
            return int(s)

        s = ns

xs = list(map(parse, sys.stdin))

# part 1
print(magnitude(_reduce(lambda a, b: reduce(add(a, b)), xs)))

# part 2
print(max(magnitude(reduce(add(a, b))) for a, b in permutations(xs, 2)))