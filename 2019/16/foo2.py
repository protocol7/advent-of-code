import sys

sig = [int(i) for i in sys.stdin.read().strip()]

def off(xs, offset, l):
    return "".join([str(i) for i in xs[offset:offset+l]])

offset = int(off(sig, 0, 7))
sig = sig * 10000

# our offset is in the second half of the signal
# the second half of the signal is independent of the first half (since the digits in the first half are all multipled by 0 when calculating the second half)
# the second half is just the accumulted sum when iterating backwards
# we only need to calculate the signal backwards up until the offset

for _ in range(100):
    s = 0 # accumulated sum
    for i in range(1, len(sig)-offset+1):
        s += sig[-i]
        sig[-i] = s % 10

print(off(sig, offset, 8))
