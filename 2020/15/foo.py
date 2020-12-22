import sys

start = [0, 13, 1, 16, 6, 17]
rounds = int(sys.argv[1])

last = dict()
for i, n in enumerate(start[:-1]):
    last[n] = i + 1

spoken = start[-1]

for turn in range(len(start) + 1, rounds + 1):
    l = last.get(spoken)
    last[spoken] = turn - 1

    if l is None:
        spoken = 0
    else:
        spoken = turn - 1 - l

print(spoken)