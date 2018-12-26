import sys
from collections import defaultdict
from itertools import chain, imap

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def parse(line):
    l = line.split()
    return [int(l[i].strip(",")) for i in [2, 4, 6, 8, 10]]

total = 100
def e(s, ing, depth, combos):
    if len(ing) == 1:
        s += str(depth) * (total-len(s))
        combos.append(s)
        return
    for i in range(len(s), total+1):
        ss = s + str(depth) * (total-i)
        e(ss, ing[1:], depth + 1,  combos)

def value(s):
    cap, dur, fla, tex, cal = 0, 0, 0, 0, 0
    for c in s:
        i = parsed[int(c)]
        cap += i[0]
        dur += i[1]
        fla += i[2]
        tex += i[3]
        cal += i[4]
    cap = max(cap, 0)
    dur = max(dur, 0)
    fla = max(fla, 0)
    tex = max(tex, 0)
    return (cap * dur * fla * tex, cal)

parsed = map(parse, sys.stdin)
combos = []
e("", parsed, 0, combos)

vals = map(value, combos)
cal500 = filter(lambda (_, c): c == 500, vals)

print(max([x for x, _ in vals]))
print(max([x for x, _ in cal500]))
