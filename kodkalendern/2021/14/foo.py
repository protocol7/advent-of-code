import sys

A = "abcdefghijklmnopqrstuvwxyzåäö"

for i, x in enumerate(sys.stdin.read().split("\n"), 1):
    print("".join(A[A.index(c) - i] for c in x))
