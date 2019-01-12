import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

judge = 0
for _ in range(40000000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647

    if (a & 0xFFFF) == (b & 0xFFFF):
        judge += 1

print(judge)
