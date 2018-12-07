import sys
from collections import defaultdict
from itertools import chain, imap

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def parse(line):
    # Step C must be finished before step A can begin.
    parts = line.split()
    prereq = parts[1]
    step = parts[7]
    return (step, prereq)

def find_new_candidates(step):
    cand = list()
    for s, prereqs in steps.iteritems():
        if step in prereqs:
            cand.append(s)
    return cand

def get_next_available(avail, done):
    for n in avail:
        prereqs = steps[n]
        if prereqs.issubset(done):
            return n

parsed = map(parse, sys.stdin)
all_steps = set(flatmap(lambda x: x, parsed))

steps = dict()
for step in all_steps:
    steps[step] = set()

for (step, prereq) in parsed:
    steps[step].add(prereq)

# find steps without prereqs
active = sorted([s for s, p in steps.iteritems() if not p])
path = list()

while active:
    active = sorted(list(set(active)))

    next = get_next_available(active, path)

    path.append(next)
    active.remove(next)

    # add new candidates
    active.extend(find_new_candidates(next))

print("".join(path))
