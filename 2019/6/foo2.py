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

san = path(d, "SAN")

l = 0
y = d["YOU"]
while y not in san:
    y = d[y]
    l += 1

print(san.index(y) + l - 1)
