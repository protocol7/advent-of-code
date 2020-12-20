import sys
from collections import *
from itertools import *
from util import *

xs = sys.stdin.read().split("\n\n")

d = dict()

for x in xs:
    x = x.split()

    a = int(x[1][:-1])

    b = x[2:]

    d[a] = b

def edge(x):
    es = []

    # top
    es.append(x[0])
    es.append("".join(reversed(x[0])))

    # bottom
    es.append(x[-1])
    es.append("".join(reversed(x[-1])))

    # left
    s = ""
    for xx in x:
        s += xx[0]
    es.append(s)
    es.append("".join(reversed(s)))

    # right
    s = ""
    for xx in x:
        s += xx[-1]
    es.append(s)
    es.append("".join(reversed(s)))

    return es

edges = dict()
for k, v in d.items():
    e = edge(v)
    edges[k] = e

#    print(e)

cs = set()
es = set()
ms = set()
c = 0
for k, v in edges.items():

    m = 0
    for e in v:
        for kk, vv in edges.items():
            if k == kk:
                continue

            for ee in vv:
                if e == ee:
                    # print(e, ee, k, kk)
                    m += 1

    if m == 6:
        es.add(k)
    elif m == 4:
        cs.add(k)
    elif m == 8:
        ms.add(k)
    else:
        assert False

print(len(cs))
print(len(es))
print(len(ms))

print(cs)

size = int(sys.argv[1])

curk = next(iter(cs))

ps = [curk]

def match_edges(x1, x2):
    for e in edges[x1]:
        for ee in edges[x2]:
            if e == ee:
                return True
    return False

for _ in range(size):
    matched = False
    for e in edges[curk]:
        if matched:
            break

        for k, v in edges.items():
            if not k in es:
                continue

            if matched:
                break

            if k == curk:
                continue

            if k in ps:
                continue

            for ee in v:
                #print(e, ee, e == ee)
                if e == ee:
                    ps.append(k)
                    curk = k
                    matched = True
                    break


for e in edges[curk]:
    for k, v in edges.items():
        if not k in cs:
            continue

        if k == curk:
            continue

        if k in ps:
            continue

        for ee in v:
            if e == ee:
                ps.append(k)
                curk = k
                break


col = ps

#print("col")
#print(col)
#print()

pic = []

def matching_edge(es, os):
    for e in es:
        for o in os:
            if e == o:
                return True
    return False

for ri, curk in enumerate(col):
    row = [curk]
    if pic:
        prev = pic[-1]
    else:
        prev = None

    for pos in range(1, size):

        matched = False

        for k, v in edges.items():
            if matched:
                break

            if ri == 0 or ri == size -1:
                if pos > 0 and pos < size -1:
                    if not k in es:
                        continue
                else:
                    if not k in cs:
                        continue
            else:
                if pos > 0 and pos < size -1:
                    if not k in ms:
                        continue
                else:
                    if not k in es:
                        continue

            if k in col:
                continue

            taken = False
            for yy in pic:
                if k in yy:
                    taken = True
                    break
            if taken:
                continue

            if k == curk:
                continue

            if k in row:
                continue

            if matching_edge(edges[curk], v):

                if prev:
                    pp = prev[pos]
                    match_prev = matching_edge(edges[pp], v)
                else:
                    match_prev = True

                if match_prev:
                    row.append(k)
                    curk = k
                    matched = True
                    break


    pic.append(row)


def pp(t):
    for r in t:
        print(r)
    print()

def transpose(x):
    for start, end, step in [(0, len(x), 1), (len(x)-1, -1, -1)]:
        for reverse in [False, True]:
            xx = []

            for yi in range(start, end, step):
                row = x[yi]
                if reverse:
                    row = "".join(reversed(row))
                xx.append(row)
            yield xx

    for start, end, step in [(0, len(x), 1), (len(x)-1, -1, -1)]:
        for reverse in [False, True]:
            xx = []

            for yi in range(start, end, step):
                row = []
                for rr in x:
                    row.append(rr[yi])
                if reverse:
                    row = reversed(row)
                row = "".join(row)

                xx.append(row)
            yield xx


def align_all(a, b):
    a = d[a]
    b = d[b]

    for aa in transpose(a):
        for bb in transpose(b):
            if aa[-1] == bb[0]:
                return aa, bb

def align(aligned, b):
    b = d[b]

    for bb in transpose(b):
        if aligned[-1] == bb[0]:
            return bb

def coll(x, col):
    return [y[col] for y in x]

def flip(x):
    return ["".join(reversed(y)) for y in x]

pict = []
for ri, row in enumerate(pic):
    nr = []
    g, h = align_all(row[0], row[1])

    nr.append(g)
    nr.append(h)

    #pp(g)
    #pp(h)

    for b in row[2:]:
        h = align(h, b)
        #pp(h)

        nr.append(h)

    # do we need to flip the row?
    if ri > 0:
        prev = pict[-1]
        if coll(prev, 0) != coll(nr, 0):
            # flip nr
            nrr = []
            for x in nr:
                nrr.append(flip(x))
            #nr = list(reversed(nrr))
            nr = nrr

        #prev[0])
        #pp(nr[0])



    pict.append(nr)

#sys.exit()

def trans(o):
    out = []
    for c in range(len(o)):
        out.append("".join(coll(o, c)))
    return out

np = []
for row in pict:
    nr = []
    for o in row:
        nr.append(trans(o))

    np.append(nr)

pict = np

def ppp(pict):
    for row in pict:
        for li in range(len(row[0])):
            s = []
            for x in row:
                s.append(x[li])

            print(" ".join(s))
        print()

ppp(pict)

def flip_row(row):
    nr = []
    for x in row:
        x = list(reversed(x))
        nr.append(x)
    return nr

# post flip
prev = pict[0]
for ri in range(1, len(pict)):
    row = pict[ri]

    if prev[0][-1] != row[0][0]:
        # flip!
        print("flip!", ri, prev[0][-1], row[0][0])
        row = flip_row(row)
        pict[ri] = row
    else:
        print("no flip!")
    print()

    prev = row

ppp(pict)

#sys.exit()

def trim(o):
    no = []
    for ri in range(1, len(o)-1):
        no.append(o[ri][1:-1])
    return no



np = []
for row in pict:
    nr = []
    for o in row:
        nr.append(trim(o))

    np.append(nr)

pict = np


np = []
for row in pict:
    for li in range(len(row[0])):
        s = []
        for x in row:
            s.append(x[li])

        np.append("".join(s))

pict = np

#for row in pict:
#    print(row)

print(len(pict))
print(len(pict[0]))

res = []
res.append("                  # ")
res.append("#    ##    ##    ###")
res.append(" #  #  #  #  #  #   ")

def count_monster(xs):
    return sum(l.count("#") for l in xs)

sc = count_monster(res)
print(sc)
rl = len(res[0])
print(rl)

import re
pos = []
for r in res:
    np = []
    for i, c in enumerate(r):
        if c == "#":
            np.append(i)
    pos.append(np)

print(pos)

print(res)


def find(rows):
    for r, p in zip(rows, pos):
        for pp in p:
            if r[pp] != "#":
                return False
    return True


dd = 0
for t in transpose(pict):
    found = False
    print("new trans")

    for rows in zip(t, t[1:], t[2:]):
        for ir in range(len(rows[0]) - rl):
            nr = [row[ir:ir+20] for row in rows]

            if find(nr):
                found = True
                print("found!")

                print(nr)

                dd += 1


print(dd)
print(sc)
print(count_monster(pict))
print(count_monster(pict) - dd * sc)
#print(dd)
#def rem()