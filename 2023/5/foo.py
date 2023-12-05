import sys
from util import ints


xs = sys.stdin.read().split("\n\n")

seeds = ints(xs[0])

maps = []
for x in xs[1:]:
    map = []
    for line in x.splitlines()[1:]:
        dst, src, l = ints(line)
        map.append((dst, src, l))
    maps.append(map)

def foo(s):
    for map in maps:
        for dest, src, l in map:
            end = src + l - 1
            if s >= src and s <= end:
                s = dest + (s - src)
                break

    return s

print(min(foo(s) for s in seeds))
