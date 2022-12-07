from collections import deque, defaultdict
from copy import deepcopy
from heapq import heappush, heappop
from re import findall
from itertools import chain, islice
from functools import reduce
from math import gcd, prod
from sys import maxsize

def flatmap(f, items):
    return list(chain.from_iterable(map(f, items)))

# get digit as position n from an int
def digit(number, n):
    return number // 10**n % 10

# partition a list into chunks of lenght n
def chunks(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]

def pairs(xs):
    return chunks(xs, 2)

# find all ints, including negative ones, in a string
def ints(s, negatives=True):
    if negatives:
        return list(map(int, findall(r"-?\d+", s)))
    else:
        return list(map(int, findall(r"\d+", s)))

# finds all simple strings and digits, including negative ints
def tokens(s):
    return findall(r"[A-Za-z0-9\-]+", s)

# is this string an int?
def isint(s):
    return s.isdigit() or (s and s[0] in ('+', '-') and s[1:].isdigit())

# make ints of everything that looks like one
def intify(xs):
    return [int(x) if isint(x) else x for x in xs]

# turn an str or int into a binary str
# if length is given, left pad to bit string of length
def binary(i, length=0):
    b = "{0:b}".format(int(i))
    if length:
        return b.rjust(length, '0')
    else:
        return b

# split a string at any character in seps
# returns list of strings, excluding any empty substrings
def msplit(s, seps):
    def f(s, seps):
        p = 0
        for i, c in enumerate(s):
            if c in seps:
                yield s[p:i]
                p = i + 1
        yield s[p:]
    return list(filter(lambda s: s, f(s, seps)))

# length of an iterator
def ilen(iter):
    return sum(1 for _ in iter)

# flattens a list of lists
def flatten(xs):
    return [x for xx in xs for x in xx]

# Returns a sliding window (of width n) over data from the iterable
# s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...
def window(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))
    out = []

    if len(result) == n:
        out.append(result)
    
    for elem in it:
        result = result[1:] + (elem,)
        out.append(result)

    return out

# joins a list into a string
def join(xs):
    return "".join(xs)

# get the only item in the collection, useful for getting items out of single item sets
# asserts that the collection only has one item
def item(xs):
    assert len(xs) == 1
    return list(xs)[0]

# removes value from collections (list, sets) without throwing exception if the value is not in the collection
# does not mutate the provided collection, but rather returns a new collection with the value removed
def safe_remove(v, xs):
    xs = deepcopy(xs)

    if type(xs) == list:
        if v in xs:
            xs.remove(v)
    elif type(xs) == set:
        xs.discard(v)

    return xs

def product(xs):
    return prod(xs)

def sign(i):
    if i > 0:
        return 1
    elif i < 0:
        return -1
    else:
        return 0

def triangular_number(n):
    return n * (n + 1) // 2

# Graphs/geometry

# manhattan((x, y)) -> manhattan for (x, y) and (0, 0)
# manhattan((x1, y1), (x2, y2)) -> manhattan for (x1, y1) and (x2, y2)
# manhattan(x, y) -> manhattan for (x, y) and (0, 0)
# manhattan(x1, y1, x2, y2) -> manhattan for (x1, y1) and (x2, y2)
def manhattan(*args):
    if len(args) == 1:
        ax, ay = args[0]
        bx, by = 0, 0
    elif len(args) == 2:
        if type(args[0]) == tuple:
            (ax, ay), (bx, by) = args
        else:
            ax, ay = args
            bx, by = 0, 0
    elif len(args) == 4:
        ax, ay, bx, by = args
    return abs(ax - bx) + abs(ay - by)


