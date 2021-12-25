import sys

A = "abcdefghijklmnopqrstuvwxyzåäö"

for x in sys.stdin.read().split("\n"):
    if sum(A.index(c) + 1 for c in x) == 133:
        print(x)