import sys
from collections import *
from itertools import *
from util import *
from csv import DictReader

def parse(line):
    return line.strip()

reader = list(DictReader(sys.stdin))

# train -> list of (station, time)
routes = defaultdict(list)

# train -> (station, time)
next_arrivals = {}
start_times = {}
completion_times = {}

all_stations = set()

for row in reader:
    station = row["station"]

    all_stations.add(station)

    for rail, time in row.items():
        if rail == "station":
            continue

        if time:
            m, s = map(int, time.split(":"))
            time = m * 60 + s
            if rail not in next_arrivals:
                next_arrivals[rail] = (station, "", time)
                start_times[rail] = time

            routes[rail].append((station, time))

# station -> list of queued trains
queues = {}

# station -> (current train, leaving time)
stations = {}



def find_next_station(train, cur_station):
    route = routes[train]
    for i, (station, this_time) in enumerate(route):
        if station == cur_station:
            if i + 1 < len(route):
                # there's a next station
                next_station, next_time = route[i + 1]

                assert next_time > this_time

                return next_station, next_time - this_time
            else:
                return None

    assert False

def format_time(ts):
    return "%s:%s (%s)" % (str(ts // 60).rjust(2, "0"), str(ts % 60).rjust(2, "0"), ts)

# train -> prev station
assert "" < "a"

for now in count():
    #print(now, len(next_arrivals), len(stations), len(queues), len(start_times), len(completion_times))
    if len(start_times) == len(completion_times):
        # done!
        
        deltas = []
        for train, start_time in start_times.items():
            completion_time = completion_times[train]

            assert completion_time > start_time
            deltas.append(completion_time - start_time)

        print(max(deltas))

        break

    # are there trains leaving stations?
    new_stations = {}
    for station, (train, leave_time) in stations.items():
        if leave_time == now:
            next = find_next_station(train, station)
            if next:
                next_station, duration = next
                arrival_time = now + duration

                next_arrivals[train] = (next_station, station, arrival_time)

                print("%s: %s is leaving %s for %s arrving at %s" % (format_time(now), train, station, next_station, arrival_time))
            else:
                delta = now - start_times[train]
                print("%s: train %s is done, started at %s, took %s" % (format_time(now), train, start_times[train], delta))
                completion_times[train] = now
        else:
            new_stations[station] = (train, leave_time)
    stations = new_stations

    # are there trains arriving this minute?
    for train, (station, prev_station, arrival_time) in next_arrivals.items():
        if arrival_time == now:
            queue = queues.get(station, [])

            queue.append((prev_station, now, train))
            queue = sorted(queue)

            print("%s: %s arriving from %s at %s , queue %s" % (format_time(now), train, prev_station, station, queue))

            queues[station] = queue

    # have trains arrive at free stations
    for station in all_stations:
        # is free?
        #print(station, station not in stations, queues.get(station, []))
        if station not in stations:
            # any train in queue?
            queue = queues.get(station, [])

            if queue:
                _, _, train = queue.pop(0)
                print("%s: %s is free and has queue, %s is entering, remaining in queue %s" % (format_time(now), station, train, queue))
                stations[station] = (train, now + 5)
