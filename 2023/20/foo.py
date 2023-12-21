import sys
from collections import deque, defaultdict


def parse(line):
    a, b = line.strip().split(" -> ")
    b = b.split(", ")

    return a, b

xs = list(map(parse, sys.stdin))

graph = {}
types = {}
cons = {}
flips = {}
for name, connected in xs:
    if name.startswith("%"):
        name = name[1:]
        types[name] = "flip"
        flips[name] = False
    elif name.startswith("&"):
        name = name[1:]
        types[name] = "con"

        cons[name] = {}

    graph[name] = connected

for name, connected in graph.items():
    for c in connected:
        if c in cons:
            cons[c][name] = False

his = 0
lows = 0

for _ in range(1000):
    q = deque([("button", False, "broadcaster")])
    while q:
        sender, hi, name = q.popleft()
        type = types.get(name)

        if hi:
            his += 1
        else:
            lows += 1

        if name == "broadcaster":
            # send to all connected
            for connected in graph[name]:
                q.append((name, hi, connected))
        elif type == "flip":
            if hi:
                # do nothing
                continue
            else:
                # If a flip-flop module receives a low pulse, it flips between on and off. 
                # If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

                flips[name] = not flips[name]
                for connected in graph[name]:
                    q.append((name, flips[name], connected))
        elif type == "con":
            # remember the type of the most recent pulse received from each of their connected input modules; 
            # they initially default to remembering a low pulse for each input. When a pulse is received, 
            # the conjunction module first updates its memory for that input. 
            # Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.

            cons[name][sender] = hi

            all_high = all(cons[name].values())

            for connected in graph[name]:
                q.append((name, not all_high, connected))

print(his * lows)
