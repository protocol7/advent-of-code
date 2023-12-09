import sys
from collections import defaultdict
from util import ints


xs = ints(sys.stdin.read())

s = defaultdict(int)
wins = defaultdict(int)
final = []
starter = "A"
player = "A"

def swap(p):
    if p == "A":
        return "B"
    else:
        return "A"

while xs:
    for _ in range(3):
        x = xs.pop(0)

        s[player] += x

        if s[player] == 501:
            wins[player] += 1
            final.append(x)

            player = swap(starter)
            starter = player
            s = defaultdict(int)

            break            
    else:
        player = swap(player)

print(sum(final) * wins["A"])


