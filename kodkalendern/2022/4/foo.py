import sys
from util import *

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

print(ilen(filter(lambda x: 0 < x < 5, xs)))