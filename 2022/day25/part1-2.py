from collections import defaultdict, deque

data = open('bb.txt').read()
lines = [x for x in data.strip().split('\n')]


decval = 0
for ln in lines:
    d = 0
    for c in ln:
        d *= 5
        if c == '2':
            d += 2
        elif c == '1':
            d += 1
        elif c == '0':
            d += 0
        elif c == '-':
            d -= 1
        elif c == '=':
            d -= 2

    decval += d

def iter(n):
    s = n // 5
    r = '1'
    while s >= 0:
        if s == 0:
            r += ''
            break
        m = s % 5
        if m == 0:
            r += '0'
            s = s // 5
        elif m == 1:
            r += '1'
            s = s // 5
        elif m == 2:
            r += '2'
            s = s // 5
        elif m == 3:
            s = (s + 2) // 5
            r += '='
        elif m == 4:
            r += '-'
            s = (s + 1) // 5
    return r


print(iter(decval)[::-1])
