import sys

xs = sys.stdin.read().strip()

chunks = []
chunk = ""
for x in xs:
    if not chunk or chunk[0] == x:
        chunk += x
    else:
        chunks.append(chunk)
        chunk = x

chunks.append(chunk)

pos = 0
for chunk in chunks:
    what = chunk[0]
    l = len(chunk)

    if what == "F":
        pos += l +1 if l > 1 else l
    else:
        pos -= 2 if l % 2 == 0 else l

print(pos)
