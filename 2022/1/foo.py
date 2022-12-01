import sys

xs = sys.stdin.read().split("\n\n")
s = sorted(sum(map(int, x.split())) for x in xs)

print(max(s))
print(sum(s[-3:]))