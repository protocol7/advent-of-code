import sys

print(sum(1 for _ in (filter(lambda x: 2000 <= x <= 3000, [int(line.strip()) * 28 for line in sys.stdin.readlines()]))))

