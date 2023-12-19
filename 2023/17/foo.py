import sys
from collections import defaultdict
from heapq import heappop, heappush
from util import Grid, Point, turn_left, turn_right, RIGHT, DOWN


def parse(line):
    return map(int, line.strip())


xs = list(map(parse, sys.stdin))

g = Grid(xs)

def ns(g, p, last_dir, min_dist, max_dist):
    # what possible jumps are available from this point, together with their costs
    out = []

    for dir in (turn_left(last_dir), turn_right(last_dir)):
        np = p
        cost = 0

        for i in range(max_dist):
            np += dir

            if np not in g:
                break

            cost += g[np]

            if i >= min_dist:
                out.append((np, dir, cost))

    return out

def dijkstra(grid, start_p, start_dirs, end, min_dist, max_dist):
    best = defaultdict(lambda: sys.maxsize)

    q = [(0, start_p, start_dir) for start_dir in start_dirs]

    while q:
        cost, p, dir = heappop(q)

        if p == end:
            return cost

        for neighbour, neighbour_dir, neighbour_cost in ns(grid, p, dir, min_dist, max_dist):
            nc = cost + neighbour_cost

            if nc < best[(neighbour, neighbour_dir)]:
                best[(neighbour, neighbour_dir)] = nc

                heappush(q, (nc, neighbour, neighbour_dir))

start = Point(0, 0)
start_dirs = (RIGHT, DOWN)
end = Point(*g.max())

# part 1
print(dijkstra(g, start, start_dirs, end, 0, 3))

# part 2
print(dijkstra(g, start, start_dirs, end, 3, 10))
