import sys
from collections import defaultdict

def parse(line):
  # #1 @ 236,827: 24x17
  _, _, coords, size = line.split()

  coords = coords.strip(':')
  x, y = [int(i) for i in coords.split(',')]
  w, h = [int(i) for i in size.split('x')]

  cs = []
  for xs in range(x, x+w):
    for ys in range(y, y+h):
        cs.append((xs, ys))

  return cs

def heatmap(cs):
    d = defaultdict(int)
    for c in cs:
        d[c] += 1
    return d

def filter_dict(d, fn):
    return {k: v for k, v in d.iteritems() if fn(k, v)}

fs = map(parse, sys.stdin)

flat_fs = [item for sublist in fs for item in sublist]

overlaps = filter_dict(heatmap(flat_fs), lambda _, v: v > 1)

print(len(overlaps))
