import sys

# this was a hard problem for me, lacking much of the maths that might make
# this easier to solve. I spent 6 hours, mostly staring at the problem. 3 hours
# or so in, when looking at the output of one round of part 1, I noticed a
# pattern. After some time, I figured this was a linear function and that I
# could simplify a shuffle using that function.
#
# Finding a and b in the linear function was easy for the small card size in
# part 1, but required me to figure out how to reverse a shuffle for a
# particular position to do it for the large deck. This took about 2 hours.
#
# Lastly, I needed to acculate the linear function over many shuffles. Some
# scribbling on paper gave me that a and b accumulates, but I could not figure
# out how to directly calculate this (afterwards, I discovered that b is a
# geometrical series that could have been summed directly...). Instead, I
# precalculated a and b for 10, 100, 1000... shuffles and then used that up to
# the sum of the input number of shuffles. (in the code below, this is
# simplified to using power of 2 instead, thanks to @yarin).
#
# On with the show...


# these functions now answers where the card at position p started out one
# shuffle earlier (n is size of deck, i is shuffle parameter)
def new_stack(n, p, _):
    # positions reversed
    return n - p - 1

def cut(n, p, i):
    if i > 0:
        return i + p
    elif i < 0:
        return n + i + p

def incr(n, p, i):
    # find placement of position. think about the new stack as a "flat" (no
    # rotation) series
    #
    # With n=10, i=3, as in the example
    # 0 1 2 3 4 5 6 7 8 9 10 11 12
    # 0     1     2     3       4
    #
    # find the position in this for p, and divide by i, gives the original
    # position
    while p % i:
        p += n
    return p / i

def parse(line):
    line = line.strip()
    if line == "deal into new stack":
        return (new_stack, 0)
    elif line.startswith("deal with increment"):
        return (incr, int(line.split()[-1]))
    elif line.startswith("cut"):
        return (cut, int(line.split()[-1]))

def run(n, p):
    for s, i in shuf:
        p = s(n, p, i)
    return p

def t(x, a, b):
    return (x * a + b) % ll

def t2(x, a, b):
    return t(t(x, a, b), a, b)

# inverse the shuffle
shuf = map(parse, sys.stdin)[::-1]

# size of deck
ll = int(sys.argv[1])

# number of shuffles
mm = int(sys.argv[2])

# for whatever reason, the output of a shuffle can be described as a linear
# function of the starting shuffle. this was discovered by staring at the
# output for one round of part 1 and seeing a pattern on every other number.
# the linear function is here described as new_pos = a * old_pos + b.
#
# a and b depends on the size of the deck.
#
# the linear function accumulates over multiple suffles, but we need to know a
# and b for the first shuffle. To do this for a large deck, we run the shuffle
# in the inverse to know what starting positions ends up at position 0 and 1.

b = run(ll, 0)
x = run(ll, 1)
a = x - b

# we now know a and b for our deck

# now we need to run this for many rounds, many more than we can iterate over.
# But, as noted above, the linear function accumulates over runs. So, we can
# calculate new a and b for a certain number of runs.

# this was first done using powers of 10, but later simplified to powers of
# two. By pre-calculating a and b for each power of 2, we can then sum up the
# values of the linear function for each 1 in the binary of our number of
# iterations.

# we already know a and b for 2^0
ab = {1: (a, b)}

# what's mm in binary
mmb = map(int, bin(mm)[2:])

# we'll need to pre-calculate up to the powers in mm
for p in range(1, len(mmb)):
    y0 = t2(0, a, b)
    y1 = t2(1, a, b)

    b = y0
    a = y1 - y0
    ab[2**p] = (a, b)

# apply for mm rounds
# this is where we start, now run this backwards for mm iterations
pos = 2020

for p, d in enumerate(reversed(mmb)):
    if d:
        # apply for this power
        a, b = ab[2**p]
        pos = t(pos, a, b)

print(pos)
