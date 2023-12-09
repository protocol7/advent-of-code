import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return int(line.strip().split()[1])

print(sum(map(parse, sys.stdin)))

