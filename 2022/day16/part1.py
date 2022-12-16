import math
import collections
import itertools
import re
import ast
import functools
from collections import defaultdict
from z3 import If, Int, Solver
from z3 import *
import copy

T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
lines = file1.read().splitlines()
valves = {}

for line in lines:
    parts = line.split()
    valve = parts[1]
    flow_rate = int(parts[4][5:-1])
    lead_to = ''.join(parts[9:]).split(',')
    valves[valve] = (flow_rate, lead_to)

valve_to_num = {}
for key in sorted(valves.keys()):
    valve_to_num[key] = 1 << len(valve_to_num)

valves = {
    valve_to_num[valve]: (flow_rate, tuple(map(valve_to_num.get, lead_to)))
    for valve, (flow_rate, lead_to) in valves.items()
}

def part1():

    states = [(valve_to_num['AA'], 0, 0)]

    best = {}

    for t in range(1, 31):
        new_states = []
        for loc, opened, pressure in states:
            key = (loc, opened)
            if key in best and pressure <= best[key]:
                continue
            best[key] = pressure
            flow_rate, lead_to = valves[loc]
            if loc & opened == 0 and flow_rate > 0:
                new_states.append((loc, opened | loc, pressure + flow_rate * (30 - t)))
            for dest in lead_to:
                new_states.append((dest, opened, pressure))
        states = new_states
    print('pt1', max(pressure for a, b, pressure in states))


part1()
