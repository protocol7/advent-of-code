from collections import defaultdict

tape = defaultdict(int)

states = dict()
states['A'] = ((1, 1, 'B'), (0, 1, 'C'))
states['B'] = ((0, -1, 'A'), (0, 1, 'D'))
states['C'] = ((1, 1, 'D'), (1, 1, 'A'))
states['D'] = ((1, -1, 'E'), (0, -1, 'D'))
states['E'] = ((1, 1, 'F'), (1, -1, 'B'))
states['F'] = ((1, 1, 'A'), (1, 1, 'E'))

pos = 0
state = 'A'
steps = 12368930

for step in range(steps):
    write, move, next = states[state][tape[pos]]
    tape[pos] = write
    pos += move
    state = next

print(len(filter(lambda v: v == 1, tape.values())))
