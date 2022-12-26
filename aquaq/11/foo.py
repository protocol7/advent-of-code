import sys
from collections import *
from itertools import *
from util import *
from csv import DictReader

def parse(line):
    return line.strip()

xs = list(DictReader(sys.stdin))

xs = [(int(d["lx"]), int(d["ly"]), int(d["ux"]), int(d["uy"])) for d in xs]

floors = []
for x1, y1, x2, y2 in xs:
    assert x1 < x2
    assert y1 < y2
    floor = set()
    for x in range(x1, x2):
        for y in range(y1, y2):
            floor.add((x, y))

    floors.append(floor)

overlapping = set()
for fi, floor in enumerate(floors):

    overlaps = False
    for fj, other in enumerate(floors):
        if fi == fj:
            continue

        if floor & other:
            overlaps = True
            break

    if overlaps:
        overlapping |= floor


Grid(overlapping).pretty_print()

print("")
print(len(overlapping))