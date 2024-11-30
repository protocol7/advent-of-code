#!/usr/bin/env python3

import sys
from collections import *
from itertools import *
from util import *


def parse(line):
    return list(line.strip())

xs = list(map(parse, sys.stdin))

def block(br, bc):
    return chunks([xs[br * 6 + r][bc * 6 + c] for r in range(8) for c in range(8)], 8)

def update(br, bc, block):
    for r in range(8):
        for c in range(8):
            v = block[r][c]
            xs[br * 6 + r][bc * 6 + c] = v


def solve_block(block):
    assert block[0][0] == "*"
    assert block[0][1] == "*"

    for r in range(2, 6):
        for c in range(2, 6):
            row = block[r]
            row_clues = row[0:2] + row[6:8]
            row_solved = [x for x in row[2:6] if x != "."]
            row_clues_set = set(row[0:2] + row[6:8]) - set(["?"])

            col = [block[rr][c] for rr in range(8)]
            col_clues = col[0:2] + col[6:8]
            col_solved = [x for x in col[2:6] if x != "."]
            col_clues_set = set(col_clues) - set(["?"])

            intersect = row_clues_set & col_clues_set

            if len(intersect) > 1:
                return None
            elif len(intersect) == 1:
                block[r][c] = item(intersect)

    # solve question marks
    for r in range(2, 6):
        for c in range(2, 6):
            if block[r][c] != ".":
                continue

            row = block[r]
            row_clues = row[0:2] + row[6:8]
            row_solved = [x for x in row[2:6] if x != "."]
            row_clues_set = set(row[0:2] + row[6:8]) - set(["?"])

            col = [block[rr][c] for rr in range(8)]
            col_clues = col[0:2] + col[6:8]
            col_solved = [x for x in col[2:6] if x != "."]
            col_clues_set = set(col_clues) - set(["?"])

            if "?" in row_clues or "?" in col_clues:
                xx = (row_clues_set | col_clues_set) - set(row_solved) - set(col_solved)
                if len(xx) == 1:
                    block[r][c] = item(xx)

                    for cc in range(0, 8):
                        if block[r][cc] == "?":
                            block[r][cc] = item(xx)
                    for rr in range(0, 8):
                        if block[rr][c] == "?":
                            block[rr][c] = item(xx)
                    pass


    return block

def solved(block):
    if block is None:
        return False
    return all(block[r][c] != "." for r in range(2, 6) for c in range(2, 6))

while True:
    blocks_solved = 0

    for br in range(10):
        for bc in range(20):
            b = block(br, bc)
            if not solved(b):
                b = solve_block(b)

                if solved(b):
                    update(br, bc, b)
                    blocks_solved += 1

    if blocks_solved == 0:
        break

def power(word):
    assert "?" not in word
    p = 0
    for i, c in enumerate(word):
        c = c.upper()
        p += (i + 1) * (ord(c) - ord("A") + 1)
    return p

s = 0
for br in range(10):
    for bc in range(20):
        b = block(br, bc)

        if solved(b):

            word = ""
            for r in range(2, 6):
                for c in range(2, 6):
                    word += b[r][c]

            s += power(word)

print(s)


