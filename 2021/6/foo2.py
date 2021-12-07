import sys
from collections import *
from util import *

xs = ints(sys.stdin.read())

dd = defaultdict(int)
for x in xs:
    dd[x] += 1

for _ in range(256):
    ns = defaultdict(int)

    for d, n in dd.items():
        if d == 0:
            ns[6] += n
            ns[8] += n
        else:
            ns[d-1] += n

    dd = ns

print(sum(dd.values()))