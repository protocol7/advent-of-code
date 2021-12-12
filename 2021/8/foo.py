import sys
from util import *

def parse(line):
    _, b = line.strip().split(" | ")

    return b.split()

xs = flatten(map(parse, sys.stdin))

print(sum(1 for x in xs if len(x) in (2, 3, 4, 7)))