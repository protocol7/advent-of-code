from itertools import count
from random import uniform


def run():
    def winner(a, b):
        if a / (a + b) > uniform(0, 1):
            return a
        else:
            return b

    teams = sorted(uniform(0, 1) for _ in range(4))

    return winner(winner(teams[0], teams[3]), winner(teams[1], teams[2]))

s = 0
for n in count(1):
    s += run()
    print(s / n)
