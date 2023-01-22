from itertools import count
from functools import cache
from collections import deque

H = 100 * 24
A = 6 * 24
S = 1

# insight: no use building ships before assemblers in an assembler
# so, how many assemblers to build before switching to spaceships?

# we can do 16 (16*6 == 96) turns of building assembers, and will then have 4 days of only building ships

# given turns remaining, how many spaceships can we build?
def foo(turns, a, s, cache):
    k = (turns, a)
    if k in cache:
        return cache[k]

    if turns == 0:
        # 4 days remain after the last round
        return a * 24 * 4 + s

    ms = s
    for assemblers_building_assemblers in range(a+1):
        assemblers_building_ships = a - assemblers_building_assemblers

        ns = foo(turns-1, a + assemblers_building_assemblers, s + assemblers_building_ships * A, cache)

        ms = max(ms, ns)

    cache[k] = ms
    return ms

print(foo(16, 1, 0, {}))