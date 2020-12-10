from collections import deque, defaultdict
from heapq import heappush, heappop
from re import findall
from itertools import chain
from math import gcd

def flatmap(f, items):
    return list(chain.from_iterable(map(f, items)))

# get digit as position n from an int
def digit(number, n):
    return number // 10**n % 10

# partition a list into chunks of lenght n
def chunks(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]

def pairs(xs):
    return chunks(xs, n)

# find all ints, including negative ones, in a string
def ints(s):
    return list(map(int, findall(r"-?\d+", s)))

# finds all simple strings and digits, including negative ints
def tokens(s):
    return findall(r"[A-Za-z0-9\-]+", s)

# is this string an int?
def isint(s):
    return s.isdigit() or (s and s[0] in ('+', '-') and s[1:].isdigit())

# make ints of everything that looks like one
def intify(xs):
    return [int(x) if isint(x) else x for x in xs]

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

def product(xs):
    p = 1
    for x in xs:
        p *= x
    return p

def sign(i):
    if i > 0:
        return 1
    elif i < 0:
        return -1
    else:
        return 0

# least common multiple
def lcm(*args):
    if len(args) == 2:
        a, b = args
        return abs(a*b) // gcd(a, b)
    elif len(args) > 2:
        return reduce(lcm, args)

def manhattan(*args):
    if len(args) == 1:
        ax, ay = args[0]
        bx, by = 0, 0
    elif len(args) == 2:
        (ax, ay), (bx, by) = args
    elif len(args) == 4:
        ax, ay, bx, by = args
    return abs(ax - bx) + abs(ay - by)

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

adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

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

        for dx, dy in adjacent:
            n = cx + dx, cy + dy
            nx, ny = n

            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue

            if is_neighbour(c, maze[cy][cx], n, maze[ny][nx]):
                g[c].append(n)

                if n not in seen:
                    heappush(q, n)
                    seen.add(n)
    return g

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
