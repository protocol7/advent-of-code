import sys
from collections import defaultdict
from itertools import chain, imap
from heapq import heappush, heappop

def parse(line):
    return sorted(line.split())

def fitness(floors):
    fit = 0
    for f, floor in enumerate(floors):
        fit += (len(floors) - f - 1) * len(floor)
    return fit

def combos(floor):
    items = floor[:]
    cs = [(i,) for i in items] # can pick any item on it's own
    while items:
        item = items.pop(0)
        others = items[:]

        while others:
            other = others.pop(0)
            if item[0] == other[0] or item[1] == other[1]:
                cs.append((item, other))
    return cs

def valid_floor(floor):
    has_gen = len(filter(lambda t: t[1] == "G", floor)) > 0
    # if floor has generator, every chip must be matched up
    if has_gen:
        chips = filter(lambda t: t[1] == "M", floor)
        for c1, _ in chips:
            if not (c1 + "G") in floor:
                return False
        return True
    else:
        return True


def move(floors, e, step):
    cs = combos(floors[e])
    # what floors could the elevator go to?
    es = [f for f in [e-1, e+1] if f >= 0 and f < len(floors)]
    #print("combos", es, cs, floors)

    for c in cs:
        for f in es:
            if f < e and len(c) == 2 and c[0][0] == c[1][0]:
                # don't move pair downwards
                continue

            new_floor = floors[f] + list(c)
            if valid_floor(new_floor):
                new_floors = floors[:]
                new_floors[e] = [t for t in new_floors[e] if t not in c]
                new_floors[f] = sorted(new_floor)
                fit = fitness(new_floors)
                if fit == 0:
                    print("step", step + 1, new_floors)
                    #sys.exit()
                else:
                    ss = str(new_floors) +  "-" + str(f)
                    if ss not in seen:
                        seen.add(ss)
                        heappush(queue, (step + 1, fit, f, new_floors))

floors = map(parse, sys.stdin)
print(floors)
e = 0

queue = []
heappush(queue, (0, fitness(floors), e, floors))

seen = set()

every = 0
while queue:
    step, fit, f, fs = heappop(queue)
    if every % 10000 == 0:
        print(step, fit, f, fs, len(queue))
    move(fs, f, step)
    every += 1
print(every)
