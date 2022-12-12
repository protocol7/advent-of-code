import sys
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

for part2 in (False, True):
    s = g.points_by_value()["S"]
    if part2:
        s += g.points_by_value()["a"]
    e = g.points_by_value()["E"][0]

    def isn(_, c, __, n):
        d = {"S": "a", "E": "z"}
        c = d.get(c, c)
        n = d.get(n, n)

        return ord(n) - ord(c) <= 1

    gr = g.to_graph(s, isn)

    p = bfs(gr, s, e)

    print(len(p) - 1)