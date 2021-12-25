import sys

for x in sys.stdin.read().split("\n"):
    x = list(map(int, x))

    if x[0] + x[1] == x[2] + x[3] == x[4] + x[5]:
        print("".join(map(str, x)))