import sys
from util import *

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

g = Grid(xs)

seen = set()
asts = []
for p, v in g.points():
    if p in seen:
        continue
    seen.add(p)

    def search(p, ast):
        for n, nv in g.orthogonal(p):
            if n in ast:
                continue

            if nv:
                ast.add(n)
                search(n, ast)
            
    if v:
        ast = set([p])
        search(p, ast)

        seen.update(ast)

        asts.append(sum(g[pp] for pp in ast))

print(int(sum(asts) / len(asts)))