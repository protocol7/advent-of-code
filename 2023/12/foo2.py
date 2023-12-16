import sys
from util import ints
from functools import cache


def parse(line):
    a, b = line.strip().split()
    return a, tuple(ints(b))


xs = list(map(parse, sys.stdin))

xs = [("?".join([ss] * 5), gs * 5) for ss, gs in xs]

@cache
# given a pattern string and some groups, how many matches are there?
def foo(ss, gs):
    if len(gs) == 0:
        return "#" not in ss

    g = gs[0]
    ngs = tuple(gs[1:])

    n = 0
    # scan ss for possible places the group can match in the range i:i+g
    for i in range(len(ss)):
        # if there is a broken spring before i, we are done scanning
        prefix = ss[:i]
        if "#" in prefix:
            break

        pattern = ss[i:i+g]
        suffix = ss[i+g:]

        # validate that the group matches
        # * the string matched must be all # or ?
        # * the next spring after the matches string must not be #
        if len(pattern) == g and "." not in pattern and (not suffix or suffix[0] != "#"):
            # search the remainder for the remaining groups
            n += foo(ss[i+g+1:], ngs)

    return n

t = 0
for ss, gs in xs:
    t += foo(ss, gs)

print(t)
