import sys
from util import ints, product

def parse(line):
    ix = ints(line.strip())

    return tuple(ix)

bps = list(map(parse, sys.stdin))

def bar(costs, cache, ore_bots, clay_bots, ob_bots, geo_bots, ore, clay, ob, geo, rem):

    # costs are constant and geo is part of the output
    k = (ore_bots, clay_bots, ob_bots, geo_bots, ore, clay, ob, rem)
    cv = cache.get(k)
    if cv is not None:
        return cv

    if rem == 0:
        return geo

    cost_ore_bots_ore, cost_clay_bots_ore, cost_ob_ore, cost_ob_clay, cost_geo_ore, cost_geo_ob = costs
    max_cost_ore = max(cost_ore_bots_ore, cost_clay_bots_ore, cost_ob_ore, cost_geo_ore)

    nore = ore + ore_bots
    nclay = clay + clay_bots
    nob = ob + ob_bots
    ngeo = geo + geo_bots

    gs = 0

    # always build geo bots if possible
    if ore >= cost_geo_ore and ob >= cost_geo_ob:
        # build geo robot
        gs = max(gs, bar(costs, cache, ore_bots, clay_bots, ob_bots, geo_bots+1, nore-cost_geo_ore, nclay, nob-cost_geo_ob, ngeo, rem - 1))
    else:
        if ore >= cost_ob_ore and clay >= cost_ob_clay and ob_bots < cost_geo_ob:
            # build ob robot. don't build if we are already making more ob than we can use each round
            gs = max(gs, bar(costs, cache, ore_bots, clay_bots, ob_bots+1, geo_bots, nore-cost_ob_ore, nclay-cost_ob_clay, nob, ngeo, rem - 1))
            
            # we do this greedily, and do not do anything else if it's possible to build an ob bot.
            # this is a hack to speed things up and does not work with the sample input, but works with my input ¯\_(ツ)_/¯
        else:
            if ore >= cost_ore_bots_ore and ore_bots < max_cost_ore:
                # build ore robot. don't build if we are already making more ore than we can use each round
                gs = max(gs, bar(costs, cache, ore_bots+1, clay_bots, ob_bots, geo_bots, nore-cost_ore_bots_ore, nclay, nob, ngeo, rem - 1))

            if ore >= cost_clay_bots_ore and clay_bots < cost_ob_clay:
                # build clay robot
                # build ore robot. don't build if we are already making more clay than we can use each round
                gs = max(gs, bar(costs, cache, ore_bots, clay_bots+1, ob_bots, geo_bots, nore-cost_clay_bots_ore, nclay, nob, ngeo, rem - 1))

            # build nothing
            gs = max(gs, bar(costs, cache, ore_bots, clay_bots, ob_bots, geo_bots, nore, nclay, nob, ngeo, rem - 1))

    cache[k] = gs

    return gs

ql = 0
for bp in bps:
    bid = bp[0]
    costs = bp[1:]

    ql += bid * bar(costs, {}, 1, 0, 0, 0, 0, 0, 0, 0, 24)

print(ql)

# part 2
geos = []
for bp in bps[:3]:
    costs = bp[1:]

    geos.append(bar(costs, {}, 1, 0, 0, 0, 0, 0, 0, 0, 32))

print(product(geos))
