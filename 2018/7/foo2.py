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
    for s in all_steps:
        prereqs = steps[s]
        if step in prereqs:
            cand.append(s)
    return cand

def get_next_available(avail, done):
    for n in avail:
        prereqs = steps[n]
        if prereqs.issubset(done):
            return n

def time_req(s):
    return ord(s) - 64 + 60

def get_free_worker():
    for i, w in workers.iteritems():
        if not w[0]:
            return i

parsed = map(parse, sys.stdin)
all_steps = set(flatmap(lambda x: x, parsed))

steps = dict()
for step in all_steps:
    steps[step] = set()

for (step, prereq) in parsed:
    steps[step].add(prereq)

# find steps without prereqs
avail = sorted([s for s, p in steps.iteritems() if not p])
done = set()

workers = dict()
for i in range(5):
    workers[i] = (None, 0)

sec = -1
# for each tick
while len(done) < len(all_steps):
    sec += 1

    # complete done tasks
    for i, (task, remaining) in workers.iteritems():
        if task and remaining == 0:
            # mark as done
            done.add(task)
            # add new candidates
            avail.extend(find_new_candidates(task))
            workers[i] = (None, 0)

    avail = sorted(list(set(avail)))

    # schedule work on free workers
    while True:
        task = get_next_available(avail, done)
        if not task:
            # no available task
            break

        free = get_free_worker()
        if free is None:
            # no free workers
            break

        # assign task to worker
        workers[free] = (task, time_req(task))

        # remove from available tasks
        avail.remove(task)

    # do work
    for i, (task, remaining) in workers.iteritems():
        if task:
            workers[i] = (task, remaining - 1)

print(sec)
