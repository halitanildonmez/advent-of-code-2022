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

for instruction in inp:
    d, a = instruction.split(' ')
    cx, cy = offset[d]
    for step in range(int(a)):
        hx += cx
        hy += cy
        while max(abs(tx - hx), abs(ty - hy)) > 1:
            if abs(tx - hx) > 0:
                if hx > tx:
                    tx += 1  
                else:
                    tx -= 1
            if abs(ty - hy) > 0:
                if hy > ty:
                    ty += 1  
                else:
                    ty -= 1
            seen.add((tx, ty))


print(len(seen))