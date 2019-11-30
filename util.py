from collections import deque
from itertools import chain, imap
from heapq import heappush, heappop

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def manhattan(*args):
    if len(args) == 2:
        (ax, ay), (bx, by) = args
    elif len(args) == 4:
        ax, ay, bx, by = args
    return abs(ax - bx) + abs(ay - by)

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


adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# maze = [[0, 0], [0, 1]]
def astar(maze, start, goal):
    q = [(0, [start])]
    seen = set([start])

    while q:
        cost, path = heappop(q)
        c = path[-1]

        if c == goal:
            return path

        cx, cy = c
        for dx, dy in adjacent:
            n = cx + dx, cy + dy
            nx, ny = n

            if nx < 0 or ny < 0 or nx >= len(maze[0]) or ny >= len(maze):
                continue

            if not maze[ny][nx]:
                if n not in seen:
                    priority = cost + 1 + manhattan(n, goal)
                    heappush(q, (priority, path + [n]))
                seen.add(n)
