import sys
import re

def parse(line):
    line = line[1:-1]
    line = re.sub(r"\\\\", r"\\", line)
    line = re.sub(r"\\\"", " ", line)
    line = re.sub(r"\\x[a-f0-9]{2}", " ", line)
    return line

codes = map(lambda l: l.strip(), sys.stdin)
strings = map(parse, codes)

print(sum(map(len, codes)) - sum(map(len, strings)))
