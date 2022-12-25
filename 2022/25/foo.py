import sys

def parse(line):
    return line.strip()

xs = list(map(parse, sys.stdin))

# "SNAFU works the same way, except it uses powers of five instead of ten. 
# Starting from the right, you have a ones place, a fives place, a 
# twenty-fives place, a one-hundred-and-twenty-fives place, and so on. It's that easy!"

# "You know, I never did ask the engineers why they did that. Instead of using digits 
# four through zero, the digits are 2, 1, 0, minus (written -), and double-minus 
# (written =). Minus is worth -1, and double-minus is worth -2."

# "You can do it the other direction, too. Say you have the SNAFU number 2=-01. 
# That's 2 in the 625s place, = (double-minus) in the 125s place, - (minus) 
# in the 25s place, 0 in the 5s place, and 1 in the 1s place. (2 times 625) 
# plus (-2 times 125) plus (-1 times 25) plus (0 times 5) plus (1 times 1). 
# That's 1250 plus -250 plus -25 plus 0 plus 1. 976!"

def snafu_to_dec(s):
    d = 0
    for i, c in enumerate(s[::-1]):
        if c == "-":
            c = -1
        elif c == "=":
            c = -2
        else:
            c = int(c)

        d += pow(5, i) * c

    return d

def dec_to_snafu(d):
    s = ""
    carry = 0
    while d > 0:
        f = d % 5 + carry

        carry = f // 5
        f = f % 5

        if f == 3:
            carry += 1
            s = "=" + s
        elif f == 4:
            carry += 1
            s = "-" + s
        else:
            s = str(f) + s

        d = d // 5

    if carry:
        s = str(carry) + s
    return s

s = sum(snafu_to_dec(x) for x in xs)

print(dec_to_snafu(s))