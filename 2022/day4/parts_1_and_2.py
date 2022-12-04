import re

def parse_intv(val):
    vvs = val.split('-')
    return int(vvs[0]), int(vvs[1])

def solve(intervals):
    ass, ae = intervals[0]
    bs, be = intervals[1]
    if bs > ae or ass > be:
        return -1, -1
    os = max(ass, bs)
    oe = min(ae, be)
    return os, oe



TEST_INPUT_FILE = "bb.txt"
INPUT_FILE = "aa.txt"

file1 = open(INPUT_FILE, 'r')
Lines = file1.readlines()

#print(len(Lines))

res = 0
res2 = 0
for line in Lines:
    #print(line, end='\n')
    assignments = line.split(',')
    first_elf = assignments[0]
    second_elf = assignments[1]

    a, b = parse_intv(first_elf)
    c, d = parse_intv(second_elf)

    if a >= c and a <= d and b >= c and b <= d:
        res = res + 1
    elif c >= a and c <= b and d >= a and d <= b:
        res = res + 1

    ss = [[a, b], [c, d]]
    x, y = solve(ss)
    #print(x, y)
    if x != -1 and y != -1:
        res2 = res2 + 1
    
print (res2)