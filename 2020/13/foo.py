import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip()

a, b = sys.stdin.readlines()

a = int(a)
b = list(map(int, filter(lambda x: x != "x", b.split(","))))


ns = dict()
for bb in b:
    for n in count(1):
        x = n * bb
        if x >= a:
            ns[bb] = x
            break


ma, mb = 0, 999999999

for x, y in ns.items():
    if y < mb:
        mb = y
        ma = x

print((mb - a) * ma )