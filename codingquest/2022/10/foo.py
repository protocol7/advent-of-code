import sys
from util import *
from PIL import Image

img = Image.open("input.png")

ps = []
for y in range(img.height):
    for x in range(img.width):

        p = img.getpixel((x, y))[0]
        ps.append(p & 1)

s = ""
for p in chunks(ps, 8):
    p = int("".join(map(str, p)), 2)

    if p == 0:
        break

    s += chr(p)

print(s)