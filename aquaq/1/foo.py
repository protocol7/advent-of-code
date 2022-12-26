import sys
from collections import *
from itertools import *
from util import *

xs = sys.stdin.read().strip()

# Set the string's non-hexadecimal characters to 0.
# Pad the string length to the next multiple of 3.
# Split the result into 3 equal sections.
# The first two digits of each remaining section are the hex components.

hex = "0123456789abcdef"

m = ""
for c in xs:
    if c in hex:
        m += c
    else:
        m += "0"

l = (len(m) // 3) + 1
m = m.ljust(l * 3)

print(m[0:2] + m[l:l+2] + m[l*2:l*2+2])