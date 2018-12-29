import sys
from itertools import count
import hashlib

inp = sys.argv[1].strip()

code = [" "] * 8
for i in count():
    h = hashlib.md5(inp + str(i)).hexdigest()
    if h.startswith("00000"):
        pos = int(h[5], 16)
        if pos <8 and code[pos] == " ":
            code[pos] = h[6]
            if " " not in code:
                break
print("".join(code))
