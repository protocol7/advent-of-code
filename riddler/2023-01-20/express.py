
def dates():
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for m in range(1, 13):
        for d in range(1, days[m-1] + 1):
            yield m, d

c = 0
for m1, d1 in dates():
    for m2, d2 in dates():
        c += (m1 * d1 == m2 and m1 + d1 == d2) or (m1 * d1 == d2 and m1 + d1 == m2)

print(c)