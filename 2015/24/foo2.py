import sys
from collections import defaultdict

def parse(line):
    return int(line)


def e(c, remaining, target, combos):
    rr = remaining[:]
    cs = sum(c)
    while rr:
        x = rr.pop(0)
        if (cs + x) == target:
            cc = c[:] + [x]
            combos.append(tuple(cc))
        elif (cs + x) > target:
            return
        else:
            cc = c[:] + [x]
            e(cc, rr, target, combos)

def t(combos):
    c = combos[:]
    while c:
        r1 = c.pop(0)
        l1 = len(r1)
        c2 = c[:]
        c2.sort(key=len, reverse=True)
        while c2:
            r2 = c2.pop(0)
            l2 = l1 + len(r2)
            c3 = c2[:]
            while c3:
                r3 = c3.pop(0)
                l3 = l2 + len(r3)

                c4 = filter(lambda x: len(x) == ll-l3, c3)
                for r4 in c4:
                    a = r1 + r2 + r3 + r4
                    if len(set(a)) == len(a):
                        # all unique
                        return (r1, r2, r3, r4)

def quantum(t):
    p = 1
    for x in t:
        p *= x
    return p

nums = map(parse, sys.stdin)
ll = len(nums)
nums.sort()
assert len(set(nums)) == len(nums)

s = sum(nums) // 4

combos = list()
e([], nums, s, combos)

combos.sort(key=lambda c: (len(c), quantum(c)))

# assume first is valid
print(quantum(combos[0]))

# slow as hell
#triplet = t(list(combos))

#print(quantum(triplet[0]))
