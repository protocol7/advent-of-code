import sys
import re

def escape(line):
    line = re.sub(r"\"", "##", line)
    line = re.sub(r"\\", "##", line)
    return "\"" + line + "\""

codes = map(lambda l: l.strip(), sys.stdin)
strings = map(escape, codes)

print(sum(map(len, strings)) - sum(map(len, codes)))
