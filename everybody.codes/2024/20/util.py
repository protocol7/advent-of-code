from collections import deque, defaultdict
from copy import deepcopy
from heapq import heappush, heappop
from re import findall
from itertools import chain, islice
from functools import reduce
from math import gcd, prod
from sys import maxsize
import collections

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

# includes from a list until the predicate it true, including the first element that matches
# takeuntil(lambda x: x == 3, [1, 2, 3, 3, 4]) == [1, 2, 3]
def takeuntil(predicate, xs):
    out = []
    for x in xs:
        out.append(x)

        if predicate(x):
            break
    return out

# joins a list into a string
def join(xs):
    return "".join(xs)

# get the only item in the collection, useful for getting items out of single item sets
# asserts that the collection only has one item
def item(xs):
    #if isinstance(xs, collections.Iterable):
    if hasattr(xs, '__next__'):
        out = next(xs)
        assert next(xs, None) is None
        return out
    else:
        assert len(xs) == 1
        return list(xs)[0]

# apply the aggregate function to each item for the lists in xs, return a list of the same length as each item in xs
#
# agg_each([[1, 2, 4], [3, 1, 7]], max) -> [3, 2, 7]
def agg_each(xs, agg):
    def f(*xx):
        return [agg(a, b) for a, b in zip(*xx)]

    return reduce(f, xs)

# return the max for each item for the lists in xs
#
# max_each([[1, 2], [3, 1]]) -> [3, 2]
def max_each(xs):
    return agg_each(xs, max)

# return the min for each item for the lists in xs
#
# min_each([[1, 2], [3, 0]]) -> [1, 0]
def min_each(xs):
    return agg_each(xs, min)

# return a list of numbers in the range a..b (inclusive), independent on a or b is the smallest
#
# diffrange(1, 3) -> [1, 2, 3]
# diffrange(3, 1) -> [3, 2, 1]
# diffrange(1, 1) -> [1]
def diffrange(a, b):
    if a < b:
        return list(range(a, b+1))
    elif a > b:
        return list(range(a, b-1, -1))
    else:
        return [a]

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

# A list that wraps around
class CircularList:
    def __init__(self, xs):
        assert type(xs) == list
        self.xs = xs

    # pop an item from the list, index will wrap around
    def pop(self, i):
        return self.xs.pop(i % len(self.xs))

    # insert an item into the list before the index, index will wrap around
    def insert(self, i, item):
        self.xs.insert(i % len(self.xs), item)

    # move the item at index i by steps, can be both positive and negative. wraps around
    def move_by(self, i, steps):
        item = self.pop(i)

        self.insert(i + steps, item)

    def append(self, item):
        self.xs.append(item)

    # move the item at index i to the new_i position. wraps around, for negative new_i it will move the item before the new_i
    # [1, 2, 3, 4].move_to(0, 1) -> [2, 1, 3, 4]
    # [1, 2, 3, 4].move_to(0, 5) -> [2, 1, 3, 4]
    # [1, 2, 3, 4].move_to(0, -1) -> [2, 3, 1, 4]
    def move_to(self, i, new_i):
        item = self.pop(i)
        self.insert(new_i, item)

    # rotate the list by some number of items
    # [1, 2, 3, 4].rotate(1) -> [2, 3, 4, 1]
    # [1, 2, 3, 4].rotate(-1) -> [4, 1, 2, 3]
    def rotate(self, by):
        by = by % len(self.xs)
        self.xs = self.xs[by:] + self.xs[:by]

    def __repr__(self):
        return str(self.xs)

    def __iter__(self):
        return iter(self.xs)

    def __len__(self):
        return len(self.xs)

    def __getitem__(self, i):
        return self.xs[i % len(self.xs)]

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
        arg, = args
        if type(arg) == tuple or type(arg) == Point:
            ax, ay = arg
            bx, by = 0, 0
        else:
            assert False
    elif len(args) == 2:
        if type(args[0]) == tuple or type(args[0]) == Point:
            (ax, ay), (bx, by) = args
        else:
            ax, ay = args
            bx, by = 0, 0
    elif len(args) == 4:
        ax, ay, bx, by = args
    return abs(ax - bx) + abs(ay - by)


