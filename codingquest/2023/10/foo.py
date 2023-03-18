import sys
from collections import defaultdict
from util import dijkstra

start = "TYC"
end = "EAR"

g = defaultdict(dict)
for line in sys.stdin.readlines():
    a, b = line.strip().split(" => ")
    for x in b.split():
        q, w = x.split(":")
        w = int(w)

        if q != end:
            w += 600

        g[a][q] = w

print(dijkstra(g, start, end)[1])