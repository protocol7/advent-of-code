import sys
from collections import *
import re

rs, msgs = sys.stdin.read().split("\n\n")

rs += "\n8: 42 | 42 8"
rs += "\n11: 42 31 | 42 11 31"

rules = defaultdict(list)
for r in rs.split("\n"):
    a, b = r.split(": ")
    if '"' in b:
        rules[a] = b[1:-1]
    else:
        for o in b.split(" | "):
            rules[a].append(o.split())

def build(rule, depth):
    if depth > 14:  # 14 is the exact threshold for my input. during the actual run
                    # a much larger value was used to be on the safe side
        return ""

    r = rules[rule]

    if type(r) == str:
        return r
    else:
        reg = ""
        for oi, ors in enumerate(r):
            if oi > 0:
                reg += "|"

            for rx in ors:
                reg += build(rx, depth+1)

        if reg == "|":
            return ""
        if "|" in reg:
            return "(%s)" % reg
        else:
            return reg


r = "^%s$" % build("0", 0)

print(sum(bool(re.match(r, m)) for m in msgs.split()))
