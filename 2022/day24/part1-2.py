from collections import defaultdict, deque

data = open('bb.txt').read()
lines = [x for x in data.strip().split('\n')]

navigable = set()
blizzards = []

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
winds = [">", "v", "<", "^"]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        ch = lines[i][j]
        if ch in winds or ch == "." or ch == "G" or ch == "S":
            navigable.add((i,j))
        if ch in winds:
            blizzards.append(((i,j), dirs[winds.index(ch)]))
        if ch == "G":
            goal = (i,j)
        if ch == "S":
            start = (i,j)

def addt(x, y):
    if len(x) == 2:
        return (x[0] + y[0], x[1] + y[1])
    return tuple(map(sum, zip(x, y)))

def ns(pos, same=False):
    if same:
        yield pos
    for d in dirs:
        yield addt(pos, d)

def move_winds(blizzards):
    ret = []
    for blizzard in blizzards:
        pos, dr = blizzard
        pos = addt(pos, dr)
        if pos[0] == 0:
            pos = (len(lines)-2, pos[1])
        if pos[0] == len(lines)-1:
            pos = (1, pos[1])
        if pos[1] == 0:
            pos = (pos[0], len(lines[0])-2)
        if pos[1] == len(lines[0])-1:
            pos = (pos[0], 1)
        ret.append((pos, dr))
    return ret

possible = set()
possible.add(start)

stage = 0
for minute in range(1000000000):
    blizzards = move_winds(blizzards)
    non_navigable = {x[0] for x in blizzards}
    next_possible = set()
    for prev in possible:
        for n in ns(prev, same=True):
            if n in navigable and n not in non_navigable:
                next_possible.add(n)
    if stage == 0:
        if goal in next_possible:
            print("pt1", minute+1)
            stage = 1
            next_possible = set([goal])
    if stage == 1:
        if start in next_possible:
            stage = 2
            next_possible = set([start])
    if stage == 2:
        if goal in next_possible:
            print("pt2", minute+1)
            break
    possible = next_possible
