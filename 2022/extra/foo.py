import sys
from string import ascii_uppercase

# https://www.reddit.com/r/adventofcode/comments/zv4ixy/my_daughter_made_me_my_own_advent_of_code/

xs = sys.stdin.read().strip()

s = ""
for a, b in zip(xs, xs[1:]):
    if a in (ascii_uppercase + "-") and a == b:
        s += a

print(s)

s = ""
for a, b in zip(xs, xs[1:]):
    if a.isdigit() and a == b:
        s += a

print(s)
