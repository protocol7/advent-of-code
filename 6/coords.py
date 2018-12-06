import sys
from collections import Counter

def parse(line):
    x, y = [int(i) for i in line.split(",")]
    return (x, y)

coords = map(parse, sys.stdin)

min_x, min_y, max_x, max_y = (sys.maxint, sys.maxint, 0, 0)
for x, y in coords:
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

def man_dist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

# for each location, find the uniquely closest coordinate. how many locations is
# a coordinate closest to?
closest = Counter()
for xs in range(min_x, max_x+1):
    for ys in range(min_y, max_y+1):
        shortest = sys.maxint
        closest_coord = None
        for c in coords:
            dist = man_dist(xs, ys, c[0], c[1])

            # discard coords of equal distance
            if dist == shortest:
                # dup
                closest_coord = None
            elif dist < shortest:
                shortest = dist
                closest_coord = c

        if closest_coord:
            closest[closest_coord] += 1

print(closest.most_common(1)[0][1])
