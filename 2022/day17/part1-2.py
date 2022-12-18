import sys
import functools

sys.setrecursionlimit(10000)

rocks, i = ((0,1,2,3),(1,0+1j,2+1j,1+2j),(0,1,2,2+1j,2+2j),(0,0+1j,0+2j,0+3j),(0,1,0+1j,1+1j)), 0
jets, j = [ord(x)-61 for x in open('aa.txt').read()], 0
tower, cache, top = set(), dict(), 0

empty = lambda pos: pos.real in range(7) and pos.imag>0 and pos not in tower
check = lambda pos, dir, rock: all(empty(pos+dir+r) for r in rock)

sim_size = 1000000000000

for step in range(sim_size):
    pos = complex(2, top + 4)
    if step == 2022:
        print('Part 1', top)
    key = i, j
    if key in cache:
        S, T = cache[key]
        d, m = divmod(sim_size - step, step - S)
        if m == 0:
            print('part2:', top + (top-T) * d)
            break
    else:
        cache[key] = step, top

    rock = rocks[i]
    i = (i+1) % len(rocks)
    while True:
        jet = jets[j]
        j = (j+1) % len(jets)

        if check(pos, jet, rock):
            pos += jet
        
        if check(pos, -1j, rock):
            pos += -1j
        else:
            break

    tower |= {pos+r for r in rock}
    top = max(top, pos.imag + [1, 0, 2, 2, 3][i])
