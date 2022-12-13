import math
import collections
import itertools
import re
import ast
import functools

T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
Lines = file1.read().splitlines()
def compare_s(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return (a < b) - (a > b)
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    for i in range(len(a)):
        if len(b) <= i:
            return -1
        val = compare_s(a[i], b[i]) 
        if val != 0:
            return val
    return len(a) < len(b)

def part1():
    input_grid = []
    compare = []
    cps = []
    sums = 0
    index = 1
    for i, line in enumerate(Lines):
        if len(line.strip()) == 0:
            compare.append(cps)
            xxx = eval(cps[0])
            yyy = eval(cps[1])
            t = compare_s(xxx, yyy)
            if t == 1:
                sums += index
            cps = []
            index += 1
            continue
        input_grid.append(line)
        cps.append(line)

    val = compare_s(eval(cps[0]), eval(cps[1]))
    if val > 0:
        sums += index
    return sums

def part2():
    input_grid = []
    compare = []
    cps = []
    sums = 0
    index = 1
    for i, line in enumerate(Lines):
        if len(line.strip()) == 0:
            continue
        input_grid.append(eval(line))

    input_grid.append(eval('[[2]]'))
    input_grid.append(eval('[[6]]'))
    input_grid.sort( key = functools.cmp_to_key( lambda x, y: -compare_s(x,y)))

    i1 = input_grid.index(eval('[[6]]')) + 1
    i0 = input_grid.index(eval('[[2]]')) + 1
    return i0 * i1
    
print(part1())
print(part2())
