#!/bin/env python3

from math import inf

with open('02.input.txt') as f:
    data = [list(map(int, line.split())) for line in f]

def f(dd):
    a = [[x[0]-x[1] for x in zip(d, d[1:])] for d in dd]
    a_pos = [all(map(lambda x: x >= 1 and x <= 3, aa)) for aa in a]
    a_neg = [all(map(lambda x: x <= -1 and x >= -3, aa)) for aa in a]
    return a_pos + a_neg

# part A
print(sum(f(data)))

# part B
print(sum([any(f([d[:i]+d[i+1:] for i in range(len(d))])) for d in data]))
