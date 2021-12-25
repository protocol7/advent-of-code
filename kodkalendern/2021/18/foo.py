import sys

for x in sys.stdin.read().split("\n"):
    if len(x) == len(set(x)):
        print(x)
