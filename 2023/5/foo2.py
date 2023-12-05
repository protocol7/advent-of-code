import sys
from util import ints, Interval, pairs


xs = sys.stdin.read().split("\n\n")

rs = []
for a, l in pairs(ints(xs[0])):
    rs.append(Interval(a, a+l-1))

maps = []
for x in xs[1:]:
    map = []
    for line in x.splitlines()[1:]:
        dst, src, l = ints(line)
        map.append((dst, src, l))
    maps.append(map)

def foo(s):
    me = sys.maxsize
    for map in maps:
        for dest, src, l in map:
            end = src + l - 1
            if s >= src and s <= end:
                me = min(me, end - s + 1)
                s = dest + (s - src)
                break

    return s, me

m = sys.maxsize
for r in rs:
    seed = r.start
    while seed <= r.end:
        ns, nl = foo(seed)
        
        m = min(m, ns)
        seed += nl

print(m)
