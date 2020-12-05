import sys
import re

print(len(list(filter(lambda p: len(re.findall(r"(\bbyr:(19[2-9]\d|200[0-2])\b)|(\biyr:20(1\d|20)\b)|(\beyr:20(2\d|30)\b)|(\bhgt:(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)\b)|(\bhcl:#[\da-f]{6}\b)|(\becl:amb|blu|brn|gry|grn|hzl|oth\b)|(\bpid:\d{9}\b)", p)) == 7, sys.stdin.read().split("\n\n")))))