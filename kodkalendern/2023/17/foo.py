import sys

def parse(line):
    return set(line.strip().lower())

ks = (
    set("qwertyuiopå"),
    set("asdfghjklöä"),
    set("zxcvbnm"),
)

xs = list(map(parse, sys.stdin))

print(sum(x & k == x for k in ks for x in xs ))
