from collections import Counter
from itertools import cycle
from blist import blist

max_marble = 71320 * 100
players = 459
scores = Counter()

current = 0
marble = 1
marbles = blist([0])

for player in cycle(range(players)):
    if marble % 23 == 0:
        scores[player] += marble
        pos = (current - 7) % len(marbles)
        m = marbles.pop(pos)
        scores[player] += m
        current = pos
    else:
        pos = (current + 1) % len(marbles) + 1
        marbles.insert(pos, marble)
        current = pos

    marble += 1
    if marble > max_marble:
        break

print(scores.most_common(1)[0][1])
