import sys

step = int(sys.argv[1])

buf = []
pos = 0

for i in range(2018):
    pos += 1
    buf.insert(pos, i)
    pos = (pos + step) % len(buf)

print(buf[buf.index(2017) + 1])
