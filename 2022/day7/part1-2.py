import re
import collections
import os

T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
Lines = file1.read().splitlines()

root = None
s = {}
dirs = {}
for line in Lines:
    if len(line.strip()) == 0:
        continue
    if line[0] == '$':
        cmd_line = line.split(' ')
        cmd = cmd_line[1]
        if cmd == 'cd':
            if cmd_line[2] == '/':
                root = cmd_line[2]
            else:
                root = os.path.normpath(os.path.join(root, cmd_line[2]))
            if root not in s:
                s[root] = 0
                dirs[root] = []
    else:
        sz, fname = line.split()
        if sz != 'dir':
            s[root] += int(sz)
        else:
            sdir = os.path.normpath(os.path.join(root, fname))
            dirs[root].append(sdir)

def xx(dirname):
    dsize = s[dirname]
    for i in dirs[dirname]:
        if i in s:
            dsize += xx(i)
    return dsize

res = 0
fs = {}
for md in s:
    sm = xx(md)
    fs[md] = sm
    if sm <= 100000:
        res += sm

to_del = 70000000 - fs['/']
ll = {}
for ff in fs:
    if to_del + fs[ff] >= 30000000:
        ll[fs[ff]] = ff

print(to_del, fs[ll[min(ll)]])


