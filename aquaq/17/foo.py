import sys
from collections import *
from itertools import *
from util import *
from csv import DictReader
import datetime

r = DictReader(sys.stdin)

xs = []

teams = defaultdict(list)

for m in r:
    dt = m["date"]
    ht = m["home_team"]
    hts = int(m["home_score"])

    teams[ht].append((dt, hts))

    at = m["away_team"]
    ats = int(m["away_score"])

    teams[at].append((dt, ats))

mm = 0
nt = {}
for team, dts in teams.items():
    if len(dts) == 1:
        continue

    def parse(dt):
        return datetime.datetime.strptime(dt, "%Y-%m-%d")

    deltas = []
    zero = None
    for dt, score in dts:
        dt = parse(dt)

        if score == 0 and zero is None:
            zero = dt
        elif score > 0 and zero is not None:
            deltas.append((zero, dt, dt - zero))
            zero = None

    if deltas:
        nt[team] = max(deltas, key=lambda i: i[2])

s = max(nt.items(), key=lambda i: i[1][2])

country = s[0]
dt1 = datetime.datetime.strftime(s[1][0], "%Y%m%d")
dt2 = datetime.datetime.strftime(s[1][1], "%Y%m%d")

print(country, dt1, dt2)