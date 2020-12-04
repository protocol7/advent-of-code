import sys
from util import *
import re

inp = sys.stdin.read().split("\n\n")

val = {
    "byr": r"^19[2-9]\d|200[0-2]$",
    "iyr": r"^20(1\d|20)$",
    "eyr": r"^20(2\d|30)$",
    "hgt": r"^(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)$",
    "hcl": r"^#[\da-f]{6}$",
    "ecl": r"^amb|blu|brn|gry|grn|hzl|oth$",
    "pid": r"^\d{9}$",
    "cid": r"^.*$"
}
req = set(val.keys()) - set(["cid"])

def validate(pp):
    p = pairs(msplit(pp, "\n :"))
    return req.issubset([x for x, _ in p]) and all([re.match(val[k], v) for k, v in p])

print(ilen(filter(validate, inp)))