import sys
from blist import blist

inp = int(sys.argv[1])

elfs = blist([(x + 1, 1) for x in range(inp)])

index = 0
while len(elfs) > 1:
    elf, c = elfs[index]
    opp = index + len(elfs) // 2
    opp %= len(elfs)

    elfs[index] = (elf, c + elfs[opp][1])
    del elfs[opp]

    if opp > index:
        index += 1
    index %= len(elfs)

print(elfs[0][0])
