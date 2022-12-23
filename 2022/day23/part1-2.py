from collections import defaultdict, deque

data = open('aa.txt').read()
lines = [x for x in data.split('\n')]

elves = set()
for row, line in enumerate(lines):
    for c, l in enumerate(line):
        if l == '#':
            elves.add((row, c))

def can_elf_move(ex, ey):
    ds = [(-1, 0), (-1, 1), (-1, -1), (1, 0), (1, 1), (1, -1), (0, 1), (0, -1)]
    res = False
    for d in ds:
        nx = ex + d[0]
        ny = ey + d[1]
        if (nx, ny) in elves:
            res = True
    if not res:
        return True
    return False


dir_list = deque(['N', 'E', 'S', 'W'])
sl = 10000
for t in range(sl):
    updated = False
    prop_move = defaultdict(list)
    for elf in elves:
        ex, ey = elf[0], elf[1]
        if can_elf_move(ex, ey):
            continue
        elf_moved = False
        for d in list(dir_list):
            if d == 'N' and (ex-1, ey) not in elves and (ex-1, ey-1) not in elves and (ex-1, ey+1) not in elves and (not elf_moved):
                prop_move[(ex-1, ey)].append((ex, ey))
                elf_moved = True
            elif d == 'E' and (ex+1, ey) not in elves and (ex+1, ey-1) not in elves and (ex+1, ey+1) not in elves and (not elf_moved):
                prop_move[(ex+1, ey)].append((ex, ey))
                elf_moved = True
            elif d == 'S' and (ex, ey-1) not in elves and (ex-1, ey-1) not in elves and (ex+1, ey-1) not in elves and (not elf_moved):
                prop_move[(ex, ey-1)].append((ex, ey))
                elf_moved = True
            elif d == 'W' and (ex, ey+1) not in elves and (ex-1, ey+1) not in elves and (ex+1, ey+1) not in elves and (not elf_moved):
                prop_move[(ex, ey+1)].append((ex, ey))
                elf_moved = True
    
    dir_list.rotate(-1)
    
    for pm in prop_move:
        if len(prop_move[pm]) == 1:
            updated = True
            elves.discard(prop_move[pm][0])
            elves.add(pm)
    if not updated:
        print('part2', t+1)
        break
    if t == 9:
        r1 = min(r for (r,c) in elves)
        r2 = max(r for (r,c) in elves)
        c1 = min(c for (r,c) in elves)
        c2 = max(c for (r,c) in elves)
        ans = 0
        for r in range(r1,r2+1):
            for c in range(c1,c2+1):
                if (r,c) not in elves:
                    ans += 1
        print('part1', ans)
