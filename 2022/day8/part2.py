import re
import collections
import os

T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
Lines = file1.read().splitlines()

inp = []
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # dx, dy pairs for check_dir

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
num_visible = []


for i in range(1, row - 1):
    for j in range(1, col - 1):
        tree = m[i][j]
        updown = []
        for k in range(0, row):
            #if k != i:
                updown.append(m[k][j])

        leftright = []
        for l in range(0, col):
            #if l != j:
                leftright.append(m[i][l])

        l_s = leftright[0:j]
        l_s.reverse()
        r_s = leftright[j+1:]

        u_s = updown[0:i]
        u_s.reverse()
        d_s = updown[i+1:]


        lds = 0
        for index, ltree in enumerate(l_s):
            lds += 1
            if ltree >= tree:
                break
        rds = 0
        for index, rtree in enumerate(r_s):
            rds += 1
            if rtree >= tree:
                break
        uds = 0
        for index, utree in enumerate(u_s):
            uds += 1
            if utree >= tree:
                break

        dds = 0
        for index, dtree in enumerate(d_s):
            dds += 1
            if dtree >= tree:
                break
                
        #print(uds, lds, dds, rds, tree, r_s, tree)

        num_visible.append((lds*rds*uds*dds))
        # if all of the other trees between it and an edge of the grid are shorter than it.

vizcount = vizcount + (2 * row) + ((col - 2) * 2)
print(vizcount, max(num_visible))
