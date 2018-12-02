import sys

print("Hello world")

total = 0
for line in sys.stdin:
    total = total + int(line)

print(total)