# predicate equals function, useful for e.g. matching exact results in BFS
def equals(x):
    return lambda y: x == y

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
# end is the target node, or a predicate function
# returns path from start to end
def bfs(graph, start, end):
    if type(start) == list:
        # multiple starting locations, wrap each in a path list
        start = [[x] for x in start]
    else:
        # single starting location, wrap in a path list
        start = [[start]]

    if callable(end):
        end_fn = end
    else:
        end_fn = lambda x: x == end

    q = deque(start)
    seen = set()

    while q:
        path = q.popleft()
        v = path[-1]
        for n in graph[v]:
            p = path + [n]
            if end_fn(n):
                return p
            if n not in seen:
                q.append(p)
                seen.add(n)

# return all paths between start and end
# graph is dict of node -> neighbours
# end is the target node, or a predicate function
# returns list of paths from start to end
def bfs_all_paths(graph, start, end, cyclic=False):
    q = deque([[start]])
    paths = []

    if callable(end):
        end_fn = end
    else:
        end_fn = lambda x: x == end

    while q:
        path = q.popleft()
        v = path[-1]
        for n in graph[v]:
            if cyclic and n in path:
                continue

            p = path + [n]
            if end_fn(n):
                paths.append(p)
            else:
                q.append(p)
    return paths

def dfs(graph, node, end, paths, path):
    path = path + [node]

    if callable(end):
        end_fn = end
    else:
        end_fn = lambda x: x == end

    if end_fn(node):
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

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def turn_left(dir):
    if dir == RIGHT:
        return UP
    elif dir == UP:
        return LEFT
    elif dir == LEFT:
        return DOWN
    elif dir == DOWN:
        return RIGHT
    else:
        assert False

def turn_right(dir):
    if dir == RIGHT:
        return DOWN
    elif dir == UP:
        return RIGHT
    elif dir == LEFT:
        return UP
    elif dir == DOWN:
        return LEFT
    else:
        assert False

ORTHOGONAL = [UP, DOWN, LEFT, RIGHT]

N = (0, -1)
NE = (1, -1)
E = (1, 0)
SE = (1, 1)
S = (0, 1)
SW = (-1, 1)
W = (-1, 0)
NW = (-1, -1)

ADJACENT = [N, NE, E, SE, S, SW, W, NW]

ORTHOGONAL_3D = [(0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1)]

# Dijkstra's shortest path for a weighted graph
# graph is a dict of node -> dict of neighbour and weight
# start is the starting node
# end is the target node, or a predicate function
# returns tuple of best path and total weight
def dijkstra(graph, start, end):
    best = defaultdict(lambda: maxsize)
    q = [(0, [start])]

    if callable(end):
        end_fn = end
    else:
        end_fn = lambda x: x == end

    while q:
        cost, path = heappop(q)
        node = path[-1]

        if end_fn(node):
            return path, cost

        for neighbour, neighbour_cost in graph[node].items():
            nc = cost + neighbour_cost

            if nc < best[neighbour]:
                best[neighbour] = nc

                heappush(q, (nc, path + [neighbour]))

# finds a path between start and goal
# graph is dict of node -> neighbours
# node and neighbours are (x, y) tuples, as is start and goal
def astar(graph, start, end):
    q = [(0, [start])]
    seen = set([start])

    if callable(end):
        end_fn = end
    else:
        end_fn = lambda x: x == end

    while q:
        cost, path = heappop(q)
        c = path[-1]

        if end_fn(c):
            return path

        for n in graph[c]:
            if n not in seen:
                priority = cost + 1 + manhattan(n, end)
                heappush(q, (priority, path + [n]))
                seen.add(n)

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
# return None if unable to find a result
def binary_search(lo, hi, check):
    blo = check(lo)
    bhi = check(hi)
    if blo == bhi:
        assert False, "lo and hi both %s" % blo

    while True:
        if lo == hi:
            # no result
            return None

        x = (lo + hi) // 2
        if check(x):
            if not check(x-1):
                return (x-1, x)
            hi = x
        else:
            lo = x


