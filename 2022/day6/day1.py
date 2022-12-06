import re
import collections

T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
Lines = file1.read().splitlines()

for line in Lines: 
    if line:
        s = []
        for i in range(0, len(line)):
            s.append(line[i])
            for j in range(i + 1, len(line)):
                if len(s) == 4:
                    print('found', j)
                    break
                if line[j] not in s:
                    s.append(line[j])
                else:
                    s = []
                    break
            if len(s) == 4:
                break