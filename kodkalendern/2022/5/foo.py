import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return ints(line)

xs = list(map(parse, sys.stdin))

for a, b in xs:
    if b > a * pow(2, 5):
        print("yes", a, b)
        break
