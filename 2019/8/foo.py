import sys
from util import *

data = sys.stdin.read().strip()

img = [int(c) for c in data]

cs = chunks(img, 25*6)

l = min(cs, key=lambda c: c.count(0))
print(l.count(1) * l.count(2))
