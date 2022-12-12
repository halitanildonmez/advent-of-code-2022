import copy

# the input has no tabs indent and two extra lines at the end
T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
Lines = file1.read().splitlines()

monkey = 0
monkeys = {}
val = []
mitems = []

m_throws = {}
m_throws_2 = {}
to_test = 1
mm = {}
for i, line in enumerate(Lines):
    if len(line.strip()) == 0:
        mm['inspected'] = {}
        monkeys[monkey] = mm
        mitems = []
        mm = {}
        continue
    if 'Monkey' in line:
        monkey = line.split(' ')[1].replace(':', '')
        monkey = int(monkey)
        m_throws[monkey] = 0
        m_throws_2[monkey] = 0
        continue
    if 'Starting items' in line:
        items = line.split(': ')[1]
        itl = items.split(', ')
        ll = []
        for l in itl:
            ll.append(int(l))
        mm['items'] = ll
        continue
    if 'Operation' in line:
        mitems.append(line.split(':')[1].replace(' new = old * ', ''))
        mm['operation'] = line.split(':')[1].replace(' new = old ', '').replace(' ', '')
        continue
    if 'Test' in line:
        mitems.append(line.split(':')[1].replace(' divisible by ', ''))
        mm['test'] = int(line.split(':')[1].replace(' divisible by ', ''))
        to_test *= int(line.split(':')[1].replace(' divisible by ', ''))
        continue
    if 'If true' in line or 'If false' in line:
        mitems.append(line.split(':')[1].replace(' throw to monkey ', ''))
        mm[line.split(':')[0].replace('If ', '')] = int(line.split(':')[1].replace(' throw to monkey ', ''))
        continue

def calc_worry(w, ops):
    if "*" in ops:
        oo = ops.replace('*', '')
        if 'old' in oo: 
            return w * w
        return w * int(oo)
    if "+" in ops:
        oo = ops.replace('+', '')
        if 'old' in oo: 
            return w + w
        return w + int(oo)
    return -1

def prmap(am):
    for mx in am:
        print(mx, am[mx])
    print('---')

def part1():
    om = copy.deepcopy(monkeys)
    num_monkey = len(om)
    rounds = 0
    while rounds < 20:
        for monkey_index in range(len(om)):
            while om[monkey_index]['items']:
                mon = om[monkey_index]['items'].pop(0)
                #print('Monkey inspects an item with a worry level of', mon)
                worry = calc_worry(mon, om[monkey_index]['operation'])
                #print('Worry level is multiplied by ', om[monkey_index]['operation'], 'to', worry)
                worry = worry // 3
                #print('Monkey gets bored with item. Worry level is divided by 3 to ', worry)
                is_divisible = False
                if worry % om[monkey_index]['test'] == 0:
                    is_divisible = True
                    #print('Current worry level is divisible by', om[monkey_index]['test'])
                #else:
                    #print('Current worry level is not divisible by', om[monkey_index]['test'])
                    #print(end='')
                
                throw_to = om[monkey_index]['false']
                if is_divisible: 
                    throw_to = om[monkey_index]['true']

                om[int(throw_to)]['items'].append(worry)
                #print('Item with worry level', worry, 'is thrown to monkey', int(throw_to), 'from', mon)
                m_throws[monkey_index] += 1
            #print()
        #print('end1')
        rounds += 1
    all_throws = m_throws.values()  
    all_throws = sorted(all_throws) 
    print('Part 1', (all_throws[-1]*all_throws[-2]))

def part2():
    ox = copy.deepcopy(monkeys)
    num_monkey = len(ox)
    rounds = 0
    while rounds < 10000:
        for monkey_index in range(len(ox)):
            while ox[monkey_index]['items']:
                mon = ox[monkey_index]['items'].pop(0)
                #print('Monkey inspects an item with a worry level of', mon)
                worry = calc_worry(mon, ox[monkey_index]['operation'])
                #print('Worry level is multiplied by ', ox[monkey_index]['operation'], 'to', worry)
                #worry = worry // 3
                worry = worry % to_test
                #print('Monkey gets bored with item. Worry level is divided by 3 to ', worry)
                is_divisible = False
                if worry % ox[monkey_index]['test'] == 0:
                    is_divisible = True
                    #print('Current worry level is divisible by', ox[monkey_index]['test'])
                #else:
                    #print('Current worry level is not divisible by', ox[monkey_index]['test'])
                    #print(end='')
                
                throw_to = ox[monkey_index]['false']
                if is_divisible: 
                    throw_to = ox[monkey_index]['true']

                ox[int(throw_to)]['items'].append(worry)
                #print('Item with worry level', worry, 'is thrown to monkey', int(throw_to), 'from', mon)
                m_throws_2[monkey_index] += 1
            #print()
        #print('end1')
        rounds += 1
    all_throws = m_throws_2.values()  
    all_throws = sorted(all_throws) 
    print('Part 1', (all_throws[-1]*all_throws[-2]))

part1()
part2()
