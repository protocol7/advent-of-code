import sys

print(sum("a" in x and "e" in x and not "r" in x and not "t" in x for x in sys.stdin))
