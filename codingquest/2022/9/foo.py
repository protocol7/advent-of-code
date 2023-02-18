import sys
from util import *

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

g = Grid(xs)

start = (xs[0].find(" "), 0)
end = (xs[-1].find(" "), len(xs)-1)

graph = g.to_graph(start, lambda _, __, ___, n: n == " ")

p = bfs(graph, start, end)

print(len(p))