# Find the intersection of two lines, e.g.
# line_intersection(((0, 0), (10, 10)), ((10, 0), (0, 10))) -> (5, 5)
#
# If lines don't intersect, an exception is raised
def line_intersection(l1, l2):
    (x0, y0), (x1, y1) = l1
    (x2, y2), (x3, y3) = l2

    xdiff = (x0 - x1, x2 - x3)
    ydiff = (y0 - y1, y2 - y3)

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception("lines do not intersect")

    d = (det(*l1), det(*l2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

# graph is dict of node -> neighbours
# returns dict of node -> best level and dict of node -> best parent
def exhaustive_bfs(graph, start):
    q = deque([start])
    levels = {start: 0}
    parent = {start: None}

    level = 1
    while q:
        v = q.popleft()
        for n in graph[v]:
            if n not in levels:
                q.append(n)
                levels[n] = level
                parent[n] = v
        level += 1
    return levels, parent

# graph is dict of node -> neighbours
# end is predicate function
# returns path from start to end
def bfs(graph, start, end):
    q = deque([[start]])
    seen = set()

    while q:
        path = q.popleft()
        v = path[-1]
        for n in graph[v]:
            p = path + [n]
            if end(n):
                return p
            if n not in seen:
                q.append(p)
                seen.add(n)

# return all paths between start and end
# graph is dict of node -> neighbours
# end is predicate function
# returns list of paths from start to end
def bfs_all_paths(graph, start, end, cyclic=False):
    q = deque([[start]])
    paths = []

    while q:
        path = q.popleft()
        v = path[-1]
        for n in graph[v]:
            if cyclic and n in path:
                continue

            p = path + [n]
            if end(n):
                paths.append(p)
            else:
                q.append(p)
    return paths

def dfs(graph, node, end, paths, path):
    path = path + [node] 

    if node == end:
        paths.append(path)
        return

    for n in graph[node]:
        if n not in path:
            dfs(graph, n, end, paths, path)

# give topological order of graph, starting at "start"
# graph is dict of node -> neighbours
# returns a list of nodes in topological order
def top_sort(graph, start):
    result = []
    seen = set()

    def visit(node):
        if node in graph:
            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    visit(n)
        result.insert(0, node) # on the return path, insert in inverse order

    visit(start)

    return result

def iter_grid(grid):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            yield x, y, c

orthogonal = [(0, -1), (0, 1), (-1, 0), (1, 0)]
adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# iterator over orthogonal coords from x and y
# if grid (list of lists) is provided, only coords in bound of the grid will be returned
def iter_orthogonal(x, y, grid=None):
    return iter_neighbours(orthogonal, x, y, grid=grid)

# iterator over adjacent coords from x and y
# if grid (list of lists) is provided, only coords in bound of the grid will be returned
def iter_adjacent(x, y, grid=None):
    return iter_neighbours(adjacent, x, y, grid=grid)

def iter_neighbours(neighbours, x, y, grid=None):
    for dx, dy in neighbours:
        xx = x + dx
        yy = y + dy
        if grid and in_grid(grid, xx, yy):
            yield xx, yy, grid[yy][xx]    
        elif not grid:
            yield xx, yy

# check if coordinate is in grid. grid is list of lists
def in_grid(grid, x, y):
    return x >= 0 and y >= 0 and y < len(grid) and x < len(grid[y])

# get the value in grid (list of lists). Return default if x, y is out of bounds
def grid_get(grid, x, y, default=None):
    if in_grid(grid, x, y):
        return grid[y][x]
    else:
        return default

# convert grid (list of lists) into a dict (x, y) -> value
def grid_to_dict(grid):
    d = dict()
    for y, row in enumerate(grid):
        for x, v in enumerate(row):
            d[(x, y)] = v
    return d

# maze = [[0, 0], [0, 1]]
# is_neighbour is a predicate to check if one can navigate from one node to
# another
# is_neighbour(current_coord, current_value, neighbour_coord, neighbour_value)
# result in graph of dict of node -> neighbours
#
# Example, maze where false values are navigatable
# maze_to_graph(maze, start, lambda _, __, ___, x: not x)
#
def maze_to_graph(maze, start, is_neighbour):
    q = [start]
    seen = set([start])
    g = defaultdict(list)
    w = len(maze[0])
    h = len(maze)

    while q:
        c = heappop(q)
        cx, cy = c

        for nx, ny, _ in iter_adjacent(cx, cy, maze):
            n = nx, ny

            if is_neighbour(c, maze[cy][cx], n, maze[ny][nx]):
                g[c].append(n)

                if n not in seen:
                    heappush(q, n)
                    seen.add(n)
    return g

# Dijkstra's shortest path for a weighted graph
# graph is a dict of node -> dict of neighbour and weight
# start is the starting node
# end is the target node
# returns tuple of best path and total weight
def dijkstra(graph, start, end):
    best = defaultdict(lambda: maxsize)
    q = [(0, [start])]

    while q:
        cost, path = heappop(q)
        node = path[-1]

        if node == end:
            return path, cost

        for neighbour, neighbour_cost in graph[node].items():
            nc = cost + neighbour_cost

            if nc < best[neighbour]:
                best[neighbour] = nc

                heappush(q, (nc, path + [neighbour]))

# finds a path between start and goal
# graph is dict of node -> neighbours
# node and neighbours are (x, y) tuples, as is start and goal
def astar(graph, start, goal):
    q = [(0, [start])]
    seen = set([start])

    while q:
        cost, path = heappop(q)
        c = path[-1]

        if c == goal:
            return path

        for n in graph[c]:
            if n not in seen:
                priority = cost + 1 + manhattan(n, goal)
                heappush(q, (priority, path + [n]))
                seen.add(n)

# flood fills neighbours in a grid starting from x and y and until the boundary condition is met
# returns the number of cells that was filled
#
# For example, using the grid:
# 0 0 1
# 0 1 0
# 1 0 0
#
# flood_fill(xs, 0, 0, lambda c: c == 1, 2)
#
# will result in
# 2 2 1
# 2 1 0
# 1 0 0
#
# and return 3
def flood_fill(xs, x ,y, boundary, fill_value, neighbours=orthogonal):
    # check that we are in the grid
    if x < 0 or x >= len(xs[0]) or y < 0 or y >= len(xs):
        return 0

    # check if we are on the boundary
    if boundary(xs[y][x]):
        return 0

    # check if we are already filled
    if xs[y][x] == fill_value:
        return 0

    # fill
    xs[y][x] = fill_value
    s = 1

    # attempt to fill the neighboring positions
    for dx, dy in neighbours:
        s += flood_fill(xs, x + dx, y + dy, boundary, fill_value)

    return s

# transposes a list of lists, e.g. [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
def transpose(xs):
    return list(map(list, zip(*xs)))

# returns all transpositions of a list of lists, that is, all rotations and mirrored versions
# e.g. ["12", "34"] => [["12", "34"], ["21", "43"], ["34", "12"], ["43", "21"], ["13", "24"], ["31", "42"], ["24", "13"], ["42", "31"]]
# if the input is a list of strings, a list of strings will be returned. same for tuples
def transpositions(xs):
    ts = []
    # rows
    for ystep in [1, -1]:
        for xstep in [1, -1]:
            ts.append([row[::xstep] for row in xs[::ystep]])

    is_strings = type(xs[0]) == str
    is_tuples = type(xs[0]) == tuple
    # columns
    for ystep in [1, -1]:
        for xstep in [1, -1]:
            out = []
            for cols in list(zip(*xs))[::ystep]:
                cols = cols[::xstep]
                if is_strings:
                    cols = "".join(cols)
                elif is_tuples:
                    cols = tuple(cols)
                out.append(cols)
            ts.append(out)

    return ts

# check(i), return True if i is too large
# returns the largest value where check is false, and the smallest where check
# is true (just to remember to think about the one-off :)
def binary_search(lo, hi, check):
    blo = check(lo)
    bhi = check(hi)
    if blo == bhi:
        assert False, "lo and hi both %s" % blo

    while True:
        x = (lo + hi) // 2
        if check(x):
            if not check(x-1):
                return (x-1, x)
            hi = x
        else:
            lo = x

# Simple memoize implementation, use with @Memoize
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        #Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]

# Maths

# least common multiple
def lcm(*args):
    if len(args) == 2:
        a, b = args
        return abs(a*b) // gcd(a, b)
    elif len(args) > 2:
        return reduce(lcm, args)

# find the smallest number x, such that x % n = a for each n and a in nx, ax
# ax thus is a list of mod remainders
# note that remainders in ax should be negative
#
# Adapted from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(nx, ax):
    prod = product(nx)

    s = 0
    for n, a in zip(nx, ax):
        p = prod // n

        s += a * mul_inv(p, n) * p

    return s % prod

# return x, such that (a * x) % m == 1, 0 <= x <= m
def mul_inv(a, m):
    m0 = m
    x0, x1 = 0, 1

    if m == 1:
        return 1

    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += m0

    return x1

# for a dict where values are list of possible options, this will reduce that down to the one unique option for each item.
# for example, given a dict of:
# {
#   0: [1, 2, 3],
#   1: [2],
#   2: [2, 3]
# }
#
# will give:
# {
#   0: 1,
#   1: 2,
#   2: 3
# }
#
# keys can be any value
#
# this function assumes that all options can be trivially assigned. if that's not the case, look at max_bipartite_matching below.
#
# keeping this one around since it might be easier to reason about or to modify
def reduce_unique_options(d):
    def car(xs):
        return next(iter(xs))

    d = deepcopy(d)

    def all1(xs):
        return all(len(x) == 1 for x in xs)

    # reduce by looking at cases where there is only one available option. do this until only one remain for each
    while not all1(d.values()):
        for v in d.values():
            if len(v) == 1:

                vvv = car(v)

                # delete from all values, except self
                for k, vv in d.items():
                    if vv != v:
                        d[k] = safe_remove(vvv, vv)

    return {k:car(v) for k, v in d.items()}

# max bipartite matching
# takes a graph of thing => possible options and find the best matching of each thing => option
# this code uses an example of job applicants => open jobs, and returns the best matching of applicant => job
# if an applicant can't be assigned to a job, it will not be included in the output
#
# based on https://www.geeksforgeeks.org/maximum-bipartite-matching/
def max_bipartite_matching(graph):

    jobs = set.union(*[set(v) for v in graph.values()])

    # a dict of job => applicant, to keep track of the applicants assigned to jobs
    assignments = dict()

    # a DFS based recursive function that returns true if an assignment for job is possible
    def bpm(applicant, seen=set()):

        # Try every job one by one, except those already seen
        for job in jobs - seen:
            # if applicant is interested in job
            if job in graph[applicant]:
                # mark job as seen
                seen.add(job)

                # if job is not assigned to an applicant OR previously assigned applicant for job has an alternate job available.
                # since job is marked as seen in the above line, assignments[job] in the following recursive call will not get job again
                if job not in assignments or bpm(assignments[job], seen):
                    assignments[job] = applicant
                    return True
        return False

    # for each applicant
    for applicant in graph.keys():
        # try to assign a job to the applicant
        bpm(applicant)

    # find it easier to get the result in the same way as the input,
    # so return a dict of who gets assigned to which job by inversing the assignments
    return {v:k for k, v in assignments.items()}

# hex stuff
# https://www.redblobgames.com/grids/hexagons/#coordinates-cube

# hex adjecent 3D cubes with east-west orientation
hex_adjacent_ew = {
    "e": (1, 0, -1),
    "w": (-1, 0, 1),
    "se": (0, 1, -1),
    "nw": (0, -1, 1),
    "ne": (1, -1, 0),
    "sw": (-1, 1, 0)
}

# hex adjecent 3D cubes with north-south orientation
hex_adjacent_ns = {
    "n": (0, -1, 1),
    "s": (0, 1, -1),
    "se": (1, 0, -1),
    "nw": (-1, 0, 1),
    "ne": (1, -1, 0),
    "sw": (-1, 1, 0)
}

# Span, a range of integers
class Span:
    # start and end inclusive
    def __init__(self, start, end):
        if end < start:
            raise Exception("end must be larger or equal to start")

        self.start = start
        self.end = end

    # does this span fully contain either an integer or another span?
    def __contains__(self, other):
        if type(other) == int:
            return self.start <= other <= self.end
        elif type(other) == Span:
            return other.start >= self.start and other.end <= self.end

    # does this span equal the other span?
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    # does this span intersect/overlap the other span?
    def intersects(self, other):
        return other.start in self or other.end in self or self.start in other or self.end in other

    # get the intersection of two span, e.g. 1..12 & 0..3 -> 1..3
    # returns None if the spans do not intersect
    def __and__(self, other):
        if self.intersects(other):
            return Span(max(self.start, other.start), min(self.end, other.end))
        else:
            return None

    # get the union of two intersecting spans, e.g. 1..12 & 0..3 -> 0..12
    # returns None if the spans do not intersect
    def __or__(self, other):
        if self.intersects(other):
            return Span(min(self.start, other.start), max(self.end, other.end))
        else:
            return None

    # get the length of the span
    def __len__(self):
        return self.end - self.start + 1

    # get the span as a range
    def range(self):
        return range(self.start, self.end + 1)

    # get the span as a set of integers
    def set(self):
        return set(self.range())

    def __repr__(self):
        return "%s..%s" % (self.start, self.end)

    def __bool__(self):
        return True
