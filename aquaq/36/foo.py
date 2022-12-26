import sys
from util import *

xs = sys.stdin.read().strip().split("\n\n")

ps = []
for problem in xs:
    g, inputs = problem.split("\n")
    g = ints(g)

    largest_grid = max(g)

    inputs = inputs[2:].split()
    ix = []
    for i in range(len(inputs)):
        f = inputs[i]
        if f == "*":
            # replace with list of possible numbers

            # find earlier number
            cc = i - 1
            start = 1
            while cc >= 0:
                if inputs[cc] == "*":
                    cc -= 1
                else:
                    start = int(inputs[cc])
                    break

            # find next number
            cc = i + 1
            end = largest_grid
            while cc < len(inputs):
                if inputs[cc] == "*":
                    cc += 1
                else:
                    end = int(inputs[cc])
                    break

            ix.append(list(range(start, end+1)))
        else:
            ix.append([int(f)])

    ps.append((g, ix))

def find_match(grid, a, b):
    ma = [i for i, g in enumerate(grid) if g == a + b]
    mp = [i for i, g in enumerate(grid) if g == a * b]

    if ma and mp:
        for aa in ma:
            if aa not in mp:
                return aa, mp[0]


def remove_at_index(xs, i):
    xs = xs[::]
    return xs[:i] + xs[i+1:]

def remove_at_indexes(xs, i, j):
    xs = xs[::]

    if i < j:
        return xs[:i] + xs[i+1:j] + xs[j+1:]
    else:
        return xs[:j] + xs[j+1:i] + xs[i+1:]

def foo(p):
    grid, candidates = p
    q = deque([(grid, candidates, [])])

    while q:
        # dfs
        grid, candidates, pairs = q.pop()

        if not grid:
            return pairs

        cands = candidates.pop(0)

        for cand in cands:
            for bi, bs in enumerate(candidates):
                for b in bs:
                    m = find_match(grid, cand, b)
                    if m:
                        g1, g2 = m

                        new_grid = remove_at_indexes(grid, g1, g2)
                        new_candidates = remove_at_index(candidates, bi)

                        q.append((new_grid, new_candidates, pairs + [(cand, b)]))

s = 0
for p in ps:
    pairs = foo(p)
    print("!!!", pairs)

    for a, b in pairs:
        s += abs(a - b)

print(s)