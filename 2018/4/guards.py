import sys
from collections import defaultdict, Counter
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
spg = Counter()
minutes = defaultdict(lambda: Counter())
for e in entries:
    spg[e[0]] += e[1]
    for m in e[2]:
        minutes[e[0]][m] += 1

# get guard with most minutes asleep
guard = spg.most_common(1)[0][0]

# get the minute that guard was most asleep
minute = minutes[guard].most_common(1)[0][0]

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
