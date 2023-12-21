import sys
from itertools import count
from collections import deque, defaultdict
from math import lcm


def parse(line):
    a, b = line.strip().split(" -> ")
    b = b.split(", ")

    return a, b

xs = list(map(parse, sys.stdin))

mods = {}
types = {}
cons = {}
flips = {}
for name, b in xs:
    if name.startswith("%"):
        name = name[1:]
        types[name] = "flip"
        flips[name] = False
    elif name.startswith("&"):
        name = name[1:]
        types[name] = "con"

        cons[name] = {}

    mods[name] = b

mods_inv = defaultdict(list)

for name, connected in mods.items():
    for c in connected:
        mods_inv[c].append(name)

        if c in cons:
            cons[c][name] = False

rx_input = mods_inv["rx"][0]

# these are the four con modules that connect to the final con module connected to rx
inputs = mods_inv[rx_input]

def foo():
    prev = {}
    cycles = {}

    for i in count():

        q = deque([("button", False, "broadcaster")])
        while q:
            sender, hi, name = q.popleft()
            type = types.get(name)

            if name == "broadcaster":
                # send to all connected
                for connected in mods[name]:
                    q.append((name, hi, connected))
            elif type == "flip":
                if hi:
                    # do nothing
                    continue
                else:
                    # If a flip-flop module receives a low pulse, it flips between on and off. 
                    # If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

                    flips[name] = not flips[name]
                    for connected in mods[name]:
                        q.append((name, flips[name], connected))
            elif type == "con":
                # remember the type of the most recent pulse received from each of their connected input modules; 
                # they initially default to remembering a low pulse for each input. When a pulse is received, 
                # the conjunction module first updates its memory for that input. 
                # Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.

                cons[name][sender] = hi

                all_high = all(cons[name].values())

                for connected in mods[name]:
                    q.append((name, not all_high, connected))

            # detect cycles for when the four con modules that connect to the final con module turn low (they only have one connected module)
            if name in inputs and all(not x for x in cons[name].values()):
                if name in prev:
                    cycles[name] = i - prev[name]

                prev[name] = i

            if len(cycles) == len(inputs):
                # we've found all the cycles
                return lcm(*cycles.values())
                
print(foo())
