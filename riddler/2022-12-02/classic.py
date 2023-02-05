from itertools import count
from random import shuffle

def run():
    xs = [True] * 11 + [False] * 7

    for bus in count(0):
        shuffle(xs)

        if not xs:
            return last, bus
        
        last = xs[0]
        while xs and last == xs[0]:
            last = xs.pop(0)

a = 0
b = 0

for n in count(1):
    aa, bb = run()
    a += aa
    b += bb

    print(a / n, b / n)