import sys
from itertools import count
import hashlib

inp = sys.argv[1].strip()

code = ""
for i in count():
    h = hashlib.md5(inp + str(i)).hexdigest()
    if h.startswith("00000"):
        code += h[5]
        if len(code) == 8:
            break
print(code)
