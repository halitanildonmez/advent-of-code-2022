import math
import collections
import itertools
import re
import ast
import functools
from collections import defaultdict
from z3 import If, Int, Solver

T = "bb.txt"
M = "aa.txt"

file1 = open(M, 'r')
lines = file1.read().splitlines()

sensors = []
beacons = []

def manhattan_dist(p1, p2, q1, q2):
    return abs(p1 - q1) + abs(p2 - q2)

def z3_man_dist(p1, p2, q1, q2):
    return If(p1-q1 >= 0, p1-q1, -1*(p1-q1)) + If(p2-q2 >= 0, p2-q2, -1*(p2-q2))

def add_sensor(sensor_str):
    strx, stry = sensor_str.replace('Sensor at ', '').split(', ')
    strx = strx.replace('x=', '')
    stry = stry.replace('y=', '')
    x = int(strx)
    y = int(stry)
    return x, y

def add_beacon(beacon_str):
    strx, stry = beacon_str.replace('closest beacon is at ', '').split(', ')
    strx = strx.replace('x=', '')
    stry = stry.replace('y=', '')
    x = int(strx)
    y = int(stry)
    return x, y

ranges = []
sensor_to_beacon = []
all_sx = []
all_bx = []
for line in lines:
    ll = line.split(': ')
    sx, sy = add_sensor(ll[0])
    all_sx.append(sx)
    bx, by = add_beacon(ll[1])
    all_bx.append(bx)
    smd = manhattan_dist(sx, sy, bx, by)
    sensor_to_beacon.append((sx,sy,bx,by,smd))
    sensors.append((sx, sy, smd))
    beacons.append((bx, by))

def part1():
    y = 2000000
    c = 0
    for x in range(-5000000, 5000000):
        found = False
        for sx, sy, bx, by, smd in sensor_to_beacon:
            mnd = manhattan_dist(sx, sy, x, y)
            if bx == x and by == y:
                found = False
                break
            if mnd <= smd:
                found = True
                break
        if found == True:
            c += 1
    print('pt1:', c)

def part2():
    max_int = 4000000
    s = Solver()
    x = Int("x")
    y = Int("y")
    s.add(x >= 0)
    s.add(x <= max_int)
    s.add(y >= 0)
    s.add(y <= max_int)
    for sx, sy, bx, by, smd in sensor_to_beacon:
        s.add(z3_man_dist(x, y, sx, sy) > smd)
    s.check()
    model = s.model()
    print('pt2:', model[x].as_long() * max_int + model[y].as_long())

part1()
part2()