# bit functions
# to use these for a BitSet, you would start with b = 0 for the empty set,
# and use set/unset to manage the members of the set

# set a bit
def bit_set(b, i):
    return b | (1 << i)

# unset a bit
def bit_unset(b, i):
    return b & ~(1 << i)

# test if a bit is set
def bit_test(b, i):
    return b & 1 << i

# flip a bit
def bit_flip(b, i):
    return b ^ (1 << i)

# flip all bits
def bit_flip_all(b):
    return ~b

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

# Interval, a range of integers
class Interval:
    # start and end inclusive
    def __init__(self, start, end):
        if end < start:
            raise Exception("end must be larger or equal to start")

        self.start = start
        self.end = end

    # does this interval fully contain either an integer or another interval?
    def __contains__(self, other):
        if type(other) == int:
            return self.start <= other <= self.end
        elif type(other) == Interval:
            return other.start >= self.start and other.end <= self.end

    # does this interval equal the other interval?
    def __eq__(self, other):
        if other is None:
            return False

        return self.start == other.start and self.end == other.end

    # does this interval intersect/overlap the other interval?
    def intersects(self, other):
        return other.start in self or other.end in self or self.start in other or self.end in other

    # get the intersection of two intervals, e.g. 1..12 & 0..3 -> 1..3
    # returns None if the intervals do not intersect
    def __and__(self, other):
        if self.intersects(other):
            return Interval(max(self.start, other.start), min(self.end, other.end))
        else:
            return None

    # get the union of two intersecting or adjacent intervals, e.g.
    # 1..12 & 0..3 -> 0..12
    # 1..12 & 13..15 -> 0..15
    # returns None if the intervals do not intersect
    def __or__(self, other):
        if self.intersects(other):
            return Interval(min(self.start, other.start), max(self.end, other.end))
        elif abs(self.start - other.end) < 2 or abs(self.end - other.start) < 2:
            # adjacent
            return Interval(min(self.start, other.start), max(self.end, other.end))
        else:
            return None

    # get the length of the interval
    def __len__(self):
        return self.end - self.start + 1

    def __iter__(self):
        return iter(self.range())

    # get the interval as a range
    def range(self):
        return range(self.start, self.end + 1)

    # get the interval as a set of integers
    def set(self):
        return set(self.range())

    def __repr__(self):
        return "%s..%s" % (self.start, self.end)

    def __bool__(self):
        return True

    def __lt__(self, other):
        if self.start < other.start:
            return True
        elif self.start > other.start:
            return False
        elif self.end < other.end:
            return True
        else:
            return False

# A set of intervals, merged when possible
class Intervals:

    def __init__(self, intervals=[]):
        assert type(intervals) == list

        self.intervals = sorted(intervals)

    # add an interval. will attempt to merge with existing intervals, including adjacent intervals
    # [1..2, 4..5].add(7..8) -> [1..2, 4..5, 7..8]
    # [1..2].add(3..4) -> [1..4]
    def add(self, interval):
        ni = []
        for other in self.intervals:
            u = interval | other

            if u:
                interval = u
            else:
                ni.append(other)

        ni.append(interval)

        self.intervals = sorted(ni)

    # return a new Intervals that is intersected with the provided interval
    # [1..2, 4..5] & 2..5 -> [2..2, 4..5]
    # [1..2, 4..5] & 3..5 -> [4..5]
    # [1..2, 4..5] & 3..4 -> [4..4]
    # [1..2, 4..5] & 98..99 -> []
    def __and__(self, interval):
        ni = []
        for other in self.intervals:
            i = other & interval

            if i:
                ni.append(i)

        return Intervals(ni)

    def __repr__(self):
        return str(self.intervals)

    def __iter__(self):
        return iter(self.intervals)

    def __len__(self):
        return len(self.intervals)

    def __getitem__(self, i):
        return self.intervals[i]



