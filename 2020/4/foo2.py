import sys
from util import *
import re

inp = sys.stdin.read().split("\n\n")

req = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.

def validate(pp):
    p = pairs(msplit(pp, "\n :"))

    ks = [x for x, _ in p]
    if not req.issubset(ks):
        return False

    for k, v in p:
        if k == "byr":
            v = int(v)
            if v < 1920 or v > 2002:
                return False
        elif k == "iyr":
            v = int(v)
            if v < 2010 or v > 2020:
                return False
        elif k == "eyr":
            v = int(v)
            if v < 2020 or v > 2030:

                return False
        elif k == "hgt":
            if not re.match(r"^[0-9]+(in|cm)$", v):
                return False

            l = int(v[:-2])
            u = v[-2:]
            if u == "cm":
                if l < 150 or l > 193:
                    return False
            elif u == "in":
                if l < 59 or l > 76:
                    return False
        elif k == "hcl":
            if not re.match(r"^#[0-9a-f]{6}$", v):
                return False
        elif k == "ecl":
            if not v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:

                return False
        elif k == "pid":
            if not re.match(r"^[0-9]{9}$", v):
                return False

    return True

print(ilen(filter(validate, inp)))