from itertools import *

coins = [2, 9, 5, 7, 3]

perms = list(permutations(coins))

for a, b, c, d, e in perms:
    if a + b * c**2 + d**3 - e == 399:
        print(a, b, c, d, e)