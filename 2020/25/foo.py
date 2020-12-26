import sys
from itertools import *

a, b = map(int, sys.stdin)

v = 1
for loop_size in count(1):
    v *= 7
    v %= 20201227

    if v == a:
        break

print(pow(b, loop_size, 20201227))