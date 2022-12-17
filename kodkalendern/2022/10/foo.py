import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

c = 0
for a in xs:
    c += (a-1) // 8 + 1

print(c)