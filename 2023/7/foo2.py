import sys
from collections import Counter
from functools import cmp_to_key

def parse(line):
    h, b = line.strip().split()
    return h, int(b)

xs = list(map(parse, sys.stdin))

CO = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

def five_of_a_kind(cs):
    cs = cs.replace("J", "")

    return len(set(cs)) == 1 or len(set(cs)) == 0

def four_of_a_kind(cs):
    cs = cs.replace("J", "")
    c = Counter(cs)
    return sorted(c.values()) == [1, len(cs)-1]

def full_house(cs):
    cs = cs.replace("J", "")

    c = Counter(cs)
    return set(c.values()) == set([2, len(cs)-2])

def three_of_a_kind(cs):
    cs = cs.replace("J", "")

    c = Counter(cs)
    return sorted(c.values()) == [1, 1, len(cs)-2]

def two_pair(cs):
    # will be three of a kind with a joker
    c = Counter(cs)
    return sorted(c.values()) == [1, 2, 2]

def one_pair(cs):
    cs = cs.replace("J", "")

    c = Counter(cs)
    return sorted(c.values()) == [1, 1, 1, 2] or sorted(c.values()) == [1, 1, 1, 1]

def high_card(cs):
    return len(set(cs)) == 5

def second_order(cs1, cs2):
    for a, b in zip(cs1, cs2):
        d = CO.index(a) - CO.index(b)
        if d:
            return d 

    return 0

FO = [five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, high_card]

def order(cs1, cs2):
    for o in FO:
        if o(cs1) and o(cs2):
            return second_order(cs1, cs2)
        elif o(cs1):
            return -1
        elif o(cs2):
            return 1

xs = sorted(xs, key=cmp_to_key(lambda i1, i2: order(i1[0], i2[0])), reverse=True)

print(sum((i+1) * bid for i, (_, bid) in enumerate(xs)))
