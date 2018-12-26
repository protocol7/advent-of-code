import sys

def parse(line):
    l = line.split()
    p1, p2, sign, val = l[0], l[-1].strip("."), l[2], int(l[3])
    if sign == "lose":
        val = -val
    return p1, p2, val

def e(seats, remains, seatings):
    if not remains:
        seatings.append(seats)
    for p in remains:
        r = set(remains)
        r.remove(p)
        s = seats[:]
        s.append(p)
        e(s, r, seatings)

def happiness(seating):
    h = 0
    for p1, p2 in zip(seating, seating[1:] + [seating[0]]):
        h += pairs[(p1, p2)]
        h += pairs[(p2, p1)]
    return h



pairs = {(p1, p2):v for p1, p2, v in map(parse, sys.stdin)}
persons = set([p for p, _ in pairs.keys()])

for p in persons:
    pairs[(p, "me")] = 0
    pairs[("me", p)] = 0
persons.add("me")

seatings = []
e([], persons, seatings)

h = map(happiness, seatings)
print(max(h))
