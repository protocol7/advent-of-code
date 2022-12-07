import sys
from util import *

xs = sys.stdin.read().strip()

for o in (4, 14):
    for i, s in enumerate(window(xs, o)):
        if len(set(s)) == o:
            print(i+o)
            break
