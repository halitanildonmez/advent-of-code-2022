import re
import collections
import os

T = "bb.txt"
M = "aa.txt"

file1 = open(T, 'r')
Lines = file1.read().splitlines()

inp = []


for line in Lines:
    if len(line.strip()) == 0:
        continue
    inp.append(line)
    
row = len(inp)
col = len(inp[0])
m = [ [0]*col for i in range(row)]

for i in range(row):
    l = inp[i]
    for j in range(col):
        m[i][j] = int(l[j])
        
#look up, down, left, or right
vizcount = 0
for i in range(1, row - 1):
    for j in range(1, col - 1):
        tree = m[i][j]
        updown = []
        for k in range(0, row):
            if k != i:
                updown.append(m[k][j])

        leftright = []
        for l in range(0, col):
            if l != j:
                leftright.append(m[i][l])

        # top
        tv = True
        for t in range(0, i):
            uu = updown[t]
            if uu >= tree:
                tv = False
                break
        td = True
        for t in range(i, len(updown)):
            uu = updown[t]
            if uu >= tree:
                td = False
                break
        tl = True
        for t in range(0, j):
            uu = leftright[t]
            if uu >= tree:
                tl = False
                break
        tr = True
        for t in range(j, len(leftright)):
            uu = leftright[t]

            if uu >= tree:
                tr = False
                break
        if tv or td or tl or tr:
            vizcount += 1
        # if all of the other trees between it and an edge of the grid are shorter than it.

print((2 * row) + ((col - 2) * 2))
vizcount = vizcount + (2 * row) + ((col - 2) * 2)
print(vizcount)