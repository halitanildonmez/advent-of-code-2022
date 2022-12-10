T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
Lines = file1.read().splitlines()

inp = []
for i, line in enumerate(Lines):
    if len(line.strip()) == 0:
        continue
    inp.append(line)

def part1():
    check = [20, 60, 100, 140, 180, 220]
    cycle = 0
    X = 1
    total = 0
    for index, i in enumerate(inp):
        vals = i.split(' ')
        a = vals[0]
        if a == 'noop':
            for _ in range(1):
                cycle += 1
                if cycle in check:
                    total += (X * cycle)
        else:
            for _ in range(2):
                cycle += 1
                if cycle in check:
                    total += (X * cycle)
            X += int(vals[1])
    print(total)

def pt2():
    cur_str = ''
    sp_s = 0
    cycle = 1
    cur_cyc = 0
    X = 1
    for ins in inp:
        vals = ins.split(' ')
        op_v = -1
        if vals[0] == 'addx':
            op_v = int(vals[1])
            cycle = 2
        else:
            cycle = 1

        for c in range(cycle):
            if cur_cyc >= sp_s and cur_cyc < sp_s + 3:
                cur_str += '#'
            else:
                cur_str += '.'
            if vals[0] == 'addx' and c == 1:
                X += op_v
                sp_s = X - 1

            if cur_cyc in (40, 80, 120, 160, 200, 240):
                print(cur_str)
                cur_str = '' 
                cur_cyc = 1
            else:
                cur_cyc += 1
    print(cur_str)

            
part1()
print()
pt2()
