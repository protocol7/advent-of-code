import sys

target = int(sys.stdin.read().strip())

def foo(x):
    if len(x) >= len(str(target)):
        n = int(x)
        return int(n <= target)

    if x:
        start = int(x[-1])
    else:
        start = 0

    return sum(foo(x + str(i)) for i in range(start, 10))

print(foo(""))