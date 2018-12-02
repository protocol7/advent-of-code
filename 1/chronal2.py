import sys
from itertools import cycle

print("Hello world")

lines = cycle(list(sys.stdin))

seen = set()
total = 0
for line in lines:
    total = total + int(line)

    if total in seen:
        print(total)
        break

    seen.add(total)
