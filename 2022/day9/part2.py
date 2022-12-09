import re
import collections
import os
import itertools
import subsetsum

T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
Lines = file1.read().splitlines()

inp = []

for i, line in enumerate(Lines):
    if len(line.strip()) == 0:
        continue
    inp.append(line)

hx, hy = 0, 0
tx, ty = 0, 0
seen = {(0, 0)}

offset = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
rope_pos = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

for instruction in inp:
    d, a = instruction.split(' ')
    cx, cy = offset[d]
    for step in range(int(a)):
        hx = rope_pos[0][0]
        hy = rope_pos[0][1]
        rope_pos[0] = hx + cx, hy + cy
        for i in range(1, 10):
            px, py = rope_pos[i - 1]
            kx, ky = rope_pos[i]
            dist_x, dist_y = abs(kx - px), abs(ky - py)
            while max(dist_x, dist_y) > 1:
                if abs(kx - px) > 0:
                    if px > kx:
                        kx += 1
                    else:
                        kx -= 1
                if abs(ky - py) > 0:
                    if py > ky:
                        ky += 1
                    else:
                        ky -= 1
                dist_x, dist_y = abs(kx - px), abs(ky - py)
            rope_pos[i] = kx, ky

        seen.add(rope_pos[len(rope_pos) - 1])

print(len(seen))