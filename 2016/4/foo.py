import sys
from collections import defaultdict

def parse(line):
    c, cs = line.strip().split("[")
    cs = cs.strip("]")
    c = c.split("-")
    seg = int(c[-1])
    code = "".join(c[:-1])
    return code, seg, cs

def checksum(code):
    d = defaultdict(int)
    for c in code:
        d[c] += 1
    xx = [(k, v) for k, v in d.iteritems()]
    xx.sort(key=lambda (c, count): (-count, c))
    xx = "".join([x for x, _ in xx])
    return xx[:5]

rooms = map(parse, sys.stdin)

valid = filter(lambda (code, seg, cs): checksum(code) == cs, rooms)

print(sum([seg for _, seg, _ in valid]))
