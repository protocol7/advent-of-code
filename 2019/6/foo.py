import sys

d = {}
for line in sys.stdin:
    a, b = line.strip().split(")")
    d[b] = a

def path(d, s):
    p = []
    while s != "COM":
        p.append(s)
        s = d[s]
    return p

print(sum([len(path(d, o)) for o in d]))
