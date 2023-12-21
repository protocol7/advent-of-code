import sys
from itertools import count
from util import ORTHOGONAL

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

def find_start(xs):
    for y, row in enumerate(xs):
        for x, c in enumerate(row):
            if c == "S":
                return x, y

sx, sy = find_start(xs)

w = len(xs[0])

# assume the map is square
assert w == len(xs)

N = 26501365

pos = set([(sx, sy)])
ps = []

for i in count(1):
    npos = set()

    for x, y in pos:
        for dx, dy in ORTHOGONAL:
            nx = x + dx
            ny = y + dy

            c = xs[ny % w][nx % w]

            if c == "#":
                continue

            npos.add((nx, ny))

    pos = npos

    if i % w == N % w:
        ps.append(len(pos))

    # we need three values to solve the equations below
    if len(ps) == 3:
        break


# N is 202300 * 131 + 65. Thus, each 131 iteration (with 65 offset) we reach a stable state. We here call these rounds.
#
# the grid forms a repeating set of rhombuses of two types, here called O (the one we start in) and P
# (made up by the four corners in the input).
# these will form an infinite map where we expand to a super rhombus for each of the 202300 round,
# looking something like this after 0 rounds:
#
#     O
#
# after 1 round:
#     O
#    P P
#   O O O
#    P P
#     O
#
# after two rounds:
#     O
#    P P
#   O O O
#  P P P P
# O O O O O
#  P P P P
#   O O O
#    P P
#     O
#
# O's and P's will be of two parities depending on odd and even iterations, looking like:
#     b
#    c d
#   b a b
#  c d c d
# b a b a b
#  d c d c
#   b a b
#    d c
#     b
#
# there's the same number of c and d, so we can treat them as one and use the number of positions in c and d together.
#
# The number of a, b, c (which here is c + d)  type rhombuses is (figured out by looking at the actual output):
# na = rounds**2
# nb = (rounds + 1)**2
# nc = (rounds * (rounds + 1)  # each of c and d is a triangular number, n * (n - 1) / 2
#
# thus the equation for the total number of positions after a round is (a, b and c are the number of positions in those
# types of rhombuses and parities):
# na * a + nb * b + nc * c
#
# or:
# rounds**2 * a + (rounds+1)**2 * b + (rounds * (rounds + 1)) * c


# these are the number of positions after round 0, 1 and 2:
p0, p1, p2 = ps

# with these, we can set up a set of equations for the number of positions in a, b anc c type rhombuses:
# 0 * a + 1 * b + 0 * c = p0 -> b = p0
# 1 * a + 4 * b + 2 * c = p1
# 4 * a + 9 * b + 6 * c = p2
#
# solving for a, b and c we get:

b = p0

c = p1 * 2 - 8 * b - (p2 - 9 * b) // 2

a = p1 - 4 * b - 2 * c

# now we can put this back into the equation for the total number of positions, at round 202300

rounds = N // 131

print(rounds**2 * a + (rounds+1)**2 * b + (rounds * (rounds + 1)) * c)

# during the actual solve, I instead used quadratic equation as a bit of a gamble, fitting on p0, p1 and p2. putting these into Wolfram Alpha:
# https://www.wolframalpha.com/input?i=quadratic+fit+calculator&assumption=%7B%22F%22%2C+%22QuadraticFitCalculator%22%2C+%22data%22%7D+-%3E%22%7B3676%2C+32808%2C+90974%7D%22
#
# gives the following equation:
# 14517 x^2 - 14419 x + 3578
# Wolfram solves this for x=1, 2, 3 etc, so here we add one on the round we're targeting

print(14517 * (rounds + 1)**2 - 14419 * (rounds + 1) + 3578)
