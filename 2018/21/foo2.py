r4 = 65536
r3 = 7041048

seen = set()
last_seen = None
while True:
    #bani 4 255 5
    x = r4 & 255

    # addr 3 5 3
    r3 = r3 + x

    # bani 3 16777215 3
    r3 = r3 & 16777215

    #muli 3 65899 3
    r3 = r3 * 65899

    # bani 3 16777215 3
    r3 = r3 & 16777215

    # gtir 256 4 5
    if 256 > r4:
        print(r3)
        if r3 in seen:
            print(last_seen)
            break
        seen.add(r3)
        last_seen = r3
        r4 = r3 | 65536
        r3 = 7041048
    else:
        r4 = r4 // 256
