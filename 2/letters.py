import sys
from collections import defaultdict

def letters(word):
    word = word.strip()
    d = defaultdict(lambda :0)
    for l in word:
        d[l] += 1
    return d

def checksum(letters):
    twos = 0
    threes = 0

    for d in letters:
        two = False
        three = False
        for x in d.itervalues():
            if x == 2:
                two = True
            if x == 3:
                three = True
        if two:
            twos += 1
        if three:
            threes += 1
    return twos * threes

ds = map(letters, sys.stdin)
print(checksum(ds))
