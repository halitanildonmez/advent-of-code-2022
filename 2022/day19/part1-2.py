from collections import defaultdict, deque

data = open('aa.txt').read().strip()
lines = [x for x in data.split('\n')]

def parse_line(l):
    bp_id = int(line.split()[1][:-1])
    ore_cost = int(line.split()[6])
    clay_cost = int(line.split()[12])
    obsidian_cost_ore, obsidian_cost_clay = int(line.split()[18]), int(line.split()[21])
    geode_cost_ore, geode_cost_clay = int(line.split()[27]), int(line.split()[30])
    return ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay, bp_id


def bfs(sim_time, ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_2, geonode_1, geonode_2):
    res = 0
    S = (sim_time, 0, 0, 0, 0, 1, 0, 0, 0)
    Q = deque([S])
    explored = set()

    max_ore_cost = max([ore_cost, clay_cost, obsidian_cost_ore, geonode_1])

    while Q:
        v = Q.popleft()
        t, o, c, ob, g, ro, rc, rob, rg = v
        res = max(res, g)
        if t == 0:
            continue

        if ro >= max_ore_cost:
            ro = max_ore_cost
        if rc >= obsidian_cost_2:
            rc = obsidian_cost_2
        if rob >= geonode_2:
            rob = geonode_2 
        
        if o >= t * max_ore_cost - ro * (t - 1):
             o = t * max_ore_cost - ro * (t - 1)
        if c >= t * obsidian_cost_2 - rc * (t - 1):
            c = t * obsidian_cost_2 - rc * (t - 1)
        if ob >= t * geonode_2 - rob * (t - 1):
            ob = t * geonode_2 - rob * (t - 1)

        new_s = (t, o, c, ob, g, ro, rc, rob, rg)
        if new_s in explored:
            continue

        explored.add(new_s)

        if o < 0 or c < 0 or ob < 0 or g < 0 or not v:
            print('failed')
            return -1
        Q.append((t-1, o+ro, c+rc, ob+rob, g+rg, ro, rc, rob,rg))
        if o>=ore_cost:
            Q.append((t-1, o-ore_cost+ro, c+rc, ob+rob, g+rg, ro+1, rc, rob, rg))
        if o>=clay_cost:
            Q.append((t-1, o-clay_cost+ro, c+rc, ob+rob, g+rg, ro, rc+1, rob, rg))
        if o>=obsidian_cost_ore and c>=obsidian_cost_2:
            Q.append((t-1, o-obsidian_cost_ore+ro, c-obsidian_cost_2+rc, ob+rob, g+rg, ro,rc,rob+1,rg))
        if o>=geonode_1 and ob>=geonode_2:
            Q.append((t-1, o-geonode_1+ro, c+rc, ob-geonode_2+rob, g+rg, ro,rc,rob,rg+1))
    return res

p1 = 0
p2 = 1
for i, line in enumerate(lines):
    ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay, bp_id = parse_line(line)
    s1 = bfs(24, ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay)
    p1 += bp_id*s1
    if i<3:
        s2 = bfs(32, ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay)
        p2 *= s2

print(p1, p2)
