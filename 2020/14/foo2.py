import sys
from util import *

def parse(line):
    return line.strip().split(" = ")

xs = list(map(parse, sys.stdin))

mem = dict()

for a, b in xs:
    if a == "mask":
        mask = b
    else:
        a = [list(binary(a.split("[")[1][:-1], 36))]

        for i, m in enumerate(mask):
            if m == "X":
                na = []
                for y in a:
                    for x in "01":
                        yy = y[:]
                        yy[i] = x
                        na.append(yy)

                a = na
            elif m == "1":
                for y in a:
                    y[i] = "1"

        for x in a:
            mem[int("".join(x), 2)] = int(b)

print(sum(mem.values()))