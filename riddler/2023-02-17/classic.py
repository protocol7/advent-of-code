from random import shuffle
from itertools import cycle, count

def run():
    cards = list(range(1, 11)) * 4
    shuffle(cards)

    for i, c in zip(cycle([1, 2,3 ]), cards):
        if i == c:
            return False
        
    return True

wins = 0
for c in count(1):
    if run():
        wins += 1

    if c % 1000 == 0:
        print(wins / c, c)
