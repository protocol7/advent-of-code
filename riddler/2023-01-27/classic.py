from string import ascii_lowercase
from random import shuffle


def run():
    letters = list(ascii_lowercase)
    shuffle(letters)

    guesses = [None] * 5

    while letters:
        l = letters[0]

        if all(guesses):
            return sorted(guesses) == guesses

        # index = sorted(letters).index(l) / len(letters) * 5
        #index = ascii_lowercase.index(l) / len(ascii_lowercase) * 5
        index = int(ascii_lowercase.index(l) / (len(ascii_lowercase)-1) * 6)

        ps = [(abs(i - index), i) for i, g in enumerate(guesses) if g is None]

        print(l, ps)

        ia = min(ps)[1]

        guesses[ia] = l

        letters.pop(0)


wins = 0
total = 0

while True:
    if run():
        wins += 1
    total += 1

    print(wins/total)
