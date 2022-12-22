data = open('aa.txt').read()
lines = [x for x in data.split('\n')]

imag_pos = {}
imag_pos_new = {}
instructions = ''
read_ins = False

for r, l in enumerate(lines):
    if len(l.strip()) == 0:
        read_ins = True
    else:
        if read_ins:
            instructions = l
            read_ins = False
        else:
            for c, ll in enumerate(l):
                if ll in '.#':
                    imag_pos[complex(c, r)] = ll
                    imag_pos_new[complex(c+1, r+1)] = ll

def part1():
    dir_ang = 1
    start = lines[0].index('.')

    for ix in instructions.replace('R', ',R,').replace('L', ',L,').split(','):
        if ix == 'R':
            dir_ang *= 1j
        elif ix == 'L':
            dir_ang *= -1j
        else:
            for _ in range(int(ix)):
                move = start + dir_ang
                if move in imag_pos:
                    if imag_pos[move] == '.':
                        start = move
                else:
                    tmp = start
                    while tmp - dir_ang in imag_pos:
                        tmp -= dir_ang
                    if imag_pos[tmp] == '.':
                        start = tmp

            
    res = (1000 * (start.imag + 1)) + (4 * (start.real + 1)) + ([1,1j,-1,-1j].index(dir_ang))
    print(res)



def part2():
    cube_portals = dict(( 
        *(((complex( 50+i,  0  ),-1j),(complex(  1  ,150+i), 1 )) for i in range(1,51)), 
        *(((complex(  0  ,150+i),-1 ),(complex( 50+i,  1  ), 1j)) for i in range(1,51)), 
        *(((complex(100+i,  0  ),-1j),(complex(    i,200  ),-1j)) for i in range(1,51)), 
        *(((complex(    i,201  ), 1j),(complex(100+i,  1  ), 1j)) for i in range(1,51)), 
        *(((complex( 50  ,    i),-1 ),(complex(  1  ,151-i), 1 )) for i in range(1,51)), 
        *(((complex(  0  ,100+i),-1 ),(complex( 51  , 51-i), 1 )) for i in range(1,51)), 
        *(((complex( 50  , 50+i),-1 ),(complex(    i,101  ), 1j)) for i in range(1,51)), 
        *(((complex(    i,100  ),-1j),(complex( 51  , 50+i), 1 )) for i in range(1,51)), 
        *(((complex(151  ,    i), 1 ),(complex(100  ,151-i),-1 )) for i in range(1,51)), 
        *(((complex(101  ,100+i), 1 ),(complex(150  , 51-i),-1 )) for i in range(1,51)), 
        *(((complex(100+i, 51  ), 1j),(complex(100  , 50+i),-1 )) for i in range(1,51)), 
        *(((complex(101  , 50+i), 1 ),(complex(100+i, 50  ),-1j)) for i in range(1,51)), 
        *(((complex( 50+i,151  ), 1j),(complex( 50  ,150+i),-1 )) for i in range(1,51)), 
        *(((complex( 51  ,150+i), 1 ),(complex( 50+i,150  ),-1j)) for i in range(1,51)), 
    ))

    d = 1
    p = complex(lines[0].index('.') + 1, 1)
    for ins in instructions.replace('R', ',R,').replace('L', ',L,').split(','):
        if ins=='L':
            d *= -1j
        elif ins=='R':
            d *= 1j
        else:
            for _ in range(int(ins)):
                np=p+d
                nd=d
                if np not in imag_pos_new:
                    np,nd=cube_portals[np,d]
                if np in imag_pos_new and imag_pos_new[np] == '#':
                    break
                p=np
                d=nd
    print("Part 2:",int(1000*p.imag+4*p.real+(1,1j,-1,-1j).index(d)))

part1()
part2()
