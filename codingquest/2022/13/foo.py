import sys
from util import ints, flatten

def parse(line):
    return ints(line.strip())

xs = list(map(parse, sys.stdin))

board = []
rolls = []

for x in xs:
    if len(x) == 2:
        rolls.append(x)
    else:
        board.append(x)

board.reverse()

flip = False
nb = []
for row in board:
    if flip:
        row.reverse()

    nb.append(row)

    flip = not flip

board = flatten(nb)

one = 0
two = 0
for c, (a, b) in enumerate(rolls):
    def move(pos, first):
        pos += first

        while pos < len(board) and board[pos] != 0:
            pos += board[pos]

        return pos
    
    one = move(one, a)

    if one + 1 >= len(board):
        print(1 * c + 1)
        break

    two = move(two, b)
    if two + 1 >= len(board):
        print(2 * c + 1)
        break
