import re
import collections
import os
import itertools
import subsetsum
import math

T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
Lines = file1.read().splitlines()

offset = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
inp = []

for i, line in enumerate(Lines):
    if len(line.strip()) == 0:
        continue
    inp.append(line)


def should_move(hx, hy, tx, ty):
    return abs(hx-tx) > 1 or abs(hy-ty) > 1

def part1():
    hx, hy = 0, 0
    tx, ty = 0, 0
    seen = {(0, 0)}

    for instruction in inp:
        [dr, mv] = instruction.split(' ')
        cx, cy = offset[dr]
        for step in range(int(mv)):
            hx += cx
            hy += cy
            if should_move(hx, hy, tx, ty):
                if abs(tx - hx) > 0:
                    if hx > tx:
                        tx += 1
                    else:
                        tx -= 1
                if abs(ty-hy) > 0:
                    if hy > ty:
                        ty += 1
                    else:
                        ty -= 1
            seen.add((tx, ty))
    print(len(seen))

def part2():
    # just use the same logic but for each rope position ?
    hx, hy = 0, 0
    seen = {(0, 0)}
    rope_pos = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

    for instruction in inp:
        [dr, mv] = instruction.split(' ')
        cx, cy = offset[dr]
        for step in range(int(mv)):
            hx, hy = rope_pos[0]
            hx += cx
            hy += cy
            rope_pos[0] = hx, hy
            for rope_index in range(1, 10):
                prx, pry = rope_pos[rope_index-1]
                crx, cry = rope_pos[rope_index]
                if should_move(prx, pry, crx, cry):
                    if abs(crx - prx) > 0:
                        if prx > crx:
                            crx += 1
                        else:
                            crx -= 1
                    if abs(cry-pry) > 0:
                        if pry > cry:
                            cry += 1
                        else:
                            cry -= 1
                rope_pos[rope_index] = crx, cry
            seen.add(rope_pos[-1])
    print(len(seen))

part1()
part2()
