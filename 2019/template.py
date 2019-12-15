import sys
from collections import *
from itertools import *
from util import *
from intcode import *
from heapq import heappop, heappush



prog = parse(sys.stdin)
ic = Intcode(prog, [])
print(ic.run())



def parse(line):
    pass

parsed = map(parse, sys.stdin)
