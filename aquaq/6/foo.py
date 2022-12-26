import sys
from collections import *
from itertools import *

# 3 numbers which sum to 123

target = 123

xs = list(range(target + 1))

s = 0
for x in product(xs, repeat=3):
    if sum(x) == target:
        s += str(x).count("1")

print(s)