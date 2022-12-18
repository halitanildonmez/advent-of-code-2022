import sys
import functools

sys.setrecursionlimit(10000)

t = 'bb.txt'
m = 'aa.txt'
FILE = m
l = ''
grid = []

with open(FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        x,y,z = line.split(',')
        grid.append((int(x),int(y),int(z)))

neigh_list = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]
cube_set = set(grid)

def get_neigh(point):
    res = []
    for nl in neigh_list:
        nx = point[0] + nl[0]
        ny = point[1] + nl[1]
        nz = point[2] + nl[2]
        res.append((nx,ny,nz))
    return res


def part1():
    r = 0
    for p in cube_set:
        for q in get_neigh(p):
            if q not in cube_set:
                r += 1
    print(r)

def part2():
    min_x = min(ax[0] for ax in cube_set) - 1
    min_y = min(ax[1] for ax in cube_set) - 1
    min_z = min(ax[2] for ax in cube_set) - 1
    min_p = (min_x, min_y, min_z)

    max_x = max(ax[0] for ax in cube_set) + 1
    max_y = max(ax[1] for ax in cube_set) + 1
    max_z = max(ax[2] for ax in cube_set) + 1
    max_p = (max_x, max_y, max_z)


    stack = [min_p]
    visited = set()
    res = 0
    while stack:
        e = stack.pop()
        if e in visited:
            continue
        visited.add(e)
        for nn in get_neigh(e):
            if nn in cube_set:
                res += 1
            if nn not in cube_set and nn not in visited and all(a <= b <= c for a, b, c in zip(min_p, e, max_p)):
                stack.append(nn)
    print(res)


part1()
part2()
