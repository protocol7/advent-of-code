import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

print(product(xs))