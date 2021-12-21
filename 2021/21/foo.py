import sys

def parse(line):
    return int(line.split()[-1])

def run(players):
    die = 1
    c = 0

    scores = [0, 0]

    while True:
        for i, p in enumerate(players):
            s = 0
            for _ in range(3):
                s += die
                c += 1
                die += 1

                die = (die - 1) % 100 + 1

            p += s

            p = (p - 1) % 10 + 1

            scores[i] += p

            if scores[i] >= 1000:
                return min(scores) * c

            players[i] = p

players = list(map(parse, sys.stdin))

print(run(players))