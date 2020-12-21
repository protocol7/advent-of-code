import sys
from collections import *
import re

rs, msgs = sys.stdin.read().split("\n\n")

rules = defaultdict(list)
for r in rs.split("\n"):
    a, b = r.split(": ")
    if '"' in b:
        rules[a] = b[1:-1]
    else:
        for o in b.split(" | "):
            rules[a].append(o.split())

def build(rule):
    reg = ""
    r = rules[rule]

    if type(r) == str:
        return r
    else:
        for oi, ors in enumerate(r):
            if oi > 0:
                reg += "|"

            for rx in ors:
                reg += build(rx)

        return "(%s)" % reg


r = "^%s$" % build("0")

print(sum(bool(re.match(r, m)) for m in msgs.split()))
