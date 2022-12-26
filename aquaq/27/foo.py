import sys
from collections import *
from itertools import *
from util import *

def parse(line):
    return line.strip("\n")

xs = list(map(parse, sys.stdin))

w = len(xs[0])
h = len(xs)

g = {}
for y, row in enumerate(xs):
    for x, c in enumerate(row):
        if c != " ":
            g[Point(x, y)] = c

g = Grid(g)

def follow_snake(g, pos):
    seen = set()

    words = []

    word = ""
    last_pos = None
    last_dir = None
    while True:
        seen.add(pos)

        if last_pos is None:
            word += g[pos]
            dir = None
        else:
            # same direction?
            dir = (pos.x - last_pos.x, pos.y - last_pos.y)
            if last_dir is None or dir == last_dir:
                word += g[pos]
            else:
                # new direction
                words.append(word)
                word = word[-1] + g[pos]
        last_pos = pos
        last_dir = dir

        # find next unwalked neighbour
        found = False
        for np, _ in g.orthogonal(pos):
            if np in g and np not in seen:
                found = True
                pos = np

        # there was no unwalked neighbour, we're at the end of the snake
        if not found:
            # at end
            words.append(word)
            return words

# points for a word
def points(word):
    s = 0
    for c in word:
        s += ord(c) - ord("a") + 1

    return s * len(word)

# find snake starts
words = []
for p in g:
    n = 0

    for np, _ in g.orthogonal(p):
        if np in g:
            n += 1

    if n == 1:
        words.extend(follow_snake(g, p))

# half as we find snakes in both directions
print(sum(points(word) for word in words) // 2)