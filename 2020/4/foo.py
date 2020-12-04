import sys
from util import *

inp = sys.stdin.read().split("\n\n")

req = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def validate(pp):
    p = [x for x, _ in pairs(msplit(pp, "\n :"))]
    return req.issubset(p)

print(ilen(filter(validate, inp)))