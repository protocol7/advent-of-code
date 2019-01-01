import sys
from itertools import count

def parse(line):
    line = line.split()
    return int(line[3]), int(line[-1].strip("."))

def tick(st):
    return all([(pos + (t+1) + st) % slots == 0 for t, (slots, pos) in enumerate(discs)])

discs = map(parse, sys.stdin)

for t in count():
    if tick(t):
        print(t)
        break
