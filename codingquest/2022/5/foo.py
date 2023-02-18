import sys
from itertools import count
from hashlib import sha256

def parse(line):
    return line.strip().split("|")

xs = list(map(parse, sys.stdin))

ph = "0000000000000000000000000000000000000000000000000000000000000000"
for desc, mined, prev_hash, hash in xs:
    print(desc, mined, prev_hash, hash)

    # mine
    for m in count():
        h = sha256("|".join([desc, str(m), ph]).encode("utf8")).hexdigest()
        if h.startswith("000000"):
            print(m, h)
            ph = h
            break