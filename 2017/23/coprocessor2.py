b = 105700
c = b + 17000
h = 0

while True:
    d = 2

    while True:
        if b == d:
            break

        if b % d == 0:
            h += 1
            break

        d += 1

    if b == c:
        break
    b += 17

print(h)
