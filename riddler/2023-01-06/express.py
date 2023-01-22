from itertools import count
from functools import cache

# return lists of ways for 2 and 3 to sum to n, in order
@cache
def foo(n):
    if n < 2:
        return []
    if n == 2:
        return [[2]]
    if n == 3:
        return [[3]]

    return [l + [2] for l in foo(n - 2) if 3 not in l] + [l + [3] for l in foo(n - 3)]

for n in count(61):
    if len(foo(n)) < len(foo(60)):
        print(n)
        break
