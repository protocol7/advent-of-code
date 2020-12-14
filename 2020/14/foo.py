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
        a = int(a.split("[")[1][:-1])
        b = list(binary(b, 36))

        for i, m in enumerate(mask):
            if m != "X":
                b[i] = m

        mem[a] = int("".join(b), 2)

print(sum(mem.values()))