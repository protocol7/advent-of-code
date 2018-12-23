import sys
from itertools import count
import hashlib

inp = sys.argv[1].strip()

for i in count():
    h = hashlib.md5(inp + str(i)).hexdigest()
    if h.startswith("000000"):
        print(i)
        break
