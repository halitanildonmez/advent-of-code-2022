import z3

data = open('aa.txt').read().strip()
lines = [x for x in data.split('\n')]
graph = {}

root_index = 0

def parse_line(line):
    vals = line.split(': ')
    if len(vals) != 2:
        return
    monkey = vals[0]
    op_or_num = vals[1]
    if op_or_num.isnumeric():
        return monkey, [int(op_or_num)]
    return monkey, op_or_num.split(' ')

def part1():
    new_all_data = ''
    for i, line in enumerate(lines):
        m, ops = parse_line(line)
        if m == 'root':
            root_index = i
        new_all_data += line.split(': ')[1] + '\n'
        graph[m] = ops

    for mm in graph:
        S = []
        S.append(mm)
        discovered = set()
        discovered.add(mm)
        while len(S) > 0:
            v = S.pop(0)
            nn = graph[v]
            if len(nn) == 1:
                new_all_data = new_all_data.replace(v, str(nn[0]))
            else:
                m1, m2 = nn[0], nn[2]
                if m1 not in discovered:
                    discovered.add(m1)
                    S.append(m1)
                if m2 not in discovered:
                    discovered.add(m1)
                    S.append(m2)
                new_all_data = new_all_data.replace(v, '('+m1+nn[1]+m2+')')

    print('part1:', eval(new_all_data.split('\n')[root_index]))


def part2():
    s = z3.Solver()
    z3_vars = {}

    def get_z3_var(v):
        if v in z3_vars:
            return z3_vars[v]
        z3_vars[v] = z3.Int(v)
        return z3_vars[v]

    for line in data.split('\n'):
        m, ops = parse_line(line)
        if m == 'humn':
            continue
        if len(ops) == 1:
            s.add(get_z3_var(m) == int(ops[0]))
        else:
            a, op, b = ops[0], ops[1], ops[2]
            za = get_z3_var(a)
            zb = get_z3_var(b)
            if m == 'root':
                s.add(za == zb)
            else:
                zm = get_z3_var(m)
                if op == '+':
                    s.add(zm == za + zb)
                elif op == '-':
                    s.add(zm == za - zb)
                elif op == '*':
                    s.add(zm == za * zb)
                elif op == '/':
                    s.add(zm == za / zb)
                    s.add(za % zb == 0)
    s.check()
    m = s.model()
    print('part2:', m[z3_vars['humn']])

part1()
part2()
