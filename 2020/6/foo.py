import sys

ans = sys.stdin.read().split("\n\n")

print(sum(len(set(a.replace("\n", ""))) for a in ans))