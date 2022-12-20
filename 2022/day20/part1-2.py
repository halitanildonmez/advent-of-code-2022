from collections import defaultdict, deque

data = open('aa.txt').read().strip()
lines = [int(x) for x in data.split('\n')]

class Node:    
    def __init__(self,value, next=None, prev=None):        
        self.value = value        
        self.next = next
        self.prev = prev

def part1():
    node_list = []
    for l in lines:
        node_list.append(Node(l))

    for index in range(1, len(node_list)):
        node_list[index-1].next = node_list[index]
        node_list[index].prev = node_list[index-1]

    node_list[-1].next = node_list[0]
    node_list[0].prev = node_list[-1]

    for nn in node_list:
        move_index = nn.value % (len(node_list) - 1)
        if move_index == 0:
            continue
        nn.prev.next = nn.next
        nn.next.prev = nn.prev
        
        to_add = nn.prev

        for _ in range(move_index):
            to_add = to_add.next

        nn.next = to_add.next
        nn.prev = to_add
        nn.next.prev = nn
        nn.prev.next = nn


    for i in range(len(node_list)):
        if node_list[i].value == 0:
            pt1 = 0
            cur = node_list[i]
            for _ in range(3):
                for _ in range(1000):
                    cur = cur.next
                pt1 += cur.value
            print(pt1)

def part2():
    node_list = []
    for l in lines:
        node_list.append(Node(l*811589153))

    for index in range(1, len(node_list)):
        node_list[index-1].next = node_list[index]
        node_list[index].prev = node_list[index-1]

    node_list[-1].next = node_list[0]
    node_list[0].prev = node_list[-1]

    for _ in range(10):
        for nn in node_list:
            move_index = (nn.value) % (len(node_list) - 1)
            if move_index == 0:
                continue
            nn.prev.next = nn.next
            nn.next.prev = nn.prev
            
            to_add = nn.prev

            for _ in range(move_index):
                to_add = to_add.next

            nn.next = to_add.next
            nn.prev = to_add
            nn.next.prev = nn
            nn.prev.next = nn


    for i in range(len(node_list)):
        if node_list[i].value == 0:
            pt2 = 0
            cur = node_list[i]
            for _ in range(3):
                for _ in range(1000):
                    cur = cur.next
                pt2 += cur.value
            print(pt2)

part1()
part2()
