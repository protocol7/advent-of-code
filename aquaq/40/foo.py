import sys
from util import ints


xs = ints(sys.stdin.read())

mi = xs.index(max(xs))

def first(fn, xs):
    for x in xs:
        if fn(x):
            return x

    return None

peaks = []
for i in range(1, len(xs)-1):
    if xs[i-1] < xs[i] > xs[i+1]:
        # i is a peak
        peaks.append(i)

prom = 0
for ii, xsi in enumerate(peaks):
    h = xs[xsi]
    if xsi == mi:
        prom += h
    else:
        rp = first(lambda x: xs[x]>= h, peaks[ii+1:])
        lp = first(lambda x: xs[x]>= h, peaks[:ii][::-1])

        rprom = sys.maxsize

        rprom = h - min(xs[xsi:rp]) if rp else sys.maxsize
        lprom = h - min(xs[lp:xsi]) if lp else sys.maxsize

        prom += min(lprom, rprom)

print(prom)
