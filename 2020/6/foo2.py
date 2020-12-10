import sys

ans = sys.stdin.read().split("\n\n")

print(sum(len(set.intersection(*[set(x) for x in a.split()])) for a in ans))