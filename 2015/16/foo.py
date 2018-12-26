import sys

def parse(line):
    l = line.split()
    sue = int(l[1].strip(":"))
    d = {}
    for i in range(2, len(l), 2):
        t, data = l[i].strip(":"), int(l[i+1].strip(","))
        d[t] = data
    return sue, d

pattern = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1}

parsed = {k:v for k, v in map(parse, sys.stdin)}

for sue, data in parsed.iteritems():
    match = True
    for k, v in pattern.iteritems():
        if k in data and data[k] != v:
            match = False
            break
    if match:
        print(sue)
