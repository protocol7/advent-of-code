import sys

xs = list(map(lambda s: s.strip(), sys.stdin))

# A for Rock, B for Paper, and C for Scissors

# 1 for Rock, 2 for Paper, and 3 for Scissors

# 0 if you lost, 3 if the round was a draw, and 6 if you won

# part 1
# X for Rock, Y for Paper, and Z for Scissors

# part 2
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win


d = {
    "A X": (3 + 1, 3 + 0),
    "B X": (0 + 1, 1 + 0),
    "C X": (6 + 1, 2 + 0),

    "A Y": (6 + 2, 1 + 3),
    "B Y": (3 + 2, 2 + 3),
    "C Y": (0 + 2, 3 + 3),

    "A Z": (0 + 3, 2 + 6),
    "B Z": (6 + 3, 3 + 6),
    "C Z": (3 + 3, 1 + 6),
}

print(sum(d[x][0] for x in xs))
print(sum(d[x][1] for x in xs))
