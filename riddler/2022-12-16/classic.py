from itertools import count
from random import choice, shuffle

def run():
    # There are 20 people in the gift exchange. 
    rem = list(range(20))

    for r in count(0):
        if not rem:
            return r

        hat = []

        # In the first round, everyone writes down the name of a random person (other than themselves) and the names go in a hat. 
        for r in rem:
            other = choice(rem)
            while other == r:
                other = choice(rem)

            hat.append(other)

        # Then if two people randomly pick each other’s names out of that hat, they will exchange gifts, and they no longer 
        # participate in the drawing. The remaining family members go on to round two. Again, they write down the name of anyone 
        # left, and again, any two people who pick each other exchange gifts.
        shuffle(hat)
        drawn = {k: v for k, v in zip(rem, hat)}
        
        for a, b in drawn.items():
            if a == b:
                continue

            c = drawn[b]

            if a == c:
                rem.remove(a)

s = 0
for n in count(1):
    s += run()
    print(s/n)

        