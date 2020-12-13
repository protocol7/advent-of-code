import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

_, b = sys.stdin.readlines()

n = []
a = []
for i, x in enumerate(b.split(",")):
    if x == "x":
        continue

    n.append(int(x))
    a.append(-i)

print(chinese_remainder(n, a))
