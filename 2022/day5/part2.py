import re

T = "bb.txt"
M = "aa.txt"

file1 = open(T, 'r')
Lines = file1.read().splitlines()

all_arr = [
    ['R', 'G', 'J', 'B', 'T', 'V', 'Z'], 
    ['J', 'R', 'V', 'L'], 
    ['S', 'Q', 'F'], 
    ['Z', 'H', 'N', 'L', 'F', 'V', 'Q', 'G'], 
    ['R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W'], 
    ['S', 'W', 'T', 'C', 'H', 'F'], 
    ['D', 'Z', 'C', 'V', 'F', 'N', 'J'], 
    ['L', 'G', 'Z', 'D', 'W', 'R', 'F', 'Q'], 
    ['J', 'B', 'W', 'V', 'P']
]

for line in Lines:
        m = -1
        f = -1
        t = -1
        nn = []
        for l in line.split(' '):
            if l.isnumeric():
                nn.append(l)

        m = int(nn[0])
        f = int(nn[1]) - 1
        t = int(nn[2]) - 1

        tmp = []
        for i in range(m):
            elem = all_arr[f].pop()
            tmp.append(elem)
        tmp.reverse()
        for x in tmp:
            all_arr[t].append(x)


for aa in all_arr:
    print(aa.pop(), end='')