import sys
from collections import *

def parse(line):
    a, b = line.strip().split(" | ")

    return a.split(), b.split()

xs = list(map(parse, sys.stdin))

def j(s):
    return "".join(sorted(s))

def ldict(xs):
    d = defaultdict(list)
    for f in xs:
        d[len(f)].append(f)

    return d

s = 0
for x, y in xs:
    d = ldict(x)

    r = {}

    one = d[2][0]
    r["c"] = one
    r["f"] = one

    seven = d[3][0]
    r["a"] = list(set(seven) - set(one))[0]

    four = d[4][0]
    cc = j(set(four) - set(one))
    r["b"] = cc
    r["d"] = cc

    # 0, 6, 9
    zsn = d[6]

    # remove segments from 4 and 7, leaves us only with segment e and g
    h = ldict([j(set(a) - set(seven) - set(four)) for a in zsn])

    # 9 will have only one of these segments, that must be g
    r["g"] = h[1][0]
    
    # ... and e is the other
    r["e"] = j(set(h[2][0]) - set(r["g"]))

    sixzero = [t for t in zsn if r["e"] in t]

    # what's in both 0 and 6?
    in_both = set(sixzero[0]) & set(sixzero[1])

    for v in sixzero:
        # find the unique segment in each of 0 and 6
        a = list(set(v) - in_both)[0]

        # if it's also in 1, it must be c
        if a in one:
            r["c"] = a
        else:
            r["d"] = a

    # reduce the two remaining
    r["b"] = j(set(r["b"]) - set(r["d"]))
    r["f"] = j(set(r["f"]) - set(r["c"]))

    # got the mapping, need the inverse
    r = {v:k for k, v in r.items()}

    # translate digits
    digits = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9
    }

    g = 0
    for yy in y:
        yx = j([r[a] for a in yy])

        g = g * 10 + digits[yx]

    s += g

print(s)