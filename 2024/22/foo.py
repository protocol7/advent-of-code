#!/usr/bin/env python3

import sys

def parse(line):
    return int(line.strip())

xs = list(map(parse, sys.stdin))

def mix_and_prune(x, r):
    return (r ^ x) % 16777216

t = 0
for x in xs:
    for _ in range(2000):
        # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
        x = mix_and_prune(x, x * 64)

        # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
        x = mix_and_prune(x, x // 32)

        # Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
        x = mix_and_prune(x, x * 2048)

    t += x

print(t)
