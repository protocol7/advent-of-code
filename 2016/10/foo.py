import sys
from collections import defaultdict
from itertools import chain, imap

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def parse(line):
    return line.split()

parsed = map(parse, sys.stdin)
init = [i for i in parsed if i[0] == "value"]
init = map(lambda i: (int(i[1]), int(i[-1])), init)
rules = [rule for rule in parsed if rule[0] == "bot"]
rules = map(lambda i: (int(i[1]), i[5], int(i[6]), i[-2], int(i[-1])), rules)

bots = defaultdict(list)
output = defaultdict(list)
sinks = {
        "bot": bots,
        "output": output
        }

for v, b in init:
    assert len(bots[b]) < 2
    bots[b].append(v)

while sum([len(v) for _, v in bots.iteritems()]) > 0:
    for b, lowt, low, hight, high in rules:
        holds = bots[b]
        if len(holds) == 2:
            if sorted(holds) == [17, 61]:
                print(b)

            if lowt == "bot" and len(bots[low]) > 1:
                continue
            if hight == "bot" and len(bots[high]) > 1:
                continue
            sinks[lowt][low].append(min(holds))
            sinks[hight][high].append(max(holds))
            bots[b] = []

print(output[0][0] * output[1][0] * output[2][0])
