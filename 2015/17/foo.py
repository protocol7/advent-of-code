import sys

def parse(line):
    return int(line)

def e(combo, vol, buck, combos):
    if vol == 0:
        combos.add(tuple(sorted(combo)))
        return
    buck = filter(lambda (_, v): v <= vol, buck)
    for i, b in buck:
        bb = buck[:]
        bb.remove((i, b))
        c = combo[:]
        c.append(i)
        e(c, vol - b, bb, combos)

total = int(sys.argv[1])
buckets = list(enumerate(map(parse, sys.stdin)))

combos = set()
e([], total, buckets, combos)
print(len(combos))

l = min(map(len, combos))
print(len(filter(lambda c: len(c) == l, combos)))
