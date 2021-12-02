from itertools import *

for a, b, c, d, e in permutations([2, 9, 5, 7, 3]):
    if a + b * c**2 + d**3 - e == 399:
        print(a, b, c, d, e)