import sys
from functools import reduce
from collections import defaultdict


xs = sys.stdin.read().strip().split(",")

def hash(s):
    return reduce(lambda h, c: (h + ord(c)) * 17 % 256, s, 0)

boxes = defaultdict(dict)

t = 0
for x in xs:
    t += hash(x)
    if "=" in x:
        l, fl = x.split("=")

        boxes[hash(l)][l] = int(fl)
    elif "-" in x:
        l = x[:-1]
        boxes[hash(l)].pop(l, None)

# part 1
print(t)

# part 2
t = 0
for i, box in boxes.items():
    for j, fl in enumerate(box.values()):
        t += (i+1) * (j+1) * fl

print(t)
