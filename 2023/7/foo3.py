import sys
from collections import Counter
from functools import cmp_to_key

def parse(line):
    h, b = line.strip().split()
    return h, int(b)

xs = list(map(parse, sys.stdin))

CO = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")
RR = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

def five_of_a_kind(cs):
    return len(set(cs)) == 1

def four_of_a_kind(cs):
    c = Counter(cs)
    return set(c.values()) == set([1, 4])

def full_house(cs):
    c = Counter(cs)
    return set(c.values()) == set([2, 3])

def three_of_a_kind(cs):
    c = Counter(cs)
    return sorted(c.values()) == [1, 1, 3]

def two_pair(cs):
    c = Counter(cs)
    return sorted(c.values()) == [1, 2, 2]

def one_pair(cs):
    c = Counter(cs)
    return sorted(c.values()) == [1, 1, 1, 2]

def high_card(cs):
    return len(set(cs)) == 5

def second_order(cs1, cs2):
    for a, b in zip(cs1, cs2):
        d = CO.index(a) - CO.index(b)
        if d:
            return d 

    return 0

FO = [five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, high_card]

def cmp(cs1, cs2, o1=None, o2=None):
    for o in FO:
        if o(cs1) and o(cs2):
            return second_order(o1 or cs1, o2 or cs2)
        elif o(cs1):
            return -1
        elif o(cs2):
            return 1

# replace jokers by all possible alternatives and get the best
ns = []
for cs, bid in xs:
    ff = []
    for r in RR:
        ff.append(cs.replace("J", r))

    ff = sorted(ff, key=cmp_to_key(lambda a, b: cmp(a, b)))

    ns.append((ff[0], cs, bid))
    
# now same as part 1, but do the second comparison using the original hands
xs = sorted(ns, key=cmp_to_key(lambda a, b: cmp(a[0], b[0], a[1], b[1])), reverse=True)

print(sum((i+1) * bid for i, (_, _, bid) in enumerate(xs)))
