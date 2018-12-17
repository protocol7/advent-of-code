import sys
from itertools import chain, imap
import re

def flatmap(f, items):
    return chain.from_iterable(imap(f, items))

def parse(line):
    ds = [int(i) for i in re.findall("\d+", line)]
    cs = list()
    if line.startswith("x"):
        x = ds[0]
        y1 = ds[1]
        y2 = ds[2]
        for y in range(y1, y2+1):
            cs.append((x, y))
    elif line.startswith("y"):
        y = ds[0]
        x1 = ds[1]
        x2 = ds[2]
        for x in range(x1, x2+1):
            cs.append((x, y))

    return cs


def bound(m):
    minx, miny, maxx, maxy = sys.maxint, sys.maxint, -sys.maxint, -sys.maxint
    for x, y in m:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    return minx, miny, maxx, maxy

def pp(m, falling, w):
    minx, miny, maxx, maxy = bound(m)
    minx -= 5
    maxx += 5
    yy = maxy
    if w:
        wminx, wminy, wmaxx, wmaxy = bound(w)
        yy = min(yy, wmaxy)
    if falling:
        fminx, fminy, fmaxx, fmaxy = bound(falling)
        if w:
            yy = max(yy, fmaxy)
        else:
            yy = min(yy, fmaxy)
    start_y = max(miny, yy-65)
    start_y = 1
    for y in range(start_y, yy+2):
        s = ""
        for x in range(minx, maxx+1):
            if (x, y) in w:
                s += "~"
            elif (x, y) in falling:
                s += "|"
            elif (x, y) in m:
                s += "#"
            else:
                s += "."
        print(str(y).ljust(4, " ") + " " + s)
    print("")

def fill(m, falling, w, b):
    minx, miny, maxx, maxy = b

    # go slightly over the edge
    minx -= 5
    maxx += 5

    end_y = max([y for _, y in falling])
    end_y = min(end_y + 40, maxy+1)

    # scan rows for hanging water
    for y in range(2, end_y):
        for x in range(minx, maxx):
            if (x, y-1) in falling:
                # water above
                if (x, y) not in m and (x, y) not in w:
                    # not clay nor water
                    # hanging water, runs down
                    falling.add((x, y))

    for y in range(2, end_y):
        # find spans
        spans = set()
        x1 = minx - 1
        for x in range(minx, maxx+1):
            if (x, y) in m:
                if x1:
                    spans.add((x1+1, x-1))
                x1 = x
        spans.add((x1+1, maxx))

        if not spans:
            # no spans at all, add outer span
            spans = set([(minx, maxx+1)])

        all_spans = set(spans)

        # spans with empty
        new_spans = set()
        for span in spans:
            for sx in range(span[0], span[1]+1):
                if (sx, y) not in w and (sx, y) not in m:
                    new_spans.add(span)
        spans = new_spans


        # spans with falling water
        new_spans = set()
        for span in spans:
            for sx in range(span[0], span[1]+1):
                if (sx, y) in falling:
                    new_spans.add(span)
        spans = new_spans

        # must be all clay or water below
        fill_spans = set()
        for span in spans:
            ok = True
            for sx in range(span[0], span[1]+1):
                if (sx, y+1) not in w and (sx, y+1) not in m:
                    ok = False
            if ok:
                fill_spans.add(span)

        # fill spans
        for span in fill_spans:
            for sx in range(span[0], span[1]+1):
                w.add((sx, y))
                falling.discard((sx, y))

        new_spans = set()
        overflow_spans = spans - fill_spans

        for span in overflow_spans:
            for sx in range(span[0], span[1]+1):
                if (sx, y) in falling and ((sx, y+1) in w or (sx, y+1) in m):
                    # fill left
                    for xx in range(sx, span[0]-1, -1):
                        if (xx, y+1) in m or (xx, y+1) in w:
                            if (xx, y) not in falling:
                                falling.add((xx, y))
                        else:
                            if (xx, y) not in falling:
                                falling.add((xx, y))
                            break
                    for xx in range(sx, span[1]+1):
                        if (xx, y+1) in m or (xx, y+1) in w:
                            if (xx, y) not in falling:
                                falling.add((xx, y))
                        else:
                            if (xx, y) not in falling:
                                falling.add((xx, y))
                            break

        # if the entire span is falling, turn into water
        for span in all_spans:
            ok = True
            for sx in range(span[0], span[1]+1):
                if (sx, y) not in falling:
                    ok = False
            if ok:
                for sx in range(span[0], span[1]+1):
                    falling.discard((sx, y))
                    w.add((sx, y))

    return w

clay = set(flatmap(parse, sys.stdin))

b = bound(clay)
falling = set()
falling.add((500, 1))
w = set()

while True:
    before = len(w.union(falling))
    fill(clay, falling, w, b)
    after = len(w.union(falling))
    if before == after:
        break

minx, miny, maxx, maxy = b
w = set([(x, y) for x, y in w if y >= miny and y <= maxy])
falling = set([(x, y) for x, y in falling if y >= miny and y <= maxy])

pp(m, falling, w)

print(len(w.union(falling)))
print(len(w))
