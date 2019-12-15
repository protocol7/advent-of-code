import sys
from intcode import *

prog = parse(sys.stdin)
inp = []
inp_iter = iter(inp)
ic = Intcode(prog, lambda: next(inp_iter))

# table of delta x, delta y -> direction
dirs = {
        (0, -1): 1,
        (0, 1): 2,
        (1, 0): 3,
        (-1, 0): 4,
        }
adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(path, seen):
    x, y = path[-1]
    for dx, dy in adj:
        xx = x + dx
        yy = y + dy

        if (xx, yy) in seen:
            continue
        seen.add((xx, yy))

        d = dirs[(xx-x, yy-y)]
        inp.append(d)
        out = ic.run()

        if out == 1 or out == 2:
            # moved
            if out == 2:
                return len(path)

            found = dfs(path + [(xx, yy)], seen)
            if found:
                return found

            # backtrack
            d = dirs[(x-xx, y-yy)]
            inp.append(d)
            out = ic.run()
            assert out == 1 or out == 2

path = []
path.append((0, 0))
seen = set(path)
print(dfs(path, seen))
