import sys
from collections import defaultdict
from itertools import chain, imap

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def parse(line):
    l = line.split()
    return l[0], l[2], int(l[4])

pairs = {(l1, l2):d for l1, l2, d in map(parse, sys.stdin)}

locations = set()
locations.update([x for x, _ in pairs.keys()])
locations.update([x for _, x in pairs.keys()])

def e(path, remains, paths):
    if not remains:
        paths.append(path)
    for loc in remains:
        r = set(remains)
        r.remove(loc)
        p = path[:]
        p.append(loc)
        e(p, r, paths)

paths = []
e([], locations, paths)

def dist(path):
    dist = 0
    for l1, l2 in zip(path, path[1:]):
        dist += pairs.get((l1, l2), pairs.get((l2, l1)))
    return dist

dists = map(dist, paths)
print(min(dists))
print(max(dists))
