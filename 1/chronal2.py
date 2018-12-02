import sys
from itertools import cycle

seen = set()
total = 0
for line in cycle(list(sys.stdin)):
    total += int(line)

    if total in seen:
        print(total)
        break

    seen.add(total)
