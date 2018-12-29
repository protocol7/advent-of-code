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

A = ord("a")
LETTERS = ord("z") - A + 1

def decrypt(name, seg):
    clear = ""
    for c in name:
        clear += chr((ord(c) - A + seg) % LETTERS + A)
    return clear, seg

rooms = map(parse, sys.stdin)

valid = filter(lambda (code, seg, cs): checksum(code) == cs, rooms)

cleared = map(lambda (code, seg): decrypt(code, seg), [(code, seg) for code, seg, _ in valid])

for room, seg in cleared:
    # found through greping
    if room == "northpoleobjectstorage":
        print(seg)