# class representing a point in a grid
class Point:
    @staticmethod
    def wrap(point):
        if type(point) == Point:
            return point
        else:
            return Point(point)

    def __init__(self, *args):
        if len(args) == 1:
            arg = args[0]
            if type(arg) == Point:
                self.x = arg.x
                self.y = arg.y
            elif type(arg) == tuple:
                self.x, self.y = arg
            else:
                assert False
        elif len(args) == 2:
            self.x, self.y = args
        else:
            assert False

    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        else:
            return self.y < other.y

    def __eq__(self, other):
        if type(other) == Point:
            return self.x == other.x and self.y == other.y
        elif type(other) == tuple:
            ox, oy = other
            return self.x == ox and self.y == oy
        else:
            assert False

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        return iter((self.x, self.y))

    # point + other_point
    # point + (1, 2)
    def __add__(self, other):
        if type(other) == tuple:
            dx, dy = other
            return Point(self.x + dx, self.y + dy)
        else:
            assert False


# a line defined by two points
class Line:
    @staticmethod
    def from_points(p1, p2):
        return Line(p1, p2)

    @staticmethod
    def from_point_and_delta(p, dx, dy):
        p = Point(p)
        return Line(p, (p.x + dx, p.y + dy))

    def __init__(self, p1, p2):
        self.p1 = Point(p1)
        self.p2 = Point(p2)

    # Find the intersection of two lines, e.g.
    # Line((0, 0), (10, 10)).intersection(Line((10, 0), (0, 10))) -> Point(5, 5)
    #
    # Returns None if lines don't intersect

    def intersection(self, other) -> Point:
        l1 = tuple(self.p1), tuple(self.p2)
        l2 = tuple(other.p1), tuple(other.p2)
        (x0, y0), (x1, y1) = l1
        (x2, y2), (x3, y3) = l2

        xdiff = (x0 - x1, x2 - x3)
        ydiff = (y0 - y1, y2 - y3)

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            return None

        d = (det(*l1), det(*l2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return Point(x, y)


# a grid starting at (0, 0)
class Grid:
    def __init__(self, grid):
        if type(grid) == dict:
            self.d = grid
        elif type(grid) == set:
            self.d = {Point.wrap(p): True for p in grid}
        elif type(grid) == list:
            self.d = {}
            for y, row in enumerate(grid):
                for x, c in enumerate(row):
                    self.d[Point(x, y)] = c
        else:
            assert False, grid

        self._min = min_each(self.d.keys())
        self._max = max_each(self.d.keys())

    # return min and max x coordinates (might not be )
    def min(self):
        return self._min

    def max(self):
        return self._max

    # return points with values, unordered
    def points(self):
        return list(self.d.items())

    def __iter__(self):
        return iter(self.d.keys())

    # return dict of value -> points
    def points_by_value(self):
        out = defaultdict(list)
        for p, v in self.d.items():
            out[v].append(p)
        return out

    # get the value at a point in the grid. None if the point is outside the grid or if not set in a sparse grid
    def __getitem__(self, point):
        return self.d.get(Point.wrap(point))

    # does the grid contain this point? assumes grid starts at (0, 0)
    def __contains__(self, point):
        return Point.wrap(point) in self.d

    def rows(self):
        class GridRow:
            def __init__(self, grid, y):
                self.grid = grid
                self.y = y

            def __iter__(self):
                return iter((Point(x, self.y), self.grid[(x, self.y)]) for x in range(self.grid._min[0], self.grid._max[0] + 1))

            def __getitem__(self, x):
                return self.grid.d.get(Point(x, self.y))

            def __repr__(self):
                row = ""
                for x in range(self.grid._min[0], self.grid._max[0]+1):
                    v = self.grid.d.get((x, self.y))
                    if v is not None:
                        row += str(v)[:1]
                    else:
                        row += "."
                return row

        for y in range(self._min[1], self._max[1] + 1):
            yield GridRow(self, y)

    # return a list of points and values from the provided point (not inclduing), in the direction given, e.g.
    # grid.direction((0, 0), (0, 1)) -> [((0, 1), 7), ((0, 2), 8), ((0, 3), 9)]
    def ray(self, point, direction):
        p = Point.wrap(point) + direction
        out = []
        while p in self:
            out.append((p, self[p]))
            p += direction

        return out

    # list neighbouring points around the provided point, including those outside the grid (with value as None)
    # returns a list of (point, value)
    def neighbours(self, point, neighbours):
        point = Point.wrap(point)
        return [(point + n, self[point + n]) for n in neighbours]

    # list orthogonal points around the provided point, including those outside the grid (with value as None)
    # returns a list of (point, value)
    def orthogonal(self, point):
        return self.neighbours(point, ORTHOGONAL)

    # list adjacent points around the provided point, including those outside the grid (with value as None)
    # returns a list of (point, value)
    def adjacent(self, point):
        return self.neighbours(point, ADJACENT)

    # return the grid is a dict of point -> value
    def to_dict(self):
        return dict(self.d)

    # return a list of lists
    def to_grid(self):
        grid = []
        minx, miny = self.min()
        maxx, maxy = self.max()

        for y in range(miny, maxy+1):
            row = [self[(x, y)] for x in range(minx, maxx+1)]
            grid.append(row)
        return grid

    # grid is considered as a maze where one can navigate from each point based on a predicate
    # start is the starting point, or a list of possible starting points
    # is_neighbour is the predicate to check if one can navigate from one point to another
    #
    # is_neighbour(current_coord, current_value, neighbour_coord, neighbour_value)
    # result in graph of dict of node -> neighbours
    #
    # Example, maze where true values are navigatable
    # grid.maze_to_graph((0, 0), lambda _, __, ___, x: x)
    def to_graph(self, start, is_neighbour, neighbours=ORTHOGONAL):
        if type(start) == list:
            q = [Point(s) for s in start]
        else:
            q = [Point(start)]

        seen = set(q)
        g = defaultdict(list)

        while q:
            p = heappop(q)

            for n, _ in self.neighbours(p, neighbours):
                if is_neighbour(p, self[p], n, self[n]):
                    g[p].append(n)

                    if n not in seen:
                        heappush(q, n)
                        seen.add(n)
        return g

    # flood fills neighbours in the grid starting from x and y and until the boundary condition is met
    # returns the number of cells that was filled
    #
    # For example, using the grid:
    # 0 0 1
    # 0 1 0
    # 1 0 0
    #
    # g.flood_fill((0, 0), lambda c: c == 1, 2)
    #
    # will result in
    # 2 2 1
    # 2 1 0
    # 1 0 0
    #
    # and return 3
    def flood_fill(self, point, boundary, fill_value, neighbours=ORTHOGONAL):
        q = deque([Point(point)])

        s = 0
        while q:
            point = q.popleft()

            # check that we are in the grid
            if point not in self:
                continue

            # check if we are on the boundary
            if boundary(self.d[point]):
                continue

            # check if we are already filled
            if self.d[point] == fill_value:
                continue

            # fill
            self.d[point] = fill_value
            s += 1

            # attempt to fill the neighboring positions
            for n in neighbours:
                q.append(point + n)

        return s

    # prints the grid, taking the first character from the value for each cell
    def pretty_print(self):
        for row in self.rows():
            print(row)
