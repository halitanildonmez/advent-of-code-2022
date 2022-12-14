import math
import collections
import itertools
import re
import ast
import functools

T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
lines = file1.read().splitlines()

def find_intervals():
    r = set()
    for line in lines:
        vals = line.split(' -> ')
        als = []
        for v in vals:
            xx, yy = v.split(',')
            als.append([int(xx), int(yy)])
        (sx, sy) = als[0]
        for i in range(1, len(als)):
            cx, cy = als[i]
            (ax, bx) = sorted((sx, cx))
            (ay, by) = sorted((sy, cy))
            dx = bx-ax
            dy = by-ay
            if dx == 0:
                for o in range(dy+1):
                    r.add((ax, ay+o))
            elif dy == 0:
                 for o in range(dx+1):
                    r.add((ax+o, ay))               
            sx = cx
            sy = cy
    ps = []
    for t in r:
        ps.append((t[0], t[1]))
    return ps

abyss = 0
intervals = []
for line in lines:
    if len(line.strip()) == 0:
        continue
    xs = line.split(' -> ')
    sx, sy = xs[0].split(',')
    sx = int(sx)
    sy = int(sy)
    abyss = max(abyss, sy)
    intervals.append((sx, sy))
    for i in range(1, len(xs)):
        cx, cy = xs[i].split(',')
        cx = int(cx)
        cy = int(cy)
        sx = cx
        sy = cy
        abyss = max(abyss, cy)

dirs = [[-1, 1], [1, 1]]
num_sand = 0

locs = set()
for k in find_intervals():
    locs.add((k[0], k[1]))

for x in range( -10000, 10000 ):
    locs.add((x, abyss + 2))

while (500 ,0) not in locs:
    x, y = 500, 0
    while True:
        cx0 = x + dirs[0][0]
        cy0 = y + dirs[0][1]
        cx1 = x + dirs[1][0]
        cy1 = y + dirs[1][1]
        if (x, y+1) not in locs:
            y += 1
            continue
        if (cx0, cy0) not in locs:
            x, y = cx0, cy0
            continue
        if (cx1, cy1) not in locs:
            x, y = cx1, cy1
            continue
        if y - 1 == abyss:
            print('part1:', num_sand)
            abyss = -1000
        num_sand += 1
        locs.add((x, y))
        break

print('part2', num_sand)
