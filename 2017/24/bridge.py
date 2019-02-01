import sys

def parse(line):
    return tuple([int(i) for i in line.split("/")])

ports = list(map(parse, sys.stdin))

bridges = set()
def build(bridge, ports):
    last = bridge[-1]
    match = False
    for p1, p2 in ports:
        if p1 == last or p2 == last:
            match = True
            if p1 == last:
                b = bridge + [p1, p2]
            elif p2 == last:
                b = bridge + [p2, p1]
            p = list(ports)
            p.remove((p1, p2))
            build(b, p)
    if not match:
        # bridge is done
        bridges.add(tuple(bridge))

build([0], ports)

# part 1
print(max(map(sum, bridges)))

# part 2
ll = max(map(len, bridges))
print(max(map(sum, filter(lambda b: len(b) == ll, bridges))))
