import sys
from collections import defaultdict

def parse(line):
  # #1 @ 236,827: 24x17
  id, _, coords, size = line.split()

  id = id.strip('#')
  coords = coords.strip(':')
  x, y = [int(i) for i in coords.split(',')]
  w, h = [int(i) for i in size.split('x')]

  cs = set([(xs, ys) for xs in range(x, x+w) for ys in range(y, y+h)])
  return (id, cs)

def heatmap(cs):
    d = defaultdict(int)
    for c in cs:
        d[c] += 1
    return d

def filter_dict(d, fn):
    return {k: v for k, v in d.iteritems() if fn(k, v)}

fs = map(parse, sys.stdin)
xs = [x[1] for x in fs]

flat_fs = [item for sublist in xs for item in sublist]

overlaps = set(filter_dict(heatmap(flat_fs), lambda _, v: v > 1).keys())

for f in fs:
    if not f[1].intersection(overlaps):
        print(f[0])
