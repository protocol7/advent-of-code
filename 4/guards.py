import sys
from collections import defaultdict
import operator

def parse(line):
    return (int(line[15:17]), line[19:].strip())

# parse into a list of (guard id, no of minutes asleep, list of minutes asleep)
def parse_lines(lines):
    entries = []
    guard = None
    asleep = None
    for line in lines:
        ts, p = parse(line)
        if p.startswith('Guard'):
            guard = int(p.split()[1].strip("#"))
        elif p == "falls asleep":
            asleep = ts
        else:
            entries.append((guard, ts - asleep, range(asleep, ts)))
    return entries

entries = parse_lines(sorted(sys.stdin))

# sum minutes asleep per guard, and sum per minute per guard
spg = defaultdict(int)
minutes = defaultdict(lambda: defaultdict(int))
for e in entries:
    spg[e[0]] += e[1]
    for m in e[2]:
        minutes[e[0]][m] += 1

# get guard with most minutes asleep
sorted_spg = sorted(spg.items(), key=operator.itemgetter(1))
guard = sorted_spg[-1][0]

# get the minute that guard was most asleep
sorted_min = sorted(minutes[guard].items(), key=operator.itemgetter(1))
minute = sorted_min[-1][0]

# print result
print(guard * minute)


# find guard that is most frequently asleep on the same minute

# tuple of (guard id, minute of the hour, minites asleep on minute)
most = (0, 0, 0)

for guard, d in minutes.iteritems():
    for m, n in d.iteritems():
        if n > most[2]:
            most = (guard, m, n)

# print result
print(most[0] * most[1])
