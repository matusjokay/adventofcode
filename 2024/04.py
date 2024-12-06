#!/bin/env python3

from collections import defaultdict
from functools import reduce

with open('04.input.txt') as f:
    data = [l.strip() for l in f.readlines()]
d = defaultdict(lambda: '.')
[d.update({(i[0],j[0]): data[i[0]][j[0]]})
    for i in enumerate(data) for j in enumerate(i[1])]
keys = list(d.keys())

# part A
ind = ((0,1), (1,1), (1,0), (-1,1), (-1,-1), (1,-1), (-1,0), (0,-1))

def string(d, c, i):
    return d[(c[0],c[1])]+d[(c[0]+i[0],c[1]+i[1])]+d[(c[0]+2*i[0],c[1]+2*i[1])]+d[(c[0]+3*i[0],c[1]+3*i[1])]

def f(d, coord):
   return sum(['XMAS' == string(d, coord, i) for i in ind])

print(sum([f(d, c) for c in keys]))

# part B

ind = ((1,1), (-1,1), (-1,-1), (1,-1))

def string(d, c, i):
    return d[(c[0]-i[0],c[1]-i[1])] + d[(c[0],c[1])] + d[(c[0]+i[0],c[1]+i[1])]

def f(d, coord):
   return sum(['MAS' == string(d, coord, i) for i in ind]) // 2

print(sum([f(d, c) for c in keys]))
