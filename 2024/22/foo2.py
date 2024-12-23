#!/usr/bin/env python3

import sys
from collections import Counter, deque

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

def mix_and_prune(x, r):
    return (r ^ x) % 16777216

total_max = Counter()
for x in xs:
    max_prize = {}
    sequence = deque([], maxlen=4)
    last_ones = x % 10

    for _ in range(2000):
        # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
        x = mix_and_prune(x, x * 64)

        # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
        x = mix_and_prune(x, x // 32)

        # Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
        x = mix_and_prune(x, x * 2048)

        ones = x % 10

        if last_ones is not None:
            df = ones - last_ones

            sequence.append(df)

            if len(sequence) == 4:
                k = tuple(sequence)
                if k not in max_prize:
                    max_prize[k] = ones

        last_ones = ones

    for k, v in max_prize.items():
        total_max[k] += v

print(max(total_max.values()))
