import sys
from collections import *
from util import *

a, b, c = sys.stdin.read().split("\n\n")

# parse ranges
rd = defaultdict(list)
for line in a.split("\n"):
    f, rs = line.split(": ")

    for r in rs.split(" or "):
        rr = tuple(map(int, r.split("-")))
        rd[f].append(rr)


ranges = set()
for rs in rd.values():
    for r in rs:
        ranges.add(r)

def matches_ranges(x, rs):
    return any(d <= x <= e for d, e in rs)

def valid_ticket(xs):
    for x in xs:
        if not matches_ranges(x, ranges):
            return False

    return True

# create list of valid, nearby tickets
near = [tuple(map(int, line.strip().split(","))) for line in c.split()[2:]]
valid = list(filter(valid_ticket, near))

# dict of int position in tickets -> remaining possible field names for each
rem = {i:list(rd.keys()) for i in range(len(valid[0]))}


# for each valid ticket
for ticket in valid:
    # for each field in the ticket
    for i, x in enumerate(ticket):
        # which field ranges does it match?
        for f, rs in rd.items():
            matches = matches_ranges(x, rs)

            # if it doesn't match, remove that field as available options for the ticket position
            if not matches and f in rem[i]:
                rem[i].remove(f)

# we now have a dict (rem) of all valid fields for each position in the ticket. reduce it down to the unique options for each
rem = reduce_unique_options(rem)

# parse own ticket
b = list(map(int, b.split("\n")[1].strip().split(",")))

# multiply up all fields starting with "departure"
print(product(b[k] for k, v in rem.items() if v.startswith("departure")))
