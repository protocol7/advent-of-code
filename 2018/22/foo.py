import sys

depth = int(sys.argv[1])
tx, ty = int(sys.argv[2]), int(sys.argv[3])

types = ".=|"

m = []
el = []
risk = 0
for y in range(ty +1):
    mrow = []
    elrow = []
    for x in range(tx + 1):
        if x == tx and y == ty:
            geo = 0
        elif x == 0 and y == 0:
            geo = 0
        elif x == 0:
            geo = y * 48271
        elif y == 0:
            geo = x * 16807
        else:
            geo = elrow[x-1] * el[y-1][x]

        ero = (geo + depth) % 20183
        elrow.append(ero)

        mrow.append(types[ero % 3])
        risk += ero % 3

    m.append(mrow)
    el.append(elrow)

for row in m:
    print("".join(row))

print(risk)
