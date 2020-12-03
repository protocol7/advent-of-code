import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

lines = list(map(parse, sys.stdin))