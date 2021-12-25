import sys

print(sum(sum(map(int, x)) % 2 == 0 for x in sys.stdin.read().split("\n")))